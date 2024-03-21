from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(579, 380)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")

        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("border: 1px solid black;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(4, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.FILE_LE = QtWidgets.QLineEdit(self.frame)
        self.FILE_LE.setMinimumSize(QtCore.QSize(0, 0))
        self.FILE_LE.setObjectName("FILE_LE")
        self.gridLayout_3.addWidget(self.FILE_LE, 0, 1, 1, 1)

        self.SELECT_BTN = QtWidgets.QPushButton(self.frame)
        self.SELECT_BTN.setObjectName("SELECT_BTN")
        self.gridLayout_3.addWidget(self.SELECT_BTN, 0, 0, 1, 1)

        self.UPLOAD_BTN = QtWidgets.QPushButton(self.frame)
        self.UPLOAD_BTN.setObjectName("UPLOAD_BTN")
        self.gridLayout_3.addWidget(self.UPLOAD_BTN, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 5)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setStyleSheet("border: 1px solid black;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.tableView = QtWidgets.QTableView(self.frame_2)
        self.tableView.setObjectName("tableView")
        self.gridLayout_4.addWidget(self.tableView, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.SELECT_BTN.setText(_translate("Form", "Select File"))
        self.UPLOAD_BTN.setText(_translate("Form", "Upload"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
