Name:           mpc-qt
Version:        22.02
Release:        1
Summary:        Media Player Classic Qute Theater
License:        GPLv2+
Group:          Video/Players
Url:            https://github.com/mpc-qt/mpc-qt
Source0:        https://github.com/mpc-qt/mpc-qt/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  qmake5
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(mpv)

%description
A clone of Media Player Classic reimplemented in Qt.

%prep
%setup -q -n %{name}-%{version}

rm -rf mpv-dev

%build
%qmake_qt5 MPCQT_VERSION=%{version} PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md DOCS/ipc.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/%{name}_*.qm
%{_iconsdir}/hicolor/scalable/*/%{name}.svg
