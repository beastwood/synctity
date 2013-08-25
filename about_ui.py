# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Fri Aug  6 13:11:44 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(368, 204)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.labelIcon = QtGui.QLabel(Dialog)
        self.labelIcon.setText("")
        self.labelIcon.setPixmap(QtGui.QPixmap(":/synctity.png"))
        self.labelIcon.setObjectName("labelIcon")
        self.gridLayout.addWidget(self.labelIcon, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelApplication = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.labelApplication.setFont(font)
        self.labelApplication.setObjectName("labelApplication")
        self.verticalLayout.addWidget(self.labelApplication)
        self.labelVersion = QtGui.QLabel(Dialog)
        self.labelVersion.setObjectName("labelVersion")
        self.verticalLayout.addWidget(self.labelVersion)
        self.labelInfo = QtGui.QLabel(Dialog)
        self.labelInfo.setTextFormat(QtCore.Qt.RichText)
        self.labelInfo.setObjectName("labelInfo")
        self.verticalLayout.addWidget(self.labelInfo)
        self.labelWebsite = QtGui.QLabel(Dialog)
        self.labelWebsite.setObjectName("labelWebsite")
        self.verticalLayout.addWidget(self.labelWebsite)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)
        self.gridLayout.setColumnStretch(1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.labelApplication.setText(QtGui.QApplication.translate("Dialog", "Synctity", None, QtGui.QApplication.UnicodeUTF8))
        self.labelVersion.setText(QtGui.QApplication.translate("Dialog", "version", None, QtGui.QApplication.UnicodeUTF8))
        self.labelInfo.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Brian S. Eastwood</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">© 2010</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelWebsite.setText(QtGui.QApplication.translate("Dialog", "website", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
