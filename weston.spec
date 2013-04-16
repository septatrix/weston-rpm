#define gitdate 20120424

Name:           weston
Version:        1.1.0
Release:        1%{?alphatag}%{?dist}
Summary:        Reference compositor for Wayland
Group:          User Interface/X
License:        BSD and CC-BY-SA
URL:            http://wayland.freedesktop.org/
%if 0%{?gitdate}
Source0:        %{name}-%{gitdate}.tar.bz2
%else
Source0:        http://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz
%endif
Source1:        make-git-snapshot.sh

# git diff-tree -p 1.0.6..origin/1.0 > weston-$(git describe origin/1.0).patch
#Patch0:		weston-1.0.5-11-g9a576c3.patch

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
BuildRequires:	libunwind-devel
BuildRequires:  libwayland-client-devel
BuildRequires:  libwayland-server-devel >= 1.1.0
BuildRequires:  libwayland-cursor-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libxkbcommon-devel >= 0.1.0-8
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

%package devel
Summary: Common headers for weston
License: MIT
%description devel
Common headers for weston

%prep
%setup -q -n %{name}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}
#%patch0 -p1 -b .git

%build
# temporary force to pick up configure.ac changes
%if 1 || 0%{?gitdate}
autoreconf -ivf
%endif
%configure --disable-static --disable-setuid-install --enable-xwayland
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name \*.la | xargs rm -f

%files
%defattr(-,root,root,-)
%doc README
%doc data/COPYING
%{_bindir}/weston
%{_bindir}/weston-info
%{_bindir}/weston-launch
%{_bindir}/weston-terminal
%{_bindir}/wcap-decode
%dir %{_libdir}/weston
%{_libdir}/weston/desktop-shell.so
%{_libdir}/weston/drm-backend.so
%{_libdir}/weston/fbdev-backend.so
%{_libdir}/weston/headless-backend.so
%{_libdir}/weston/tablet-shell.so
%{_libdir}/weston/wayland-backend.so
%{_libdir}/weston/x11-backend.so
%{_libdir}/weston/xwayland.so
%{_libexecdir}/weston-*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man7/*.7*
%dir %{_datadir}/weston
%{_datadir}/weston/*.png
%{_datadir}/weston/wayland.svg

%files devel
%defattr(-,root,root,-)
%{_includedir}/weston/compositor.h
%{_includedir}/weston/config-parser.h
%{_includedir}/weston/matrix.h
%{_includedir}/weston/version.h
%{_libdir}/pkgconfig/weston.pc

%changelog
* Tue Apr 16 2013 Richard Hughes <richard@hughsie.com> 1.1.0-1
- weston 1.1.0

* Wed Mar 27 2013 Richard Hughes <richard@hughsie.com> 1.0.6-1
- weston 1.0.6

* Thu Feb 21 2013 Adam Jackson <ajax@redhat.com> 1.0.5-1
- weston 1.0.5+ (actually tip of 1.0 branch)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.0.3-2
- rebuild due to "jpeg8-ABI" feature drop

* Wed Jan 02 2013 Adam Jackson <ajax@redhat.com> 1.0.3-1
- weston 1.0.3

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.0.0-2
- rebuild against new libjpeg

* Tue Oct 23 2012 Adam Jackson <ajax@redhat.com> 1.0.0-1
- weston 1.0.0

* Thu Oct 18 2012 Adam Jackson <ajax@redhat.com> 0.99.0-1
- weston 0.99.0

* Mon Sep 17 2012 Thorsten Leemhuis <fedora@leemhuis.info> 0.95.0-3
- add libXcursor-devel as BR

* Mon Sep 17 2012 Thorsten Leemhuis <fedora@leemhuis.info> 0.95.0-2
- rebuild

* Mon Sep 17 2012 Thorsten Leemhuis <fedora@leemhuis.info> 0.95.0-1
- Update to 0.95.0
- enable xwayland
- make it easier to switch between a release and a git snapshot in spec file

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.89-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 05 2012 Adam Jackson <ajax@redhat.com> 0.89-0.4
- Rebuild for new libudev
- Conditional buildreq for libudev-devel

* Wed Apr 25 2012 Richard Hughes <richard@hughsie.com> 0.89-0.3
- New package addressing Fedora package review concerns.

* Tue Apr 24 2012 Richard Hughes <richard@hughsie.com> 0.89-0.2
- Initial package for Fedora package review.
