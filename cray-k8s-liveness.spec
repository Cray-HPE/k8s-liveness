# Copyright 2024 Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# (MIT License)

# Define which Python flavors python-rpm-macros will use (this can be a list).
# https://github.com/openSUSE/python-rpm-macros#terminology
%define pythons %(echo ${PYTHON_BIN})
%define py_version %(echo ${PY_VERSION})

Name: %(echo ${RPM_NAME})
License: MIT
Summary: Cray Kubernetes liveness Python package for Python %{py_version}
Group: System/Management
Version: %(cat .version)
Release: %(echo ${BUILD_METADATA})
Source: %{name}-%{version}.tar.bz2
BuildArch: %(echo ${RPM_ARCH})
Vendor: Cray Inc.
# Using or statements in spec files requires RPM >= 4.13
BuildRequires: rpm-build >= 4.13
Requires: rpm >= 4.13
BuildRequires: (python%{python_version_nodots}-base or python3-base >= %{py_version})
BuildRequires: python-rpm-generators
BuildRequires: python-rpm-macros
Requires: (python%{python_version_nodots}-base or python3-base >= %{py_version})

%description
Cray Kubernetes liveness Python package for Python %{py_version}

%prep
%setup
%python_exec -m pip install --user --upgrade pip

%build

%install
%python_exec -m pip install ./dist/*.whl --root %{buildroot} --no-deps --force-reinstall
find %{buildroot} -type f -print | tee -a PY3_INSTALLED_FILES
sed -i -e 's:^%{buildroot}::' -e 's:^\([^/]\):/\1:' PY3_INSTALLED_FILES
cat PY3_INSTALLED_FILES

%files -f PY3_INSTALLED_FILES
%defattr(-,root,root)
