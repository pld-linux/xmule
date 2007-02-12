# TODO: it hanges after few minutes, hgw why.
Summary:	Unix port of eMule client
Summary(pl.UTF-8):   Uniksowy port klienta eMule
Name:		xmule
Version:	1.12.2
Release:	0.2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/xmule/%{name}-%{version}.tar.bz2
# Source0-md5:	372c02793f8282312a1370443420fda7
Patch0:		%{name}-pl_typos.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-locale_names.patch
Patch3:		%{name}-configure.patch
Patch4:		%{name}-wx-config.patch
Patch5:		%{name}-libcrypto.patch
URL:		http://www.xmule.ws/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7.3
BuildRequires:	bison
BuildRequires:	cryptopp-devel
BuildRequires:	expat-devel
BuildRequires:	gettext-devel >= 0.14.5
BuildRequires:	gtk+2-devel >= 2.0.3
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	wxGTK2-devel >= 2.6.2
Requires:	wget
Obsoletes:	aMule
Obsoletes:	lmule
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xMule is a Linux port of eMule client.

%description -l pl.UTF-8
xMule to linuksowy port klienta eMule.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

mv -f po/{ee,et}.po

%build
# Regenerate POTFILES.in because it wasn't actualized since 2004
for i in src/*.cpp; do echo $i; done > po/POTFILES.in
cp -f /usr/share/automake/config.sub .
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	--prefix=$RPM_BUILD_ROOT \
	--disable-debug-syms \
	--with-wx-config=/usr/bin/wx-gtk2-ansi-config 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}
install {ed2k.xmule-2.0,xmule} $RPM_BUILD_ROOT%{_bindir}
ln -sf %{_bindir}/ed2k.xmule-2.0 $RPM_BUILD_ROOT%{_bindir}/ed2k
install xmule.desktop $RPM_BUILD_ROOT%{_desktopdir}/xmule.desktop
install xmule.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/xmule.xpm
cd po
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} install-data \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

%find_lang xMule

%clean
rm -rf $RPM_BUILD_ROOT

%files -f xMule.lang
%defattr(644,root,root,755)
%doc ChangeLog ChangeLog-UNSTABLE docs/{AUTHORS,ED2K-Links.HOWTO,README,TODO}
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/%{name}.desktop
