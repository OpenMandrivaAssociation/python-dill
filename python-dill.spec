%define module dill

Name:		python-dill
Version:	0.4.1
Release:	1
Summary:	Serialize all of python
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/dill/
Source0:	https://files.pythonhosted.org/packages/source/d/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(objgraph)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
dill extends Python’s pickle module for serializing and de-serializing Python
objects to the majority of the built-in Python types. Serialization is the
process of converting an object to a byte stream, and the inverse of which is
converting a byte stream back to a Python object hierarchy.

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module}.egg-info

%install
%py_install

# Remove shebangs from (installed) non-script sources. The find-then-modify
# pattern preserves mtimes on sources that did not need to be modified.
find '%{buildroot}%{python3_sitelib}/dill' -type f -name '*.py' ! -perm /0111 \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'

%files
%doc README.md
%license LICENSE
%{_bindir}/un%{module}
%{_bindir}/get_objgraph
%{_bindir}/get_gprof
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
