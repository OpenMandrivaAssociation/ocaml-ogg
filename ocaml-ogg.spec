Name:           ocaml-ogg
Version:        0.3.1
Release:        %mkrel 2
Summary:        OCaml bindings for the Ogg bitstream library
License:        LGPL with exceptions
Group:          Development/Other
URL:            http://sourceforge.net/projects/savonet/files/
Source0:        http://downloads.sourceforge.net/savonet/ocaml-ogg/ocaml-ogg-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml-findlib
BuildRequires:  libogg-devel

%description
OCaml bindings for the Ogg bitstream library, libogg is a library
for manipulating ogg bitstreams. It handles both making ogg bitstreams
and getting packets from ogg bitstreams.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure
make
make doc

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/ogg
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING CHANGES README
%dir %{_libdir}/ocaml/ogg
%{_libdir}/ocaml/ogg/META
%{_libdir}/ocaml/ogg/*.cma
%{_libdir}/ocaml/ogg/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc doc/html
%{_libdir}/ocaml/ogg/*.a
%{_libdir}/ocaml/ogg/*.cmxa
%{_libdir}/ocaml/ogg/*.mli
%{_libdir}/ocaml/ogg/*.h

