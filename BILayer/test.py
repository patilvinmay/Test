self.widget_27 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_27.setObjectName("widget_27")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.widget_27)
        self.verticalLayout_22.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_10 = QtWidgets.QLabel(self.widget_27)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_22.addWidget(self.label_10)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_27)
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.149254 rgba(59, 59, 59, 255), stop:0.328358 rgba(60, 60, 60, 255), stop:0.517413 rgba(68, 68, 68, 255), stop:0.716418 rgba(80, 80, 80, 255), stop:1 rgba(115, 115, 115, 255));\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"width:60;\n"
"height:30;\n"
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
        self.pushButton_12.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/whiteIcons/featherwhite/calendar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon4)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_22.addWidget(self.pushButton_12)
        self.verticalLayout_16.addWidget(self.widget_27)
        
 self.label_10.setText(_translate("MainWindow", "PROC_DT"))
