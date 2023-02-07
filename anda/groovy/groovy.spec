Name:			groovy
Version:		4.0.7
Release:		1%{?dist}
Summary:		A multi-faceted language for the Java platform
BuildArch:		noarch
URL:			https://groovy-lang.org/
License:		Apache-2.0
BuildRequires:	gendesk unzip
Requires:		bash java-latest-openjdk
Recommends:		groovy-docs
Source0:		https://groovy.jfrog.io/artifactory/dist-release-local/groovy-zips/apache-groovy-binary-%{version}.zip

%description
Apache Groovy is a powerful, optionally typed and dynamic language, with static-typing and static compilation capabilities, for the Java platform aimed at improving developer productivity thanks to a concise, familiar and easy to learn syntax. It integrates smoothly with any Java program, and immediately delivers to your application powerful features, including scripting capabilities, Domain-Specific Language authoring, runtime and compile-time meta-programming and functional programming. 

%prep
unzip %{SOURCE0}
gendesk -f -n --pkgname %{name} --pkgdesc 'Groovy programming language' --exec groovyConsole --name 'Groovy Console'

for f in bin/*; do
	sed 's:bin/env\ sh:bin/env\ sh\nGROOVY_HOME=/usr/share/groovy\nexport _JAVA_OPTIONS="-Dawt.useSystemAAFontSettings=gasp $_JAVA_OPTIONS":' -i "$f"
done

%build

%install
# Create the directories and package the files
install -d %{buildroot}/usr/share/groovy %{buildroot}/usr/bin
cp -r lib conf %{buildroot}/usr/share/groovy
cp bin/* %{buildroot}/usr/bin
rm %{buildroot}/usr/bin/*completion
install -Dm644 bin/*completion -t %{buildroot}/usr/share/bash-completion/completions

# Remove all DOS/Windows batch files
find %{buildroot} -name '*.bat' -exec rm {} \;

# Package the license file
install -Dm644 LICENSE -t %{buildroot}/usr/share/licenses/%{name}

# Package the desktop shortcut for Groovy Console
install -Dm644 %{name}.desktop -t %{buildroot}/usr/share/applications
