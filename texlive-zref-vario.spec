%global tl_name zref-vario
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.12
Release:	%{tl_revision}.1
Summary:	Extended LaTeX page cross-references with varioref and zref-clever
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/zref-vario
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zref-vario.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zref-vario.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zref-vario.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(tools)
Requires:	texlive(zref-clever)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package offers a compatibility layer for varioref to be used
alongside zref-clever. It provides \z... counterparts to varioref's main
reference commands, each of which essentially does some (scoped) setup
for varioref, then calls the original one.

