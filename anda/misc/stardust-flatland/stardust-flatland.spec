%global commit b83f2eced868fe71248ba7681df978698eb978f0
%global commit_date 20240824
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}
%define __os_install_post %{nil}

Name:           stardust-flatland
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Flatland for StardustXR.
URL:            https://github.com/StardustXR/flatland
Source0:        https://github.com/StardustXR/flatland/archive/%commit/flatland-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold
Requires:       libgcc glibc

Provides:       flatland
Conflicts:      flatland

%description
Flatland for StardustXR.

%prep
%autosetup -n flatland-%commit
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install

%files
%_bindir/flatland
%license LICENSE
%doc README.md

%changelog
* Sat Sep 7 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR Flatland
