Name:			depthcharge-tools
Version:		0.6.2
Release:		1%?dist
Summary:		Tools to manage the Chrome OS bootloader
License:		GPL-2.0-or-later
URL:			https://github.com/alpernebbi/depthcharge-tools
Source0:		%url/archive/%version/%version.tar.gz
Requires:		cgpt dtc gzip lz4 python3-setuptools uboot-tools vboot-utils xz
BuildRequires:	python3-setuptools
BuildArch:		noarch

%description
depthcharge-tools is a collection of tools that ease and automate interacting
with depthcharge, the Chrome OS bootloader.

%prep
%autosetup

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root=%buildroot

%files
%doc README.rst
%license LICENSE

%changelog
%autochangelog
