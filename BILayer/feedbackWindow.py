# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feedbackWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(744, 612)
        Dialog.setStyleSheet("background-color: rgb(42, 38, 62);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(11, 2, 11, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("QLabel{\n"
"    background-color: rgb(42, 38, 62);\n"
"    color: rgb(238, 236, 255);/* Set your desired text color */\n"
"    font-family: Arial;\n"
"    font-size: 20px; /* Set your desired font size */\n"
"    font-weight: bold;\n"
"    }")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("QLabel{\n"
"    background-color: rgb(42, 38, 62);\n"
"    color: rgb(238, 236, 255);/* Set your desired text color */\n"
"    font-family: Arial;\n"
"    font-size: 11px; /* Set your desired font size */\n"
"    font-weight: bold;\n"
"    }")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setStyleSheet("QTextEdit{\n"
"    background-color: rgb(59, 56, 84);/* Set your desired background color */\n"
"    color: rgb(238, 236, 255);/* Set your desired text color */\n"
"    font-family: Arial;\n"
"    font-size: 15px; /* Set your desired font size */\n"
"    border-style: none;\n"
"    /*border: 1px solid #CCCCCC;  Set your desired border style */\n"
"    border-radius: 15px; /* Set your desired border radius */\n"
"    padding: 5px; /* Set your desired padding */\n"
"    height:100px;\n"
"    }")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(642, 38, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
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
"    width:100;\n"
"    height:40;\n"
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
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
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
"    width:100;\n"
"    height:40;\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "SEND US YOUR FEEDBACK !"))
        self.label_2.setText(_translate("Dialog", "We would like your feedback to improve us."))
        self.pushButton.setText(_translate("Dialog", "Cancel"))
        self.pushButton_2.setText(_translate("Dialog", "Send"))