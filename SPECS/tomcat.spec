Name:		tomcat
Version:        9M
Release:        1
Summary:        tomcat-9M
Group:          Application/Web-Servers
URL:            https://tomcat.apache.org
License:	MIT
Source:         %{name}-%{version}.tar.gz
Prefix:         %{_prefix}
BuildRoot:      %{_tmppath}/%{name}-root

%description
tomcat-9M

%global debug_package %{nil}

%prep

%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure.sh --prefix=%{_prefix} --mandir=%{_mandir} --sysconfdir=/etc

%install
install -m 0755 -d $RPM_BUILD_ROOT/usr/local/%{name}-%{version}
cp -a . $RPM_BUILD_ROOT/usr/local/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(777,root,root) /usr/local/%{name}-%{version}/logs
%dir /usr/local/%{name}-%{version}
/usr/local/%{name}-%{version}

%post
if [ $1 == 1 ]; then
  echo 'installing tomcat'
  python /usr/local/%{name}-%{version}/install.py
else
  echo 'upgrading tomcat'
  python /usr/local/%{name}-%{version}/upgrade.py
fi

