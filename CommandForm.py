'''
Copyright 2009, 2010 Brian S. Eastwood.

This file is part of Synctus.

Synctus is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Synctus is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Synctus.  If not, see <http://www.gnu.org/licenses/>.

Created on Dec 2, 2009
'''
import math
from PyQt4 import QtCore, QtGui

from command_ui import Ui_CommandForm
import rsync

# A set of common options, short descriptions, and tool tips to include.
# The None entries here are later filled with QCheckButtons.
optionSet = {'a': ['archive mode', 'archive mode; same as -rlptgoD', None],
             'r': ['recursive', 'recurse into directories', None],
             'z': ['compress', 'compress file data during the transfer', None],
             'v': ['verbose', 'increase verbosity', None],
             'h': ['human readable', 'output numbers in a human-readable format', None],
             'n': ['dry run', 'show what would have been transferred', None],
             'u': ['update', 'skip files that are newer on the receiver', None],
             'l': ['links', 'copy symlinks as symlinks', None],
             'L': ['copy links', 'transform symlinks into referent file/dir', None],
             'H': ['hard links', 'preserve hard links', None],
             'p': ['permissions', 'preserve permissions', None],
             't': ['times', 'preserve times', None],
             'm': ['prune empty dirs', 'prune empty directory chains from the file list', None],
             'C': ['cvs exclude', 'auto-ignore files the same way CVS does', None],
             'P': ['partial + progress', 'show progress during transfer and keep partially transferred files', None],
             'E': ['extended attributes', 'copy extended attributes', None],
             'D': ['devices + specials', 'preserve device files and special files', None]}

class OptionModel(QtCore.QAbstractTableModel):
    '''
    A model for maintaining a list of options as name-value pairs.  This is a
    two column model. 
    '''
    def __init__(self, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self.options = list()
        
    def setOptions(self, options):
        '''
        Set the options in this model from an rsync.Option object.
        '''
        # clear the options list
        self.options = list()
        # add all options that are not in the common options set
        for key in sorted(options):
            if key not in optionSet:
                # each key might have multiple values
                for value in options.getOptions()[key]:
                    self.options.append((key, value))
        self.reset()
        
    def getOptions(self):
        '''
        Returns an rsync.Option object built from the options in this model.
        '''
        options = rsync.Option()
        for (key, value) in self.options:
            options.enable(str(key), str(value))
        return options
        
    def isValid(self, index):
        '''
        Checks if a QModelIndex is valid for this model.
        '''
        return (index.isValid() and 
                index.row() >= 0 and 
                index.row() < self.rowCount() and
                index.column() >= 0 and
                index.column() < 2)
        
    def rowCount(self, parent=QtCore.QModelIndex()):
        '''
        Returns the number of options in this model
        '''
        return len(self.options)
    
    def columnCount(self, parent=QtCore.QModelIndex()):
        '''
        Returns the number of columns in this model (2: name, value)
        '''
        return 2
    
    def data(self, index, role=QtCore.Qt.DisplayRole):
        '''
        Returns the option data in this model given a QModelIndex.
        '''
        if self.isValid(index) and role==QtCore.Qt.DisplayRole:
            return self.options[index.row()][index.column()]
        
    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        '''
        Output headers for this model.  Horizontal headers are "Name" and 
        "Value", Vertical headers are section numbers, which I guess are 
        rows...I couldn't find a good explanation of what these are anywhere.
        '''
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Vertical:
                return str(section)
            elif section == 0:
                return "Name"
            else:
                return "Value"
            
    def get(self, index):
        '''
        Returns the option at the given index as a (name, value) tuple.
        '''
        if self.isValid(self.index(index, 0)):
            return self.options[index]
                
    def append(self, name, value):
        '''
        Add an option to this model, appends to the end.
        '''
        # get the index for the new addition and notify any views
        newIdx = len(self.options)
        self.beginInsertRows(QtCore.QModelIndex(), newIdx, newIdx)
        # add the command to the underlying data
        self.options.append((name, value))
        # notify views that the addition is complete
        self.endInsertRows()
        self.emit(QtCore.SIGNAL("dataChanged(QModelIndex, QModelIndex)"), 
                  self.index(newIdx, 0), self.index(newIdx, 1))
    
    def remove(self, index):
        '''
        Removes the option at the given single-value index from this model.
        '''
        if self.isValid(self.index(index, 0)):
            # notify views and remove data
            self.beginRemoveRows(QtCore.QModelIndex(), index, index)
            self.options.remove(self.options[index])
            self.endRemoveRows()
            # notify any listeners
            self.emit(QtCore.SIGNAL("dataChanged(QModelIndex, QModelIndex)"), 
                      self.index(index, 0), self.index(index, 1))
            
    def edit(self, index, name, value):
        '''
        Updates the option at an index with a (name, value) pair.
        '''
        if self.isValid(self.index(index, 0)):
            self.options[index] = (name, value)
            # notify any views that the model data has changed
            self.emit(QtCore.SIGNAL("dataChanged(QModelIndex, QModelIndex)"), 
                      self.index(index, 0), self.index(index, 1))

class CommandForm(QtGui.QDialog):
    def __init__(self, parent=None):
        # set up the rsync command editing widget
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_CommandForm()
        self.ui.setupUi(self)
        self.initializeOptions()
        
        self.optionModel = OptionModel(self)
        self.ui.tableOptions.setModel(self.optionModel)
        # register for the model changed signal so the text showing the
        # rsync command can be updated appropriately
        self.connect(self.optionModel, 
                     QtCore.SIGNAL("dataChanged(QModelIndex, QModelIndex)"), 
                     self.onAdvancedOption)
                
        # set up the rsync command
        self.command = None
                        
    def setCommand(self, command):
        '''
        Set the command that this form configures.
        '''
        self.command = command
        self.dataToForm()
        
    def dataToForm(self):
        '''
        Transfer data from the rsync command to the form elements.
        '''
        # the source information
        self.ui.textSourcePath.setText(self.command.getSource().getPath())
        self.ui.textSourceHost.setText(self.command.getSource().getHost())
        self.ui.textSourceUser.setText(self.command.getSource().getUser())
        
        # the destination information
        self.ui.textDestinationPath.setText(self.command.getDestination().getPath())
        self.ui.textDestinationHost.setText(self.command.getDestination().getHost())
        self.ui.textDestinationUser.setText(self.command.getDestination().getUser())
        
        # find enabled common options, and check the appropriate boxes
        for opt in self.command.getOptions():
            if (opt in optionSet):
                optionSet[opt][2].setChecked(True)
                
        self.optionModel.setOptions(self.command.getOptions())
        
        # update the text that shows the command written out
        self.ui.labelCommand.setText(str(self.command))
        
    def onCheckOption(self):
        '''
        Respond to options being checked.
        '''        
        # cycle through the common options
        options = self.optionModel.getOptions()
        for key in optionSet:
            if (optionSet[key][2].isChecked()):
                options.enable(key)
        self.command.setOptions(options)
        
        # update the text that shows the command written out
        self.ui.labelCommand.setText(str(self.command))
        
    def onAdvancedOption(self, index1, index2):
        self.onCheckOption()
        
    def onSourcePath(self, value):
        self.command.getSource().setPath(str(value))
        self.ui.labelCommand.setText(str(self.command))
    
    def onSourceHost(self, value):
        self.command.getSource().setHost(str(value))
        self.ui.labelCommand.setText(str(self.command))
        
    def onSourceUser(self, value):
        self.command.getSource().setUser(str(value))
        self.ui.labelCommand.setText(str(self.command))
        
    def onDestinationPath(self, value):
        self.command.getDestination().setPath(str(value))
        self.ui.labelCommand.setText(str(self.command))
        
    def onDestinationHost(self, value):
        self.command.getDestination().setHost(str(value))
        self.ui.labelCommand.setText(str(self.command))
        
    def onDestinationUser(self, value):
        self.command.getDestination().setUser(str(value))
        self.ui.labelCommand.setText(str(self.command))
        
    def onChooseSource(self):
        '''
        Respond to the source path browse button click by having the user
        select a directory on the local file system
        '''
        dialog = QtGui.QFileDialog(self, "Select a file");
        dialog.setFileMode(QtGui.QFileDialog.Directory)
        if dialog.exec_():
            filename = dialog.selectedFiles()[0]
            self.ui.textSourcePath.setText(filename)
            
    def onChooseDestination(self):
        '''
        Respond to the source path browse button click by having the user
        select a directory on the local file system
        '''
        dialog = QtGui.QFileDialog(self, "Select a file")
        dialog.setFileMode(QtGui.QFileDialog.Directory)
        if dialog.exec_():
            filename = dialog.selectedFiles()[0]
            self.ui.textDestinationPath.setText(filename)
            
    def onAddOption(self):
        '''
        Add the (name, value) pair as an option.  Requires that name is not
        empty.
        '''
        name = self.ui.textName.text()
        value = self.ui.textValue.text()
        if name != None and name != '':
            self.optionModel.append(name, value)
    
    def onEditOption(self):
        '''
        Update the selected option with the current (name, value) pair in the
        text fields.  Requires that name is not empty. 
        '''
        index = self.ui.tableOptions.currentIndex()
        name = self.ui.textName.text()
        value = self.ui.textValue.text()
        if name != None and name != '':
            self.optionModel.edit(index.row(), name, value)
    
    def onRemoveOption(self):
        '''
        Removes the currently selected option.
        '''
        index = self.ui.tableOptions.currentIndex()
        self.optionModel.remove(index.row())
    
    def onSelectOption(self, index):
        '''
        When an option is selected, populate the name and value text fields
        with the option (name, value) pair.
        '''
        pair = self.optionModel.get(index.row())
        if pair != None:
            self.ui.textName.setText(pair[0])
            self.ui.textValue.setText(pair[1])
    
    def initializeOptions(self):
        '''
        Build the common options window, which contains a grid of check boxes,
        each of which is hooked up to the onCheckOption method
        '''
        # setup the layout strategy.  make an nx3 grid
        cols = 3
        rows = math.ceil(len(optionSet) / float(cols))        
        layout = QtGui.QGridLayout(self.ui.tabCommon)
        idx = 0;
        
        # add a check box for every common option that calls the onCheckOption
        # method when clicked
        for key in sorted(optionSet):            
            button = QtGui.QCheckBox(key + " - " + optionSet[key][0], self)
            button.setToolTip(optionSet[key][1])
            self.connect(button, QtCore.SIGNAL("clicked()"), self.onCheckOption)
            optionSet[key][2] = button
            layout.addWidget(button, idx % rows, idx / rows)
            idx += 1
