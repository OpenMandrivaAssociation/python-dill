Name:		python-dill
Version:	0.3.6
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/d/dill/dill-%{version}.tar.gz
Summary:	serialize all of python
URL:		https://pypi.org/project/dill/
License:	3-clause BSD
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildArch:	noarch

%description
serialize all of python

%prep
%autosetup -p1 -n dill-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/*
%{py_sitedir}/dill
%{py_sitedir}/dill-*.dist-info
