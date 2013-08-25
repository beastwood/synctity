.. index:: backups
.. index:: snapshots

Incremental Backups
===================

With a little configuration, Synctity can be set up to peform incremental backups of a file system.  Incremental backups initally create a complete backup of a file system, and subsequently backup only the modified files.  This results in an enormous reduction in the time it takes to run a backup.
	
Snapshots provide a view of a complete file system at a backup point.  Combined with incremental backups, one can store a complete history of many backups in a relatively small space.  For example, one of my backup systems is currently storing 42 snapshots of an 18.4 GB file system, but the whole collection of snapshots occupies only 23 GB of disk space.

.. note::
	
	One caveat for setting up incremental backup snapshots is that the destination file system needs to support hard links.  Common file systems with hard link support include ``ext2``, ``ext3``, ``ext4``, ``ReiserFS``, ``XFS``, ``JFS``, among others.

Configuration
-------------

Creating incremental backup snapshots requires configuring the following components for each command in the backup profile.

#. 	From the :guilabel:`Paths` tab of the command setup, each backup source directory should point to a common destination directory on the backup file system, e.g. myserver:/media/backup/myclient/username-incoming.

	Using this naming convention on the server means you can easily backup multiple machines and users to the same remote host.
	
	.. image:: images/backuppaths.png
		:width: 95%
		:target: _images/backuppaths.png

#.	From the :guilabel:`Common` tab, enable the ``-a`` (archive) option to preserve file permissions and ownership.  If backing up to a remote machine, use the ``-z`` (compress) option to speed the transfer over the network.  Optionally enable ``-P`` to see the partial progress and ``-h`` for human-readable output.

#. 	From the :guilabel:`Advanced` tab, each command should specify a ``link-dest`` directory containing the most recent backup as a symbolic link, e.g. ../username-current.

	.. image:: images/backupadvanced.png
		:width: 95%
		:target: _images/backupadvanced.png

#.	After backup, the incoming backup directory should be moved to a time-stamped directory.

#.	The old symbolic link current directory should be removed and a new current directory should be created, linking to the new backup directory.

Post-Sync Script
----------------

The following script performs the final two tasks remotely using SSH, and should be configured as the :guilabel:`Post-Sync` task for the backup profile::

	#!/bin/bash

	# date stamp
	date=$(date "+%Y%m%d-%H%M%S")
	
	# root backup directory
	backup=/media/backup/myclient
	
	# move directories around on remote server
	ssh username@myserver \
	"mv $backup/username-incoming $backup/username-$date \
	&& rm -f $backup/username-current \
	&& ln -s $backup/username-$date $backup/username-current"

If you want to backup a database, you should create a dump of your database before running the backup commands.  For example, the following script is one I use as a :guilabel:`Pre-Sync` task for my backup profile::

	#!/bin/bash
	mysqldump -umysqluser -pmysqlpassword database > /Users/username/database.sql

You can see how much space is being occupied by your backup snapshots on the backup file system with the following command::

	$ du -sch username-*
	3.9G	username-20100105-132515
	2.5G	username-20100118-170833
	2.0G	username-20100127-165608
	...
	146M	username-20100730-103810
	16M	username-20100805-113006
	31M	username-20100806-133213
	0	username-current
	23G	total

.. note::

	Any of the backup snapshots created in this manner can be deleted without affecting other snapshots.  This can be useful if creating one snapshot every day---old snapshots can be culled to one per week or month.

.. seealso::

	The instructions provided here for creating incremental backup snapshots combine information from from several web resources on creating incremental backup snapshots.  Michael Jakl has a good `blog post <http://blog.interlinked.org/tutorials/rsync_time_machine.html>`_ and `addendum <http://blog.interlinked.org/tutorials/rsync_addendum.yaml.html>`_ detailing his methods for doing this.

Synctity vs. Time Machine
-------------------------

Mac OS X users have a backup system built-in to the operating syste, called Time Machine.  Time Machine creates incremental backup snapshots much like the ones described here.  While Time Machine integrates well with the Mac OS, and performs backups in the background transparently, there are a few reasons one might prefer Synctity over Time Machine.

Because you need Mac OS X to get Time Machine, you can only backup a Mac.  Time Machine works only with Mac's HFS Plus file system with journaling enabled.  This means remote backups need to be performed to another Mac, or to Mac's proprietary Time Capsule device.  Finally, you need a Mac to read and restore the backups.  

I have personal experience with an external USB drive that stopped being recognized by the Mac that was using it for Time Machine backups.  Although I could mount the file system on a Linux machine, I could not recover any of the backup files because the hard links Time Machine used were not recognized---the disk was a jumble of directories and files named by inode, not by the original file names.

While there may be work arounds for some of these issues, at its core Time Machine is a Mac-only solution.  Synctity, however, is a cross-platform solution for any Unix-based machine.  Although I have never tried, it may even work on Windows machines running Cygwin.

In short, if you only use Macs, use Time Machine; it's a nice program.  If you use other operating systems, or more than one operating system, Synctity might be a good solution.



