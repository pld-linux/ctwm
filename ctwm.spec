Summary:	CTWM - an extention to the twm window manager
Summary(pl):	CTWM - rozszerzenie do zarz±dcy okien twm
Name:		ctwm
Version:	3.6
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://ctwm.dl.nu/dist/%{name}-%{version}.tar.gz
# Source0-md5:	c9e9e161e07e3d1c7e27684436f01e2b
Source1:	%{name}.desktop
Patch0:		%{name}-pld-dir.patch
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties

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
opcjonalnym panelu (zarz±dcy przestrzeni roboczej) lub wywo³uj±c
funkcjê. Jest to wersja wspó³pracuj±ca z GNU libc (RedHat
5.0/TurboLinux 2.0 i wy¿sze).

%prep
%setup -q
%patch -p1

%build
xmkmf

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} install.man \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES PROBLEMS README ctwm.txt sound.doc
%config /etc/X11/twm/system.ctwmrc
%attr(755,root,root) %{_bindir}/ctwm
%{_libdir}/X11/ctwm
%{_wmpropsdir}/ctwm.desktop
%{_mandir}/man1/*
