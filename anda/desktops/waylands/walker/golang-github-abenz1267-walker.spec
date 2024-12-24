# Generated by go2rpm 1.14.0
%bcond check 0
%bcond bootstrap 0

%global debug_package %{nil}

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/abenz1267/walker
%global goipath         github.com/abenz1267/walker
Version:                0.11.2

%gometa -f

%global common_description %{expand:
Multi-Purpose Launcher with a lot of features. Highly Customizable and fast.}

%global golicenses      LICENSE
%global godocs          README.md cmd/version.txt

Name:           golang-github-abenz1267-walker
Release:        %autorelease
Summary:        Multi-Purpose Launcher with a lot of features. Highly Customizable and fast

License:        MIT
URL:            %{gourl}
Source:         %{gosource}
Provides:       walker
Packager:       madonuko <mado@fyralabs.com>
Requires:       gtk4-layer-shell
BuildRequires:  anda-srpm-macros
BuildRequires:  gtk4-devel
BuildRequires:  gtk4-layer-shell-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  pkgconfig(vips)

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1
%go_prep_online


%build
%go_build_online cmd/walker.go

%install
#gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                         %{buildroot}%{_bindir}
install -m 0755 -vp build/bin/cmd/walker.go %{buildroot}%{_bindir}/walker
%endif

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%if %{without bootstrap}
%files
%license LICENSE
%doc README.md
%{_bindir}/walker
%endif

#gopkgfiles

%changelog
* Tue Dec 24 2024 madonuko <mado@fyralabs.com> - 0.11.2-1
- Initial package