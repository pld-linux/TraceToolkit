Summary:	Linux Trace Toolkit
Summary(pl):	Narzêdzia do ¶ledzenia Linuksa
Name:		TraceToolkit
Version:	0.9.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.opersys.com/ftp/pub/LTT/%{name}-%{version}.tgz
URL:		http://www.opersys.com/LTT/
BuildRequires:	gtk+-devel
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install
 
%clean
rm -rf $RPM_BUILD_ROOT/%{name}-%{version}

%files
%defattr(644,root,root,755)
%doc README 
#%attr(755,root,root) %{_bindir}/
#%attr(755,root,root) %{_libdir}/
#%attr(755,root,root) %{_sbindir}/
