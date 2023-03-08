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

mkdir -p %{buildroot}%{_datadir}/applications
install -m 0755 src/resources/%{name}.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -m 0755 src/resources/%{name}_32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
install -m 0755 src/resources/%{name}_64x64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -m 0755 src/resources/%{name}_128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 0755 src/resources/%{name}_256x256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/512x512/apps
install -m 0755 src/resources/%{name}_512x512.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png

%changelog
* Wed Mar 8 2023 Martin Jungblut Schreiner <martinjungblut@gmail.com> - 1.15-2
- Add .desktop entry and icons.

* Sat Mar 4 2023 Martin Jungblut Schreiner <martinjungblut@gmail.com> - 1.15-1
- First release.