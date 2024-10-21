%global commit c40a4ad05a8e6ea99eed4a7d7d2098a08686e065
%global commit_date 20241021
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           envision
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        UI for building, configuring and running Monado, the open source OpenXR runtime
License:        AGPL-3.0-or-later
URL:            https://gitlab.com/gabmus/envision/
Source0:        %url/-/archive/%commit/envision-%commit.tar.gz
BuildRequires:  meson ninja-build cargo 
BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(gio-2.0) >= 2.66
BuildRequires:  pkgconfig(gtk4) >= 4.10.0
BuildRequires:  pkgconfig(vte-2.91-gtk4) >= 0.72.0
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  openssl-devel-engine
BuildRequires:  openxr-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
BuildRequires:  git-core
Recommends:     android-tools

%description
%summary.

%prep
%autosetup -n envision-%commit

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%_bindir/envision
%_datadir/applications/org.gabmus.envision.Devel.desktop
%_datadir/envision/
%_iconsdir/hicolor/scalable/apps/org.gabmus.envision.Devel.svg
%_iconsdir/hicolor/symbolic/apps/org.gabmus.envision.Devel-symbolic.svg
%_metainfodir/org.gabmus.envision.Devel.appdata.xml
