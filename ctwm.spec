Summary:	CTWM - an extention to the twm window manager
Name:		ctwm
Version:	3.5.1
Release:	1TL
License:	GPL
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy Okien
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Source0:	ftp://slhp1.epfl.ch/pub/%{name}-3.5.tar.gz
Patch0:		ctwm-3.5beta1.patch
Patch1:		ctwm-3.5-3.5.1.diffs
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
CTWM jest rozszerzeniem twm obs³uguj±cym wiele ekranów wirtualnych
oraz posiadaj±cycm wiele innych u¿ytecznych funkcji. Mo¿na u¿ywaæ i
zarz±dzaæ nawet 32 ekranami wirtualnymi zwanymi "przestrzeni± robocz±"
(workspace). Mo¿na siê miêdzy nimi prze³±czaæ klikaj±c na przycisku w
opcjonalnym panelu (mened¿erze przestrzeni roboczej) lub wywo³uj±c
funkcjê. Jest to wersja wspó³pracuj±ca z GNU libc (RedHat
5.0/TurboLinux 2.0 i wy¿sze).

%prep
%setup -q -n ctwm-3.5
%patch1 -p1 -b .351
%patch -p1

xmkmf

%build
make CDEBUGFLAGS="$RPM_OPT_FLAGS" CXXDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/X11/twm/images \
	$RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT%{_sysconfdir}/X11/ctwm

make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES PROBLEMS README README.VMS vms.txt sound.doc
%config %{_sysconfdir}/X11/ctwm/system.ctwmrc

%attr(755,root,root) %{_bindir}/ctwm
%{_mandir}/man1/*
%{_libdir}/X11/twm/images
