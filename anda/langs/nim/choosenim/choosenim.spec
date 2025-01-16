
Name:			choosenim
Version:		0.8.10
Release:		1%?dist
Summary:		Easily install and manage multiple versions of the Nim programming language
License:		BSD-3-Clause
URL:			https://github.com/nim-lang/choosenim
Source0:        %url/archive/refs/tags/v%version.tar.gz
# Fix for https://github.com/nim-lang/choosenim/issues/13
Patch0:         https://patch-diff.githubusercontent.com/raw/nim-lang/choosenim/pull/38.patch
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:  nim
BuildRequires:	git-core anda-srpm-macros

%description
choosenim installs the Nim programming language from official downloads and
sources, enabling you to easily switch between stable and development compilers.

%prep
%autosetup -p1
#? https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=choosenim
# we compile proxyexe in a separate step
sed -i -e '/static: compileProxyexe()/d' src/choosenimpkg/switcher.nim
%nim_prep

%build
%nim_c -p:/usr/lib/nim/dist/nimble/src/ -p:`pwd` src/choosenimpkg/proxyexe
strip src/choosenimpkg/proxyexe
%nim_c -p:/usr/lib/nim/dist/nimble/src/ -p:`pwd` src/choosenim

%install
install -Dm755 src/choosenim %buildroot%_bindir/choosenim


%files
%doc readme.md
%license LICENSE
%_bindir/choosenim

%changelog
%autochangelog
