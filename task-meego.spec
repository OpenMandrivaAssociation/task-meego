Name: task-meego
Version: 1.1
Release: %mkrel 1
Summary: Metapackage for the MeeGo experience
Group:Graphical desktop/Other
License: Various
URL: https://www.meego.com
BuildArch: noarch
Requires: bisho
Requires: chrome-meego-extension
Requires: clutter-imcontext
Requires: clutter-qt
Requires: gnome-control-center-netbook
Requires: gnome-settings-daemon
Requires: meego-help
Requires: meego-menus
Requires: meego-mutter
Requires: meego-netbook-icon-theme
Requires: meego-netbook-theme
Requires: meego-panel-applications
Requires: meego-panel-devices
Requires: meego-panel-devices-test
Requires: meego-panel-myzone
Requires: meego-panel-networks
Requires: meego-panel-pasteboard
Requires: meego-panel-people
Requires: meego-panel-status
Requires: meego-panel-web
Requires: meego-panel-zones
Requires: meego-session
Requires: meego-sound-theme
Requires: mutter-meego
Requires: mutter-meego-branding-upstream
Requires: mx
Requires: nbtk
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

%description
MeeGo is an open source project focused on building a Linux-based
platform optimized for the next generation of mobile devices including
netbooks, mobile internet devices, and in-vehicle infotainment systems.

This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal Moblin environment.

%package devel
Summary: MeeGo development metapackage
Group: Development/Other
Requires: bisho-devel
Requires: clutter-qt-devel
Requires: gnome-control-center-netbook-devel
Requires: gnome-settings-daemon-devel
Requires: libanerley-devel
Requires: libclutter-imcontext-devel
Requires: libjana-devel
Requires: libmeego-mutter-private-devel
Requires: libnbtk-devel
Requires: libpenge-devel
Requires: librest-devel
Requires: libsocialweb-devel
Requires: meego-panel-status-devel
Requires: mutter-meego-devel
Requires: mx-devel

%description devel
This package is a meta-package, meaning that its purpose is to contain
dependencies for Moblin development environment.

%files

%files devel
