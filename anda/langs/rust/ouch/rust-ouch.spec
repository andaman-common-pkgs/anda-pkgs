# Generated by rust2rpm 25
%bcond_without check

%global crate ouch

Name:           rust-ouch
Version:        0.5.1
Release:        1%{?dist}
Summary:        Command-line utility for easily compressing and decompressing files and directories

License:        MIT
URL:            https://crates.io/crates/ouch
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          ouch-fix-metadata-auto.diff

BuildRequires:  anda-srpm-macros cargo-rpm-macros >= 24
BuildRequires:  gcc-c++

%global _description %{expand:
A command-line utility for easily compressing and decompressing files
and directories.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc README.md
%{_bindir}/ouch

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep_online

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
