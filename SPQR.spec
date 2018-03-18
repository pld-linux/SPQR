Summary:	SuiteSparseQR: multithreaded multifrontal sparse QR factorization
Summary(pl.UTF-8):	SuiteSparseQR - wielowątkowy, wielofrontalny rozkład QR dla macierzy rzadkich
Name:		SPQR
Version:	1.3.3
Release:	3
License:	GPL v2+
Group:		Libraries
Source0:	http://www.cise.ufl.edu/research/sparse/SPQR/%{name}-%{version}.tar.gz
# Source0-md5:	bdd05fa144f68fe318510888a89e9906
Patch0:		%{name}-ufconfig.patch
Patch1:		%{name}-shared.patch
URL:		http://www.cise.ufl.edu/research/sparse/SPQR/
BuildRequires:	CHOLMOD-devel >= 2.0.0
BuildRequires:	SuiteSparse_config-devel >= 4.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
Requires:	CHOLMOD >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SuiteSparseQR is an implementation of the multifrontal sparse QR
factorization method. Parallelism is exploited both in the BLAS and
across different frontal matrices using Intel's Threading Building
Blocks, a shared-memory programming model for modern multicore
architectures. It can obtain a substantial fraction of the theoretical
peak performance of a multicore computer. The package is written in
C++ with user interfaces for MATLAB, C, and C++.

%description -l pl.UTF-8
SuiteSparseQR to implementacja wielofrontalnej metody rozkładu QR dla
macierzy rzadkich. Równoległość jest wykorzystywna zarówno w BLAS, jak
i poprzez różne macierze frontalne przy użyciu Threading Building
Blocks Intela - model programowania ze współdzieloną pamięcią dla
architektur wielordzeniowych. Dzięki temu możliwe jest osiągnięcie
znaczącej części teoretycznej maksymalnej wydajności na komputerze
wielordzeniowym. Pakiet jest napisany w C++ z interfejsami dla
MATLAB-a, C i C++.

%package devel
Summary:	Header files for SPQR library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SPQR
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	CHOLMOD-devel >= 2.0.0
Requires:	SuiteSparse_config-devel >= 4.0.0
Requires:	libstdc++-devel

%description devel
Header files for SPQR library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SPQR.

%package static
Summary:	Static SPQR library
Summary(pl.UTF-8):	Statyczna biblioteka SPQR
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SPQR library.

%description static -l pl.UTF-8
Statyczna biblioteka SPQR.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags}" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/spqr

%{__make} -C Lib install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

install Include/*.{h,hpp} $RPM_BUILD_ROOT%{_includedir}/spqr

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt Doc/ChangeLog
%attr(755,root,root) %{_libdir}/libspqr.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspqr.so.0

%files devel
%defattr(644,root,root,755)
%doc Doc/{algo_spqr,spqr,spqr_user_guide}.pdf
%attr(755,root,root) %{_libdir}/libspqr.so
%{_libdir}/libspqr.la
%{_includedir}/spqr

%files static
%defattr(644,root,root,755)
%{_libdir}/libspqr.a
