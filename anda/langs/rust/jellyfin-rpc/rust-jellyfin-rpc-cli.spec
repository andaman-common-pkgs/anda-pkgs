# Generated by rust2rpm 26
%bcond_without check
%bcond_without mold

%global crate jellyfin-rpc-cli

Name:           rust-jellyfin-rpc-cli
Version:        1.2.2
Release:        %autorelease
Summary:        Displays the content you're currently watching on Discord!

License:        GPL-3.0-or-later
URL:            https://crates.io/crates/jellyfin-rpc-cli
Source0:        %{crates_source}
Source1:        https://raw.githubusercontent.com/Radiicall/jellyfin-rpc/%version/LICENSE
Packager:       madonuko <mado@fyralabs.com>

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Displays the content you're currently watching on Discord!.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        GPL-3.0-or-later
Provides:       jellyfin-rpc

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/jellyfin-rpc

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep_online

%build
#{cargo_license_summary_online}
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install

install -Dpm644 %SOURCE1 %buildroot%_datadir/licenses/%name/LICENSE

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Aug 15 2024 madonuko <mado@fyralabs.com> - 1.2.2-1
- Initial package
