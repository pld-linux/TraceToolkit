Summary:	Linux Trace Toolkit
Summary(pl):	Narz�dzia do �ledzenia Linuksa
Name:		TraceToolkit
Version:	0.9.6
%define		_pre pre2
Release:	0.%{_pre}.2
License:	GPL
Group:		X11/Applications
Source0:	http://www.opersys.com/ftp/pub/LTT/%{name}-%{version}%{_pre}.tgz
# Source0-md5:	09be9c2b411070a51ba85be5570f0d05
URL:		http://www.opersys.com/LTT/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Linux Trace Toolkit, more commonly known as LTT, is a
fully-featured tracing system for the Linux kernel. It includes both
the kernel components required for tracing and the user-level tools
required to view the traces.

%description -l pl
Linux Trace Toolkit, znany bardziej jako LTT, jest w pe�ni
funkcjonalnym systemem do �ledzenia j�dra Linuksa. Zawiera elementy
j�dra potrzebne do �ledzenia oraz narz�dzia u�ytkownika potrzebne do
przegl�dania wynik�w �ledzenia.

%package devel 
Summary:	Header files for Linux Trace Toolkit library
Summary(pl):	Pliki nag��wkowe biblioteki Linux Trace Toolkit
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for Linux Trace Toolkit library

%description devel -l pl
Pliki nag��wkowe biblioteki Linux Trace Toolkit

%package static
Summary:	Static version of Linux Trace Toolkit library
Summary(pl):	Statyczna wersja biblioteki Linux Trace Toolkit
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static version of Linux Trace Toolkit library.

%description static -l pl
Statyczna wersja biblioteki Linux Trace Toolkit.

%prep
%setup -q -n %{name}-%{version}%{_pre}

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
