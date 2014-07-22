zxfer
=====

A continuation of development on zxfer, a popular script for managing ZFS snapshot replication

The Original author seems to have abandonded the project, there have been no updates since May 2011 and 
the script fails to work correctly in FreeBSD versions after 8.2 and 9.0 due to new ZFS properties.

[Original Project Home](http://code.google.com/p/zxfer/)


For now, most of the documentation will reside at the original page, until someone reorganizes it.



Changes
=======

+ Implement new -D parameter, allows you to put a progress indicator app between the zfs send and zfs receive. 
  provides macros %%size%% and %%title%%. Example usage: -D 'bar -s %%size%% -bl 1m -bs 256m'
+ Ignore new read-only properties added in FreeBSD 9.1: 'written' and 'refcompressratio'
+ Ignore new read-only properties added in FreeBSD 9.2/8.4: 'logicalused' and 'logicalreferenced'
+ "Unsupported Properties" support, do not copy properties that are unsupported by the destination pool. Allows replication from 11-CURRENT to 9.2 etc, by automatically ignoring new properties such as: volmode,filesystem_limit,snapshot_limit,filesystem_count,snapshot_count,redundant_metadata
+ Fixed -o mountpoint=foo , it is no longer ignored as readonly if explicitly requested by the user
+ Implemented new -I parameter, ignore these properties and do not try to set them
