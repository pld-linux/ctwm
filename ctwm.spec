Summary:	CTWM - an extention to the twm window manager
Summary(pl):	CTWM - rozszerzenie do zarz±dcy okien twm
Name:		ctwm
Version:	3.5.2
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://ctwm.dl.nu/dist/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-pld-dir.patch
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_wmpropsdir	%{_datadir}/wm-properties

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
%setup -q
%patch -p1

xmkmf

%build
%{__make} \
	CDEBUGFLAGS="%{rpmcflags}" \
	CXXDEBUGFLAGS="%{rpmcflags}" \
	PIXDIR=/etc/X11/

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT/etc/X11/twm \
	$RPM_BUILD_ROOT%{_libdir}/X11/ctwm \
	$RPM_BUILD_ROOT%{_wmpropsdir}

%{__make} DESTDIR=$RPM_BUILD_ROOT install
%{__make} DESTDIR=$RPM_BUILD_ROOT install.man

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES PROBLEMS README ctwm.txt sound.doc
%config /etc/X11/twm/system.ctwmrc
%{_wmpropsdir}/ctwm.desktop

%attr(755,root,root) %{_bindir}/ctwm
%{_mandir}/man1/*
%{_libdir}/X11/ctwm
