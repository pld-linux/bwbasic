Name:		bwbasic
License:	GPL
Group:		Development
Group(pl):	Programowanie
Version:	2.20.1
Release:	1
Summary:	There is Basic under Linux, too
Summary(pl):	Interpreter BASIC-a dla Linuxa
Source0:	bwbasic-2.20.tar.gz
Source1:	bwb-2.20-patch01.tar.gz
Patch0:		bwbasic-2.20.dif
Patch1:		bwbasic-2.20-CFLAGS.diff
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Basic interpreter.

%description -l pl
Interpreter BASIC-a dla Linuxa.

%prep
%setup -q -n bwbasic-2.20 -a 1
%patch0
%patch1 -p1

%build
mv -f bwb-2.20-patch01/* .
./configure --prefix=$RPM_BUILD_ROOT%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} \
           $RPM_BUILD_ROOT%{_prefix}/src/%{name}-examples
%{__make} install DESTDIR=$RPM_BUILD_ROOT%{_prefix}
cp -f bwbtest/* $RPM_BUILD_ROOT%{_prefix}/src/%{name}-examples
strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/%{name}
gzip -9nf README README.patch01 bwbasic.doc

%files
%defattr(644,root,root,755)
%doc *.gz 
%attr(755,root,root) %{_bindir}/bwbasic
%attr(644,root,root) %{_prefix}/src/%{name}-examples
