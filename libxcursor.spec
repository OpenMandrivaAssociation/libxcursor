%define major 1
%define libname %mklibname xcursor %{major}
%define develname %mklibname xcursor -d
%define staticdevelname %mklibname xcursor -d -s

Name: libxcursor
Summary:  X Cursor Library
Version: 1.1.8
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXcursor-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxfixes-devel >= 3.0.1.2
BuildRequires: libxrender-devel >= 0.9.0.2
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

BuildRoot: %{_tmppath}/%{name}-root

%description
X Cursor Library.

#-----------------------------------------------------------

%package -n %{libname}
Summary:  X Cursor Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
X Cursor Library.

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11

Requires: x11-proto-devel >= 1.0.0
Provides: %{name}-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0
Obsoletes: %mklibname xcursor 1 -d
Requires: %{libname} = %{version}

%description -n %{develname}
Development files for %{name}.

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXcursor.so
%{_libdir}/libXcursor.la
%{_libdir}/pkgconfig/xcursor.pc
%{_includedir}/X11/Xcursor/Xcursor.h
%{_mandir}/man3/Xcursor.3*

#-----------------------------------------------------------

%package -n %{staticdevelname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}
Provides: %{name}-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0
Obsoletes: %{mklibname xcursor 1 -d -s}

%description -n %{staticdevelname}
Static development files for %{name}

%files -n %{staticdevelname}
%defattr(-,root,root)
%{_libdir}/libXcursor.a

#-----------------------------------------------------------

%prep
%setup -q -n libXcursor-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXcursor.so.%{major}*
