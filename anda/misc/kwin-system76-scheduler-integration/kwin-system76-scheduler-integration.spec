%global debug_package %nil

Name:       kwin-system76-scheduler-integration

%global forgeurl https://github.com/maxiberta/%{name}
%global commit 093a269670275feaa240d02c712f1ec8b812fd80
%global date 20240320
%forgemeta

Version:    0.1
Release:    5%?dist
Summary:    Notify the System76 Scheduler which app has focus so it can be prioritized
License:    MIT
URL:        %forgeurl
Source0:    %forgesource
Source1:    com.system76.Scheduler.dbusproxy.service
Requires:   bash dbus-tools system76-scheduler kde-cli-tools systemd kf6-kconfig-core
BuildRequires: systemd-rpm-macros

%description
System76 Scheduler is a service which optimizes Linux's CPU scheduler and
automatically assigns process priorities for improved desktop responsiveness.

This KWin Script interactively notifies System76 Scheduler which app has focus
via D-Bus, so it is prioritized.

%prep
%forgeautosetup

%build

%install
mkdir -p %buildroot%_datadir/kwin/scripts/%{name}/
mkdir -p %buildroot%_libexecdir/
mkdir -p %buildroot%_userunitdir/

cp -r contents %buildroot%_datadir/kwin/scripts/%{name}/
cp -r metadata.json %buildroot%_datadir/kwin/scripts/%{name}/
cp -r system76-scheduler-dbus-proxy.sh %buildroot%_libexecdir/

install -Dm644 %SOURCE1 %buildroot%_userunitdir/com.system76.Scheduler.dbusproxy.service

%post
%systemd_user_post com.system76.Scheduler.dbusproxy.service

%preun
%systemd_user_preun com.system76.Scheduler.dbusproxy.service

%postun
%systemd_user_postun_with_restart com.system76.Scheduler.dbusproxy.service

%files
%license LICENSE
%doc README.md
%config %_userunitdir/com.system76.Scheduler.dbusproxy.service
%_libexecdir/system76-scheduler-dbus-proxy.sh
%_datadir/kwin/scripts/%{name}/

%changelog
%autochangelog
