%define upstream_name	 XML-RSS-SimpleGen
%define upstream_version 11.11
Name:		perl-%{upstream_name}
Version:	11.11
Release:	3

Summary:	Really Simple RSS Generator
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-RSS-SimpleGen
Source0:	https://cpan.metacpan.org/authors/id/S/SB/SBURKE/XML-RSS-SimpleGen-11.11.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

Suggests:	perl(LWP::Simple)

%description
An easy-to-use screen scraper and RSS generator module. It transparently
handles all the unpleasant details of RSS, like proper XML escaping, and also
has a good number of Do-What-I-Mean features, like not changing the modtime on
a written-out RSS file if the file content hasn't changed, and like
automatically removing any HTML tags from content you might pass in.

%prep
%setup -q -n XML-RSS-SimpleGen-11.11

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
# Seems to depend on site content which changed
#make test || :

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorlib}/XML/*
%{_mandir}/*/*

