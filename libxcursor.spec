%define major 1
%define libname %mklibname xcursor %{major}
%define develname %mklibname xcursor -d

Name: libxcursor
Summary:  X Cursor Library
Version: 1.1.12
Release: 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXcursor-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxfixes-devel >= 3.0.1.2
BuildRequires: libxrender-devel >= 0.9.0.2
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
X Cursor Library.

%package -n %{libname}
Summary:  X Cursor Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
X Cursor Library.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Provides: %{name}-devel = %{version}-%{release}
Requires: %{libname} = %{version}
Conflicts: libxorg-x11-devel < 7.0
Obsoletes: %{_lib}xcursor1-devel
Obsoletes: %{_lib}xcursor-static-devel

%description -n %{develname}
Development files for %{name}.

%prep
%setup -qn libXcursor-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libname}
%{_libdir}/libXcursor.so.%{major}*

%files -n %{develname}
%{_libdir}/libXcursor.so
%{_libdir}/pkgconfig/xcursor.pc
%{_includedir}/X11/Xcursor/Xcursor.h
%{_mandir}/man3/*

