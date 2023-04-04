import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog


class Ui_DateDialog(QDialog):
    def __init__(self, parent=None):
        super(Ui_DateDialog, self).__init__(parent)
        self.setObjectName("Dialog")
        self.resize(430, 400)
        self.setStyleSheet("background-color: rgb(39, 39, 47);")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.widget_3)
        self.calendarWidget.setStyleSheet("color: black;\n"
                                          "background-color:white;")
        self.calendarWidget.setMinimumDate(QtCore.QDate(2021, 7, 1))
        self.calendarWidget.setMaximumDate(QtCore.QDate(2023, 4, 30))
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_3.addWidget(self.calendarWidget)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "color: white;\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.149254 rgba(59, 59, 59, 255), stop:0.328358 rgba(60, 60, 60, 255), stop:0.517413 rgba(68, 68, 68, 255), stop:0.716418 rgba(80, 80, 80, 255), stop:1 rgba(115, 115, 115, 255));\n"
                                        "border-style: outset;\n"
                                        "border-width: 0px;\n"
                                        "width:60;\n"
                                        "height:40;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0248756 rgba(115, 115, 115, 255), stop:0.353234 rgba(80, 80, 80, 255), stop:0.547264 rgba(68, 68, 68, 255), stop:0.781095 rgba(60, 60, 60, 255), stop:1 rgba(59, 59, 59, 255));\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 0.5px;\n"
                                        "    border-color: rgb(0, 255, 127);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 0.5px;\n"
                                        "    border-color: rgb(253, 204, 96);\n"
                                        "}")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/whiteIcons/featherwhite/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "color: white;\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.149254 rgba(59, 59, 59, 255), stop:0.328358 rgba(60, 60, 60, 255), stop:0.517413 rgba(68, 68, 68, 255), stop:0.716418 rgba(80, 80, 80, 255), stop:1 rgba(115, 115, 115, 255));\n"
                                      "border-style: outset;\n"
                                      "border-width: 0px;\n"
                                      "width:60;\n"
                                      "height:40;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0248756 rgba(115, 115, 115, 255), stop:0.353234 rgba(80, 80, 80, 255), stop:0.547264 rgba(68, 68, 68, 255), stop:0.781095 rgba(60, 60, 60, 255), stop:1 rgba(59, 59, 59, 255));\n"
                                      "    border-style: outset;\n"
                                      "    border-width: 0.5px;\n"
                                      "    border-color: rgb(0, 255, 127);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    border-style: outset;\n"
                                      "    border-width: 0.5px;\n"
                                      "    border-color: rgb(253, 204, 96);\n"
                                      "}")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/whiteIcons/featherwhite/arrow-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.pushButton.clicked.connect(self.accept)
        self.pushButton_2.clicked.connect(self.close)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
