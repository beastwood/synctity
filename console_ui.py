# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'console.ui'
#
# Created: Wed Dec  2 21:18:39 2009
#      by: PyQt4 UI code generator 4.6.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Console(object):
    def setupUi(self, Console):
        Console.setObjectName("Console")
        Console.resize(639, 343)
        self.centralwidget = QtGui.QWidget(Console)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textCommandLine = QtGui.QLineEdit(self.centralwidget)
        self.textCommandLine.setObjectName("textCommandLine")
        self.gridLayout.addWidget(self.textCommandLine, 0, 0, 2, 3)
        spacerItem = QtGui.QSpacerItem(507, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.buttonCandel = QtGui.QPushButton(self.centralwidget)
        self.buttonCandel.setObjectName("buttonCandel")
        self.gridLayout.addWidget(self.buttonCandel, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 2)
        Console.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Console)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 22))
        self.menubar.setObjectName("menubar")
        Console.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Console)
        self.statusbar.setObjectName("statusbar")
        Console.setStatusBar(self.statusbar)
        self.dockConsole = QtGui.QDockWidget(Console)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.dockConsole.sizePolicy().hasHeightForWidth())
        self.dockConsole.setSizePolicy(sizePolicy)
        self.dockConsole.setMinimumSize(QtCore.QSize(200, 200))
        self.dockConsole.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockConsole.setObjectName("dockConsole")
        self.dockWidgetContents_3 = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_3.setSizePolicy(sizePolicy)
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textConsole = QtGui.QTextEdit(self.dockWidgetContents_3)
        self.textConsole.setObjectName("textConsole")
        self.verticalLayout_2.addWidget(self.textConsole)
        self.dockConsole.setWidget(self.dockWidgetContents_3)
        Console.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockConsole)

        self.retranslateUi(Console)
        QtCore.QObject.connect(self.buttonCandel, QtCore.SIGNAL("clicked()"), Console.onCancel)
        QtCore.QObject.connect(self.textCommandLine, QtCore.SIGNAL("returnPressed()"), Console.onCommandLine)
        QtCore.QMetaObject.connectSlotsByName(Console)

    def retranslateUi(self, Console):
        Console.setWindowTitle(QtGui.QApplication.translate("Console", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCandel.setText(QtGui.QApplication.translate("Console", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.dockConsole.setWindowTitle(QtGui.QApplication.translate("Console", "Console", None, QtGui.QApplication.UnicodeUTF8))

