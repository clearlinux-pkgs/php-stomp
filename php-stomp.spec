#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-stomp
Version  : 2.0.2
Release  : 1
URL      : https://pecl.php.net//get/stomp-2.0.2.tgz
Source0  : https://pecl.php.net//get/stomp-2.0.2.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-stomp-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
stomp
=====
This extension allows php applications to communicate with any Stomp compliant Message Broker(s) through easy object
oriented and procedural interfaces.

%package lib
Summary: lib components for the php-stomp package.
Group: Libraries

%description lib
lib components for the php-stomp package.


%prep
%setup -q -n stomp-2.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20180731/stomp.so