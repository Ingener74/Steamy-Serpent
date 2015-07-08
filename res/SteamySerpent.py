# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Pavel/workspace/Steamy-Serpent/res/SteamySerpent.ui'
#
# Created: Wed Jul 08 23:09:35 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SteamySerpent(object):
    def setupUi(self, SteamySerpent):
        SteamySerpent.setObjectName("SteamySerpent")
        SteamySerpent.resize(308, 43)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main/smile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SteamySerpent.setWindowIcon(icon)
        self.horizontalLayout = QtGui.QHBoxLayout(SteamySerpent)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ChangeState = QtGui.QPushButton(SteamySerpent)
        self.ChangeState.setObjectName("ChangeState")
        self.horizontalLayout.addWidget(self.ChangeState)
        self.label = QtGui.QLabel(SteamySerpent)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(SteamySerpent)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.retranslateUi(SteamySerpent)
        QtCore.QMetaObject.connectSlotsByName(SteamySerpent)

    def retranslateUi(self, SteamySerpent):
        SteamySerpent.setWindowTitle(QtGui.QApplication.translate("SteamySerpent", "Скабрезный змей", None, QtGui.QApplication.UnicodeUTF8))
        self.ChangeState.setText(QtGui.QApplication.translate("SteamySerpent", "Бамц!", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SteamySerpent", "Состояние", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
