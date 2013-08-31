'''
Copyright 2009, 2010 Brian S. Eastwood.

This file is part of Synctity.

Synctity is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Synctity is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Synctity.  If not, see <http://www.gnu.org/licenses/>.

Created on Nov 18, 2009
'''
from collections import deque
import os
import shelve
import sys
from PyQt4 import QtCore, QtGui

import command
import rsync
import about_ui
import synctity_ui

APPLICATION_NAME="Synctity"
APPLICATION_VERSION="1.03"
APPLICATION_WEBSITE="https://github.com/beastwood/synctity"
DEFAULT_CONFIG=os.path.expanduser("~/synctity.txt")

class ProfileModel(QtCore.QAbstractListModel):
    '''
    A model that presents a set of profiles as a list.
    '''
    def __init__(self, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self.profiles = list()
        
    def setProfiles(self, profiles):
        self.profiles = profiles
        self.reset()
        
    def getProfiles(self):
        return self.profiles
        
    def isValid(self, index):
        '''
        Determines if an index references a profile in this model.  Index
        is a single number, not a QModelIndex.
        '''
        return index >= 0 and index < len(self.profiles)
    
    def data(self, index, role=QtCore.Qt.DisplayRole):
        '''
        Return the representation of data in this model at a given index.
        Index is a QModelIndex.  If the role is Qt.DisplayRole and the index
        is valid, returns the name of the profile.
        '''
        if (role == QtCore.Qt.DisplayRole and
            index.isValid() and 
            self.isValid(index.row())):
            data = self.profiles[index.row()].getName()
        else:
            data = QtCore.QVariant()
        return data
    
    def rowCount(self, parent=QtCore.QModelIndex()):
        '''
        Gets the number of profiles stored in this model
        '''
        return len(self.profiles)
    
    def append(self, profile):
        '''
        Add a profile to this model, and return the new item's QModelIndex
        '''
        # find the index of inserting and notify any views
        newIdx = len(self.profiles)
        self.beginInsertRows(QtCore.QModelIndex(), newIdx, newIdx)
        # add the profile to the model
        self.profiles.append(profile)
        # alert any views, and return a QModelIndex of the new element
        self.endInsertRows()
        return self.index(newIdx, 0)
        
    def remove(self, index):
        '''
        Remove the profile at the given index.  Index is a single number,
        not a QModelIndex.
        '''
        if self.isValid(index):
            # notify any views and remove the profile
            self.beginRemoveRows(QtCore.QModelIndex(), index, index)
            self.profiles.remove(self.profiles[index])
            self.endRemoveRows()
    
    def get(self, index):
        '''
        Get a reference to the profile at the given index.  Index is a single
        number, not a QModelIndex.
        '''
        if self.isValid(index):
            return self.profiles[index]
        
    def update(self, profile):
        '''
        Notify any views that the given profile has been modified.
        '''
        idx = self.profiles.index(profile)
        if self.isValid(idx):
            # build the QModelIndex, and emit the changed signal
            modelIdx = self.index(idx, 0)
            self.emit(QtCore.SIGNAL("dataChanged(QModelIndex, QModelIndex)"), 
                      modelIdx, modelIdx)        
        
class CommandModel(QtCore.QAbstractListModel):
    '''
    A list model for a set of rsync commands attached to a profile.
    '''
    def __init__(self, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self.profile = None
        
    def setProfile(self, profile):
        '''
        Set the profile that contains the commands this model represents
        '''
        self.profile = profile
        # notify any views that this model has completely changed
        self.reset()
        
    def isValid(self, index):
        '''
        Determines whether a single-value index is valid for this model
        '''
        return (self.profile != None and
                index >= 0 and 
                index < len(self.profile.getCommands()))

    def rowCount(self, parent=QtCore.QModelIndex()):
        '''
        Gets the number of commands in this model
        '''
        if self.profile == None:
            count = 0
        else:
            count = len(self.profile.getCommands())
        return count
    
    def data(self, index, role=QtCore.Qt.DisplayRole):
        '''
        Gets the model item at a given QModelIndex index.  If the index is
        valid for this model and role is Qt.DisplayRole, return the description
        of the command at the index.
        '''
        if (role == QtCore.Qt.DisplayRole and
            index.isValid() and
            self.isValid(index.row())):
            data = self.profile.getCommands()[index.row()].getDescription()
        else:
            data = QtCore.QVariant()
        return data
    
    def append(self, command):
        '''
        Add a command to this model.  Returns the QModelIndex where the
        addition was made.
        '''
        # get the index for the new addition and notify any views
        newIdx = len(self.profile.getCommands())
        self.beginInsertRows(QtCore.QModelIndex(), newIdx, newIdx)
        # add the command to the underlying data
        self.profile.add(command)
        # notify views that the addition is complete
        self.endInsertRows()
        return self.index(newIdx, 0)
        
    def remove(self, index):
        '''
        Removes the command at the given single-value index from this model.
        '''
        if self.isValid(index):
            # if the index is valid, notify views and remove data
            self.beginRemoveRows(QtCore.QModelIndex(), index, index)
            self.profile.remove(index)
            self.endRemoveRows()
            
    def edit(self, index):
        '''
        Edit the command at the given single-value index.
        '''
        if self.isValid(index):
            # build a command form for editing the command
            selected = self.profile.get(index)
            dialog = command.CommandForm()
            dialog.setCommand(selected)
            
            # launch as a modal dialog
            dialog.exec_()
            
            # notify any views that we have changed
            self.emit(QtCore.SIGNAL("dataChanged(QModelIndex, QModelIndex)"), 
                      self.index(index, 0), self.index(index, 0))
            
class ProfileRunner:
    '''
    ProfileRunner is responsible for running commands as separate processes 
    and sending the output to a text window.  Commands are queued and started
    as prior commands finish.
    '''
    def __init__(self, textEdit):
        '''
        Initialize a ProfileRunner.  textEdit ought to be a QTextEdit.
        '''
        # output is sent to a text box
        self.textConsole = textEdit;
                
        # commands are held in a queue until ready to be run.
        self.commands = deque()
        
        # commands are run through a QProcess
        self.process = QtCore.QProcess()
        # connect the QProcess signals to our slots
        QtGui.qApp.connect(self.process, QtCore.SIGNAL("started()"), self.onStarted)
        QtGui.qApp.connect(self.process, QtCore.SIGNAL("readyReadStandardOutput()"), self.onStdout)
        QtGui.qApp.connect(self.process, QtCore.SIGNAL("readyReadStandardError()"), self.onStderr)
        QtGui.qApp.connect(self.process, QtCore.SIGNAL("finished(int)"), self.onFinished)
    
    def onStarted(self):
        '''
        Do nothing when the process launches.  Could print out the pid.
        '''
        pass
    
    def onStdout(self):
        '''
        When the process generates standard output, print it to the text box.
        '''
        self.textConsole.insertPlainText(str(self.process.readAllStandardOutput()))
        # auto scroll
        scroll = self.textConsole.verticalScrollBar()
        scroll.setValue(scroll.maximum())
        
    def onStderr(self):
        '''
        When the process generates standard error, print it to the text box in red.
        '''
        color = self.textConsole.textColor()
        self.textConsole.setTextColor(QtGui.QColor.fromHsvF(0.0, 0.9, 0.7))
        self.textConsole.insertPlainText(str(self.process.readAllStandardError()))
        self.textConsole.setTextColor(color)
        # auto scroll
        scroll = self.textConsole.verticalScrollBar()
        scroll.setValue(scroll.maximum())
        
    def onFinished(self, exitCode):
        '''
        Report the result of a finished command, and launch the next one.
        '''
        if exitCode != 0:
            message = "There may have been an error with the transfer."
        else:
            message = ""
        self.textConsole.append("Finished (%d)\n%s" % (exitCode, message))

        # launch the next command
        self.runNext()
        
    def runProfile(self, profile, reverse=False):
        '''
        Queue up all commands in a profile and start running them.
        '''
        if not reverse:
            # forward direction runs any pre-sync and post-sync commands
            if profile.getPreSync() != '':
                self.commands.append(profile.getPreSync())
            for command in profile:
                self.commands.append(command.forward())
            if profile.getPostSync() != '':
                self.commands.append(profile.getPostSync())
        else:
            for command in profile:
                self.commands.append(command.reverse())
        
        # launch the next command
        self.runNext()
        
    def runNext(self):
        '''
        Run the next command in the queue.
        '''
        # check if there are commands to run and that there is not a process
        # currently running.
        if (len(self.commands) > 0 and
            self.process.state() == QtCore.QProcess.NotRunning):
            # remove a command from the queue and start it
            command = self.commands.popleft()
            self.textConsole.append(command + '\n')
            self.process.start(command)
        
        
class SynctityWindow(QtGui.QMainWindow):
    '''
    The main Synctity window, which enables editing and running profiles of
    rsync commands.
    '''
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        # set up user interface
        self.ui = synctity_ui.Ui_Synctity()
        self.ui.setupUi(self)
        self.setWindowTitle("{0} {1}".format(APPLICATION_NAME, APPLICATION_VERSION))
                
        # set up profile and command views
        self.profileModel = ProfileModel(self)
        self.ui.listProfiles.setModel(self.profileModel)
        self.commandModel = CommandModel(self)
        self.ui.listCommands.setModel(self.commandModel)
        
        # initially disable profile editing
        self.ui.groupProfile.setEnabled(False)
        
        # setup process for running profiles
        self.runner = ProfileRunner(self.ui.textConsole)
        
        # filename used to store profiles
        if os.path.exists(DEFAULT_CONFIG):
            self.filename = DEFAULT_CONFIG
            self.loadProfiles()
        else:
            self.filename = None
            
        # add About menu item
        # Note that on Mac OS, this menu item gets placed in the application menu, not the help menu
        about = QtGui.QAction("About", self)
        self.ui.menuHelp.addAction(about)
        self.connect(about, QtCore.SIGNAL("triggered()"), self.onAbout)
        
        # add Help menu item
        help = QtGui.QAction("Manual", self)
        self.ui.menuHelp.addAction(help)
        self.connect(help, QtCore.SIGNAL("triggered()"), self.onHelp)
        
    def currentProfile(self):
        '''
        Returns a reference to the currently-selected profile
        '''
        profIdx = self.ui.listProfiles.currentIndex()
        return self.profileModel.get(profIdx.row())
                
    def onAddProfile(self):
        '''
        Adds a new default profile to the list of profiles.  The new
        profile is selected.
        '''
        # add a profile to the model
        index = self.profileModel.append(rsync.Profile())
        # select profile and set focus to edit the profile name
        self.ui.listProfiles.setCurrentIndex(index)
        self.onSelectProfile(index)
        self.ui.textProfileName.setFocus()
        self.ui.textProfileName.selectAll()
        
    def onRemoveProfile(self):
        '''
        Removes the currently selected profile from the list of profiles. 
        '''
        # remove the selected profile
        profIdx = self.ui.listProfiles.currentIndex()
        self.profileModel.remove(profIdx.row())
        # update profile editing for next selected profile
        newIdx = self.ui.listProfiles.currentIndex()
        self.onSelectProfile(newIdx)
            
    def onSelectProfile(self, index):
        '''
        Responds to a profile being selected from the list.  If a valid
        profile is selected, updates the profile edit area to hold that
        profile's data.  If no valid profile is selected, disables the
        profile edit area.
        '''
        profile = self.profileModel.get(index.row())
        if profile != None:
            self.ui.groupProfile.setEnabled(True)
            self.ui.textProfileName.setText(profile.getName())
            self.ui.textPreSync.setText(profile.getPreSync())
            self.ui.textPostSync.setText(profile.getPostSync())
            self.commandModel.setProfile(profile)
        else:
            self.ui.groupProfile.setEnabled(False)
        
    def onProfileName(self):
        '''
        Renames the currently selected profile according to the text in the
        profile name field.
        '''
        # get the currently selected profile
        profile = self.currentProfile()
        if profile != None:
            # update the profile name
            profile.setName(self.ui.textProfileName.text())
            # notify the model that underlying data has changed
            self.profileModel.update(profile)
            
    def onTextSync(self):
        '''
        Updates the currently selected profile's pre and post sync commands.
        '''
        # get the currently selected profile
        profile = self.currentProfile()
        if profile != None:
            # update the command
            profile.setPreSync(self.ui.textPreSync.text())
            profile.setPostSync(self.ui.textPostSync.text())
            # notify the model that underlying data has changed
            self.profileModel.update(profile)
    
    def onPreSync(self):
        qfile = QtGui.QFileDialog.getOpenFileName(self, "Select pre-sync command...")
        if qfile != None and qfile != '':
            self.ui.textPreSync.setText(qfile)
            self.onTextSync()
    
    def onPostSync(self):
        qfile = QtGui.QFileDialog.getOpenFileName(self, "Select post-sync command...")
        if qfile != None and qfile != '':
            self.ui.textPostSync.setText(qfile)
            self.onTextSync()
            
    def onAddCommand(self):
        '''
        Adds a new rsync command to the profile currently being edited.
        '''
        # add a command to the command model
        index = self.commandModel.append(rsync.Command())
        # edit the command
        self.commandModel.edit(index.row())
        
    def onRemoveCommand(self):
        '''
        Removes the currently selected command from the profile currently being
        edited.
        '''
        index = self.ui.listCommands.currentIndex()
        self.commandModel.remove(index.row())
        
    def onEditCommand(self, index):
        '''
        Edits the command at the given QModelIndex in the command model.
        '''
        self.commandModel.edit(index.row())
        
    def onForward(self):
        '''
        Runs the currently selected rsync profile in the forward direction,
        source -> destination.
        '''
        profile = self.currentProfile()
        if profile != None:
            self.runner.runProfile(profile, False)
    
    def onReverse(self):
        '''
        Runs the currently selected rsync profile in the reverse direction,
        destination -> source.
        '''
        profile = self.currentProfile()
        if profile != None:
            self.runner.runProfile(profile, True)
                        
    def loadProfiles(self):
        '''
        Loads a set of profiles from a file.
        '''
        try:
            # open the shelve file, and grab an object called profiles
            store = shelve.open(self.filename)
            if "profiles" in store:
                self.profileModel.setProfiles(store["profiles"])
            else:
                QtGui.QMessageBox.warning(self, "Cannot read file", 
                      "Sorry, this file is not a valid Synctus file:\n" + self.filename)
            store.close()
            self.ui.statusbar.showMessage("Loaded profiles from " + self.filename)
        except:
            # opening shelve databases can easily throw an error if the file
            # is invalid
            QtGui.QMessageBox.warning(self, "Cannot read file",
                      "Sorry, this file is not a valid Synctus file:\n" + self.filename)
    
    def writeProfiles(self):
        '''
        Saves the set of profiles to a file.
        '''
        try:
            # open the shelve file, and store the profiles
            store = shelve.open(self.filename)
            store["profiles"] = self.profileModel.getProfiles()
            store.close()
            self.ui.statusbar.showMessage("Wrote profiles to " + self.filename)
        except:
            # exceptions are common when dealing with file IO
            QtGui.QMessageBox.warning(self, "Cannot write file",
                      "Sorry, this file is not a valid Synctus file:\n" + self.filename)
            
    def onLoad(self):
        '''
        Prompts the user for a file to load Synctus profiles from.
        '''
        qfile = QtGui.QFileDialog.getOpenFileName(self, "Load from...", DEFAULT_CONFIG)
        if qfile != None and qfile != '':
            self.filename = str(qfile)
            self.loadProfiles()

            # select the first profile that was loaded
            if self.profileModel.rowCount() > 0:
                index = self.profileModel.index(0, 0)
            else:
                index = QtCore.QModelIndex()
            self.ui.listProfiles.setCurrentIndex(index)
            self.onSelectProfile(index)
        
    def onSave(self):
        '''
        Saves the Synctus profiles to a file.
        '''
        if self.filename == None:
            self.onSaveAs()
        else:
            self.writeProfiles()
            
    def onSaveAs(self):
        '''
        Prompts the user for a file to save Synctus profiles in.
        '''
        qfile = QtGui.QFileDialog.getSaveFileName(self, "Save to...", DEFAULT_CONFIG)
        if qfile != None and qfile != '':
            self.filename = str(qfile)
            self.writeProfiles()
            
    def onAbout(self):
        '''
        Displays information about the application.
        '''
        # build the help dialog
        dialog = QtGui.QDialog(self)
        ui = about_ui.Ui_Dialog()
        ui.setupUi(dialog)
        
        # set dynamic content
        today = QtCore.QDate.currentDate()
        ui.labelApplication.setText(APPLICATION_NAME)
        ui.labelCopyright.setText("&copy; 2010 - {0}".format(today.year()))
        ui.labelVersion.setText("version {0}".format(APPLICATION_VERSION))
        ui.labelWebsite.setText("<a href={0}>{0}</a>".format(APPLICATION_WEBSITE))
        ui.labelWebsite.setOpenExternalLinks(True)
        ui.labelIcon.setPixmap(QtGui.QPixmap(":/synctity"))
        
        dialog.setWindowTitle("About {0}".format(APPLICATION_NAME))
        dialog.show()
        
    def onHelp(self):
        '''
        Opens the help manual.
        '''
        # find the manual index page
        basepath = os.getenv("RESOURCEPATH")
        if basepath is not None:
            # in a Mac app bundle look in the Resources directory
            helpfile = os.path.join(basepath, "html/index.html")
        else:
            # otherwise use the current file directory
            basepath = os.path.split(os.path.abspath(__file__))[0]        
            helpfile = os.path.join(basepath, "doc/html/index.html")
        
        # check whether the index file exists
        if os.path.exists(helpfile):
            helpfile = "file://" + helpfile
            print "Opening", helpfile
            QtGui.QDesktopServices.openUrl(QtCore.QUrl(helpfile))
        else:
            QtGui.QMessageBox.warning(self, "Could not find manual", "Could not find the help manual in\n{0}".format(helpfile))

    def onQuit(self):
        QtGui.qApp.exit(0)
        
def runSynctity():
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName(APPLICATION_NAME)
    app.setApplicationVersion(APPLICATION_VERSION)
    
    myapp = SynctityWindow()
    myapp.show()
    myapp.raise_()
    myapp.setFocus()
    sys.exit(app.exec_())
        
if __name__ == "__main__":
    runSynctity()