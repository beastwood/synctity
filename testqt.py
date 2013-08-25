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

Created on Nov 11, 2009
'''
import sys
from PyQt4 import QtCore, QtGui

from console_ui import Ui_Console

class Console(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_Console()
        self.ui.setupUi(self)
        
        self.process = QtCore.QProcess(self)
        self.connect(self.process, QtCore.SIGNAL("started()"), self.onStarted)
        self.connect(self.process, QtCore.SIGNAL("readyReadStandardOutput()"), self.onOutput)
        self.connect(self.process, QtCore.SIGNAL("finished(int)"), self.onFinished)
        
    def onCommandLine(self):
        self.ui.textConsole.append('> ' + self.ui.textCommandLine.text() + '\n')
        # spawn subprocess and capture output
        if self.process.state() == QtCore.QProcess.NotRunning:
            self.process.start(self.ui.textCommandLine.text())
        
        self.ui.textCommandLine.setEnabled(self.process.state() == QtCore.QProcess.NotRunning)
        
    def onCancel(self):
        if self.process != None:
            self.process.kill()
        self.ui.textCommandLine.setEnabled(self.process.state() == QtCore.QProcess.NotRunning)
        self.ui.textCommandLine.selectAll()
            
    def onStarted(self):
        print "Started: ", self.process.pid()
        
    def onOutput(self):
            self.ui.textConsole.insertPlainText(str(self.process.readAll()))
            
    def onFinished(self, retCode):
        print "Finished: ", retCode
        self.ui.textConsole.append("")
        self.ui.textCommandLine.setEnabled(self.process.state() == QtCore.QProcess.NotRunning)
        self.ui.textCommandLine.selectAll()
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Console()
    myapp.show()
    sys.exit(app.exec_())
    