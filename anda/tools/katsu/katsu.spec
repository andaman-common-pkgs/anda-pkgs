Name:			katsu
Version:		0.1.0
Release:		1%?dist
Summary:		The vicious image builder
License:		MIT
URL:			https://github.com/FyraLabs/katsu
Source0:		%url/archive/refs/tags/%version.tar.gz
Requires:		xorriso clang-devel dracut limine grub2 systemd-devel squashfs-tools
Requires:		dracut-live dracut-config-generic dracut-config-rescue grub2-tools-extra dracut-squash
BuildRequires:	cargo rust-packaging

%description
Katsu is a tool for building bootable images from RPM based systems.
It is an alternative to Lennart Poettering's mkosi tool, designed to be robust,
fast, and easy to use while still providing many output formats.

%prep
%autosetup

%build
%(echo "%{cargo_build}" | sed 's@--profile rpm@--profile release@g')

%install
%cargo_install

%files
%doc README.md
%license LICENSE
%_bindir/katsu

%changelog
%autochangelog
