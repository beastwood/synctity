# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'command.ui'
#
# Created: Mon Aug  9 11:47:17 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CommandForm(object):
    def setupUi(self, CommandForm):
        CommandForm.setObjectName("CommandForm")
        CommandForm.resize(677, 423)
        self.gridLayout_4 = QtGui.QGridLayout(CommandForm)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabPaths = QtGui.QTabWidget(CommandForm)
        self.tabPaths.setObjectName("tabPaths")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textSourcePath = QtGui.QLineEdit(self.groupBox)
        self.textSourcePath.setObjectName("textSourcePath")
        self.gridLayout.addWidget(self.textSourcePath, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.textSourceHost = QtGui.QLineEdit(self.groupBox)
        self.textSourceHost.setObjectName("textSourceHost")
        self.gridLayout.addWidget(self.textSourceHost, 2, 1, 1, 2)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.textSourceUser = QtGui.QLineEdit(self.groupBox)
        self.textSourceUser.setObjectName("textSourceUser")
        self.gridLayout.addWidget(self.textSourceUser, 3, 1, 1, 2)
        self.buttonSourcePath = QtGui.QPushButton(self.groupBox)
        self.buttonSourcePath.setObjectName("buttonSourcePath")
        self.gridLayout.addWidget(self.buttonSourcePath, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.textDestinationPath = QtGui.QLineEdit(self.groupBox_2)
        self.textDestinationPath.setObjectName("textDestinationPath")
        self.gridLayout_2.addWidget(self.textDestinationPath, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.textDestinationHost = QtGui.QLineEdit(self.groupBox_2)
        self.textDestinationHost.setObjectName("textDestinationHost")
        self.gridLayout_2.addWidget(self.textDestinationHost, 1, 1, 1, 2)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.textDestinationUser = QtGui.QLineEdit(self.groupBox_2)
        self.textDestinationUser.setObjectName("textDestinationUser")
        self.gridLayout_2.addWidget(self.textDestinationUser, 2, 1, 1, 2)
        self.buttonDestinationPath = QtGui.QPushButton(self.groupBox_2)
        self.buttonDestinationPath.setObjectName("buttonDestinationPath")
        self.gridLayout_2.addWidget(self.buttonDestinationPath, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.tabPaths.addTab(self.tab, "")
        self.tabCommon = QtGui.QWidget()
        self.tabCommon.setObjectName("tabCommon")
        self.tabPaths.addTab(self.tabCommon, "")
        self.tabAdvanced = QtGui.QWidget()
        self.tabAdvanced.setObjectName("tabAdvanced")
        self.gridLayout_3 = QtGui.QGridLayout(self.tabAdvanced)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtGui.QLabel(self.tabAdvanced)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.textName = QtGui.QLineEdit(self.tabAdvanced)
        self.textName.setObjectName("textName")
        self.gridLayout_3.addWidget(self.textName, 0, 1, 1, 3)
        self.label_8 = QtGui.QLabel(self.tabAdvanced)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.textValue = QtGui.QLineEdit(self.tabAdvanced)
        self.textValue.setObjectName("textValue")
        self.gridLayout_3.addWidget(self.textValue, 1, 1, 1, 3)
        self.buttonAdd = QtGui.QPushButton(self.tabAdvanced)
        self.buttonAdd.setObjectName("buttonAdd")
        self.gridLayout_3.addWidget(self.buttonAdd, 2, 0, 1, 1)
        self.buttonEdit = QtGui.QPushButton(self.tabAdvanced)
        self.buttonEdit.setObjectName("buttonEdit")
        self.gridLayout_3.addWidget(self.buttonEdit, 2, 1, 1, 1)
        self.buttonRemove = QtGui.QPushButton(self.tabAdvanced)
        self.buttonRemove.setObjectName("buttonRemove")
        self.gridLayout_3.addWidget(self.buttonRemove, 2, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(374, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 2, 3, 1, 1)
        self.tableOptions = QtGui.QTableView(self.tabAdvanced)
        self.tableOptions.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableOptions.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableOptions.setObjectName("tableOptions")
        self.tableOptions.horizontalHeader().setHighlightSections(False)
        self.tableOptions.horizontalHeader().setStretchLastSection(False)
        self.tableOptions.verticalHeader().setVisible(False)
        self.tableOptions.verticalHeader().setHighlightSections(False)
        self.gridLayout_3.addWidget(self.tableOptions, 3, 0, 1, 4)
        self.tabPaths.addTab(self.tabAdvanced, "")
        self.gridLayout_4.addWidget(self.tabPaths, 0, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(CommandForm)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 40))
        self.scrollArea.setBaseSize(QtCore.QSize(0, 0))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 649, 36))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setSpacing(-1)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelCommand = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.labelCommand.setObjectName("labelCommand")
        self.horizontalLayout_3.addWidget(self.labelCommand)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.buttonOK = QtGui.QPushButton(CommandForm)
        self.buttonOK.setAutoDefault(False)
        self.buttonOK.setDefault(True)
        self.buttonOK.setObjectName("buttonOK")
        self.horizontalLayout_2.addWidget(self.buttonOK)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(CommandForm)
        self.tabPaths.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonOK, QtCore.SIGNAL("clicked()"), CommandForm.accept)
        QtCore.QObject.connect(self.textSourcePath, QtCore.SIGNAL("textChanged(QString)"), CommandForm.onSourcePath)
        QtCore.QObject.connect(self.textSourceHost, QtCore.SIGNAL("textChanged(QString)"), CommandForm.onSourceHost)
        QtCore.QObject.connect(self.textSourceUser, QtCore.SIGNAL("textChanged(QString)"), CommandForm.onSourceUser)
        QtCore.QObject.connect(self.textDestinationPath, QtCore.SIGNAL("textChanged(QString)"), CommandForm.onDestinationPath)
        QtCore.QObject.connect(self.textDestinationHost, QtCore.SIGNAL("textChanged(QString)"), CommandForm.onDestinationHost)
        QtCore.QObject.connect(self.textDestinationUser, QtCore.SIGNAL("textChanged(QString)"), CommandForm.onDestinationUser)
        QtCore.QObject.connect(self.buttonSourcePath, QtCore.SIGNAL("clicked()"), CommandForm.onChooseSource)
        QtCore.QObject.connect(self.buttonDestinationPath, QtCore.SIGNAL("clicked()"), CommandForm.onChooseDestination)
        QtCore.QObject.connect(self.buttonAdd, QtCore.SIGNAL("clicked()"), CommandForm.onAddOption)
        QtCore.QObject.connect(self.buttonEdit, QtCore.SIGNAL("clicked()"), CommandForm.onEditOption)
        QtCore.QObject.connect(self.buttonRemove, QtCore.SIGNAL("clicked()"), CommandForm.onRemoveOption)
        QtCore.QObject.connect(self.tableOptions, QtCore.SIGNAL("clicked(QModelIndex)"), CommandForm.onSelectOption)
        QtCore.QMetaObject.connectSlotsByName(CommandForm)

    def retranslateUi(self, CommandForm):
        CommandForm.setWindowTitle(QtGui.QApplication.translate("CommandForm", "rsync command", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("CommandForm", "Source", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CommandForm", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CommandForm", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CommandForm", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSourcePath.setText(QtGui.QApplication.translate("CommandForm", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("CommandForm", "Destination", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CommandForm", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("CommandForm", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("CommandForm", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDestinationPath.setText(QtGui.QApplication.translate("CommandForm", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabPaths.setTabText(self.tabPaths.indexOf(self.tab), QtGui.QApplication.translate("CommandForm", "Paths", None, QtGui.QApplication.UnicodeUTF8))
        self.tabPaths.setTabText(self.tabPaths.indexOf(self.tabCommon), QtGui.QApplication.translate("CommandForm", "Common", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("CommandForm", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("CommandForm", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAdd.setText(QtGui.QApplication.translate("CommandForm", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonEdit.setText(QtGui.QApplication.translate("CommandForm", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonRemove.setText(QtGui.QApplication.translate("CommandForm", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.tabPaths.setTabText(self.tabPaths.indexOf(self.tabAdvanced), QtGui.QApplication.translate("CommandForm", "Advanced", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCommand.setText(QtGui.QApplication.translate("CommandForm", "rsync command", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonOK.setText(QtGui.QApplication.translate("CommandForm", "OK", None, QtGui.QApplication.UnicodeUTF8))
