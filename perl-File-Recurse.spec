%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Recurse
Summary:	File::Recurse perl module
Summary(es):	Modulo Perl File::Recurse
Summary(no):	Perlmodul File::Recurse
Summary(pl):	Modu� perla File::Recurse
Name:		perl-%{pdir}-%{pnam}
Version:	0.11
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
# does not seem to be available on CPAN ftp
Source0:	http://www.cpan.org/authors/id/D/DI/DIONALM/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Recurse is used to recurse directory structures and saving the
data into an array.

%description -l pl
Modu� File::Recurse zapisuje w spos�b rekurencyjny struktury
katalog�w w postaci tablicy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/File/Recurse.pm
%{perl_sitearch}/auto/File/Recurse
# probably bogus
#%{perl_sitearch}/perllocal.pod

%{_mandir}/man3/*
