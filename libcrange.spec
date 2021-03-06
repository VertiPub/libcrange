Name:		libcrange
Version:	1.0.1
Release:	3%{?dist}
Summary:	C version of range

Group:		Base
License:	GPL
URL:		http://github.com/ytoolshed/libcrange
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: libyaml-devel pcre-devel apr-devel sqlite-devel
Requires:      libyaml perl-ExtUtils-Embed pcre apr sqlite

%description


%prep
%setup -q


%build
aclocal || exit 1
libtoolize --force || exit 1
autoheader || exit 1
automake -a || exit 1
autoconf || exit 1
%configure --prefix=/usr
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/crange
%{_includedir}/libcrange.h
%{_libdir}/libcrange*


%changelog

