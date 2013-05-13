Summary:	A gesture-recognition application for X11
Name:		easystroke
Version:	0.5.5.1
Release:	2
Group:		Accessibility
License:	ISC
Url:		http://easystroke.sourceforge.net/
Source0:	http://downloads.sourceforge.net/easystroke/%{name}-%{version}.tar.gz

BuildRequires:	gtkmm2.4-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	x11-server-devel
BuildRequires:	intltool
BuildRequires:	help2man

%description
Easystroke is a gesture-recognition application for X11. Gestures or 
strokes are movements that you make with you mouse (or your pen, 
finger etc.) while holding down a specific mouse button. Easystroke 
will execute certain actions if it recognizes the stroke; currently 
easystroke can emulate key presses, execute shell commands, hold down 
modifiers and emulate a scroll wheel. 
The program was designed with Tablet PCs in mind and can be used 
effectively even without access to a keyboard. Easystroke tries to 
provide an intuitive and efficient user interface, while at the same 
time being highly configurable and offering many advanced features. 

%prep
%setup -q
# fix PREFIX
sed -i -e 's:/usr/local:%{_prefix}:' Makefile

%build
%make	CXX="g++ %{optflags}" \
	CC="gcc -std=c99 %{optflags}" \
	LDFLAGS="%{ldflags}"

# man page
make man

%install
%makeinstall_std

# man page install
install -D -m644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%find_lang %{name}

%files -f %{name}.lang
%doc LICENSE changelog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}*



%changelog
* Fri Jun 08 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.5.5.1-2
+ Revision: 803597
- rebuild for boost lib
- cleaned up spec

* Thu Oct 13 2011 Andrey Bondrov <abondrov@mandriva.org> 0.5.5.1-1
+ Revision: 704592
- New version: 0.5.5.1

* Mon Mar 14 2011 Funda Wang <fwang@mandriva.org> 0.5.3-3
+ Revision: 644476
- rebuild for new boost

* Mon Aug 23 2010 Funda Wang <fwang@mandriva.org> 0.5.3-2mdv2011.0
+ Revision: 572153
- rebuild for new boost

* Sun Feb 14 2010 Jérôme Brenier <incubusss@mandriva.org> 0.5.3-1mdv2011.0
+ Revision: 505851
- add a precison : x11-server-devel >= 1.7

* Sun Feb 14 2010 Jérôme Brenier <incubusss@mandriva.org> 0.5.3-1mdv2010.1
+ Revision: 505618
- new version 0.5.3
- drop Patch0 (merged upstream)

* Mon Feb 08 2010 Anssi Hannula <anssi@mandriva.org> 0.5.2-3mdv2010.1
+ Revision: 501882
- rebuild for new boost

* Fri Feb 05 2010 Jérôme Brenier <incubusss@mandriva.org> 0.5.2-2mdv2010.1
+ Revision: 501026
- rebuild

  + Funda Wang <fwang@mandriva.org>
    - BR x11 server
    - New version 0.5.2
    - rebuild for new boost

* Wed Dec 23 2009 Jérôme Brenier <incubusss@mandriva.org> 0.4.10-2mdv2010.1
+ Revision: 481773
- buildrequires help2man
- add the man page

* Wed Dec 23 2009 Jérôme Brenier <incubusss@mandriva.org> 0.4.10-1mdv2010.1
+ Revision: 481639
- import easystroke


