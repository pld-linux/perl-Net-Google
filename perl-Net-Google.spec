# Don't do tests - they require Google Web API license key
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Google
Summary:	Simple OOP-ish interface to the Google SOAP API
Summary(pl):	Prosty, zorientowany obiektowo interfejs do Google SOAP API
Name:		perl-Net-Google
Version:	0.61
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	98e32b9c487fe0c4b823670aca18fb09
BuildRequires:	perl-SOAP-Lite
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple OOP-ish interface to the Google SOAP API.

%description -l pl
Prosty, zorientowany obiektowo interfejs do Google SOAP API.

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
