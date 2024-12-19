# Generated by go2rpm 1.14.0
%bcond check 0
%bcond bootstrap 0

#if %{with bootstrap}
%global debug_package %{nil}
#endif

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/savedra1/clipse
%global goipath         github.com/savedra1/clipse
Version:                1.1.0

%gometa -f

%global common_description %{expand:
Configurable TUI clipboard manager for Unix.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md examples resources/library.md\\\
                        resources/test_data/top_secret_credentials.txt

Name:           golang-github-savedra1-clipse
Release:        %autorelease
Summary:        Configurable TUI clipboard manager for Unix
Provides:       clipse
Packager:       madonuko <mado@fyralabs.com>
License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%autosetup -p1 -n clipse-%version
%go_prep_online

#if %{without bootstrap}
#generate_buildrequires
#go_generate_buildrequires
#endif

%if %{without bootstrap}
%build
mkdir -p build/bin
go build -ldflags="-linkmode=external" -o build/bin/%{name}
%endif

%install
#gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                 %{buildroot}%{_bindir}
install -m 0755 -vp build/bin/%name %{buildroot}%{_bindir}/clipse
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
%doc CHANGELOG.md README.md
%{_bindir}/clipse
%endif

#gopkgfiles

%changelog
%autochangelog
