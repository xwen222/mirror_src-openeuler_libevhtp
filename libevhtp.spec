Name:     	libevhtp
Version:  	1.2.16
Release:  	2
Summary:  	Libevent based HTTP API.

License:  	BSD3
URL:      	https://criticalstack.com
Source0:  	https://github.com/criticalstack/%{name}/archive/%{name}-%{version}.tar.gz
Patch9000:   	0001-support-dynamic-threads.patch
Patch9001:   	0002-close-openssl.patch

BuildRequires: 	git gcc-c++ cmake libevent-devel

%description
Libevent based HTTP API.Libevent's http interface was created as a JIT server, never meant
to be a full-fledged HTTP service. This library attempts to improve on that with the following
features: + design as a fully functional HTTP server + HTTP parser able to process data with a
low memory footprint + use of regular expressions for routing + out-of-the box HTTPS server
This package contains the runtime library.

%package 	devel
Summary: 	Headers for developing programs that will use %{name} 
Requires: 	%{name} = %{version}-%{release}

%description 	devel
%{name}-devel contains the header files for developing
applications that want to make use of %{name}.

%global debug_package %{nil}

%prep
%autosetup -n %{name}-%{version} -p1 

%build
mkdir -p build
cd build
%cmake -DEVHTP_BUILD_SHARED=ON -DEVHTP_DISABLE_SSL=ON -DLIB_INSTALL_DIR=lib ..
%make_build

%install
rm -rf %{buildroot}
cd build
%make_install

%delete_la_and_a
find %{buildroot} -name '*.cmake' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%defattr(-,root,root)
/usr/lib/%{name}.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_includedir}/evhtp/*.h
/usr/lib/%{name}.so
/usr/lib/pkgconfig/evhtp.pc

%changelog
* Sun Sep 15 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.2.16-2
- Package init

