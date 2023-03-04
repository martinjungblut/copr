Name:           seergdb
Version:        1.15
Release:        1%{?dist}
Summary:        A GUI front-end for GNU gdb.

License:        GPLv3+
URL:            https://github.com/epasveer/seer

%undefine _disable_source_fetch
Source0:        https://github.com/epasveer/seer/archive/refs/tags/v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtcharts-devel

%description
A GUI front-end for GNU gdb.

%prep
%setup -n seer-%{version}

%build
mkdir -p src/build
cd src/build
%{set_build_flags}
cmake ..
make seergdb -j%{_smp_build_ncpus}

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 src/build/%{name} %{buildroot}/%{_bindir}/%{name}

#%ldconfig_scriptlets

%files
%{_bindir}/%{name}

%changelog
* Sat Mar 4 2023 Martin Jungblut Schreiner <martinjungblut@gmail.com> - 1.15-1
- First release.