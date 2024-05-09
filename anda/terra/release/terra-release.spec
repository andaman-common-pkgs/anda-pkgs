Name:           terra-release
Version:        40
Release:        3
Summary:        Release package for Terra

License:        MIT
URL:            https://terra.fyralabs.com
Source0:        terra.repo
Source1:        terra.urls
BuildArch:      noarch

Requires:       system-release(%{version})

%description
Release package for Terra, containing the Terra repository configuration.

%prep

%build

%install
install -D -p -m 0644 -t %{buildroot}%{_sysconfdir}/yum.repos.d %{SOURCE0}
install -D -p -m 0644 -t %{buildroot}%{_sysconfdir}/debuginfod %{SOURCE1}

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/terra.repo
%config(noreplace) %{_sysconfdir}/debuginfod/terra.urls

%changelog
* Mon Feb 26 2024 Lleyton Gray <lleyton@fyralabs.com> - 39-3
- Add debuginfod url

* Thu Nov 16 2023 Lleyton Gray <lleyton@fyralabs.com> - 39-2
- Add source repository

* Wed Aug 16 2023 Lleyton Gray <lleyton@fyralabs.com> - 39-1
- Update for Terra 39

* Sat May 6 2023 Lleyton Gray <lleyton@fyralabs.com> - 38-1
- Initial package
