%{!?dist: %define dist .el6}
%define debug_package %{nil}

Summary: HTCondor Machine Job Features Discovery and Implementation
Name: htcondor-mjf
Version: 0.1
Release: 1%{?dist}
BuildArch: noarch
Source: %{name}-%{version}.tgz
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Packager: iain.steers@cern.ch
Vendor: CERN 
License: Apache 2.0
URL: https://github.com/IainSteers/htcondor-mjf

BuildRequires: python-devel
Requires: condor >= 8.0.0

%description
An extensible backend for handling and generating HTCondor Machine Job Features
according to the specification.

%prep
%setup -q

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr (-, root, root)
%{python_sitelib}/*
