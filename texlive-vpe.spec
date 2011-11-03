# revision 18835
# category Package
# catalog-ctan /macros/latex/contrib/vpe
# catalog-date 2007-03-13 09:06:46 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-vpe
Version:	0.1
Release:	1
Summary:	Source specials for PDF output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/vpe
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vpe.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vpe.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-vpe.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3

%description
VPE is a system to make the equivalent of "source special"
marks in a PDF file. Clicking on a mark will activate an
editor, pointing at the source line that produced the text that
was marked. The system comprises a perl file (vpe.pl) and a
LaTeX package (vpe.sty); it will work with PDF files generated
via LaTeX/dvips, pdfTeX (version 0.14 or better), and
LaTeX/VTeX. Using the LaTeX/dvips or pdfLaTeX routes, the
(pdf)TeX processor shoud be run with shell escapes enabled.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/vpe
%{_texmfdistdir}/scripts/vpe/vpe.pl
%{_texmfdistdir}/tex/latex/vpe/vpe.sty
%doc %{_texmfdistdir}/doc/latex/vpe/vpe.txt
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/vpe/vpe.pl vpe
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
