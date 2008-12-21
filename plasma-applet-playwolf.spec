%define     oname  playwolf
Summary:	A simple plasmoid that controls amaroK 2 using D-Bus
Name:		plasma-applet-playwolf
Version: 	0.3.1
Release: 	%mkrel 1
Source0:    93882-%oname-%version.tar.bz2	
License: 	GPLv2+
Group: 		Graphical desktop/KDE
Url: 		http://kde-look.org/content/show.php/PlayWolf?content=93882
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	amarok >= 3:1.80
Obsoletes:  plasma-applet-am4rok
Provides:   plasma-applet-am4rok
BuildRequires: 	plasma-devel >= 4.0.70

%description 
This is a simple plasmoid that controls amaroK 2 using D-Bus.

%files
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_playwolf.so
%_kde_datadir/kde4/services/plasma-applet-playwolf.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %oname

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
cd build
%{makeinstall_std}
cd -

%clean
rm -rf %{buildroot}