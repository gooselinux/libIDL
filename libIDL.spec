Summary: Library for parsing IDL (Interface Definition Language)
Name: libIDL
Version: 0.8.13
Release: 2.1%{?dist}
Source: http://download.gnome.org/sources/libIDL/0.8/%{name}-%{version}.tar.bz2
Patch0: libIDL-0.8.6-multilib.patch
Group: System Environment/Libraries
License: LGPLv2+
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: pkgconfig >= 0.8
BuildRequires: glib2-devel >= 2.0
BuildRequires: flex bison

%description
libIDL is a library for parsing IDL (Interface Definition Language).
It can be used for both COM-style and CORBA-style IDL.

%package devel
Summary: Development libraries and header files for libIDL
Group: Development/Libraries
Requires: libIDL = %{version}-%{release}
Requires: pkgconfig >= 1:0.8
Requires: glib2-devel >= 2.0
Requires(post): /sbin/install-info

%description devel
libIDL is a library for parsing IDL (Interface Definition Language).
It can be used for both COM-style and CORBA-style IDL.

This package contains the header files and libraries needed to write
or compile programs that use libIDL.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .multilib

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_libdir}/*a

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel
/sbin/install-info --quiet %{_infodir}/libIDL2.info.gz %{_infodir}/dir || :

%preun devel
if [ $1 = 0 ]; then
   /sbin/install-info --quiet --delete %{_infodir}/libIDL2.info.gz %{_infodir}/dir || :
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%doc AUTHORS COPYING README NEWS

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_bindir}/libIDL-config-2
%{_infodir}/libIDL2.info.gz

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.8.13-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 17 2009 Matthias Clasen <mclasen@redhat.com> - 0.8.13-1
- Update to 0.8.13

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec  3 2008 Matthias Clasen <mclasen@redhat.com> - 0.8.12-1
- Update to 0.8.12

* Fri Aug 22 2008 Matthias Clasen <mclasen@redhat.com> - 0.8.11-1
- Update to 0.8.11

* Fri Feb  8 2008 Matthias Clasen <mclasen@redhat.com> - 0.8.10-2
- Rebuild for gcc 4.3

* Tue Jan 29 2008 Matthias Clasen <mclasen@redhat.com> - 0.8.10-1
- Update to 0.8.10

* Tue Jan 29 2008 Matthias Clasen <mclasen@redhat.com> - 0.8.9-2
- Don't use G_GNUC_PRETTY_FUNCTION

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 0.8.9-1
- Update to 0.8.9

* Wed Aug  8 2007 Matthias Clasen <mclasen@redhat.com> - 0.8.8-2
- Update the license field

* Tue Feb 27 2007 Matthias Clasen <mclasen@redhat.com> - 0.8.8-1
- Update to 0.8.8

* Tue Jan 30 2007 Matthias Clasen <mclasen@redhat.com> - 0.8.7-2
- Fix scriptlets to be failsafe (#223706)

* Wed Aug  2 2006 Matthias Clasen <mclasen@redhat.com> - 0.8.7-1.fc6
- Update to 0.8.7

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.8.6-6.1
- rebuild

* Mon Jun 12 2006 Bill Nottingham <notting@redhat.com> - 0.8.6-6
- we don't call the autotools or libtoolize during build - don't
  buildreq them

* Fri Jun  9 2006 Matthias Clasen <mclasen@redhat.com> - 0.8.6-5
- Fix missing BuildRequires

* Mon Jun  5 2006 Matthias Clasen <mclasen@redhat.com> - 0.8.6-4
- Fix missing BuildRequires

* Tue May 23 2006 Matthias Clasen <mclasen@redhat.com> - 0.8.6-3
- Fix multilib conflicts

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.8.6-2.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.8.6-2.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov  7 2005 Matthias Clasen <mclasen@redhat.com> 0.8.6-2
- Remove .la files and static libraries from the 
  -devel package

* Wed Sep  7 2005 Matthias Clasen <mclasen@redhat.com> 0.8.6-1
- Update to 0.8.6

* Fri Mar  4 2005 David Zeuthen <davidz@redhat.com> 0.8.5-2
- Rebuild

* Wed Feb  9 2005 Matthias Clasen <mclasen@redhat.com> 0.8.5-1
- Update to 0.8.5

* Wed Aug 18 2004 Mark McLoughlin <markmc@redhat.com> 0.8.4-1
- Update to 0.8.4

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jan 26 2004 Alexander Larsson <alexl@redhat.com> 0.8.3-1
- update to 0.8.3

* Thu Aug  7 2003 Jonathan Blandford <jrb@redhat.com> 0.8.2-1
- rebuild for GNOME 2.4

* Thu Jun 26 2003 Havoc Pennington <hp@redhat.com> 0.8.0-10
- rebuild again in different place...

* Tue Jun 24 2003 Havoc Pennington <hp@redhat.com> 0.8.0-9
- rebuild

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Jeff Johnson <jbj@redhat.com>
- add explicit epoch's where needed.

* Tue Feb 11 2003 Bill Nottingham <notting@redhat.com> 0.8.0-7
- fix URL (#79157)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Dec 10 2002 Tim Powers <timp@redhat.com> 0.8.0-5
- don't include info/dir, it conflicts with the info package

* Mon Dec  9 2002 Havoc Pennington <hp@redhat.com>
- rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun 06 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Tue Jun  4 2002 Havoc Pennington <hp@redhat.com>
- 0.8.0

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri May 17 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Thu Apr 25 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Thu Apr  4 2002 Jeremy Katz <katzj@redhat.com>
- move include files to -devel
- other spec file tweaks

* Thu Feb 14 2002 Havoc Pennington <hp@redhat.com>
- 0.7.4

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- cvs snap 0.7.1.91

* Sun Nov 25 2001 Havoc Pennington <hp@redhat.com>
- cvs snap, rebuild on new glib 1.3.11

* Fri Oct 26 2001 Havoc Pennington <hp@redhat.com>
- glib 1.3.10

* Thu Oct  4 2001 Havoc Pennington <hp@redhat.com>
- rebuild for new glib

* Thu Sep 27 2001 Havoc Pennington <hp@redhat.com>
- initial build of standalone libIDL
- fix braindamage

