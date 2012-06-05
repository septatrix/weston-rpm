%define gitdate 20120424

Name:           weston
Version:        0.89
Release:        0.4%{?alphatag}%{?dist}
Summary:        Reference compositor for Wayland
Group:          User Interface/X
License:        BSD and CC-BY-SA
URL:            http://wayland.freedesktop.org/
Source0:        %{name}-%{gitdate}.tar.bz2
Source1:        make-git-snapshot.sh

BuildRequires:  autoconf
BuildRequires:  cairo-devel >= 1.10.0
BuildRequires:  glib2-devel
BuildRequires:  libdrm-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2
BuildRequires:  libtool
%if 0%{?fedora} < 18
BuildRequires:  libudev-devel
%endif
BuildRequires:  libwayland-client-devel
BuildRequires:  libwayland-server-devel
BuildRequires:  libxcb-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  mesa-libEGL-devel >= 8.1
BuildRequires:  mesa-libgbm-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mesa-libwayland-egl-devel
BuildRequires:  mtdev-devel
BuildRequires:  pam-devel
BuildRequires:  pixman-devel
BuildRequires:  poppler-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  systemd-devel

%description
Weston is the reference wayland compositor that can run on KMS, under X11
or under another compositor.

%prep
%setup -q -n weston-%{gitdate}

%build
autoreconf -ivf
%configure --disable-static --disable-setuid-install
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name \*.la | xargs rm -f

%files
%defattr(-,root,root,-)
%doc README
%doc data/COPYING
%{_bindir}/weston
%{_bindir}/weston-launch
%{_bindir}/weston-terminal
%dir %{_libdir}/weston
%{_libdir}/weston/desktop-shell.so
%{_libdir}/weston/drm-backend.so
%{_libdir}/weston/tablet-shell.so
%{_libdir}/weston/wayland-backend.so
%{_libdir}/weston/x11-backend.so
%{_libdir}/weston/xserver-launcher.so
%{_libexecdir}/weston-*
%dir %{_datadir}/weston
%{_datadir}/weston/*.png
%{_datadir}/weston/wayland.svg

%changelog
* Tue Jun 05 2012 Adam Jackson <ajax@redhat.com> 0.89-0.4
- Rebuild for new libudev
- Conditional buildreq for libudev-devel

* Wed Apr 25 2012 Richard Hughes <richard@hughsie.com> 0.89-0.3
- New package addressing Fedora package review concerns.

* Tue Apr 24 2012 Richard Hughes <richard@hughsie.com> 0.89-0.2
- Initial package for Fedora package review.
