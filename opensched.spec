Summary:	Opensched is a tool for project management
Summary(pl):	Opensched jest narzêdziem do zarz±dzania projektami
Name:		opensched
Version:	0.3.8
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	224459867aef89502e0b3806ec8b4262
Source1:	%{name}-eps2png.sh
URL:		http://opensched.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tetex-latex
Requires:	ghostscript
Requires:	psutils
Requires:	awk
Requires:	netpbm-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Opensched is a tool for project management. It takes as input a file
describing the project and generates the following:

- Textural descriptions of the generated project plan.
- Gantt charts.
- Network diagrams.

The textural description can be generated in one or more of raw text,
HTML, and TeX formats. The Gantt charts and network diagrams are
generated directly as EPS drawings. The package contains a routine to
convert these to PNGs.

%description -l pl
Opensched jest narzêdziem do zarz±dzania projektami. Przyjmuje jako
wej¶cie plik opisuj±cy projekt i generuje:

- tekstowy opis wygenerowanego planu przebiegu projektu,
- wykresy Gantta,
- grafy zale¿no¶ci

Tekstowy opis mo¿e byæ generowany w jednym lub wiêcej z formatów:
tekst, HTML, TeX. Wykresy Gantta i grafy zale¿no¶ci s± generowane jako
obrazy w formacie EPS. Pakiet zawiera skrypt do konwertowania tych
obrazów na PNGy.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}-eps2png

rm -f gui/Makefile* $RPM_BUILD_ROOT%{_bindir}/*gif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html gui examples README ChangeLog ChangeLog.0 AUTHORS
%attr(755,root,root) %{_bindir}/opensched*
%{_mandir}/man*/*
