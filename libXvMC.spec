#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCFDF148828C642A7 (alanc@freedesktop.org)
#
Name     : libXvMC
Version  : 1.0.11
Release  : 16
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXvMC-1.0.11.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXvMC-1.0.11.tar.gz
Source99 : http://xorg.freedesktop.org/releases/individual/lib/libXvMC-1.0.11.tar.gz.sig
Summary  : X11 Video Motion Compensation extension library
Group    : Development/Tools
License  : MIT
Requires: libXvMC-lib = %{version}-%{release}
Requires: libXvMC-license = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32videoproto)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(32xextproto)
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(32xv)
BuildRequires : pkgconfig(videoproto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xv)

%description
libXvMC - X-Video Motion Compensation API
-----------------------------------------

%package dev
Summary: dev components for the libXvMC package.
Group: Development
Requires: libXvMC-lib = %{version}-%{release}
Provides: libXvMC-devel = %{version}-%{release}
Requires: libXvMC = %{version}-%{release}

%description dev
dev components for the libXvMC package.


%package dev32
Summary: dev32 components for the libXvMC package.
Group: Default
Requires: libXvMC-lib32 = %{version}-%{release}
Requires: libXvMC-dev = %{version}-%{release}

%description dev32
dev32 components for the libXvMC package.


%package doc
Summary: doc components for the libXvMC package.
Group: Documentation

%description doc
doc components for the libXvMC package.


%package lib
Summary: lib components for the libXvMC package.
Group: Libraries
Requires: libXvMC-license = %{version}-%{release}

%description lib
lib components for the libXvMC package.


%package lib32
Summary: lib32 components for the libXvMC package.
Group: Default
Requires: libXvMC-license = %{version}-%{release}

%description lib32
lib32 components for the libXvMC package.


%package license
Summary: license components for the libXvMC package.
Group: Default

%description license
license components for the libXvMC package.


%prep
%setup -q -n libXvMC-1.0.11
pushd ..
cp -a libXvMC-1.0.11 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552834381
export LDFLAGS="${LDFLAGS} -fno-lto"
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1552834381
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libXvMC
cp COPYING %{buildroot}/usr/share/package-licenses/libXvMC/COPYING
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/XvMClib.h
/usr/lib64/libXvMC.so
/usr/lib64/libXvMCW.so
/usr/lib64/pkgconfig/xvmc.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libXvMC.so
/usr/lib32/libXvMCW.so
/usr/lib32/pkgconfig/32xvmc.pc
/usr/lib32/pkgconfig/xvmc.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libXvMC/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXvMC.so.1
/usr/lib64/libXvMC.so.1.0.0
/usr/lib64/libXvMCW.so.1
/usr/lib64/libXvMCW.so.1.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libXvMC.so.1
/usr/lib32/libXvMC.so.1.0.0
/usr/lib32/libXvMCW.so.1
/usr/lib32/libXvMCW.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libXvMC/COPYING
