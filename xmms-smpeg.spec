%define name xmms-smpeg
%define version 0.3.5
%define release %mkrel 6

Name: %{name}
Summary: This plugin lets you play mpeg videos with the xmms multimedia player
Version: %{version}
Release: %{release}
License: GPL
Group: Video
Source0: ftp://ftp.xmms.org/xmms/plugins/smpeg-xmms/smpeg-xmms-%{version}.tar.bz2
Patch0:	%{name}-0.3.5-configure-gcc-3.3.fix.patch
URL: http://195.139.204.136/xmms/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires:	esound-devel
BuildRequires:	libsmpeg-devel
BuildRequires:	libxmms-devel
BuildRequires:	mawk
BuildRequires:	texinfo
BuildRequires:	automake1.4
BuildRequires:  gtk+-devel
Requires: xmms

%description
This plugin lets you play mpeg videos with the xmms multimedia player.

%prep
%setup -q -n smpeg-xmms-%{version}
%patch0 -p0
libtoolize --copy --force
aclocal-1.4
automake-1.4 -a -c --gnu
FORCE_AUTOCONF_2_5=1 autoconf-2.5x

%build
# I ran into big trouble using the %%configure script, because of libtoolize; it won't link the shared library
export CFLAGS=$RPM_OPT_FLAGS
export CXXFLAGS=$RPM_OPT_FLAGS
./configure %{_target_platform} --prefix=%{_prefix} --libdir=%{_libdir}
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README AUTHORS COPYING NEWS TODO
%{_libdir}/xmms/Input/*

