%global scenefxVersion 0.1

Name:           scenefx
Version:        %{scenefxVersion}
Release:        1%{?dist}

Summary:        A drop-in replacement for the wlroots scene API that allows wayland compositors to render surfaces with eye-candy effects
URL:            https://github.com/wlrfx/scenefx
License:        MIT

Source0:        %{url}/archive/refs/tags/%{scenefxVersion}.tar.gz


BuildRequires:  gcc
BuildRequires:  glslang
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.59.0

BuildRequires:  (pkgconfig(wlroots) >= 0.17.0 with pkgconfig(wlroots) < 0.18)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(libdrm) >= 2.4.114
BuildRequires:  pkgconfig(pixman-1) >= 0.42.0
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.32
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.22


Packager:       Atmois <atmois@atmois.com>
 
%description
%{summary}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} == %{version}-%{release}
# for examples
Suggests:       gcc
Suggests:       meson >= 0.58.0
Suggests:       pkgconfig(wayland-egl)

%description    devel
Development files for %{name}.


%prep
%autosetup -N

%build
MESON_OPTIONS=(
    # Disable options requiring extra/unpackaged dependencies
    -Dexamples=false
    -Dwerror=false
)
%{meson} "${MESON_OPTIONS[@]}"
%{meson_build}

%install
%{meson_install}

%check
%{meson_test}


%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.*


%files  devel
%{_includedir}/scenefx
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
