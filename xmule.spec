#
# Conditional build:
%bcond_with	gtk1	# build with gtk1 instead of gtk2
#
Summary:	Unix port of eMule client
Summary(pl):	Uniksowy port klienta eMule
Name:		xmule
Version:	1.8.2
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	4d87272ba1a224e78a9368986bb4510e
Patch0:		%{name}-pl_typos.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.xmule.org/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.7.3
BuildRequires:	bison
BuildRequires:	expat-devel
BuildRequires:	gettext-devel >= 0.11.5
%if %{with gtk1}
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	wxGTK-devel >= 2.4.0
%else
BuildRequires:	gtk+2-devel
BuildRequires:	wxGTK2-devel >= 2.4.0
%endif
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
%setup  -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub .
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	--with-wx-config=/usr/bin/wxgtk%{!?with_gtk1:2}-2.4-config \
	--enable-optimise \
	--enable-profile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}
install src/{ed2k,xmule} $RPM_BUILD_ROOT%{_bindir}
install xmule.desktop $RPM_BUILD_ROOT%{_desktopdir}/xmule.desktop
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
%{_desktopdir}/%{name}.desktop
