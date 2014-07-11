%define major 1
%define libname %mklibname xcursor %{major}
%define devname %mklibname xcursor -d

Summary:	X Cursor Library
Name:		libxcursor
Version:	1.1.14
Release:	9
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXcursor-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xfixes) >= 3.0.1.2
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xrender) >= 0.9.0.2

%description
X Cursor Library.

%package -n %{libname}
Summary:	X Cursor Library
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
X Cursor Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
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
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXcursor.so.%{major}*

%files -n %{devname}
%{_libdir}/libXcursor.so
%{_libdir}/pkgconfig/xcursor.pc
%{_includedir}/X11/Xcursor/Xcursor.h
%{_mandir}/man3/*

