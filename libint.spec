Summary:	Evaluation of certain two-body molecular integrals over Cartesian Gaussian functions
Summary(pl):	Obliczania ca³ek dwuelementowych cz±steczek po kartezjañskich funkcjach Gaussa
Name:		libint
Version:	1.1.2
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: http://www.ccmst.gatech.edu/evaleev/libint/download.html
Source0:	http://www.ccmst.gatech.edu/evaleev/libint/src/%{name}-%{version}.tar.gz
# Source0-md5:	df23c63d46be7dd88a70a39e98f67d34
Patch0:		%{name}-link.patch
URL:		http://www.ccmst.gatech.edu/evaleev/libint/
BuildRequires:	libstdc++-devel >= 3.0
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libint library is used to evaluate the traditional (electron
repulsion) and certain novel two-body matrix elements (integrals) over
Cartesian Gaussian functions operative in modern atomic and molecular
theory. It is specifically designed with high efficiency on
(super)scalar computer architectures in mind. Libint has been utilized
to implement methods such as Hartree-Fock (HF) and Kohn-Sham density
functional theory (KS DFT), second-order Moller-Plesset perturbation
theory (MP2), coupled cluster singles and doubles (CCSD) method, as
well as the lesser known highly accurate linear R12 second-order
Moller-Plesset theory (MP2-R12).

%description -l pl
Biblioteka libint s³u¿y do obliczania tradycyjnych (odpychania
elektronowego) i pewnych nowych dwuelementowych elementów macierzy
(ca³ek) po kartezjañskich funkcjach Gaussa wystêpuj±cych we
wspó³czesnej teorii atomowej i cz±steczkowej. Jest zaprojektowana
zw³aszcza z my¶l± o (super)skalarnych architekturach komputerów.
libint jest wykorzystywana do implementowania metod takich jak:
metoda Hartree-Focka (HF) i teorii funkcjona³ów gêsto¶ci Kohna-Shama
(KS DFT), teorii zaburzeñ Mollera-Plesseta drugiego rzêdu (MP2),
metody klasterowej z jedno- i dwucia³owymi operatorami (CCSD), a tak¿e
mniej znanej bardzo dok³adnej teorii liniowej R12 Mollera-Plesseta
drugiego rzêdu (MP2-R12).

%package devel
Summary:	Header files for libint library
Summary(pl):	Pliki nag³ówkowe biblioteki libint
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 3.0

%description devel
Header files for libint library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libint.

%package static
Summary:	Static libint library
Summary(pl):	Statyczna biblioteka libint
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libint library.

%description static -l pl
Statyczna biblioteka libint.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-shared

sed -i -e 's/^CFLAGS =.*/CFLAGS = %{rpmcflags}/;s/^CXXFLAGS =.*/CXXFLAGS = %{rpmcxxflags}/' src/lib/MakeVars

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	libdir=$RPM_BUILD_ROOT%{_libdir}

# help rpm to find deps
chmod 755 $RPM_BUILD_ROOT%{_libdir}/lib*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_libdir}/libderiv-stable.so.*.*.*
%attr(755,root,root) %{_libdir}/libint-stable.so.*.*.*
%attr(755,root,root) %{_libdir}/libr12-stable.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libderiv.so
%attr(755,root,root) %{_libdir}/libint.so
%attr(755,root,root) %{_libdir}/libr12.so
%{_libdir}/libderiv.la
%{_libdir}/libint.la
%{_libdir}/libr12.la
%{_includedir}/libderiv
%{_includedir}/libint
%{_includedir}/libr12

%files static
%defattr(644,root,root,755)
%{_libdir}/libderiv.a
%{_libdir}/libint.a
%{_libdir}/libr12.a
