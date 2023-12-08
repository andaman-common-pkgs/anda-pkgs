# saves time so we don't have to download the thing manually
%undefine _disable_source_fetch
# We don't have debug symbols, because .NET
%define debug_package %{nil}
# We aren't using Mono but RPM expected Mono
%global __requires_exclude_from ^/usr/lib/opentabletdriver/.*$
%global __os_install_post %{nil}

Name: opentabletdriver
Version: 0.6.3.0
Release: 2%{?dist}
Summary: A cross-platform open source tablet driver
License: LGPLv3
URL: https://github.com/OpenTabletDriver/OpenTabletDriver
Source0: %{url}/archive/refs/tags/v%{version}.tar.gz
%define otddir OpenTabletDriver-%{version}

BuildRequires: dotnet-sdk-6.0

Requires: dotnet-runtime-6.0
Requires: libevdev.so.2()(64bit)
Requires: gtk3
Requires: gtk3
Requires: udev
Requires(post): grep
Suggests: libX11
Suggests: libXrandr

%description
OpenTabletDriver is an open source, cross platform, user mode tablet driver. The goal of OpenTabletDriver is to be cross platform as possible with the highest compatibility in an easily configurable graphical user interface.

%prep
%autosetup -n %{otddir}

%build
./eng/linux/package.sh --output bin

%install
export DONT_STRIP=1
PREFIX="%{_prefix}" ./eng/linux/package.sh --package Generic --build false
mkdir -p "%{buildroot}"
mv ./dist/files/* "%{buildroot}"/
rm -rf ./dist
mkdir -p "%{buildroot}/%{_prefix}/lib/"
cp -r bin "%{buildroot}/%{_prefix}/lib/opentabletdriver"


%files
%defattr(-,root,root)
%dir %{_prefix}/lib/opentabletdriver
%dir %{_prefix}/share/doc/opentabletdriver
%{_bindir}/otd
%{_bindir}/otd-daemon
%{_bindir}/otd-gui
%{_prefix}/lib/modprobe.d/99-opentabletdriver.conf
%{_prefix}/lib/modules-load.d/opentabletdriver.conf
%{_prefix}/lib/opentabletdriver/*
%{_prefix}/lib/systemd/user/opentabletdriver.service
%{_prefix}/lib/udev/rules.d/70-opentabletdriver.rules
%{_prefix}/share/applications/opentabletdriver.desktop
%{_prefix}/share/man/man8/opentabletdriver.8.gz
%{_prefix}/share/doc/opentabletdriver/LICENSE
%{_prefix}/share/pixmaps/otd.ico
%{_prefix}/share/pixmaps/otd.png
