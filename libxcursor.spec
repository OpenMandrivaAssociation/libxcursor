# libxcursor is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major 1
%define libname %mklibname xcursor %{major}
%define devname %mklibname xcursor -d

%if %{with compat32}
%define lib32name libxcursor%{major}
%define dev32name libxcursor-devel
%endif

Summary:	X Cursor Library
Name:		libxcursor
Version:	1.2.2
Release:	1
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXcursor-%{version}.tar.xz
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xfixes) >= 3.0.1.2
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xrender) >= 0.9.0.2
%if %{with compat32}
BuildRequires:	libc6
BuildRequires:	devel(libX11)
BuildRequires:	devel(libXfixes)
BuildRequires:	devel(libXrender)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
%endif

%description
X Cursor Library.

%package -n %{libname}
Summary:	X Cursor Library
Group:		Development/X11
Requires:	x11-data-cursor-themes

%description -n %{libname}
X Cursor Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	X Cursor Library (32-bit)
Group:		Development/X11

%description -n %{lib32name}
X Cursor Library.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n %{dev32name}
Development files for %{name}.
%endif

%prep
%autosetup -n libXcursor-%{version}
export CONFIGURE_TOP="$(pwd)"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libXcursor.so.%{major}*

%files -n %{devname}
%{_libdir}/libXcursor.so
%{_libdir}/pkgconfig/xcursor.pc
%{_includedir}/X11/Xcursor/Xcursor.h
%doc %{_mandir}/man3/*

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libXcursor.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libXcursor.so
%{_prefix}/lib/pkgconfig/xcursor.pc
%endif
