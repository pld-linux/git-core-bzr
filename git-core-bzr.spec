%bcond_with	tests

Summary:	Git tools for working with mercurial repositories
Name:		git-core-bzr
Version:	0.3
Release:	1
Epoch:		1
License:	GPL v2
Group:		Development/Tools
Source0:	https://github.com/felipec/git-remote-bzr/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	8cd2a654e9ef928bb89ff8524faaa8a1
URL:		https://github.com/felipec/git-remote-bzr
BuildRequires:	rpm-pythonprov
Requires:	bzr
Requires:	git-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Git tools for working with mercurial repositories.

%define         gitcoredir      %{_libexecdir}/git-core

%prep
%setup -q -n git-remote-bzr-%{version}

%{__sed} -i -e '1s,/usr/bin/env python2$,%{__python2},' git-remote-bzr

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
