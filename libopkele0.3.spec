%define	major 2
%define libname %mklibname opkele %{major}
%define develname %mklibname opkele -d %{major}

Summary:	C++ implementation of OpenID protocol
Name:		libopkele0.3
Version:	0.3.2
Release:	%mkrel 6
Group:		System/Libraries
License:	MIT
URL:		http://kin.klever.net/libopkele/
Source0:	http://kin.klever.net/dist/libopkele-%{version}.tar.gz
Patch0:		libopkele-newer_libcurl.m4_fix.diff
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	doxygen
BuildRequires:	libxslt-proc
BuildRequires:	konforka-devel
BuildRequires:	curl-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	libpqxx-devel
BuildRequires:	postgresql-devel
BuildRequires:	graphviz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
libopkele is a C++ implementation of an OpenID decentralized identity system.
It provides OpenID protocol handling, leaving authentication and user
interaction to the implementor.

%package -n	%{libname}
Summary:	C++ implementation of OpenID protocol
Group:          System/Libraries

%description -n	%{libname}
libopkele is a C++ implementation of an OpenID decentralized identity system.
It provides OpenID protocol handling, leaving authentication and user
interaction to the implementor.

%package -n	%{develname}
Summary:	Static library and header files for the libopkele library
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	opkele0.3-devel = %{version}-%{release}
Obsoletes:	%{mklibname opkele 1 -d}
Conflicts:	opkele-devel <= 2.0

%description -n	%{develname}
libopkele is a C++ implementation of an OpenID decentralized identity system.
It provides OpenID protocol handling, leaving authentication and user
interaction to the implementor.

This package contains the static libopkele library and its header files.

%prep

%setup -q -n libopkele-%{version}
%patch0 -p0

%build
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force; aclocal; autoheader; automake --add-missing --copy; autoconf --force

%configure2_5x \
    --with-pkgconfigdir=%{_libdir}/pkgconfig

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/opkele
%{_includedir}/opkele/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc

