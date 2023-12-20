Name:		texlive-zref-vario
Version:	68846
Release:	1
Summary:	Extended LaTeX page cross-references with varioref and zref-clever
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/zref-vario
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zref-vario.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zref-vario.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zref-vario.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package offers a compatibility layer for varioref to be
used alongside zref-clever. It provides \z... counterparts to
varioref's main reference commands, each of which essentially
does some (scoped) setup for varioref, then calls the original
one.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/zref-vario
%{_texmfdistdir}/tex/latex/zref-vario
%doc %{_texmfdistdir}/doc/latex/zref-vario

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
