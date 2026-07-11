%global tl_name etoc
%global tl_revision 78908

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2e
Release:	%{tl_revision}.1
Summary:	Completely customisable TOCs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/etoc
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etoc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etoc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etoc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
With etoc loaded, \tableofcontents can be used multiple times, and an
added command \localtableofcontents allows to typeset "local" tables of
contents, i.e. TOCs having their scope limited to the last sectioning
command encountered. Since release 1.2, also \locallistoffigures and
\locallistoftables are available. Loading etoc per itself does not
modify the "contents lines" inherited from the class default or changed
via other packages. But full usage of the package allows spectacular
effects such as displaying TOCs as trees or mind maps.

