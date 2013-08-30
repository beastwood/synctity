'''
Created on Aug 6, 2010

@author: bseastwo
'''
import sys
from PyQt4.QtGui import QApplication

from synctus import SynctityWindow, APPLICATION_NAME, APPLICATION_VERSION 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName(APPLICATION_NAME)
    app.setApplicationVersion(APPLICATION_VERSION)
    
    myapp = SynctityWindow()
    myapp.setWindowTitle(APPLICATION_NAME + " " + APPLICATION_VERSION)
    myapp.show()
    myapp.raise_()
    myapp.setFocus()
    sys.exit(app.exec_())