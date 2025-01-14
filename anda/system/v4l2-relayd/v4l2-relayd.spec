%global commit 2e4d5c9ba53bfe8cfe16ea91932c8e5ecb090a87
%global commitdate 20220126
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           v4l2-relayd
Summary:        Utils for relaying the video stream between two video devices
Version:        
Release:        1%?dist
License:        GPL-2.0-only
Source0:        https://gitlab.com/vicamo/v4l2-relayd//-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        v4l2-relayd.preset
### RPM Fusion | [v4l2-relayd] Set output stream to I420
## https://lists.rpmfusion.org/archives/list/rpmfusion-commits@lists.rpmfusion.org/thread/VUMAJABDYISF3UVOSESSFYQBAMQK7VKY/
Patch0:         0000-set-new-offset.patch
BuildRequires:  systemd-rpm-macros
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  glib2-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  systemd
Requires:       v4l2loopback

%description
This is used to relay the input GStreamer source to an output source or a V4L2 device.

%prep
%autosetup -p1 -n %{name}-%{commit}
autoreconf --force --install --verbose

%build
%configure
%make_build

%install
%make_install modprobedir=%{_modprobedir}
sed -i '/^EnvironmentFile=\/etc\/default\/v4l2-relayd/a EnvironmentFile=-\/run\/v4l2-relayd' %{buildroot}%{_unitdir}/v4l2-relayd.service
sed -i 's/videoconvert/videoconvert ! video\/x-raw,format=I420/g' %{buildroot}%{_unitdir}/v4l2-relayd.service
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_presetdir}/95-v4l2-relayd.preset

%post
%systemd_post v4l2-relayd.service

%preun
%systemd_preun v4l2-relayd.service

%postun
%systemd_postun_with_restart v4l2-relayd.service

%files
%license LICENSE
%{_bindir}/v4l2-relayd
%{_sysconfdir}/default/v4l2-relayd
%{_modprobedir}/v4l2-relayd.conf
%{_modulesloaddir}/v4l2-relayd.conf
%{_unitdir}/v4l2-relayd.service
%{_presetdir}/95-v4l2-relayd.preset

%changelog
%autochangelog
