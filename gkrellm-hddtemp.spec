%define		_beta beta
Summary:	Hddtemp plugin for GKrellM
Summary(pl):	Wtyczka hddtemp dla GKrellM
Name:		gkrellm-hddtemp
Version:	0.2
Release:	0.%{_beta}.2
License:	GPL
Group:		X11/Applications
Source0:	http://www.guzu.net/linux/%{name}-%{version}-%{_beta}.tar.gz
# Source0-md5:	b4f3b90692acbce1f74cac05ce2264fa
URL:		http://www.guzu.net/linux/hddtemp.php
BuildRequires:	gkrellm-devel >= 2.0
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
Requires:	gkrellm >= 2.0
Requires:	hddtemp-hddtempd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hard disk drive temperature plugin for GKrellM.

%description -l pl
Wtyczka pomiaru temperatury twardego dysku dla GKrellM.

%prep
%setup -q -n %{name}-%{version}-%{_beta}

%build
%{__make} gkrellm2

%install
rm -rf $RPM_BUILD_ROOT
install -D gkrellm-hddtemp.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins/gkrellm-hddtemp.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/gkrellm-hddtemp.so
