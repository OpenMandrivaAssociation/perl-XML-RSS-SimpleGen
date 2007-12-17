%define module	XML-RSS-SimpleGen
%define name	perl-%{module}
%define version	11.11
%define	release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Really Simple RSS Generator
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildArch:	noarch
BuildRequires:	perl-devel
# actually, that's a "suggests", not a "requires"
Requires:	perl(LWP::Simple)

%description
An easy-to-use screen scraper and RSS generator module. It transparently
handles all the unpleasant details of RSS, like proper XML escaping, and also
has a good number of Do-What-I-Mean features, like not changing the modtime on
a written-out RSS file if the file content hasn't changed, and like
automatically removing any HTML tags from content you might pass in.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/XML/*
%{_mandir}/*/*

