%global apiver 4

Name:           weston
Version:        3.0.92
Release:        1%{?dist}
Summary:        Reference compositor for Wayland

License:        BSD and CC-BY-SA
URL:            http://wayland.freedesktop.org/
Source0:        http://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz

BuildRequires:  glib2-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(cairo-xcb)
BuildRequires:  pkgconfig(colord) >= 0.1.27
BuildRequires:  pkgconfig(dbus-1) >= 1.6
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freerdp2) >= 2.0.0
BuildRequires:  pkgconfig(gbm) >= 10.2
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libdrm) >= 2.4.30
BuildRequires:  pkgconfig(libinput) >= 0.8.0
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(libudev) >= 136
# libunwind available only on selected arches
%ifarch %{arm} aarch64 hppa ia64 mips ppc %{power64} %{ix86} x86_64
BuildRequires:	libunwind-devel
%endif
BuildRequires:  pkgconfig(libva) >= 0.34.0
BuildRequires:  pkgconfig(libva-drm) >= 0.34.0
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6
BuildRequires:  pkgconfig(mtdev) >= 1.1.0
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1) >= 0.25.2
BuildRequires:  pkgconfig(wayland-client) >= 1.12.0
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.13
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  poppler-devel
BuildRequires:  poppler-glib-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Weston is the reference wayland compositor that can run on KMS, under X11
or under another compositor.

%package        libs
Summary:        Weston compositor libraries

%description    libs
This package contains Weston compositor libraries.

%package        devel
Summary:        Common headers for weston
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Common headers for weston

%prep
%setup -q

%build
%configure \
  --disable-silent-rules \
  --disable-static \
  --disable-setuid-install \
  --enable-xwayland \
  --enable-rdp-compositor

# https://fedoraproject.org/wiki/Packaging:Guidelines#Beware_of_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -name \*.la -delete

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%license COPYING
%doc README
%{_bindir}/weston
%{_bindir}/weston-info
%attr(4755,root,root) %{_bindir}/weston-launch
%{_bindir}/weston-terminal
%{_bindir}/wcap-decode
%dir %{_libdir}/weston
%{_libdir}/weston/cms-colord.so
%{_libdir}/weston/cms-static.so
%{_libdir}/weston/desktop-shell.so
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

%files libs
%license COPYING
%dir %{_libdir}/libweston-%{apiver}
%{_libdir}/libweston-%{apiver}/drm-backend.so
%{_libdir}/libweston-%{apiver}/fbdev-backend.so
%{_libdir}/libweston-%{apiver}/gl-renderer.so
%{_libdir}/libweston-%{apiver}/headless-backend.so
%{_libdir}/libweston-%{apiver}/rdp-backend.so
%{_libdir}/libweston-%{apiver}/wayland-backend.so
%{_libdir}/libweston-%{apiver}/x11-backend.so
%{_libdir}/libweston-%{apiver}/xwayland.so
%{_libdir}/libweston-%{apiver}.so.0*
%{_libdir}/libweston-desktop-%{apiver}.so.0*

%files devel
%{_includedir}/libweston-%{apiver}/
%{_includedir}/weston/
%{_libdir}/pkgconfig/libweston-%{apiver}.pc
%{_libdir}/pkgconfig/libweston-desktop-%{apiver}.pc
%{_libdir}/pkgconfig/weston.pc
%{_libdir}/libweston-%{apiver}.so
%{_libdir}/libweston-desktop-%{apiver}.so

%changelog
* Tue Mar 20 2018 Kalev Lember <klember@redhat.com> - 3.0.92-1
- Update to 3.0.92

* Tue Feb 27 2018 Kalev Lember <klember@redhat.com> - 3.0.91-1
- Update to 3.0.91

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Simone Caronni <negativo17@gmail.com> - 3.0.0-3
- Drop FreeRDP 1.2 requirement, use FreeRDP 2.0.

* Mon Jan 15 2018 Björn Esser <besser82@fedoraproject.org> - 3.0.0-2
- Rebuilt for libva.so.2

* Wed Aug 09 2017 Kalev Lember <klember@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Wed Aug 02 2017 Kalev Lember <klember@redhat.com> - 2.99.93-1
- Update to 2.99.93

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 2.99.92-2
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Kalev Lember <klember@redhat.com> - 2.99.92-1
- Update to 2.99.92

* Wed Jul 19 2017 Kalev Lember <klember@redhat.com> - 2.99.91-1
- Update to 2.99.91

* Thu Jul 13 2017 Adam Jackson <ajax@redhat.com> - 2.0.0-2
- Stop BuildRequiring cairo-gl. We install none of the additional demo clients
  it builds, and it's going away from the cairo package soon.

* Wed Jun 21 2017 Kalev Lember <klember@redhat.com> - 2.0.0-1
- Update to 2.0.0

* Tue Mar 21 2017 Simone Caronni <negativo17@gmail.com> - 1.12.0-6
- Build requirement compat-freerdp12 has been renamed to freerdp1.2.

* Tue Mar 07 2017 Simone Caronni <negativo17@gmail.com> - 1.12.0-5
- Update build requirements, enable RDP again through FreeRDP 1.2 compatibility
  package.

* Sat Mar 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.12.0-4
- %%build: --disable-silent-rules
- fix FTBFS: disable broken rpd support (#1424540)
- fix rpaths

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 1.12.0-2
- Rebuild (libwebp)

* Wed Sep 21 2016 Kalev Lember <klember@redhat.com> - 1.12.0-1
- Update to 1.12.0

* Wed Sep 14 2016 Kalev Lember <klember@redhat.com> - 1.11.94-1
- Update to 1.11.94

* Thu Sep 08 2016 Kalev Lember <klember@redhat.com> - 1.11.93-1
- Update to 1.11.93

* Wed Aug 31 2016 Kalev Lember <klember@redhat.com> - 1.11.92-1
- Update to 1.11.92
- Don't set group tags

* Wed Aug 17 2016 Kalev Lember <klember@redhat.com> - 1.11.91-2
- Run ldconfig scripts for the new -libs subpackage

* Wed Aug 17 2016 Kalev Lember <klember@redhat.com> - 1.11.91-1
- Update to 1.11.91
- Add a -libs subpackage

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
