zxfer
=====

A continuation of development on zxfer, a popular script for managing ZFS snapshot replication

The Original author seems to have abandonded the project, there have been no updates since May 2011 and 
the script fails to work correctly in FreeBSD versions after 8.2 and 9.0 due to new ZFS properties.

[Original Project Home](http://code.google.com/p/zxfer/)


For now, most of the documentation will reside at the original page, until someone reorganizes it.



Changes
=======

+ Ignore new read-only properties added in FreeBSD 9.1: 'written' and 'refcompressratio'
+ Ignore new read-only properties added in FreeBSD 9.2/8.4: 'logicalused' and 'logicalreferenced'


