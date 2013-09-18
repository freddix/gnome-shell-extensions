Summary:	Collection of GNOME Shell extensions
Name:		gnome-shell-extensions
Version:	3.8.4
Release:	1
Group:		X11/Applications
License:	GPL v2 / BSD
# not available as tarball yet
Source0:	http://download.gnome.org/sources/gnome-shell-extensions/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	b891f58cb10a489b069a4e5aef9be21f
URL:		http://live.gnome.org/GnomeShell/Extensions
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-desktop-devel
BuildRequires:	intltool
BuildRequires:	libgtop-devel
BuildRequires:	libtool
Requires(post,postun):	glib-gio-gsettings
Requires:	gnome-shell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Shell Extensions is a collection of extensions providing
additional and optional functionality to GNOME Shell.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-compile	\
	--disable-silent-rules		\
	--enable-extensions=all
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING NEWS README
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.alternative-status-menu.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.auto-move-windows.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.classic-overrides.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.native-window-placement.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.user-theme.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.window-list.gschema.xml

%{_datadir}/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.gcampax.github.com
%{_datadir}/gnome-shell/extensions/alternative-status-menu@gnome-shell-extensions.gcampax.github.com
%{_datadir}/gnome-shell/extensions/apps-menu@gnome-shell-extensions.gcampax.github.com
%{_datadir}/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.gcampax.github.com
%{_datadir}/gnome-shell/extensions/drive-menu@gnome-shell-extensions.gcampax.github.com
%{_datadir}/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com
%{_datadir}/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.gcampax.github.com
%{_datadir}/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com
%{_datadir}/gnome-shell/extensions/systemMonitor@gnome-shell-extensions.gcampax.github.com
%{_datadir}/gnome-shell/extensions/user-theme@gnome-shell-extensions.gcampax.github.com
%{_datadir}/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com
%{_datadir}/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.gcampax.github.com
%{_datadir}/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com
%{_datadir}/gnome-shell/extensions/xrandr-indicator@gnome-shell-extensions.gcampax.github.com

%{_datadir}/gnome-session/sessions/gnome-classic.session
%{_datadir}/gnome-shell/modes/classic.json
%{_datadir}/gnome-shell/theme/classic-process-working.svg
%{_datadir}/gnome-shell/theme/classic-toggle-off-intl.svg
%{_datadir}/gnome-shell/theme/classic-toggle-off-us.svg
%{_datadir}/gnome-shell/theme/classic-toggle-on-intl.svg
%{_datadir}/gnome-shell/theme/classic-toggle-on-us.svg
%{_datadir}/gnome-shell/theme/gnome-classic.css
%{_datadir}/xsessions/gnome-classic.desktop
%{_desktopdir}/gnome-shell-classic.desktop
