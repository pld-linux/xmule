# bconds
# --with gtk1
#
Summary:	Unix port of eMule client
Summary(pl):	Uniksowy port klienta eMule
Name:		xmule
Version:	1.7.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	dae1f5067288209ad520f340b67c4d14
URL:		http://www.xmule.org/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.7.3
BuildRequires:	bison
BuildRequires:	gettext-devel >= 0.11.5
BuildRequires:	expat-devel
%if 0%{?_with_gtk1:1}
BuildRequires:	wxGTK-devel >= 2.4.0
BuildRequires:	gtk+-devel >= 1.2.0
%else
BuildRequires:	wxGTK2-devel >= 2.4.0
BuildRequires:	gtk+2-devel
%endif
BuildRequires:	libstdc++-devel
Requires:	wget
Conflicts:	aMule
Obsoletes:	lmule
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xMule is a Linux port of eMule client.

%description -l pl
xMule to linuksowy port klienta eMule.

%prep
%setup  -q

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-wx-config=/usr/bin/wxgtk%{?!_with_gtk1:2}-2.4-config \
	--enable-optimise \
	--enable-profile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Network/Misc,%{_pixmapsdir}}
install src/{ed2k,xmule} $RPM_BUILD_ROOT%{_bindir}
install xmule.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc/xmule.desktop
install xmule.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/xmule.xpm
cd po
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} install-data \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog ChangeLog-UNSTABLE README TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_applnkdir}/Network/Misc/%{name}.desktop
