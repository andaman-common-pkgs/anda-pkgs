Name:			keyd
Version:		2.4.3
Release:		2%?dist
Summary:		Key remapping daemon for linux
URL:			https://github.com/rvaiya/keyd
License:		MIT
Source0:		%url/archive/refs/tags/v%version.tar.gz
Suggests:		python3 python3-xlib
BuildRequires:	gcc mold make kernel-headers systemd-rpm-macros

%description
keyd provides a flexible system wide daemon which remaps keys using kernel
level input primitives (evdev, uinput).

%prep
%autosetup

%build
%make_build

%install
%make_install
install -Dm644 keyd.service %buildroot%_unitdir/keyd.service

%post
%systemd_post keyd.service

%preun
%systemd_preun keyd.service

%postun
%systemd_postun_with_restart keyd.service

%files
%doc README.md
%license LICENSE
%_unitdir/keyd.service
%_bindir/keyd
%_bindir/keyd-application-mapper
%_datadir/keyd
%_datadir/doc/keyd/
%_mandir/man1/keyd-application-mapper.1.gz
%_mandir/man1/keyd.1.gz

%changelog
* Tue May 23 2023 windowsboy111 <windowsboy111@fyralabs.com> - 2.4.3-1
- Initial package
