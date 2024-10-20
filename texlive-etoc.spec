Name:		texlive-etoc
Version:	69343
Release:	1
Summary:	Completely customisable TOCs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/etoc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etoc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etoc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etoc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package gives the user complete control of how the entries
of the table of contents should be constituted from the name,
number, and page number of each sectioning unit. The layout is
controlled by the definition of 'line styles' for each
sectioning level used in the document. The package provides its
own custom line styles (which may be used as examples), and
continues to support the standard formatting inherited from the
LaTeX document classes, but the package can also allow the user
to delegate the details to packages dealing with list making
environments (such as enumitem). The package's default global
style typesets tables of contents in a multi-column format,
with either a standard heading, or a ruled title (optionally
with a frame around the table). The \tableofcontents command
may be used arbitrarily many times in the same document, while
\localtableofcontents provides a 'local' table of contents.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/etoc
%doc %{_texmfdistdir}/doc/latex/etoc
#- source
%doc %{_texmfdistdir}/source/latex/etoc

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
