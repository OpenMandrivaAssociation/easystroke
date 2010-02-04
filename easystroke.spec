%define version		0.5.2
%define release		%mkrel 1

Summary:		A gesture-recognition application for X11
Name:			easystroke
Version:		%{version}
Release:		%{release}
Group:			Accessibility
License:		ISC
Url:			http://easystroke.sourceforge.net/
Source0:		http://downloads.sourceforge.net/easystroke/%{name}-%{version}.tar.gz
Patch0:			easystroke-0.5.2-timeout.patch
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:		gtkmm2.4-devel
BuildRequires:		dbus-glib-devel
BuildRequires:		boost-devel
BuildRequires:		libxtst-devel
BuildRequires:		intltool
BuildRequires:		help2man

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
%patch0 -p1
# fix PREFIX
sed -i -e 's:/usr/local:%{_prefix}:' Makefile

%build
%make	CXX="g++ %{optflags}" \
	CC="gcc -std=c99 %{optflags}" \
	LDFLAGS="%{ldflags}"

# man page
make man

%install
rm -rf %{buildroot}
%makeinstall_std

# man page install
install -D -m644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc LICENSE changelog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}*
