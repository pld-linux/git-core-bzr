#
# Conditional build:
%bcond_with	tests	# functional tests

Summary:	Git tools for working with Bazaar repositories
Summary(pl.UTF-8):	Narzędzia Gita do pracy z repozytoriami Bazaar
Name:		git-core-bzr
Version:	0.3
Release:	2
Epoch:		1
License:	GPL v2
Group:		Development/Tools
#Source0Download: https://github.com/felipec/git-remote-bzr/tags
# TODO use:
#Source0:	https://github.com/felipec/git-remote-bzr/archive/v%{version}/git-remote-bzr-%{version}.tar.gz
Source0:	https://github.com/felipec/git-remote-bzr/archive/v%{version}.tar.gz
# Source0-md5:	8cd2a654e9ef928bb89ff8524faaa8a1
URL:		https://github.com/felipec/git-remote-bzr
BuildRequires:	asciidoc
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	bzr
BuildRequires:	git-core
%endif
Requires:	bzr
Requires:	git-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Git tools for working with Bazaar repositories.

%description -l pl.UTF-8
Narzędzia Gita do pracy z repozytoriami Bazaar.

%define         gitcoredir      %{_libexecdir}/git-core

%prep
%setup -q -n git-remote-bzr-%{version}

%{__sed} -i -e '1s,/usr/bin/env python2$,%{__python},' git-remote-bzr

%build
%{__make} \
	V=1

%if %{with tests}
%{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{gitcoredir},%{_mandir}/man1}

cp -p git-remote-bzr $RPM_BUILD_ROOT%{gitcoredir}
cp -p doc/git-remote-bzr.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.asciidoc
%attr(755,root,root) %{gitcoredir}/git-remote-bzr
%{_mandir}/man1/git-remote-bzr.1*
