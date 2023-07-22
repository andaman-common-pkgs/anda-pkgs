%define debug_package %nil

Name:		args-hxx
Version:	6.4.6
Release:	1%?dist
Summary:	A simple header-only C++ argument parser library
License:	MIT
URL:		https://github.com/Taywee/args
Source0:	%url/archive/refs/tags/%version.tar.gz
BuildRequires:	make doxygen gcc-c++ cmake

%description
A simple header-only C++ argument parser library. Supposed to be flexible and
powerful, and attempts to be compatible with the functionality of the Python
standard argparse library (though not necessarily the API).

%prep
%autosetup -n args-%version

%build
%cmake
%cmake_build
make doc/man

%install
%cmake_install
make installman DESTDIR=%buildroot%_prefix

%files

%changelog
%autochangelog
