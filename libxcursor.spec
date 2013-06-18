%define major 1
%define libname %mklibname xcursor %{major}
%define develname %mklibname xcursor -d

Summary:	X Cursor Library
Name:		libxcursor
Version:	1.1.14
Release:	2
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXcursor-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xfixes) >= 3.0.1.2
BuildRequires:	pkgconfig(xrender) >= 0.9.0.2
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
X Cursor Library.

%package -n %{libname}
Summary:	X Cursor Library
Group:		Development/X11
Provides:	%{name} = %{EVRD}

%description -n %{libname}
X Cursor Library.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{version}
Obsoletes:	%{_lib}xcursor1-devel < 1.1.13
Obsoletes:	%{_lib}xcursor-static-devel < 1.1.13

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
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXcursor.so.%{major}*

%files -n %{develname}
%{_libdir}/libXcursor.so
%{_libdir}/pkgconfig/xcursor.pc
%{_includedir}/X11/Xcursor/Xcursor.h
%{_mandir}/man3/*


