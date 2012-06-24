Summary:	CTWM - an extention to the twm window manager
Summary(pl):	CTWM - rozszerzenie do zarz�dcy okien twm
Name:		ctwm
Version:	3.5.2
Release:	1
License:	GPL
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fen�tres
Group(pl):	X11/Zarz�dcy Okien
Source0:	http://ctwm.dl.nu/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
CTWM is an extension to twm, that support multiple virtual screens,
and a lot of other goodies. You can use and manage up to 32 virtual
screens called workspaces. You swap from one workspace to another by
clicking on a button in an optional panel of buttons (the workspace
manager) or by invoking a function. This is the GNU libc version
(RedHat 5.0/TurboLinux 2.0 and above).

%description -l pl
CTWM jest rozszerzeniem twm obs�uguj�cym wiele ekran�w wirtualnych
oraz posiadaj�cycm wiele innych u�ytecznych funkcji. Mo�na u�ywa� i
zarz�dza� nawet 32 ekranami wirtualnymi zwanymi "przestrzeni� robocz�"
(workspace). Mo�na si� mi�dzy nimi prze��cza� klikaj�c na przycisku w
opcjonalnym panelu (mened�erze przestrzeni roboczej) lub wywo�uj�c
funkcj�. Jest to wersja wsp�pracuj�ca z GNU libc (RedHat
5.0/TurboLinux 2.0 i wy�sze).

%prep
%setup -q

xmkmf

%build
%{__make} CDEBUGFLAGS="%{rpmcflags}" CXXDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/X11/twm/images} \
	$RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT%{_sysconfdir}/X11/ctwm

%{__make} DESTDIR=$RPM_BUILD_ROOT install
%{__make} DESTDIR=$RPM_BUILD_ROOT install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES PROBLEMS README ctwm.txt vms.txt vms2.txt sound.doc
%config %{_sysconfdir}/X11/ctwm/system.ctwmrc

%attr(755,root,root) %{_bindir}/ctwm
%{_mandir}/man1/*
%{_libdir}/X11/twm/images
