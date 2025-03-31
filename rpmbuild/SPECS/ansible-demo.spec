Name: ansible-demo
Version: 0.1
Release: 1%{?dist}
Summary: Utility for running Ansible playbooks
License: MIT
Source0: ansible-demo-0.1.tar.gz
BuildRequires: python3-setuptools ansible

%description
This package allows running Ansible playbooks from the command line.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/demo
