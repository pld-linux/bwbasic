Summary:	Basic interpreter under Linux
Summary(pl):	Interpreter BASIC-a dla Linuxa
Name:		bwbasic
Version:	2.20.2
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	%{name}-2.20.tar.bz2
Source1:	bwb-2.20-patch01.tar.bz2
Source2:	bwb-2.20-patch02.tar.bz2
#Source0:	ftp://ftp.rahul.net/pub/rhn/%{name}-%{version}.tar.Z
#Source1:	ftp://ftp.rahul.net/pub/rhn/bwb-2.20-patch01.tar.Z.uu.txt
#Source2:	ftp://ftp.rahul.net/pub/rhn/bwb-2.20-patch02.tar.Z.uu.txt
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-CFLAGS.patch
URL:		ftp://ftp.rahul.net/pub/rhn/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Basic interpreter.

%description -l pl
Interpreter BASIC-a dla Linuxa.

%package examples
Summary:	Example files for bwBasic
Summary(pl):	Pliki przykładowe dla bwbasica
Group:		Development/Languages

%description examples
Example sources for bwbasic.

%description examples -l pl
Programy przykładowe dla bwbasica.

%prep
%setup -q -n bwbasic-2.20 -a 1 -a 2
%patch0
%patch1 -p1

%build
mv -f bwb-2.20-patch01/* .
mv -f bwb-2.20-patch02/* .

./configure --prefix=$RPM_BUILD_ROOT%{_prefix}
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} \
           $RPM_BUILD_ROOT%{_prefix}/src/%{name}-examples
%{__make} install DESTDIR=$RPM_BUILD_ROOT%{_prefix}
cp -f bwbtest/* $RPM_BUILD_ROOT%{_prefix}/src/%{name}-examples
gzip -9nf README README.patch01 README.patch02 bwbasic.doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz 
%attr(755,root,root) %{_bindir}/bwbasic

%files examples
%defattr(644,root,root,755)
%attr(644,root,root) %{_prefix}/src/%{name}-examples
