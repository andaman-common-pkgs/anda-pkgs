%define commit bb6165c1ad640ea7c45ecff2efbc01b48eaf2445

Name:           openasar-canary
Version:        nightly.%{autogitdate}
Release:        1%{?dist}
Summary:        OpenAsar is a rewrite of part of Discord's desktop code, making it snappier and include more features like further customization and theming

License:        MIT
URL:            https://github.com/GooseMod/OpenAsar
Source0:        %{url}/releases/download/nightly/app.asar

Requires:       discord-canary

%description
%{summary}.

%prep


%build


%install
mkdir -p %{buildroot}%{_datadir}/openasar-canary
cp -v %{SOURCE0} %{buildroot}%{_datadir}/openasar-canary/app.asar


# trigger on discord-canary
%triggerin -- discord-canary
cp %{_datadir}/openasar-canary/app.asar %{_datadir}/discord-canary/resources/app.asar



%files
%{_datadir}/openasar-canary/app.asar



%changelog
* Thu Oct 20 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- 
