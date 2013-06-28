%define _fontsdir               %{_usr}/share/fonts
%define _ttfontsdir             %{_fontsdir}/truetype
%define _miscfontsdir           %{_fontsdir}/misc
%define _fontsconfdir           %{_sysconfdir}/fonts
%define _fontsconfddir          %{_fontsconfdir}/conf.d
%define _fontsconfavaildir      %{_datadir}/%{name}/conf.avail

%define cantarell_dir %{_fontsdir}/cantarell

Name:           cantarell-fonts
Version:        0.0.12
Release:        0
Summary:        Contemporary Humanist Sans Serif Font
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://live.gnome.org/CantarellFonts
Source:         http://download.gnome.org/sources/cantarell-fonts/0.0/%{name}-%{version}.tar.xz
Source1001: 	cantarell-fonts.manifest
BuildRequires:  dos2unix
BuildRequires:  fontconfig
BuildRequires:  pkg-config
BuildRequires:  xz
Requires(pre):  %{_bindir}/fc-cache
BuildArch:      noarch

%description
The Cantarell font family is a contemporary Humanist sans serif designed
for on-screen reading.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure
dos2unix COPYING

%install
make install DESTDIR=%{?buildroot} configdir=%{_fontsconfavaildir}
mkdir -p %{buildroot}%{_fontsconfddir}
ln -s ../../..%{_fontsconfavaildir}/31-cantarell.conf  %{buildroot}%{_fontsconfddir}

%post
%{_bindir}/fc-cache %{cantarell_dir} || :

%postun
%{_bindir}/fc-cache %{cantarell_dir} || :


%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%dir %{_datadir}/%{name}
%dir %{_fontsconfavaildir}
%{_fontsconfavaildir}/31-cantarell.conf
%config %{_fontsconfddir}/31-cantarell.conf
%dir %{cantarell_dir}
%{cantarell_dir}/Cantarell-Bold.otf
%{cantarell_dir}/Cantarell-Regular.otf

%changelog
