.. index:: profile configuration

Profiles
========

Profiles are collections of Commands.  Some file synchronization tasks are too complex to be specified by a single command.  For example, there may be several files in different locations that need to be backed up to a single location.  Or, there may be a website that needs to be distributed to multiple machines.  Profiles provide a way to associate several commands as a single unit, referred to by name.

Profiles are edited from the main :guilabel:`Synctity` window.

Managing
--------

Profiles are managed in the :guilabel:`Profiles` section of the main window.  Profiles are listed by name in the list box.  The :guilabel:`+` and :guilabel:`-` buttons add and remove profiles.  Selecting a profile displays its properties in the :guilabel:`Edit Profile` section of the main window.  When a new profile is created, it is automatically selected.

Editing
-------

Profiles are edited in the :guilabel:`Edit Profile` section of the main window.  This section has the following components:

Name
	The name of the profile.  This is the name that appears in the :guilabel:`Profiles` list box.  Use a descriptive name.
	
Commands
	The list of commands associated with the profile.  Double-click on any command to open the :guilabel:`rsync command` dialog for the command.
	
\+
	Add a new command to the profile.  The the :guilabel:`rsync command` dialog will automatically be opened.
	
\-
	Remove the currently selected command from the profile.
	
Pre-Sync
	A command to run before executing all of the commands in the profile.
	
Post-Sync
	A command to run after executing all of the commands in the profile.
	
.. seealso::

	:guilabel:`Pre-Sync` and :guilabel:`Post-Sync` scripts are discussed in :ref:`profile_scripts`.

Running
-------

When a profile is run, all of the commands in the profile are executed in order.  The :guilabel:`Run profile` section of the main window provides buttons for running a profile forward and in reverse.

Forward
	All commands are run as configured, where source files are copied to destination files.  The pre-sync and post-sync tasks are executed, if specified.

Reverse
	All commands are run in reverse, where destination files are copied to source files.  The pre-sync and post-sync tasks are not executed.

As an example where the forward and reverse profile execution might be used, consider synchronizing a personal directory on two computers, e.g. a desktop at work and a desktop at home.  The forward execution would copy files from the computer at work to the computer at home, when someone wants to start working at home.  The reverse execution would copy the modified files back to the work computer after the user has finished working from home.

.. _profile_scripts:

Scripts
-------

The :guilabel:`Pre-` and :guilabel:`Post-Sync` text fields provide a means to specify a command that should be executed before and after all synchronization commands are executed.  These can be any valid terminal command, including shell scripts that perform any arbitrary tasks.

Some examples of Pre-Sync tasks include backing up a database to a dump file, mounting a local file system with write permissions (for a backup), or mounting a remote file system through sshfs.  Examples of Post-Sync tasks include unmounting file systems and renaming files created during the synchronization.  The section on :doc:`backups` provides a complete example of performing incremental backups to a remote file system.

Pre-sync and post-sync tasks are not run in reverse because it is presumed a single script would often not do the "right" thing in both cases.  For example, a common pre-sync script might backup a database to a dump file.  The same script would probably not restore the database from the dump file as well.  If one wanted to restore a backup, it would probably be wise to create a separate profile for this task.

Saving and Loading
------------------

It would not do much good to enable users to configure collections of profiles, each of which collects multiple commands, if there was no way to save these configurations.  The :guilabel:`Synctity` menu provides this capability.

A profile file stores multiple profile configurations.  All profiles currently displayed in the :guilabel:`Profiles` list are saved to a single file.

Load
	Load a collection of profiles from a file.  Any unsaved changes to the current profile set will be lost.

Save
	Save the current set of profiles to the current profile file.  The file name will be displayed in the status bar at the bottom of the main window.  The default profile file name is ``synctity.txt``.

Save as...
	Specify the file name to save the current profile set to.

The profile sets are saved using the Python ``shelve`` module.  The choice of the default ``.txt`` extension is admittedly a poor one, as these files are not human-readable.  With no standard extension to use for ``shelve`` files, however, there was no clear alternative.