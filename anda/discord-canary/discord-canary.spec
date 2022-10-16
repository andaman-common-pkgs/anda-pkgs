Name:           discord-canary
Version:        0.0.139
Release:        %autorelease
Summary:        Free Voice and Text Chat for Gamers.
URL:            discord.com
Source0:        https://dl-canary.discordapp.net/apps/linux/%{version}/discord-canary-%{version}.tar.gz
License:        https://discord.com/terms
Requires:       libatomic, glibc, alsa-lib, GConf2, libnotify, nspr >= 4.13, nss >= 3.27, libstdc++, libX11 >= 1.6, libXtst >= 1.2, libappindicator, libcxx, libXScrnSaver
Group:          Applications/Internet
ExclusiveArch:  x86_64
%description
Imagine a place where you can belong to a school club, a gaming group, or a worldwide art community. Where just you and a handful of friends can spend time together. A place that makes it easy to talk every day and hang out more often.

%prep
%autosetup -n DiscordCanary


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/discord-canary
cp -rv * %{buildroot}%{_datadir}/discord-canary
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/pixmaps
install discord-canary.desktop %{buildroot}%{_datadir}/applications/discord-canary.desktop
install discord.png %{buildroot}%{_datadir}/pixmaps/discord-canary.png

%files
%{_datadir}/discord-canary/
%{_datadir}/applications/discord-canary.desktop
%{_datadir}/pixmaps/discord-canary.png

%changelog
* Sun Oct 16 2022 windowsboy111 <wboy111@outlook.com> - 0.0.139
- Repackaged for Terra

* Tue Feb 22 2022 Ultramarine Release Tracking Service - 0.0.133-2
- Mass rebuild for release um36

* Sat Nov 20 2021 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial release
