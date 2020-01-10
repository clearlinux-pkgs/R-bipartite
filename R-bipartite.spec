#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bipartite
Version  : 2.14
Release  : 28
URL      : https://cran.r-project.org/src/contrib/bipartite_2.14.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bipartite_2.14.tar.gz
Summary  : Visualising Bipartite Networks and Calculating Some (Ecological)
Group    : Development/Tools
License  : GPL-2.0
Requires: R-bipartite-lib = %{version}-%{release}
Requires: R-fields
Requires: R-igraph
Requires: R-permute
Requires: R-sna
Requires: R-vegan
BuildRequires : R-fields
BuildRequires : R-igraph
BuildRequires : R-permute
BuildRequires : R-sna
BuildRequires : R-statnet.common
BuildRequires : R-vegan
BuildRequires : buildreq-R
BuildRequires : texlive

%description
No detailed description available

%package lib
Summary: lib components for the R-bipartite package.
Group: Libraries

%description lib
lib components for the R-bipartite package.


%prep
%setup -q -c -n bipartite

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1578692630

%install
export SOURCE_DATE_EPOCH=1578692630
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bipartite
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bipartite
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bipartite
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc bipartite || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bipartite/CITATION
/usr/lib64/R/library/bipartite/DESCRIPTION
/usr/lib64/R/library/bipartite/INDEX
/usr/lib64/R/library/bipartite/Meta/Rd.rds
/usr/lib64/R/library/bipartite/Meta/data.rds
/usr/lib64/R/library/bipartite/Meta/features.rds
/usr/lib64/R/library/bipartite/Meta/hsearch.rds
/usr/lib64/R/library/bipartite/Meta/links.rds
/usr/lib64/R/library/bipartite/Meta/nsInfo.rds
/usr/lib64/R/library/bipartite/Meta/package.rds
/usr/lib64/R/library/bipartite/Meta/vignette.rds
/usr/lib64/R/library/bipartite/NAMESPACE
/usr/lib64/R/library/bipartite/R/bipartite
/usr/lib64/R/library/bipartite/R/bipartite.rdb
/usr/lib64/R/library/bipartite/R/bipartite.rdx
/usr/lib64/R/library/bipartite/data/Rdata.rdb
/usr/lib64/R/library/bipartite/data/Rdata.rds
/usr/lib64/R/library/bipartite/data/Rdata.rdx
/usr/lib64/R/library/bipartite/doc/Dormann2008Rnews.pdf
/usr/lib64/R/library/bipartite/doc/Dormann2009OpenEcolJ.pdf
/usr/lib64/R/library/bipartite/doc/Dormann2011NetworkBiology.pdf
/usr/lib64/R/library/bipartite/doc/Intro2bipartite.R
/usr/lib64/R/library/bipartite/doc/Intro2bipartite.Rnw
/usr/lib64/R/library/bipartite/doc/Intro2bipartite.pdf
/usr/lib64/R/library/bipartite/doc/index.html
/usr/lib64/R/library/bipartite/help/AnIndex
/usr/lib64/R/library/bipartite/help/aliases.rds
/usr/lib64/R/library/bipartite/help/bipartite.rdb
/usr/lib64/R/library/bipartite/help/bipartite.rdx
/usr/lib64/R/library/bipartite/help/paths.rds
/usr/lib64/R/library/bipartite/html/00Index.html
/usr/lib64/R/library/bipartite/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/bipartite/libs/bipartite.so
/usr/lib64/R/library/bipartite/libs/bipartite.so.avx2
/usr/lib64/R/library/bipartite/libs/bipartite.so.avx512
