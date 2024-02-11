# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-netifaces
Epoch: 100
Version: 0.11.0
Release: 1%{?dist}
Summary: Portable network interface information
License: MIT
URL: https://github.com/al45tair/netifaces/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This package provides a cross platform API for getting address
information from network interfaces.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-netifaces
Summary: Portable network interface information
Requires: python3
Provides: python3-netifaces = %{epoch}:%{version}-%{release}
Provides: python3dist(netifaces) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-netifaces = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(netifaces) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-netifaces = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(netifaces) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-netifaces
This package provides a cross platform API for getting address
information from network interfaces.

%files -n python%{python3_version_nodots}-netifaces
%license LICENSE
%{python3_sitearch}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-netifaces
Summary: Portable network interface information
Requires: python3
Provides: python3-netifaces = %{epoch}:%{version}-%{release}
Provides: python3dist(netifaces) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-netifaces = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(netifaces) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-netifaces = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(netifaces) = %{epoch}:%{version}-%{release}

%description -n python3-netifaces
This package provides a cross platform API for getting address
information from network interfaces.

%files -n python3-netifaces
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-netifaces
Summary: Portable network interface information
Requires: python3
Provides: python3-netifaces = %{epoch}:%{version}-%{release}
Provides: python3dist(netifaces) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-netifaces = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(netifaces) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-netifaces = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(netifaces) = %{epoch}:%{version}-%{release}

%description -n python3-netifaces
This package provides a cross platform API for getting address
information from network interfaces.

%files -n python3-netifaces
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog