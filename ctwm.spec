Summary:	CTWM - an extention to the twm window manager
Summary(pl.UTF-8):	CTWM - rozszerzenie do zarządcy okien twm
Name:		ctwm
Version:	3.6
Release:	2
License:	MIT
Group:		X11/Window Managers
Source0:	http://ctwm.free.lp.se/dist/%{name}-%{version}.tar.gz
# Source0-md5:	c9e9e161e07e3d1c7e27684436f01e2b
Source1:	%{name}.desktop
Source2:	%{name}-xsession.desktop
Patch0:		%{name}-pld-dir.patch
Patch1:		%{name}-bison.patch
URL:		http://ctwm.free.lp.se/
BuildRequires:	XFree86-devel
Conflicts:	filesystem < 3.0-20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# NOTE: if prefix==/usr, %{_libdir}/X11 must not be used
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_wmpropsdir	/usr/share/gnome/wm-properties

%description
CTWM is an extension to twm, that support multiple virtual screens,
and a lot of other goodies. You can use and manage up to 32 virtual
screens called workspaces. You swap from one workspace to another by
clicking on a button in an optional panel of buttons (the workspace
manager) or by invoking a function. This is the GNU libc version
(RedHat 5.0/TurboLinux 2.0 and above).

%description -l pl.UTF-8
CTWM jest rozszerzeniem twm obsługującym wiele ekranów wirtualnych
oraz posiadającym wiele innych użytecznych funkcji. Można używać i
zarządzać nawet 32 ekranami wirtualnymi zwanymi "przestrzenią roboczą"
(workspace). Można się między nimi przełączać klikając na przycisku w
opcjonalnym panelu (zarządcy przestrzeni roboczej) lub wywołując
funkcję. Jest to wersja współpracująca z GNU libc (RedHat
5.0/TurboLinux 2.0 i wyższe).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
	$RPM_BUILD_ROOT%{_wmpropsdir} \
	$RPM_BUILD_ROOT%{_datadir}/xsessions

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} install.man \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES PROBLEMS README ctwm.txt sound.doc
%config /etc/X11/twm/system.ctwmrc
%attr(755,root,root) %{_bindir}/ctwm
%{_libdir}/X11/ctwm
%{_wmpropsdir}/ctwm.desktop
%{_datadir}/xsessions/ctwm.desktop
%{_mandir}/man1/*
