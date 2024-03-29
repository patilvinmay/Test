# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\vinmayp\Desktop\BILayer\White Theme\CalenderDialogWhiteTheme.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(821, 400)
        Dialog.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.widget_3)
        self.calendarWidget.setStyleSheet("color: black;\n"
"background-color:white;")
        self.calendarWidget.setSelectedDate(QtCore.QDate(2021, 7, 1))
        self.calendarWidget.setMinimumDate(QtCore.QDate(2021, 7, 1))
        self.calendarWidget.setMaximumDate(QtCore.QDate(2023, 4, 30))
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout_2.addWidget(self.calendarWidget)
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.widget_3)
        self.calendarWidget_2.setStyleSheet("color: black;\n"
"background-color:white;")
        self.calendarWidget_2.setSelectedDate(QtCore.QDate(2023, 4, 30))
        self.calendarWidget_2.setMinimumDate(QtCore.QDate(2021, 7, 1))
        self.calendarWidget_2.setMaximumDate(QtCore.QDate(2023, 4, 30))
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.horizontalLayout_2.addWidget(self.calendarWidget_2)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color:white;\n"
"background-color: rgb(170, 170, 255);\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"width:60;\n"
"height:40;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(170, 170, 255);\n"
"    border-style: outset;\n"
"    border-width: 0.5px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: outset;\n"
"    border-width: 0.5px;\n"
"    border-color: rgb(85, 85, 255);\n"
"}")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/feather/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setStyleSheet("QPushButton{\n"
"color:white;\n"
"background-color: rgb(170, 170, 255);\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"width:60;\n"
"height:40;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(170, 170, 255);\n"
"    border-style: outset;\n"
"    border-width: 0.5px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: outset;\n"
"    border-width: 0.5px;\n"
"    border-color: rgb(85, 85, 255);\n"
"}")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/feather/arrow-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_10.setText(_translate("Dialog", "Start Date"))
        self.label_11.setText(_translate("Dialog", "End Date"))
        self.pushButton_2.setToolTip(_translate("Dialog", "<html><head/><body><p>Run SQL</p></body></html>"))
        self.pushButton.setToolTip(_translate("Dialog", "<html><head/><body><p>Run SQL</p></body></html>"))
import resource_rc
