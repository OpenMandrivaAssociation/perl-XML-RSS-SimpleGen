%define upstream_name	 XML-RSS-SimpleGen
%define upstream_version 11.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Really Simple RSS Generator
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
