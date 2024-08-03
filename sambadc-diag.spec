%define _unpackaged_files_terminate_build 1
Name: sambadc-diag
Version: 0.0.1
Release: alt1

Summary: Domain Controller Diagnostic Tool.
License: GPLv3
Group: Other
URL: https://github.com/Medovi/SambaDC-diag.git
BuildArch: noarch
Source0: %name-%version.tar

%description
Domain Controller Diagnostic Tool.

%prep
%setup

%install
mkdir -p %buildroot%_libexecdir/%name
mkdir -p %buildroot%_sysconfdir/alterator/backends
mkdir -p %buildroot%_datadir/alterator/objects/%name

install -v -p -m 755 -D sambadc-diag %buildroot%_libexecdir/%name
install -v -p -m 644 -D diagnostic-tool.backend %buildroot%_sysconfdir/alterator/backends
install -v -p -m 655 -D diagnostic-tool.diag %buildroot%_datadir/alterator/objects/%name

%files
%_libexecdir/%name/sambadc-diag
%_sysconfdir/alterator/backends/diagnostic-tool.backend
%_datadir/alterator/objects/%name/diagnostic-tool.diag
%changelog
* Sun Jul 28 2024 Sergey Savelev <savelevsa@basealt.ru> 0.0.1-alt1
- initial build

