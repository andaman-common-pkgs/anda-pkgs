%global commit 5ac7f04f6876097aa8c3cf9af033d609a8a49944
%global commit_date 20240824
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-non-spatial-input
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Tools you can easily snap together to get non-spatial input into stardust.
URL:            https://github.com/StardustXR/non-spatial-input
Source0:        %url/archive/%commit/non-spatial-input-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold libudev-devel g++ libinput-devel libxkbcommon-x11-devel

Provides:       non-spatial-input
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Tools you can easily snap together to get non-spatial input into stardust.

%prep
%autosetup -n non-spatial-input-%commit
%cargo_prep_online

%build

%install
cd non-spatial-input
%cargo_install

%files
%_bindir/non-spatial-input
%license LICENSE
%doc README.md

%changelog
* Mon Sep 9 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR non-spatial-input
