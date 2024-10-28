Name:           terra-release
Version:        42
Release:        2
Summary:        Release package for Terra

License:        MIT
URL:            https://terra.fyralabs.com
Source0:        terra.repo
Source1:        terra-extra.repo
BuildArch:      noarch

%dnl We probably shouldn't do this in Rawhide!
%dnl Requires:       system-release(%{version})

%description
Release package for Terra, containing the Terra repository configuration.

%package extra
Summary: Release package for Terra Extra

%description extra
Release package for Terra Extra, which is a repository with packages that might cause
conflict with Fedora.

%prep

%build

%install
install -D -p -m 0644 -t %{buildroot}%{_sysconfdir}/yum.repos.d %{SOURCE0}
install -Dpm644 -t %buildroot%_sysconfdir/yum.repos.d %SOURCE1

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/terra.repo

%files extra
%config(noreplace) %{_sysconfdir}/yum.repos.d/terra-extra.repo

%changelog
* Fri Oct 25 2024 madonuko <mado@fyralabs.com> - 42-2
- Add terra-release-extra

* Thu Nov 16 2023 Lleyton Gray <lleyton@fyralabs.com> - 41-1
- Update for Terra 41 (in this case rawhide)

* Thu Nov 16 2023 Lleyton Gray <lleyton@fyralabs.com> - 40-1
- Update for Terra 40 (in this case rawhide)

* Thu Nov 16 2023 Lleyton Gray <lleyton@fyralabs.com> - 39-2
- Add source repository

* Wed Aug 16 2023 Lleyton Gray <lleyton@fyralabs.com> - 39-1
- Update for Terra 39

* Sat May 6 2023 Lleyton Gray <lleyton@fyralabs.com> - 38-1
- Initial package
