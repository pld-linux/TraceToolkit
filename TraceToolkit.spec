Summary:	Linux Trace Toolkit
Name:		TraceToolkit
Version:	0.9.5
Release:	1
License:	GPL
Group:		Applications
######		Unknown group!
Source0:	ftp://ftp.opersys.com/pub/LTT/%{name}-%{version}.tgz
Url:		http://www.opersys.com/LTT/
BuildRequires:	gtk+-devel
Requires:	gtk+	
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/
%description
The Linux Trace Toolkit, more commonly known as LTT, is a fully-featured
tracing system for the Linux kernel. It includes both the kernel components
required for tracing and the user-level tools required to view the traces.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
gzip -9nf COPYING README 
 
%clean
rm -rf $RPM_BUILD_ROOT/%{name}-%{version}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/
%attr(755,root,root) %{_libdir}/
%attr(755,root,root) %{_sbindir}/
