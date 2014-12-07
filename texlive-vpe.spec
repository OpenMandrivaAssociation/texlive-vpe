# revision 26039
# category Package
# catalog-ctan /macros/latex/contrib/vpe
# catalog-date 2012-04-18 16:26:37 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-vpe
Version:	0.2
Release:	8
Summary:	Source specials for PDF output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/vpe
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vpe.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vpe.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-vpe.bin = %{EVRD}

%description
VPE is a system to make the equivalent of "source special"
marks in a PDF file. Clicking on a mark will activate an
editor, pointing at the source line that produced the text that
was marked. The system comprises a perl file (vpe.pl) and a
LaTeX package (vpe.sty); it will work with PDF files generated
via LaTeX/dvips, pdfTeX (version 0.14 or better), and
LaTeX/VTeX. Using the LaTeX/dvips or pdfLaTeX routes, the
(pdf)TeX processor should be run with shell escapes enabled.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/vpe
%{_texmfdistdir}/scripts/vpe/vpe.pl
%{_texmfdistdir}/tex/latex/vpe/vpe.sty
%doc %{_texmfdistdir}/doc/latex/vpe/README

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


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 813174
- Update to latest release.

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 757489
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 719896
- texlive-vpe
- texlive-vpe
- texlive-vpe

