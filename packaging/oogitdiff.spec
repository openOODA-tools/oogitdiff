Name:           oogitdiff
Version:        0.2.0
Release:        1%{?dist}
Summary:        Fast working tree vs commit object differ without requiring ambient git porcelain.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oogitdiff
Source0:        oogitdiff-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oogitdiff is a sovereign, capability-bounded GIT TREE DIFF written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oogitdiff
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oogitdiff-uninstall

%files
/usr/bin/oogitdiff
/usr/bin/oogitdiff-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
