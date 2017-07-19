Name:        zxfer
Version:     1.1.6
Release:     2%{?dist}
License:     see COPYING
Group:       External packages
URL:         https://github.com/allanjude/zxfer/
# master version
#Source:      https://github.com/allanjude/zxfer/archive/master.zip
# release version
#https://github.com/allanjude/zxfer/archive/%{version}.gz
Source:      %{name}-%{version}.tar.gz
BuildRoot:   %{_tmppath}/%{pkg}-%{version}
Requires:  zfs /bin/sh /usr/bin/cat /usr/bin/rsync /usr/bin/gawk
Summary:  zxfer: transfer ZFS filesystems, snapshots, properties, files and directories
BuildArch:	noarch
%description

A continuation of development on zxfer, a popular script for managing ZFS
snapshot replication

The Original author seems to have abandoned the project, there have been no
updates since May 2011 and the script fails to work correctly in FreeBSD
versions after 8.2 and 9.0 due to new ZFS properties.

For now, most of the documentation will reside at the original page, until
someone reorganizes it.

Original Project Home: http://code.google.com/p/zxfer/
...
transfer ZFS filesystems, snapshots, properties, files and directories

Zxfer is a fork of Constantin Gonzalez's zfs-replicate, with many additional
features (80%+ of code is new). In a nutshell, the aim of zxfer is to make
backups, restores and transfers on ZFS filesystems able to be done with a
single command, while having similar end-to-end assurance of data integrity as
the ZFS filesystem itself.

...

%prep
# master version
#%setup -q -n %{name}-master
# release version
%setup -q -n %{name}-%{version}

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p \
${RPM_BUILD_ROOT}%{_bindir} \
${RPM_BUILD_ROOT}%{_mandir}/man8 \
${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version} 

install -m0644 zxfer.8 \
   ${RPM_BUILD_ROOT}%{_mandir}/man8 
install -m0644 CHANGELOG.txt COPYING README.md README.txt \
   ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version}
install -m0755 zxfer ${RPM_BUILD_ROOT}%{_bindir}

%clean
rm -rf %{buildroot}


%files
%{_bindir}/zxfer

%doc
%{_docdir}/%{name}-%{version}/CHANGELOG.txt
%{_docdir}/%{name}-%{version}/COPYING
%{_docdir}/%{name}-%{version}/README.md
%{_docdir}/%{name}-%{version}/README.txt
%{_mandir}/man8/zxfer.8.gz

%changelog
* Wed Jul 19 2017 Tru Huynh <tru@pasteur.fr> - 1.1.6-2
- add Requires for: cat rsync gawk
* Wed Jul 19 2017 Tru Huynh <tru@pasteur.fr> - 1.1.6-1
- initial version
