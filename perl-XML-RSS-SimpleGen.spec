%define upstream_name	 XML-RSS-SimpleGen
%define upstream_version 11.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Really Simple RSS Generator
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# Seems to depend on site content which changed
#make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorlib}/XML/*
%{_mandir}/*/*

%changelog
* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 11.110.0-1mdv2010.0
+ Revision: 408255
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 11.11-6mdv2009.0
+ Revision: 242269
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 11.11-4mdv2008.0
+ Revision: 23493
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 11.11-3mdk
- Fix According to perl Policy
	- Source URL

* Fri Jan 13 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 11.11-2mdk
- Rebuild.

* Tue Jul 27 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 11.11-1mdk
- Initial MDK release.

