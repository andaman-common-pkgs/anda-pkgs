%{?python_enable_dependency_generator}

%global __arch_install_post /bin/true

%bcond_with tests

Name:           apparmor
Version:        4.1.0~beta1
Release:        1%?dist
Summary:        AppArmor userspace components

%define baseversion %(echo %{version} | cut -d. -f-2)
%global normver %(echo %version | sed 's/~/-/')

License:        GPL-2.0
URL:            https://gitlab.com/apparmor/apparmor
Source0:        %url/-/archive/v%normver/apparmor-v%normver.tar.gz
Source1:        apparmor.preset
Patch01:        0001-fix-avahi-daemon-authselect-denial-in-fedora.patch

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-static
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  swig
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{_bindir}/podchecker
BuildRequires:  %{_bindir}/pod2html
BuildRequires:  gettext
BuildRequires:  pam-devel
BuildRequires:  httpd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  autoconf-archive
BuildRequires:  gawk
BuildRequires:  which
%if %{with tests}
BuildRequires:  %{_bindir}/runtest
BuildRequires:  %{_bindir}/prove
BuildRequires:  perl(Locale::gettext)
BuildRequires:  perl(Test::More)
%endif

Provides:       %{name}-profiles = %{version}-%{release}
Requires:       %{name}-parser
Recommends:     %{name}-utils
%{?systemd_requires}

%description
AppArmor protects systems from insecure or untrusted processes by running
them in restricted confinement, while still allowing processes to share files,
exercise privilege and communicate with other processes. AppArmor is a Mandatory
Access Control (MAC) mechanism which uses the Linux Security Module (LSM)
framework. The confinement's restrictions are mandatory and are not bound to
identity, group membership, or object ownership. The protections provided are in
addition to the kernel's regular access control mechanisms (including DAC) and
can be used to restrict the superuser.

%package      libs
Summary:      AppArmor library

%description  libs
This package contains the shared library used for making use of the AppArmor
profile and changehat functionality, as well as common log parsing routines.

%package       devel
Summary:       AppArmor development libraries and header files
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package contains AppArmor development libraries and header files.

%package -n     python3-apparmor
Summary:        AppArmor Python3 utility library
Requires:       python3-LibAppArmor = %{version}-%{release}
BuildArch:      noarch

%description -n python3-apparmor
This package provides the python interface to AppArmor. It is used for python
applications interfacing with AppArmor.

%package -n     python3-LibAppArmor
Summary:        AppArmor library Python3 bindings
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description -n python3-LibAppArmor
This package contains Python3 module that contains the language bindings for 
the AppArmor library, libapparmor, which were autogenerated via SWIG.

%package        profiles
Summary:        AppArmor profiles
Provides:       apparmor-profiles = %{version}-%{release}
BuildArch:      noarch

%description    profiles
This package contains default AppArmor profiles.

%package        parser
Summary:        AppArmor userlevel parser utility
Requires:       python3-apparmor = %{version}
# Let it be the AppArmor metapackage
Provides:       %{name} = %{version}-%{release}
Requires:       %{name}-profiles = %{version}-%{release}
Recommends:     %{name}-utils

%description    parser
The AppArmor Parser is a userlevel program that is used to load in
program profiles to the AppArmor Security kernel module.

%package        utils
Summary:        AppArmor User-Level Utilities
Requires:       python3-apparmor = %{version}
Requires:       python3-notify2

%description    utils
This package provides the aa-logprof, aa-genprof, aa-autodep,
aa-enforce, and aa-complain tools to assist with profile authoring.
Besides it provides the aa-unconfined server information tool.

%package -n     pam_apparmor
Summary:        PAM module for AppArmor change_hat
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pam%{?_isa}
 
%description -n pam_apparmor
This package provides the PAM module needed to declare various differing
confinement policies when starting PAM sessions by using the changehat 
abilities exposed through libapparmor.

%package -n     mod_apparmor
Summary:        AppArmor module for apache2
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       httpd%{?_isa}

%description -n mod_apparmor
This package provides the Apache module needed to declare various differing
confinement policies when running virtual hosts in the webserver by using the
changehat abilities exposed through libapparmor.

%prep
%autosetup -p1 -n %name-v%normver
sed -i 's/@VERSION@/%normver/g' libraries/libapparmor/swig/python/setup.py.in
sed -i 's/${VERSION}/%normver/g' utils/Makefile

%build
export PYTHON=%{__python3}
export PYTHON_VERSION=3
export PYTHON_VERSIONS=python3

pushd libraries/libapparmor
./autogen.sh
%configure \
    --with-python \

%make_build VERSION=%normver
popd

%make_build -C binutils
%make_build -C parser
%make_build -C profiles
%make_build -C utils
%make_build -C changehat/pam_apparmor
%make_build -C changehat/mod_apparmor
%make_build -C utils/vim

%install
mkdir -p %buildroot%_datadir/polkit-1/actions/
%make_install -C libraries/libapparmor
%make_install -C binutils
%make_install -C parser \
    APPARMOR_BIN_PREFIX=%{buildroot}%{_prefix}/lib/apparmor \
    SBINDIR=%{buildroot}%{_sbindir}
%make_install -C profiles
%make_install -C utils
%make_install -C changehat/pam_apparmor \
    SECDIR=%{buildroot}%{_libdir}/security
%make_install -C changehat/mod_apparmor
%make_install -C utils/vim

install -Dm644 %{SOURCE1} %{buildroot}%{_presetdir}/70-apparmor.preset

find %{buildroot} \( -name "*.a" -o -name "*.la" \) -delete

%find_lang aa-binutils
%find_lang apparmor-parser
%find_lang apparmor-utils


%if %{with tests}
%check
make -C libraries/libapparmor check
make -C binutils check
make -C parser check
# only running check-parser, as check-logprof (included in check) fails:
# https://gitlab.com/apparmor/apparmor/issues/36
make -C profiles check-parser
make -C profiles check
# shutil.copytree has a regression
# https://gitlab.com/apparmor/apparmor/issues/62
make -C utils check
%endif

%post parser
%systemd_post %{name}.service

%preun parser
%systemd_preun %{name}.service

%postun parser
%systemd_postun_with_restart %{name}.service

%files libs
%license LICENSE
%{_libdir}/libapparmor.so.*

%files devel
%{_libdir}/libapparmor.so
%{_includedir}/aalogparse
%{_includedir}/sys/apparmor*
%{_libdir}/pkgconfig/libapparmor.pc
%{_mandir}/man2/aa_*.2.gz
%{_mandir}/man3/aa_*.3.gz

%files -n python3-apparmor
%doc README.md
%{python3_sitelib}/apparmor
%{python3_sitelib}/apparmor-*.egg-info

%files -n python3-LibAppArmor
%doc README.md
%{python3_sitearch}/LibAppArmor
%{python3_sitearch}/LibAppArmor-*.egg-info

%files profiles
%dir %{_sysconfdir}/apparmor.d/
%dir %{_sysconfdir}/apparmor.d/abi
%config(noreplace) %{_sysconfdir}/apparmor.d/abi/3.0
%config(noreplace) %{_sysconfdir}/apparmor.d/abi/4.0
%config(noreplace) %{_sysconfdir}/apparmor.d/abi/kernel-5.4-outoftree-network
%config(noreplace) %{_sysconfdir}/apparmor.d/abi/kernel-5.4-vanilla
%config(noreplace) %{_sysconfdir}/apparmor.d/php-fpm
%config(noreplace) %{_sysconfdir}/apparmor.d/samba-bgqd
%config(noreplace) %{_sysconfdir}/apparmor.d/samba-dcerpcd
%config(noreplace) %{_sysconfdir}/apparmor.d/samba-rpcd
%config(noreplace) %{_sysconfdir}/apparmor.d/samba-rpcd-classic
%config(noreplace) %{_sysconfdir}/apparmor.d/samba-rpcd-spoolss
%config(noreplace) %{_sysconfdir}/apparmor.d/zgrep
%dir %{_sysconfdir}/apparmor.d/abstractions
%config(noreplace) %{_sysconfdir}/apparmor.d/abstractions/*
%dir %{_sysconfdir}/apparmor.d/disable
%dir %{_sysconfdir}/apparmor.d/local
%dir %{_sysconfdir}/apparmor.d/tunables
%config(noreplace) %{_sysconfdir}/apparmor.d/tunables/*
%dir %{_sysconfdir}/apparmor.d/apache2.d
%config(noreplace) %{_sysconfdir}/apparmor.d/apache2.d/phpsysinfo
%config(noreplace) %{_sysconfdir}/apparmor.d/bin.*
%config(noreplace) %{_sysconfdir}/apparmor.d/sbin.*
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.*
%config(noreplace) %{_sysconfdir}/apparmor.d/lsb_release
%config(noreplace) %{_sysconfdir}/apparmor.d/nvidia_modprobe
%config(noreplace) %{_sysconfdir}/apparmor.d/local/*
%dir %{_datadir}/apparmor/
%{_datadir}/apparmor/extra-profiles

%files parser -f apparmor-parser.lang -f aa-binutils.lang
%license parser/COPYING.GPL
%doc parser/README
%doc parser/*.[1-9].html
%doc common/apparmor.css
%{_sbindir}/apparmor_parser
%{_bindir}/aa-enabled
%{_bindir}/aa-exec
%{_bindir}/aa-features-abi
%{_sbindir}/aa-load
%{_sbindir}/aa-teardown
%{_unitdir}/apparmor.service
%{_presetdir}/70-apparmor.preset
%{_prefix}/lib/apparmor
%dir %{_sysconfdir}/apparmor
%config(noreplace) %{_sysconfdir}/apparmor.d/
%config(noreplace) %{_sysconfdir}/apparmor/parser.conf
%{_mandir}/man1/aa-enabled.1.gz
%{_mandir}/man1/aa-exec.1.gz
%{_mandir}/man1/aa-features-abi.1.gz
%{_mandir}/man5/apparmor.d.5.gz
%{_mandir}/man5/apparmor.vim.5.gz
%{_mandir}/man7/apparmor.7.gz
%{_mandir}/man7/apparmor_xattrs.7.gz
%{_mandir}/man8/aa-teardown.8.gz
%{_mandir}/man8/apparmor_parser.8.gz

%files utils -f apparmor-utils.lang
%doc utils/*.[0-9].html
%doc utils/vim/apparmor.vim.5.html
%doc common/apparmor.css
%dir %{_sysconfdir}/apparmor
%config(noreplace) %{_sysconfdir}/apparmor/easyprof.conf
%config(noreplace) %{_sysconfdir}/apparmor/logprof.conf
%config(noreplace) %{_sysconfdir}/apparmor/notify.conf
%config(noreplace) %{_sysconfdir}/apparmor/severity.db
%{_sbindir}/aa-audit
%{_sbindir}/aa-autodep
%{_sbindir}/aa-cleanprof
%{_sbindir}/aa-complain
%{_sbindir}/aa-decode
%{_sbindir}/aa-disable
%{_sbindir}/aa-enforce
%{_sbindir}/aa-genprof
%{_sbindir}/aa-logprof
%{_sbindir}/aa-mergeprof
%{_sbindir}/aa-notify
%{_sbindir}/aa-remove-unknown
%{_sbindir}/aa-status
%{_sbindir}/aa-unconfined
%{_sbindir}/apparmor_status
%{_bindir}/aa-easyprof
%dir %{_datadir}/apparmor
%{_datadir}/apparmor/easyprof
%{_datadir}/apparmor/apparmor.vim
%{_mandir}/man5/logprof.conf.5.gz
%{_mandir}/man8/aa-audit.8.gz
%{_mandir}/man8/aa-autodep.8.gz
%{_mandir}/man8/aa-cleanprof.8.gz
%{_mandir}/man8/aa-complain.8.gz
%{_mandir}/man8/aa-decode.8.gz
%{_mandir}/man8/aa-disable.8.gz
%{_mandir}/man8/aa-easyprof.8.gz
%{_mandir}/man8/aa-enforce.8.gz
%{_mandir}/man8/aa-genprof.8.gz
%{_mandir}/man8/aa-logprof.8.gz
%{_mandir}/man8/aa-mergeprof.8.gz
%{_mandir}/man8/aa-notify.8.gz
%{_mandir}/man8/aa-remove-unknown.8.gz
%{_mandir}/man8/aa-status.8.gz
%{_mandir}/man8/aa-unconfined.8.gz
%{_mandir}/man8/apparmor_status.8.gz

%files -n pam_apparmor
%doc README.md
%{_libdir}/security/pam_apparmor.so

%files -n mod_apparmor
%{_libdir}/httpd/modules/mod_apparmor.so
%{_mandir}/man8/mod_apparmor.8.gz

%changelog
%autochangelog
