Summary: CTWM - an extention to the twm window manager
Name: ctwm
Version: 3.5.1
Release: 1TL
Copyright: GPL
Group: X11/Window Managers
Source: ftp://slhp1.epfl.ch/pub/ctwm-3.5.tar.gz
Patch: ctwm-3.5beta1.patch
Patch1: ctwm-3.5-3.5.1.diffs
BuildRoot: /var/tmp/ctwm-root

%description
CTWM is an extension to twm, that support multiple virtual screens,
and a lot of other goodies. You can use and manage up to 32 virtual
screens called workspaces. You swap from one workspace to another by
clicking on a button in an optional panel of buttons (the workspace
manager) or by invoking a function. This is the GNU libc version
(RedHat 5.0/TurboLinux 2.0 and above).

%description -l pl
CTWM jest rozszerzeniem twm obs³uguj±cym wiele ekranów wirtualnych oraz
posiadaj±cycm wiele innych u¿ytecznych funkcji. Mo¿na u¿ywaæ i zarz±dzaæ
nawet 32 ekranami wirtualnymi zwanymi "przestrzeni± robocz±" (workspace).
Mo¿na siê miêdzy nimi prze³±czaæ klikaj±c na przycisku w opcjonalnym
panelu (mened¿erze przestrzeni roboczej) lub wywo³uj±c funkcjê. Jest to
wersja wspó³pracuj±ca z GNU libc (RedHat 5.0/TurboLinux 2.0 i wy¿sze).

%prep
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/twm/images
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/man/man1
mkdir -p $RPM_BUILD_ROOT/etc/X11/ctwm
%setup -q -n ctwm-3.5
%patch1 -p1 -b .351
%patch -p1

xmkmf

%build
make CDEBUGFLAGS="$RPM_OPT_FLAGS" CXXDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT install.man

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /etc/turbowmcfgrc ]; then
   CTWM=`grep -i 'ctwm' /etc/turbowmcfgrc`
   if [ "$CTWM" = "" ]; then
      echo "CTWM*/usr/X11R6/bin/ctwm*8" >> /etc/turbowmcfgrc
   fi;
fi;

%postun
if [ -f /etc/turbowmcfgrc ]; then
   grep -vi 'ctwm' /etc/turbowmcfgrc > /etc/turbowmcfgrc.new
   mv -f /etc/turbowmcfgrc.new /etc/turbowmcfgrc
fi;

%files
%doc CHANGES PROBLEMS README README.VMS vms.txt sound.doc
%config /etc/X11/ctwm/system.ctwmrc

/usr/X11R6/bin/ctwm
/usr/X11R6/man/man1/ctwm.1x
/usr/X11R6/lib/X11/twm/images
