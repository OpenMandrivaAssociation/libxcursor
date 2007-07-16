%define libxcursor %mklibname xcursor 1
Name: libxcursor
Summary:  X Cursor Library
Version: 1.1.8
Release: %mkrel 1
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXcursor-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxfixes-devel >= 3.0.1.2
BuildRequires: libxrender-devel >= 0.9.0.2
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
X Cursor Library

#-----------------------------------------------------------

%package -n %{libxcursor}
Summary:  X Cursor Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxcursor}
X Cursor Library

#-----------------------------------------------------------

%package -n %{libxcursor}-devel
Summary: Development files for %{name}
Group: Development/X11

Requires: x11-proto-devel >= 1.0.0
Provides: libxcursor-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0

Requires: %{libxcursor} = %{version}

%description -n %{libxcursor}-devel
Development files for %{name}

%pre -n %{libxcursor}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxcursor}-devel
%defattr(-,root,root)
%{_libdir}/libXcursor.so
%{_libdir}/libXcursor.la
%{_libdir}/pkgconfig/xcursor.pc
%{_includedir}/X11/Xcursor/Xcursor.h
%{_mandir}/man3/Xcursor.3x.bz2

#-----------------------------------------------------------

%package -n %{libxcursor}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxcursor}-devel = %{version}
Provides: libxcursor-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxcursor}-static-devel
Static development files for %{name}

%files -n %{libxcursor}-static-devel
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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxcursor}
%defattr(-,root,root)
%{_libdir}/libXcursor.so.1
%{_libdir}/libXcursor.so.1.0.2
