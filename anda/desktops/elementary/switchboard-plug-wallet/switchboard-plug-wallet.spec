%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-wallet

%global plug_type personal
%global plug_name wallet
%global plug_rdnn io.elementary.switchboard.wallet

%global commit 50582fc7ee43a4b47647d04786dcf1d0eb45af36
%global commit_date 240218

Name:           switchboard-plug-wallet
Summary:        Switchboard Wallet Plug
Version:        %commit_date.%(c=%commit; echo ${c:0:7})
Release:        2%?dist
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/%name
Source0:        %url/archive/%commit/%srcname-%commit.tar.gz

BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  fdupes

BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  gtk3-devel
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  switchboard-devel

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

%description
Manage Payment Methods and related settings.


%prep
%autosetup -n %srcname-%commit -p1


%build
%meson
%meson_build


%install
%meson_install
%fdupes %buildroot%_datadir/icons/hicolor


%files
%doc README.md
%license COPYING

%_libdir/switchboard/%plug_type/lib%plug_rdnn.so
%_datadir/icons/hicolor/*/apps/%plug_rdnn.svg
%_datadir/locale/*/LC_MESSAGES/%plug_rdnn.mo


%changelog
* Tue Jun 13 2023 windowsboy111 <windowsboy111@fyralabs.com> - bfe73dfb95d9b46a0a34e0db35a178233c8552b0-1
- Initial package.
