# qmake doesn't support debugsource detection
#undefine _debugsource_packages

Name:           mpc-qt

Version:        26.07
Release:        1
Summary:        Media Player Classic Qute Theater
License:        GPLv2+
Group:          Video/Players
Url:            https://github.com/mpc-qt/mpc-qt
Source0:        https://github.com/mpc-qt/mpc-qt/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	cmake
BuildRequires:	cmake(Qt6)
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
BuildRequires:	pkgconfig(libunwind)
BuildRequires:	boost-devel

%description
A clone of Media Player Classic reimplemented in Qt.

%prep
%autosetup -p1
rm -rf mpv-dev

%build
# specify the correct directory for finding unwind
%cmake -DCMAKE_CXX_FLAGS="-I/usr/include/libunwind"
%make_build

%install
%make_install -C build

%files
%doc README.md DOCS/ipc.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/io.github.mpc_qt.mpc-qt.desktop
%{_datadir}/applications/io.github.mpc_qt.mpc-qt_enqueue.desktop
%{_iconsdir}/hicolor/scalable/*/%{name}.svg
%{_datadir}/metainfo/io.github.mpc_qt.mpc-qt.metainfo.xml
