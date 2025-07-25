Summary:	Basic interpreter under Linux
Summary(pl.UTF-8):	Interpreter BASIC-a dla Linuksa
Name:		bwbasic
Version:	2.20.2
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	%{name}-2.20.tar.bz2
# Source0-md5:	489d3dab12f7edf1d210682e6af04059
Source1:	bwb-2.20-patch01.tar.bz2
# Source1-md5:	949b085551398ed8c756d9d15920ff6d
Source2:	bwb-2.20-patch02.tar.bz2
# Source2-md5:	d7b712d1349638dff168f3418e995a63
#Source0:	ftp://ftp.rahul.net/pub/rhn/%{name}-%{version}.tar.Z
#Source1:	ftp://ftp.rahul.net/pub/rhn/bwb-2.20-patch01.tar.Z.uu.txt
#Source2:	ftp://ftp.rahul.net/pub/rhn/bwb-2.20-patch02.tar.Z.uu.txt
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-CFLAGS.patch
URL:		ftp://ftp.rahul.net/pub/rhn/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Basic interpreter.

%description -l pl.UTF-8
Interpreter BASIC-a dla Linuksa.

%package examples
Summary:	Example files for bwBasic
Summary(pl.UTF-8):	Pliki przykładowe dla bwbasica
Group:		Development/Languages

%description examples
Example sources for bwbasic.

%description examples -l pl.UTF-8
Programy przykładowe dla bwbasica.

%prep
%setup -q -n %{name}-2.20 -a1 -a2
%patch -P0
%patch -P1 -p1

%build
mv -f bwb-2.20-patch01/* .
mv -f bwb-2.20-patch02/* .

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir}

cp -f bwbtest/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.patch01 README.patch02 bwbasic.doc
%attr(755,root,root) %{_bindir}/bwbasic

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
