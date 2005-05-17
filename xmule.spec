Summary:	Unix port of eMule client
Summary(pl):	Uniksowy port klienta eMule
Name:		xmule
Version:	1.9.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/xmule/%{name}-%{version}.tar.bz2
# Source0-md5:	6a466ba740b55e6d283622aa84570921
Patch0:		%{name}-pl_typos.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-types.patch
Patch3:		%{name}-locale_names.patch
Patch4:		%{name}-configure.patch
URL:		http://www.xmule.org/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7.3
BuildRequires:	bison
BuildRequires:	expat-devel
BuildRequires:	gettext-devel >= 0.11.5
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	wxGTK2-devel >= 2.6.0
BuildRequires:	libstdc++-devel
Requires:	wget
Obsoletes:	aMule
Obsoletes:	lmule
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xMule is a Linux port of eMule client.

%description -l pl
xMule to linuksowy port klienta eMule.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

mv -f po/{ee,et}.po

%build
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
install {ed2k,xmule} $RPM_BUILD_ROOT%{_bindir}
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
%doc AUTHORS ChangeLog ChangeLog-UNSTABLE README TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/%{name}.desktop
