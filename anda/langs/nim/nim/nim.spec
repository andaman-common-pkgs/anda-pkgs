%global csrc_commit 561b417c65791cd8356b5f73620914ceff845d10
%global debug_package %{nil}

Name:			nim
Version:		2.2.0
Release:		2%?dist
Summary:		Imperative, multi-paradigm, compiled programming language
License:		MIT and BSD
URL:			https://nim-lang.org
Source1:		nim.1
Source2:		nimgrep.1
Source3:		nimble.1
Source4:		nimsuggest.1
BuildRequires:	gcc mold git-core gcc-c++ nodejs openssl-devel pkgconfig(bash-completion) gc-devel pcre-devel
BuildRequires:  redhat-rpm-config
Requires:		gcc


%description
Nim is a compiled, garbage-collected systems programming language with a
design that focuses on efficiency, expressiveness, and elegance (in that
order of priority).


%package tools
Summary:	Tools for Nim programming language
%description tools
Nim is a compiled, garbage-collected systems programming language with a
design that focuses on efficiency, expressiveness, and elegance (in that
order of priority).

This package provides various tools, which help Nim programmers.

%ifarch x86_64
%package doc
Summary:	Documentation for Nim programming language
BuildArch:	noarch
%description doc
Nim is a compiled, garbage-collected systems programming language with a
design that focuses on efficiency, expressiveness, and elegance (in that
order of priority).

This package provides documentation and reference manual for the language
and its standard library.
%endif


%prep
rm -rf ./*
# using git clone to include submodules
git clone --recurse-submodules -j8 https://github.com/nim-lang/Nim -b v%version --depth 1 .
# hack
cp /usr/bin/mold /usr/bin/ld


%build
export CFLAGS="${CFLAGS} -Ofast"
export CXXFLAGS="${CXXFLAGS} -Ofast"
export FFLAGS="${FFLAGS} -Ofast"
export FCFLAGS="${FCFLAGS} -Ofast"

export PATH="$(pwd):$(pwd)/bin:${PATH}"

. ci/funs.sh
nimBuildCsourcesIfNeeded CFLAGS="${CFLAGS} -Ic_code -w -O3 -fno-strict-aliasing -fPIE" LDFLAGS="-ldl -lm -lrt -pie"

nim c --noNimblePath --skipUserCfg --skipParentCfg --hints:off -d:danger koch.nim
koch boot -d:release -d:nimStrictMode --lib:lib

%ifarch x86_64
koch docs &
%endif
(cd lib && nim c --app:lib -d:createNimRtl -d:release nimrtl.nim) &
koch tools -t:-fPIE -l:-pie &
nim c -d:danger -t:-fPIE -l:-pie nimsuggest/nimsuggest.nim &
wait

%ifarch x86_64
sed -i '/<link.*fonts.googleapis.com/d' doc/html/*.html
%endif


%install
export PATH="$(pwd):$(pwd)/bin:${PATH}"

# --main:compiler/nim.nim
bin/nim cc -d:nimCallDepthLimit=10000 -r tools/niminst/niminst --var:version=%ver --var:mingw=none scripts compiler/installer.ini

sh ./install.sh %buildroot/usr/bin

mkdir -p %buildroot/%_bindir %buildroot/%_datadir/bash-completion/completions %buildroot/usr/lib/nim %buildroot%_datadir
install -Dpm755 bin/nim{grep,suggest,pretty} %buildroot/%_bindir
install -Dpm644 tools/nim.bash-completion %buildroot/%_datadir/bash-completion/completions/nim
install -Dpm644 dist/nimble/nimble.bash-completion %buildroot/%_datadir/bash-completion/completions/nimble
install -Dpm644 -t%buildroot/%_mandir/man1 %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4
mv %buildroot%_bindir/nim %buildroot%_datadir/
ln -s %_datadir/nim/bin/nim %buildroot%_bindir/nim

%ifarch x86_64
mkdir -p %buildroot/%_docdir/%name/html || true
cp -a doc/html/*.html %buildroot/%_docdir/%name/html/ || true
cp tools/dochack/dochack.js %buildroot/%_docdir/%name/ || true
ln -s %_datadir/nim/doc %buildroot%_prefix/lib/nim/doc
%endif

cp -a lib %buildroot%_prefix/lib/
mv %buildroot%_prefix/lib/{lib,nim}
cp -a compiler %buildroot%_prefix/lib/nim
install -Dm644 nim.nimble %buildroot%_prefix/lib/nim/compiler
install -m755 lib/libnimrtl.so %buildroot%_prefix/lib/libnimrtl.so  # compiler needs
install -Dm644 config/* -t %buildroot/etc/nim
install -Dm755 bin/* -t %buildroot%_bindir
install -d %buildroot%_includedir
cp -a %buildroot%_prefix/lib/nim/lib/*.h %buildroot%_includedir
ln -s %_prefix/lib/nim %buildroot%_prefix/lib/nim/lib  # compiler needs lib from here
ln -s %_prefix/lib/nim/system.nim %_prefix/lib/system.nim  # nimsuggest bug
rm -rf %buildroot/nim || true
rm %buildroot%_bindir/*.bat || true
rm -rf %buildroot%_bindir/empty.txt

cp -r dist %buildroot%_datadir/nim/


%files
%license copying.txt dist/nimble/license.txt
%doc doc/readme.txt
%_sysconfdir/nim/
%_bindir/atlas
%_bindir/nim_dbg
%_bindir/nim-gdb
%_bindir/testament
%_bindir/nim
%_bindir/nimble
%_bindir/nim_csources_*
%_mandir/man1/nim.1*
%_mandir/man1/nimble.1*
%_prefix/lib/nim/
%_prefix/lib/libnimrtl.so
%_includedir/cycle.h
%_includedir/nimbase.h
%_datadir/nim
%bash_completions_dir/nim
%bash_completions_dir/nimble

%files tools
%license copying.txt
%_bindir/nimgrep
%_bindir/nimsuggest
%_bindir/nimpretty
%_mandir/man1/nimgrep.1*
%_mandir/man1/nimsuggest.1*

%ifarch x86_64
%files doc
%doc %_docdir/nim
%endif

%changelog
%autochangelog
