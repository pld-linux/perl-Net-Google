# Don't do tests - they require Google Web API license key
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Google
Summary:	Net::Google - simple OOP-ish interface to the Google SOAP API
Summary(pl):	Net::Google - prosty, zorientowany obiektowo interfejs do Google SOAP API
Name:		perl-Net-Google
Version:	0.62
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	570b7c777ec9ff6388f826b3c5a90c9e
BuildRequires:	perl-SOAP-Lite
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Google Perl module provides a simple OOP-ish interface to the
Google SOAP API

%description -l pl
Modu� Perla Net::Google udost�pnia prosty, zorientowany obiektowo
interfejs do Google SOAP API.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Net/*
%{_mandir}/man3/*
