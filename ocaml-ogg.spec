Name:           ocaml-ogg
Version:        0.4.0
Release:        2
Summary:        OCaml bindings for the Ogg bitstream library
License:        LGPL with exceptions
Group:          Development/Other
URL:            http://sourceforge.net/projects/savonet/files/
Source0:        http://downloads.sourceforge.net/savonet/ocaml-ogg/ocaml-ogg-%{version}.tar.gz
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml
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
%configure2_5x
make
make doc

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/ogg
make install

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



%changelog
* Wed Oct 06 2010 Funda Wang <fwang@mandriva.org> 0.4.0-2mdv2011.0
+ Revision: 583529
- rebuild

* Mon Aug 23 2010 Florent Monnier <blue_prawn@mandriva.org> 0.4.0-1mdv2011.0
+ Revision: 572242
- updated to last version 0.4.0

* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-2mdv2010.1
+ Revision: 496367
- rebuild
- update to new version 0.3.1

  + Florent Monnier <blue_prawn@mandriva.org>
    - a better Source0 field

* Sat Aug 01 2009 Florent Monnier <blue_prawn@mandriva.org> 0.3.0-1mdv2010.0
+ Revision: 405294
- import ocaml-ogg


