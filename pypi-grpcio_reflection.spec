#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-grpcio_reflection
Version  : 1.50.0
Release  : 32
URL      : https://files.pythonhosted.org/packages/c9/d0/39c619e7b53c762abc662bead3f842a69cfefc0ce23b1713b9f1d2de2abd/grpcio-reflection-1.50.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c9/d0/39c619e7b53c762abc662bead3f842a69cfefc0ce23b1713b9f1d2de2abd/grpcio-reflection-1.50.0.tar.gz
Summary  : Standard Protobuf Reflection Service for gRPC
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-grpcio_reflection-license = %{version}-%{release}
Requires: pypi-grpcio_reflection-python = %{version}-%{release}
Requires: pypi-grpcio_reflection-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(grpcio)
BuildRequires : pypi(protobuf)

%description
gRPC Python Reflection package
==============================
Reference package for reflection in GRPC Python.

%package license
Summary: license components for the pypi-grpcio_reflection package.
Group: Default

%description license
license components for the pypi-grpcio_reflection package.


%package python
Summary: python components for the pypi-grpcio_reflection package.
Group: Default
Requires: pypi-grpcio_reflection-python3 = %{version}-%{release}

%description python
python components for the pypi-grpcio_reflection package.


%package python3
Summary: python3 components for the pypi-grpcio_reflection package.
Group: Default
Requires: python3-core
Provides: pypi(grpcio_reflection)
Requires: pypi(grpcio)
Requires: pypi(protobuf)

%description python3
python3 components for the pypi-grpcio_reflection package.


%prep
%setup -q -n grpcio-reflection-1.50.0
cd %{_builddir}/grpcio-reflection-1.50.0
pushd ..
cp -a grpcio-reflection-1.50.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666135367
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-grpcio_reflection
cp %{_builddir}/grpcio-reflection-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-grpcio_reflection/242ec6abfdd8c114f2e803b84934469c299348fc || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-grpcio_reflection/242ec6abfdd8c114f2e803b84934469c299348fc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
