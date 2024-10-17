Name: firejail
Version: 0.9.72
Release: 2
Summary: Linux namepaces sandbox program
License: GPLv2+
Group: Development/Tools
Source0: https://github.com/netblue30/firejail/releases/download/%{version}/firejail-%{version}.tar.xz
URL: https://github.com/netblue30/firejail
Requires: xdg-dbus-proxy

%description
Firejail is a SUID sandbox program that reduces the risk of security
breaches by restricting the running environment of untrusted applications
using Linux namespaces. It includes a number of sandbox profiles for
applications such as Mozilla Firefox.

%prep
%autosetup -p1
autoreconf -fi
%configure

%build
%make_build

%install
%make_install

%files
%defattr(-, root, root, -)
%attr(4755, -, -) %{_bindir}/firejail
%{_bindir}/firecfg
%{_bindir}/firemon
%{_libdir}/firejail

%{_datarootdir}/bash-completion/completions/firejail
%{_datarootdir}/bash-completion/completions/firecfg
%{_datarootdir}/bash-completion/completions/firemon
%{_docdir}/firejail
%{_mandir}/*/*
%config(noreplace) %{_sysconfdir}/firejail

%{_datadir}/gtksourceview-5/language-specs/firejail-profile.lang

%{_datadir}/vim/vimfiles/ftdetect/firejail.vim
%{_datadir}/vim/vimfiles/syntax/firejail.vim   

%{_bindir}/jailcheck
%{_datadir}/zsh/site-functions/_firejail
