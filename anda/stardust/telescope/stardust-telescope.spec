%define debug_package %nil

%global commit 7846913e5068591973d479464f21cfa6b82bb2fd
%global commit_date 20241023
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           stardust-telescope
Version:        %commit_date.git~%shortcommit
Release:        1%?dist
Summary:        See the stars! Easy stardust setups to run on your computer. 
License:        MIT
URL:            https://github.com/StardustXR/telescope
Source0:		%url/archive/%commit.tar.gz
Requires:       bash
Requires:       stardust-server
Requires:       stardust-gravity
Requires:       stardust-black-hole
Requires:       stardust-protostar
Requires:       xwayland-satellite
BuildArch:      noarch

%description
See the stars! Easy stardust setups to run on your computer.

%prep
%autosetup -n telescope-%commit

%build

%install
install -Dm755 scripts/telescope          %buildroot%_bindir/telescope
install -Dm755 scripts/_telescope_startup %buildroot%_bindir/_telescope_startup

%files
%doc README.md
%license LICENSE
%_bindir/telescope
%_bindir/_telescope_startup