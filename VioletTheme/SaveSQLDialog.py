# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\vinmayp\Desktop\BILayer\VioletTheme\SaveSQLDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SaveSQL(object):
    def setupUi(self, SaveSQL):
        SaveSQL.setObjectName("SaveSQL")
        SaveSQL.resize(537, 223)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SaveSQL.sizePolicy().hasHeightForWidth())
        SaveSQL.setSizePolicy(sizePolicy)
        SaveSQL.setStyleSheet("background-color: rgb(42, 38, 62);")
        self.verticalLayout = QtWidgets.QVBoxLayout(SaveSQL)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(SaveSQL)
        self.widget.setStyleSheet("QWidget{\n"
"    background-color: rgb(53, 50, 76);\n"
"    border-radius: 5px;\n"
"    padding:8px;\n"
"    }")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("QLabel{\n"
"    color: rgb(238, 236, 255);/* Set your desired text color */\n"
"    font-family: Arial;\n"
"    font-size: 15px; /* Set your desired font size */\n"
"    }")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(64, 58, 95);/* Set your desired background color */\n"
"    color: rgb(238, 236, 255);/* Set your desired text color */\n"
"    font-family: Arial;\n"
"    font-size: 18px; /* Set your desired font size */\n"
"    border-style: none;\n"
"    /*border: 1px solid #CCCCCC;  Set your desired border style */\n"
"    border-radius: 5px; /* Set your desired border radius */\n"
"    padding: 5px; /* Set your desired padding */\n"
"    }")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    /*background-image: url(:/whiteIcons/featherwhite/calendar.svg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;*/\n"
"    background-color:rgb(99, 89, 145);\n"
"    \n"
"    border-style: none;\n"
"    border-color: rgb(59, 56, 84);\n"
"    border-radius: 8px; /* Set your desired border radius */\n"
"\n"
"    color:white;\n"
"    font-family: Arial;\n"
"    font-size: 15px; /* Set your desired font size */\n"
"    width:60;\n"
"    height:30;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(53, 50, 76);\n"
"    border-style: outset;\n"
"    border-width: 0.5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(67, 42, 73);\n"
"    border-style: none;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/WhiteIcons/featherwhite/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    /*background-image: url(:/whiteIcons/featherwhite/calendar.svg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;*/\n"
"    background-color:rgb(99, 89, 145);\n"
"    \n"
"    border-style: none;\n"
"    border-color: rgb(59, 56, 84);\n"
"    border-radius: 8px; /* Set your desired border radius */\n"
"\n"
"    color:white;\n"
"    font-family: Arial;\n"
"    font-size: 15px; /* Set your desired font size */\n"
"    width:60;\n"
"    height:30;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(53, 50, 76);\n"
"    border-style: outset;\n"
"    border-width: 0.5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(67, 42, 73);\n"
"    border-style: none;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/WhiteIcons/featherwhite/users.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(SaveSQL)
        QtCore.QMetaObject.connectSlotsByName(SaveSQL)

    def retranslateUi(self, SaveSQL):
        _translate = QtCore.QCoreApplication.translate
        SaveSQL.setWindowTitle(_translate("SaveSQL", "Save SQL"))
        self.label.setText(_translate("SaveSQL", "SQL Name:"))
        self.pushButton.setText(_translate("SaveSQL", "Private Repository"))
        self.pushButton_2.setText(_translate("SaveSQL", "Public Repository"))
import resource_rc
