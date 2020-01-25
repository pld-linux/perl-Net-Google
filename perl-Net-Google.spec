# Don't do tests - they require Google Web API license key
%define		pdir	Net
%define		pnam	Google
Summary:	Net::Google - simple OOP-ish interface to the Google SOAP API
Summary(pl.UTF-8):	Net::Google - prosty, zorientowany obiektowo interfejs do Google SOAP API
Name:		perl-Net-Google
Version:	1.0.1
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	842a1a81aac15683acea0cb7f40855a5
URL:		http://search.cpan.org/dist/Net-Google/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-SOAP-Lite
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Google Perl module provides a simple OOP-ish interface to the
Google SOAP API

%description -l pl.UTF-8
Moduł Perla Net::Google udostępnia prosty, zorientowany obiektowo
interfejs do Google SOAP API.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Net/*
%{_mandir}/man3/*
