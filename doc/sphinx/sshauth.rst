.. index:: ssh authorization
.. index:: remote file systems

SSH Authorization
=================

Synctity is able to securely use remote file systems in synchronization tasks through secure shell (:command:`ssh`).  Synctity does not, however, save or prompt for passwords to access remote file systems.  Instead, it relies on an existing public/private key pair.

SSH Server/Client
-----------------

SSH establishes a secure and encrypted communication link between two machines: the ssh server is the remote machine being accessed; the ssh client is the local machine from which a connection is established.  An ssh public/priviate key pair establishes a trusted relationship between user accounts on these two machines.

In Synctity, the local machine---where Synctity is running---acts as an SSH client, and therefore needs an ssh client installed.  The remote machine acts as the ssh server, and therefore needs to have an SSH sever running.  On both Mac and Linux operating systems, OpenSSH provides a commonly-used SSH implementation that can be installed through MacPorts or the Linux package manager.

Public/Private Keys
-------------------

To set up an SSH public/private key pair on your system, first login to the SSH client (where Synctity will be running).  From the command terminal::

	$ cd ~/.ssh
	$ ssh-keygen
	Generating public/private rsa key pair.
	Enter file in which to save the key (~/.ssh/id_rsa): 
	Enter passphrase (empty for no passphrase): 
	Enter same passphrase again: 
	Your identification has been saved in ~/.ssh/id_rsa.
	Your public key has been saved in ~/.ssh/id_rsa.
	The key fingerprint is:
	...

	$ ls
	id_rsa		id_rsa.pub

If the ``~/.ssh`` directory does not exist on your machine, create it.  You can accept all defaults when running the :command:`ssh-keygen` command.  Whether you specify a passphrase is up to you---the OpenSSH folks recommend it.  For some added security, use ``ssh-keygen -b 4096``.

The :command:`ssh-keygen` command creates a private (``id_rsa``) and public (``id_rsa.pub``) pair of files.  Copy the contents of the public file into ``~/.ssh/authorized_keys`` on the remote SSH server, where ``~`` refers to the home directory of the user account you will be using on the remote machine::

	$ scp id_rsa.pub username@myserver:~/.ssh/myclient.pub
	username@myserver's password:
	$ ssh username@myserver
	username@myserver's password:
	$ cd .ssh
	$ cat myclient.pub >> authorized_keys
	$ rm myclient.pub

You will be prompted to enter your remote user's password for the ``scp`` and ``ssh`` commands above.  But, after you have set up the public/private key pair, you will be prompted for the local ``id_rsa`` passphrase instead of your remote user's password.  If you did not specify a passphrase, you will get no prompt at all::

	$ ssh username@myserver
	Last login: Mon Aug  9 10:06:36 2010 from myclient
	[username@myserver ~]$

Now you can use the remote file system that your user has access to in Synctity commands.  If you specified a passphrase for your ``id_rsa`` file, you will receive a prompt for the passphrase when you run each command that uses the remote file system.

.. note::

	Passphrase entry has been tested and works on Mac OS X, but not confirmed for Linux SSH clients.)