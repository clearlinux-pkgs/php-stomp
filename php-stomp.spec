#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-stomp
Version  : 2.0.3
Release  : 67
URL      : https://pecl.php.net/get/stomp-2.0.3.tgz
Source0  : https://pecl.php.net/get/stomp-2.0.3.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-stomp-lib = %{version}-%{release}
Requires: php-stomp-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : perl(Getopt::Long)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
stomp
=====
This extension allows php applications to communicate with any Stomp compliant Message Broker(s) through easy object
oriented and procedural interfaces.

%package lib
Summary: lib components for the php-stomp package.
Group: Libraries
Requires: php-stomp-license = %{version}-%{release}

%description lib
lib components for the php-stomp package.


%package license
Summary: license components for the php-stomp package.
Group: Default

%description license
license components for the php-stomp package.


%prep
%setup -q -n stomp-2.0.3
cd %{_builddir}/stomp-2.0.3
pushd ..
cp -a stomp-2.0.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-stomp
cp %{_builddir}/stomp-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-stomp/b5469c326673cd097cc5e081bf40b1d9c0577644 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/stomp.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-stomp/b5469c326673cd097cc5e081bf40b1d9c0577644
