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

%build
sed -i 's/^VERSION=.*/VERSION=%version/' %name

%install
mkdir -p %buildroot%_alterator_datadir/diagnostictools/%name

install -p -D -m755 sambadc-diag %buildroot%_bindir/%name
install -p -D -m644 sambadc-diag.backend %buildroot%_alterator_datadir/backends/%name.backend
install -p -D -m644 sambadc-diag.diagnostictool %buildroot%_alterator_datadir/diagnostictools/%name/%name.diagnostictool

%files
%_bindir/%name
%_alterator_datadir/backends/%name.backend
%_alterator_datadir/diagnostictools/%name/%name.diagnostictool

%changelog
* Sun Jul 28 2024 Sergey Savelev <savelevsa@basealt.ru> 0.0.1-alt1
- initial build


