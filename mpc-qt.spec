# qmake doesn't support debugsource detection
%undefine _debugsource_packages

Name:           mpc-qt

Version:        24.06
Release:        2
Summary:        Media Player Classic Qute Theater
License:        GPLv2+
Group:          Video/Players
Url:            https://github.com/mpc-qt/mpc-qt
Source0:        https://github.com/mpc-qt/mpc-qt/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:		mpc-qt-24.06-bogus-workaround-for-crash-on-video-playback.patch

BuildRequires:	cmake
BuildRequires:	cmake(Qt6)
BuildRequires:	qmake-qt6
BuildRequires:  cmake(Qt6DBus)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Help)
BuildRequires:  cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	qt6-qtbase-theme-gtk3

BuildRequires:  pkgconfig(mpv)

%description
A clone of Media Player Classic reimplemented in Qt.

%prep
%autosetup -p1
rm -rf mpv-dev

%build
qmake-qt6 MPCQT_VERSION=%{version} PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md DOCS/ipc.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/mpc-qt.desktop
%{_iconsdir}/hicolor/scalable/*/%{name}.svg
