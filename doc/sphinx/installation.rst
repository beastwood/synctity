.. index:: installation

Installation
============

Synctity runs on Unix-based systems such as Mac OS X and Linux. On Mac OS X, Synctity can be installed with a stand-alone application bundle or from source. On Linux, Synctity can only be installed from source.

Mac OS X Installer
------------------

Download the latest Mac installer (``synctity-01.03.dmg``) from `GitHub <https://github.com/beastwood/synctity/tree/master/install>`_. Open the disk image, and drag the Synctity icon into your :guilabel:`Applications` folder. Launch the application by double-clicking on the icon.

.. note::

	The Mac OS X application bundle does not contain the source code for Synctity. The source code is hosted on `GitHub <https://github.com/beastwood/synctity>`_.

Installing from Source (Linux or Mac)
-------------------------------------

The following table enumerates software required prior to installation from source.  :command:`rsync` is usually already provided on Unix-based systems such as Linux and Mac OS X.  The program will likely work with any reasonably recent version of the software listed, but the version numbers used during development and the most recently tested versions are provided as a reference.

========	===================		==============		=======
Software	Development Version		Latest Version		Website
========	===================		==============		=======
rsync		2.6.9					2.6.9				
Python		2.6.5 					2.7.5				`Python <http://www.python.org/>`_
Qt4     	4.6.3 					4.8.5				`Nokia <http://qt.nokia.com/>`_
SIP 		4.10.4					4.15.0				`Riverbank SIP <http://www.riverbankcomputing.co.uk/software/sip/intro>`_
PyQt4		4.7.4 					4.10.3				`Riverbank PyQt <http://www.riverbankcomputing.co.uk/software/pyqt/intro>`_
========	===================		==============		=======


Mac OS X Prerequisites
^^^^^^^^^^^^^^^^^^^^^^

The easy way to install all the prerequisites is using MacPorts.  MacPorts, in turn, requires Apple's Xcode Developer Tools that come with Mac OS X. The MacPorts website has good instructions on how to install Xcode for different versions of Mac OS X. `Install MacPorts <http://www.macports.org/install.php>`_, and then use the following command to install the prerequisites::

	$ sudo port install python27 py27-pyqt4

.. note::

	This will take a fairly long time to complete because MacPorts downloads and compiles software from source.

Using MacPorts means the Python installation with PyQt4 resides within the MacPorts system (in ``/opt/local/...``), which does not house your computer's default Python installation (often ``/Library/Frameworks/Python.framework/...``).  If you perfer to manage software packages yourself, a good tutorial on installing PyQt4 on the Mac can be found from `Rob Oakes <http://www.oak-tree.us/blog/index.php/2009/05/12/pyqt-mac>`_.  In that case, you will need to update the script Syncity runs on startup, ``startsynctity`` to use your preferred Python executable.

Linux Prerequisites
^^^^^^^^^^^^^^^^^^^

Most Linux distributions will have PyQt4 bundled within their package managers, which handle dependencies quite well.

For example, on Ubuntu 10.10 or later, the following command should prepare your system::

	$ sudo aptitude install python python-qt4

On Fedora 13 or later, the following command should prepare your system::

	$ sudo yum install python PyQt4

Application
^^^^^^^^^^^

Synctity is hosted on `GitHub <https://github.com/beastwood/synctity/>`_.  Go there to download the latest versions of the source, and place it in a directory of your choice. You can safely remove the ``install`` directory; this just contains installers for specific versions of Synctity.

Launch the application by launching the ``synctity.py`` script from the source directory::

	$ python synctity.py

Alternatively, you can edit the ``startsynctity`` script to reference the directory where you have installed Synctity, and run that script.  You can configure an application launcher for your particular system to launch the ``startsynctity`` script; a suitable icon can be found within the source directory at ``doc/sphinx/images/synctity.png``.

.. note::

	On Mac OS X, launching Synctity puts two icons on the dock---Synctity's and Python's.  Activate the Python icon to bring the application to the foreground.  If anyone knows of an easy way to make OS X treat a Python application as a first-class application, drop me a line.
