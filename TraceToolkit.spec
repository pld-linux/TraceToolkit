Summary:	Linux Trace Toolkit
Summary(pl):	Narzêdzia do ¶ledzenia Linuksa
Name:		TraceToolkit
Version:	0.9.6
%define		_pre pre2
Release:	0.%{_pre}.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.opersys.com/ftp/pub/LTT/%{name}-%{version}%{_pre}.tgz
# Source0-md5:	09be9c2b411070a51ba85be5570f0d05
URL:		http://www.opersys.com/LTT/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Linux Trace Toolkit, more commonly known as LTT, is a
fully-featured tracing system for the Linux kernel. It includes both
the kernel components required for tracing and the user-level tools
required to view the traces.

%description -l pl
Linux Trace Toolkit, znany bardziej jako LTT, jest w pe³ni
funkcjonalnym systemem do ¶ledzenia j±dra Linuksa. Zawiera elementy
j±dra potrzebne do ¶ledzenia oraz narzêdzia u¿ytkownika potrzebne do
przegl±dania wyników ¶ledzenia.

%package devel 
Summary:        Linux Trace Toolkit - devel
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Linux Trace Toolkit - development files.

%package static
Summary:        Linux Trace Toolkit - devel
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description static
Linux Trace Toolkit - static libraries.

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
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la

%files static
%{_libdir}/lib*.a
