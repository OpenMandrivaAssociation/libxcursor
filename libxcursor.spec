%define major 1
%define libname %mklibname xcursor %{major}
%define develname %mklibname xcursor -d

Name: libxcursor
Summary:  X Cursor Library
Version: 1.1.13
Release: 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXcursor-%{version}.tar.bz2

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xfixes) >= 3.0.1.2
BuildRequires: pkgconfig(xrender) >= 0.9.0.2
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
X Cursor Library.

%package -n %{libname}
Summary:  X Cursor Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{EVRD}

%description -n %{libname}
X Cursor Library.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Provides: %{name}-devel = %{EVRD}
Requires: %{libname} = %{version}
Conflicts: libxorg-x11-devel < 7.0
Obsoletes: %{_lib}xcursor1-devel < 1.1.13
Obsoletes: %{_lib}xcursor-static-devel < 1.1.13

%description -n %{develname}
Development files for %{name}.

%prep
%setup -qn libXcursor-%{version}

%build
autoreconf -fi
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXcursor.so.%{major}*

%files -n %{develname}
%{_libdir}/libXcursor.so
%{_libdir}/pkgconfig/xcursor.pc
%{_includedir}/X11/Xcursor/Xcursor.h
%{_mandir}/man3/*



%changelog
* Sat Mar 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.13-1
+ Revision: 783810
- version update 1.1.13

* Thu Mar 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1.12-3
+ Revision: 783357
- Remove pre scriptlet to correct rpm upgrade moving from /usr/X11R6.

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.12-2
+ Revision: 745695
- rebuild
- disabled static build
- removed .la files
- cleaned up spec

* Sat Sep 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.12-1
+ Revision: 699278
- update to new version 1.1.12

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.11-2
+ Revision: 660297
- mass rebuild

* Thu Oct 28 2010 Thierry Vignaud <tv@mandriva.org> 1.1.11-1mdv2011.0
+ Revision: 589777
- new release

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.10-2mdv2010.1
+ Revision: 520963
- rebuilt for 2010.1

* Mon Aug 31 2009 Thierry Vignaud <tv@mandriva.org> 1.1.10-1mdv2010.0
+ Revision: 422876
- new release

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.1.9-3mdv2009.0
+ Revision: 223067
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Mon Jan 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.9-2mdv2008.1
+ Revision: 151699
- Update BuildRequires and rebuild.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Aug 28 2007 Thierry Vignaud <tv@mandriva.org> 1.1.9-1mdv2008.0
+ Revision: 72713
- fix man page list
- new release

* Sat Jul 21 2007 Adam Williamson <awilliamson@mandriva.org> 1.1.8-3mdv2008.0
+ Revision: 54095
- fix static-devel's dependency on devel and make it obsolete the old one

* Tue Jul 17 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.8-2mdv2008.0
+ Revision: 52908
- fix libification (thanks goes to Frederik Himpe for pointing this out)

* Tue Jul 17 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.8-1mdv2008.0
+ Revision: 52778
- new devel library policy
- spec file clean
- new version

