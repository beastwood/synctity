# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Thu Aug 29 22:57:47 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(375, 206)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelIcon = QtGui.QLabel(Dialog)
        self.labelIcon.setText(_fromUtf8(""))
        self.labelIcon.setPixmap(QtGui.QPixmap(_fromUtf8(":/synctity.png")))
        self.labelIcon.setObjectName(_fromUtf8("labelIcon"))
        self.gridLayout.addWidget(self.labelIcon, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelApplication = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelApplication.setFont(font)
        self.labelApplication.setObjectName(_fromUtf8("labelApplication"))
        self.verticalLayout.addWidget(self.labelApplication)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.labelVersion = QtGui.QLabel(Dialog)
        self.labelVersion.setObjectName(_fromUtf8("labelVersion"))
        self.verticalLayout.addWidget(self.labelVersion)
        self.labelCopyright = QtGui.QLabel(Dialog)
        self.labelCopyright.setTextFormat(QtCore.Qt.RichText)
        self.labelCopyright.setObjectName(_fromUtf8("labelCopyright"))
        self.verticalLayout.addWidget(self.labelCopyright)
        self.labelAuthors = QtGui.QLabel(Dialog)
        self.labelAuthors.setTextFormat(QtCore.Qt.PlainText)
        self.labelAuthors.setObjectName(_fromUtf8("labelAuthors"))
        self.verticalLayout.addWidget(self.labelAuthors)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.labelWebsite = QtGui.QLabel(Dialog)
        self.labelWebsite.setObjectName(_fromUtf8("labelWebsite"))
        self.verticalLayout.addWidget(self.labelWebsite)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 2)
        self.gridLayout.setColumnStretch(1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelApplication.setText(_translate("Dialog", "Synctity", None))
        self.labelVersion.setText(_translate("Dialog", "version", None))
        self.labelCopyright.setText(_translate("Dialog", "copyright", None))
        self.labelAuthors.setText(_translate("Dialog", "Brian S. Eastwood", None))
        self.labelWebsite.setText(_translate("Dialog", "website", None))

import resources_rc
