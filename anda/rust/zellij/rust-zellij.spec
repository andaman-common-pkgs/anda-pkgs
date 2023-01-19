# Generated by rust2rpm 22
%global debug_package %{nil}
%bcond_without check
%define sccache_prep (\
export CC="%{_sccache} gcc" \
export CXX="%{_sccache} g++" \
export RUSTC_WRAPPER="sccache" \
\
export SCCACHE_BUCKET=%{?sccache_bucket}\
export SCCACHE_ENDPOINT=%{?sccache_endpoint}\
export AWS_SECRET_ACCESS_KEY=%{?sccache_secret}\
export AWS_ACCESS_KEY_ID=%{?sccache_accesskey}\
export SCCACHE_S3_USE_SSL=true\
)


%define cargo_prep_online_sccache (\
set -eu \
%{__mkdir} -p .cargo \
cat > .cargo/config << EOF \
[build]\
rustc = "%{__rustc}"\
rustc-wrapper = "%{_sccache}"\
rustdoc = "%{__rustdoc}"\
\
[env]\
CFLAGS = "%{build_cflags}"\
CXXFLAGS = "%{build_cxxflags}"\
LDFLAGS = "%{build_ldflags}"\
\
[install]\
root = "%{buildroot}%{_prefix}"\
\
[term]\
verbose = true\
\
[source]\
\
[source.local-registry]\
directory = "%{cargo_registry}"\
\
EOF\
%{__rm} -f Cargo.lock \
%{__rm} -f Cargo.toml.orig \
)
%global crate zellij

Name:           rust-zellij
Version:        0.34.4
Release:        %autorelease
Summary:        Terminal workspace with batteries included

License:        MIT
URL:            https://crates.io/crates/zellij
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  anda-srpm-macros
BuildRequires:  rust-packaging
BuildRequires:  openssl-devel
BuildRequires:  sccache

#BuildRequires:  external:crate:sccache

%global _description %{expand:
Terminal workspace with batteries included.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE.md
%doc README.md
%{_bindir}/zellij

%prep
%autosetup -n %{crate}-%{version_no_tilde}
%cargo_prep_online_sccache


%build
%sccache_prep
%cargo_build

%install
%cargo_install

%changelog
%autochangelog
