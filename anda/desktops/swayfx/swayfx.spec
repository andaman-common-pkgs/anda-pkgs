%global swayVersion 1.9

Name:           swayfx
Version:        0.4
Release:        1%{?dist}

Summary:        SwayFX: Sway, but with eye candy!
URL:            https://github.com/WillPower3309/swayfx
License:        MIT

Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
Source101:      https://github.com/wlrfx/packages/raw/fe1355c4844078f49761e9d73a376179d3007646/COPR/swayfx/sway-portals.conf


BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.60.0
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(json-c) >= 0.13
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput) >= 1.21.0
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libsystemd) >= 239
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server) >= 1.21.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  (pkgconfig(wlroots) >= 0.17.0 with pkgconfig(wlroots) < 0.18)
BuildRequires:  (pkgconfig(scenefx) >= 0.1 with pkgconfig(scenefx) < 0.2)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xkbcommon) >= 1.5.0

Requires:       sway-config
Suggests:       %{name}-config-upstream

Conflicts:      sway
Provides:       sway = %{swayVersion}


Packager:       Atmois <atmois@atmois.com>
 
%description
%{summary}


# Configuration presets:
%package        config-upstream
Summary:        Upstream configuration for Sway
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Provides:       sway-config = %{version}-%{release}
Conflicts:      sway-config


%package        wallpapers
Summary:        Wallpapers for Sway
BuildArch:      noarch
License:        CC0

%description    wallpapers
Wallpaper collection provided with Sway


# Require the wallpaper referenced in the config.
# Weak dependency here causes a swaynag warning during the configuration load
Requires:       sway-wallpapers
# Lack of graphical drivers may hurt the common use case
Requires:       mesa-dri-drivers
# Logind needs polkit to create a graphical session
Requires:       polkit
# swaybg is used in the default config
Requires:       swaybg
# dmenu (as well as rxvt any many others) requires XWayland on Sway
Requires:       xorg-x11-server-Xwayland

# Sway binds the terminal shortcut to one specific terminal. In our case foot
Recommends:     foot
# grim is the recommended way to take screenshots on sway 1.0+
Recommends:     grim
# wmenu is the default launcher in sway, but it still requires dmenu_path to work
Recommends:     dmenu
Recommends:     wmenu
# In addition, xargs is recommended for use in such a launcher arrangement
Recommends:     findutils
# Install configs and scripts for better integration with systemd user session
Recommends:     sway-systemd
# Both utilities are suggested in the default configuration
Recommends:     swayidle
Recommends:     swaylock

# Minimal installation doesn't include Qt Wayland backend
Recommends:     (qt5-qtwayland if qt5-qtbase-gui)
Recommends:     (qt6-qtwayland if qt6-qtbase-gui)


%description    config-upstream
Upstream configuration for Sway.
Includes all important dependencies for a typical desktop system with minimal or no divergence from the upstream.


%prep
%autosetup -N -n %{name}-%{version}

%build
%meson \
    -Dsd-bus-provider=libsystemd \
    -Dwerror=false \
%meson_build

%install
%meson_install
# Install portals.conf for xdg-desktop-portal
install -D -m644 -pv %{SOURCE101} %{buildroot}%{_datadir}/xdg-desktop-portal/sway-portals.conf
# Create directory for extra config snippets
install -d -m755 -pv %{buildroot}%{_sysconfdir}/sway/config.d
 
%files
%license LICENSE
%dir %{_sysconfdir}/sway
%dir %{_sysconfdir}/sway/config.d
%{_mandir}/man1/sway*
%{_mandir}/man5/*
%{_mandir}/man7/*
%caps(cap_sys_nice=ep) %{_bindir}/sway
%{_bindir}/swaybar
%{_bindir}/swaymsg
%{_bindir}/swaynag
%dir %{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal/sway-portals.conf
%{bash_completions_dir}/sway*
%{fish_completions_dir}/sway*.fish
%{zsh_completions_dir}/_sway*


%files config-upstream
%config(noreplace) %{_sysconfdir}/sway/config
%{_datadir}/wayland-sessions/sway.desktop


%files wallpapers
%license assets/LICENSE
%{_datadir}/backgrounds/sway