Summary:	CTWM - an extention to the twm window manager
Summary(pl.UTF-8):   CTWM - rozszerzenie do zarządcy okien twm
Name:		ctwm
Version:	3.6
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://ctwm.dl.nu/dist/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-pld-dir.patch
Patch1:		%{name}-gram.patch
Patch2:		%{name}-noxpm.patch
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

%description -l pl.UTF-8
CTWM jest rozszerzeniem twm obsługującym wiele ekranów wirtualnych
oraz posiadającycm wiele innych użytecznych funkcji. Można używać i
zarządzać nawet 32 ekranami wirtualnymi zwanymi "przestrzenią roboczą"
(workspace). Można się między nimi przełączać klikając na przycisku w
opcjonalnym panelu (menedżerze przestrzeni roboczej) lub wywołując
funkcję. Jest to wersja współpracująca z GNU libc (RedHat
5.0/TurboLinux 2.0 i wyższe).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

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

gzip -9nf CHANGES PROBLEMS README ctwm.txt sound.doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%config /etc/X11/twm/system.ctwmrc
%{_wmpropsdir}/ctwm.desktop

%attr(755,root,root) %{_bindir}/ctwm
%{_mandir}/man1/*
%{_libdir}/X11/ctwm
