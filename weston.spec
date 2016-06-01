Name:           weston
Version:        1.11.0
Release:        1%{?dist}
Summary:        Reference compositor for Wayland
Group:          User Interface/X
License:        BSD and CC-BY-SA
URL:            http://wayland.freedesktop.org/
Source0:        http://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz

BuildRequires:  cairo-devel >= 1.10.0
BuildRequires:  glib2-devel
BuildRequires:  libdrm-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2
BuildRequires:  libinput-devel >= 0.8
# libunwind available only on selected arches
%ifarch %{arm} aarch64 hppa ia64 mips ppc %{power64} %{ix86} x86_64
BuildRequires:	libunwind-devel
%endif
BuildRequires:  libva-devel
BuildRequires:  libwayland-client-devel
BuildRequires:  libwayland-server-devel >= 1.10.0
BuildRequires:  libwayland-cursor-devel
BuildRequires:  libwebp-devel
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
BuildRequires:  dbus-devel
BuildRequires:  lcms2-devel
BuildRequires:  colord-devel
BuildRequires:  freerdp-devel >= 2.0.0
BuildRequires:  wayland-protocols-devel

%description
Weston is the reference wayland compositor that can run on KMS, under X11
or under another compositor.

%package devel
Summary: Common headers for weston
License: MIT
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Common headers for weston

%prep
%setup -q

%build
%configure --disable-static --disable-setuid-install --enable-xwayland \
           --enable-rdp-compositor
make %{?_smp_mflags}

%install
%make_install

find $RPM_BUILD_ROOT -name \*.la | xargs rm -f

%files
%doc README
%license COPYING
%{_bindir}/weston
%{_bindir}/weston-info
%attr(4755,root,root) %{_bindir}/weston-launch
%{_bindir}/weston-terminal
%{_bindir}/wcap-decode
%dir %{_libdir}/weston
%{_libdir}/weston/cms-colord.so
%{_libdir}/weston/cms-static.so
%{_libdir}/weston/desktop-shell.so
%{_libdir}/weston/drm-backend.so
%{_libdir}/weston/fbdev-backend.so
%{_libdir}/weston/headless-backend.so
%{_libdir}/weston/rdp-backend.so
%{_libdir}/weston/gl-renderer.so
%{_libdir}/weston/wayland-backend.so
%{_libdir}/weston/x11-backend.so
%{_libdir}/weston/xwayland.so
%{_libdir}/weston/fullscreen-shell.so
%{_libdir}/weston/hmi-controller.so
%{_libdir}/weston/ivi-shell.so
%{_libexecdir}/weston-*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man7/*.7*
%dir %{_datadir}/weston
%{_datadir}/weston/*.png
%{_datadir}/weston/wayland.svg
%{_datadir}/wayland-sessions/weston.desktop

%files devel
%{_includedir}/weston/
%{_libdir}/pkgconfig/weston.pc

%changelog
* Wed Jun 01 2016 Kalev Lember <klember@redhat.com> - 1.11.0-1
- Update to 1.11.0

* Wed May 25 2016 Kalev Lember <klember@redhat.com> - 1.10.93-1
- Update to 1.10.93

* Wed May 18 2016 Kalev Lember <klember@redhat.com> - 1.10.92-1
- Update to 1.10.92

* Sun May 08 2016 Kalev Lember <klember@redhat.com> - 1.10.91-1
- Update to 1.10.91

* Fri Apr 22 2016 Adam Williamson <awilliam@redhat.com> - 1.10.0-2
- rebuild for changed freerdp sonames

* Thu Feb 18 2016 Kalev Lember <klember@redhat.com> - 1.10.0-1
- Update to 1.10.0

* Thu Feb 04 2016 Kalev Lember <klember@redhat.com> - 1.9.92-1
- Update to 1.9.92

* Mon Dec 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.9.0-3
- Rebuilt for libwebp soname bump

* Fri Nov 20 2015 Kalev Lember <klember@redhat.com> - 1.9.0-2
- Rebuilt for freerdp soname bump

* Tue Sep 22 2015 Kalev Lember <klember@redhat.com> - 1.9.0-1
- Update to 1.9.0
- Use make_install macro

* Wed Sep 16 2015 Kalev Lember <klember@redhat.com> - 1.8.93-1
- Update to 1.8.93

* Wed Sep 02 2015 Kalev Lember <klember@redhat.com> - 1.8.92-1
- Update to 1.8.92

* Fri Aug 21 2015 Kalev Lember <klember@redhat.com> - 1.8.91-1
- Update to 1.8.91
- Use license macro for COPYING

* Tue Jul 21 2015 Adam Jackson <ajax@redhat.com> 1.8.0-1
- weston 1.8.0

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Adam Jackson <ajax@redhat.com> 1.7.92-1
- weston 1.7.92
- Backport patches to fall back to argb buffer if no xrgb is available

* Tue Mar 10 2015 Peter Hutterer <peter.hutterer@redhat.com> - 1.7.0-2
- Rebuild for libinput soname bump

* Tue Feb 17 2015 Richard Hughes <rhughes@redhat.com> - 1.7.0-1
- Update to 1.7.0

* Fri Jan 16 2015 Peter Hutterer <peter.hutterer@redhat.com> 1.6.0-4
- Update to and require libinput 0.8

* Fri Dec 19 2014 Kevin Fenzi <kevin@scrye.com> 1.6.0-3
- Rebuild for new freerdp

* Sun Sep 21 2014 Kalev Lember <kalevlember@gmail.com> - 1.6.0-2
- Enable webp and vaapi support
- Install weston-launch as setuid root (#1064023)

* Sun Sep 21 2014 Kalev Lember <kalevlember@gmail.com> - 1.6.0-1
- Update to 1.6.0
- Pull in the main package for -devel subpackage

* Fri Sep 12 2014 Peter Hutterer <peter.hutterer@redhat.com> - 1.5.91-2
- Rebuild for libinput soname bump

* Fri Aug 22 2014 Kevin Fenzi <kevin@scrye.com> 1.5.91-1
- Update to 1.5.91

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 19 2014 Kevin Fenzi <kevin@scrye.com> 1.5.0-6
- Rebuild for new libfreerdp

* Sun Jun 15 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.5.0-5
- Enable DBus support so that logind integration actually works

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Dan Horák <dan[at]danny.cz> - 1.5.0-3
- libunwind available only on selected arches

* Wed May 21 2014 Richard Hughes <rhughes@redhat.com> - 1.5.0-1
- Weston 1.5.0

* Tue May 13 2014 Richard Hughes <rhughes@redhat.com> - 1.4.93-1
- Weston 1.4.93

* Mon Jan 27 2014 Adam Jackson <ajax@redhat.com> 1.4.0-2
- Rebuild for new sonames in libxcb 1.10

* Fri Jan 24 2014 Richard Hughes <rhughes@redhat.com> - 1.4.0-1
- Weston 1.4.0

* Mon Jan 20 2014 Richard Hughes <rhughes@redhat.com> - 1.3.93-1
- Weston 1.3.93

* Tue Dec 17 2013 Richard Hughes <rhughes@redhat.com> - 1.3.91-1
- Weston 1.3.91

* Mon Nov 25 2013 Lubomir Rintel <lkundrak@v3.sk> - 1.3.1-1
- Weston 1.3.1

* Thu Oct 03 2013 Adam Jackson <ajax@redhat.com> 1.2.0-3
- Build RDP backend if we have new enough freerdp (#991220)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 15 2013 Richard Hughes <rhughes@redhat.com> - 1.1.90-0.1.20130515
- Update to a git snapshot based on what will become 1.1.90

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
