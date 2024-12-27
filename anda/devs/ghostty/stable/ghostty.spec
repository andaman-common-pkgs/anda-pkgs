Name:           ghostty
Version:        1.0.0
Release:        1%?dist
Summary:        A fast, native terminal emulator written in Zig
License:        MIT
URL:            https://ghostty.org/
Source0:        https://release.files.ghostty.org/%version/ghostty-source.tar.gz
#Patch0:         pkgconfig-libadwaita-1.diff
#Patch1:         use-pkg-config.diff
Patch2:         no-strip.diff
BuildRequires:  zig
BuildRequires:  gtk4-devel libadwaita-devel
#BuildRequires:  pkg-config
#BuildRequires:  pkgconfig(harfbuzz)
#BuildRequires:  pkgconfig(fontconfig)
#BuildRequires:  pkgconfig(libpng)
#BuildRequires:  pkgconfig(zlib)
#BuildRequires:  pkgconfig(oniguruma)
#BuildRequires:  pkgconfig(glslang)
# Not in Fedora
#BuildRequires:  pkgconfig(spirv-cross)
#BuildRequires:  pkgconfig(simdutf)
#BuildRequires:  pkgconfig(libxml-2.0)
Requires:       %name-terminfo
Suggests:       %name-shell-integration
Conflicts:      ghostty-nightly
Packager:       ShinyGil <rockgrub@protonmail.com>

%description
👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.

%package        bash-completion
Summary:        Ghostty Bash completion
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description    bash-completion
%summary.

%package        fish-completion
Summary:        Ghostty Fish completion
Requires:       %{name}
Requires:       fish
Supplements:    (%{name} and fish)

%description    fish-completion
%summary.

%package        zsh-completion
Summary:        Ghostty Zsh completion
Requires:       %{name}
Requires:       zsh
Supplements:    (%{name} and zsh)

%description    zsh-completion
%summary.

%package        shell-integration
Summary:        Ghostty shell integration
Requires:       %{name}
Supplements:    %{name}

%package        terminfo
Summary:        Ghostty terminfo
Requires:       %{name}
Supplements:    %{name}

%prep
%autosetup -n ghostty-source -p1

%build

%install
zig build \
    -Doptimize=ReleaseFast --release=fast \
    --prefix %buildroot%_prefix --verbose

%files
%doc README.md
%license LICENSE
%_bindir/ghostty
%_datadir/applications/com.mitchellh.ghostty.desktop
%_datadir/bat/syntaxes/ghostty.sublime-syntax
%_datadir/ghostty/
%_datadir/kio/servicemenus/com.mitchellh.ghostty.desktop
%_datadir/nvim/site/ftdetect/ghostty.vim
%_datadir/nvim/site/ftplugin/ghostty.vim
%_datadir/nvim/site/syntax/ghostty.vim
%_datadir/vim/vimfiles/ftdetect/ghostty.vim
%_datadir/vim/vimfiles/ftplugin/ghostty.vim
%_datadir/vim/vimfiles/syntax/ghostty.vim
%_datadir/terminfo/x/xterm-ghostty
%_iconsdir/hicolor/16x16/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/16x16@2/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/32x32/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/32x32@2/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/128x128/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/128x128@2/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/256x256/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/256x256@2/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/512x512/apps/com.mitchellh.ghostty.png
%_mandir/man1/ghostty.1.gz
%_mandir/man5/ghostty.5.gz

%files bash-completion
%bash_completions_dir/ghostty.bash

%files fish-completion
%fish_completions_dir/ghostty.fish

%files zsh-completion
%zsh_completions_dir/_ghostty

%files shell-integration
%_datadir/ghostty/shell-integration/bash/bash-preexec.sh
%_datadir/ghostty/shell-integration/bash/ghostty.bash
%_datadir/ghostty/shell-integration/elvish/lib/ghostty-integration.elv
%_datadir/ghostty/shell-integration/fish/vendor_conf.d/ghostty-shell-integration.fish
%_datadir/ghostty/shell-integration/zsh/.zshenv
%_datadir/ghostty/shell-integration/zsh/ghostty-integration

%files terminfo
%_datadir/terminfo/ghostty.termcap
%_datadir/terminfo/ghostty.terminfo
%_datadir/terminfo/g/ghostty
%_datadir/terminfo/x/xterm-ghostty

%changelog
* Thu Dec 26 2024 ShinyGil <rockgrub@protonmail.com>
- Initial package
