Name:		groovy-docs
Version:	3.0.9
Release:	1%{?dist}
Summary:	Documentation for the Groovy programming language
URL:		https://groovy-lang.org/
License:	Apache-2.0
BuildArch:	noarch
Source0:	https://groovy.jfrog.io/artifactory/dist-release-local/groovy-zips/apache-groovy-docs-%{version}.zip
BuildRequires: unzip

%description
%{summary}.

%prep
unzip %{SOURCE0}
find . -type f -exec chmod -x {} \;

%build

%install
install -d %{buildroot}/usr/share/doc/groovy-%{version}
cp -r groovy-%{version} %{buildroot}/usr/share/doc/

%files
%doc README.md
%license LICENSE
/usr/share/doc/groovy-%{version}

%changelog
* Tue Feb 7 2023 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package
