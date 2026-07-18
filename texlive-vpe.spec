%global tl_name vpe
%global tl_revision 79618
%global tl_bin_links vpe:%{_texmfdistdir}/scripts/vpe/vpe.pl

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Source specials for PDF output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/vpe
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vpe.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vpe.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(vpe.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
VPE is a system to make the equivalent of "source special" marks in a
PDF file. Clicking on a mark will activate an editor, pointing at the
source line that produced the text that was marked. The system comprises
a perl file (vpe.pl) and a LaTeX package (vpe.sty); it will work with
PDF files generated via LaTeX/dvips, pdfTeX (version 0.14 or better),
and LaTeX/VTeX. Using the LaTeX/dvips or pdfLaTeX routes, the (pdf)TeX
processor should be run with shell escapes enabled.

