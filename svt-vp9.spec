Summary:	Scalable Video Technology for VP9 encoder library
Summary(pl.UTF-8):	Biblioteka kodera Scalable Video Technology dla VP9
Name:		svt-vp9
Version:	0.3.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/OpenVisualCloud/SVT-VP9/releases
Source0:	https://github.com/OpenVisualCloud/SVT-VP9/archive/v%{version}/SVT-VP9-%{version}.tar.gz
# Source0-md5:	1490ef3d1ce01ff06fd289a0df46870f
Patch0:		%{name}-x32.patch
URL:		https://github.com/OpenVisualCloud/SVT-VP9
BuildRequires:	cmake >= 2.8
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	yasm >= 1.2.0
ExclusiveArch:	%{x8664} x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Scalable Video Technology for VP9 Encoder (SVT-VP9 Encoder) is a
VP9-compliant encoder library core. The SVT-VP9 Encoder development is
a work-in-progress targeting performance levels applicable to both VOD
and Live encoding/transcoding video applications.

%description -l pl.UTF-8
Koder Scalable Video Technology dla VP9 to główna biblioteka kodera
zgodnego z VP9. Rozwój kodera SVT-VP9 trwa, a jego celem jest
osiągnięcie wydajności nadającej się do kodowania i przekodowywania
obrazu zarówno VOD, jak i w czasie rzeczywistym.

%package devel
Summary:	Header files for SVT-VP9 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SVT-VP9
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for SVT-VP9 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SVT-VP9.

%prep
%setup -q -n SVT-VP9-%{version}
%patch -P0 -p1

%build
install -d build
cd build
%cmake .. \
%ifarch x32
	-DCMAKE_ASM_NASM_OBJECT_FORMAT=elfx32
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.md NOTICES.md README.md
%attr(755,root,root) %{_bindir}/SvtVp9EncApp
%attr(755,root,root) %{_libdir}/libSvtVp9Enc.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSvtVp9Enc.so
%{_includedir}/svt-vp9
%{_pkgconfigdir}/SvtVp9Enc.pc
