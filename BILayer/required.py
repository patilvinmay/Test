
import resource_rc
import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDataStream, pyqtSignal
from PyQt5.QtWidgets import QDialog, QListWidget, QApplication


class SelectDropableListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        source = event.source()
        target = QApplication.widgetAt(self.mapToGlobal(event.pos()))

        if isinstance(event.source(), SelectDropableListWidget) or isinstance(event.source(), FilterDropableListWidget):
            event.ignore()
        else:
            event.accept()

    def dropEvent(self, event):
        source = event.source()
        target = QApplication.widgetAt(self.mapToGlobal(event.pos()))

        mime = event.mimeData()
        if mime.hasText():
            print(mime.text())
        elif mime.hasFormat('application/x-qabstractitemmodeldatalist'):
            textList = []
            stream = QDataStream(mime.data('application/x-qabstractitemmodeldatalist'))
            while not stream.atEnd():
                # we're not using row and columns, but we *must* read them
                row = stream.readInt()
                col = stream.readInt()
                for dataSize in range(stream.readInt()):
                    role, value = stream.readInt(), stream.readQVariant()
                    if role == Qt.DisplayRole:
                        textList.append(value)
                        self.addItem(value)


class FilterDropableListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        source = event.source()
        target = QApplication.widgetAt(self.mapToGlobal(event.pos()))

        if isinstance(event.source(), SelectDropableListWidget) or isinstance(event.source(), FilterDropableListWidget):
            event.ignore()
        else:
            event.accept()

    def dropEvent(self, event):
        source = event.source()
        target = QApplication.widgetAt(self.mapToGlobal(event.pos()))

        mime = event.mimeData()
        if mime.hasText():
            print(mime.text())
        elif mime.hasFormat('application/x-qabstractitemmodeldatalist'):
            textList = []
            stream = QDataStream(mime.data('application/x-qabstractitemmodeldatalist'))
            while not stream.atEnd():
                # we're not using row and columns, but we *must* read them
                row = stream.readInt()
                col = stream.readInt()
                for dataSize in range(stream.readInt()):
                    role, value = stream.readInt(), stream.readQVariant()
                    if role == Qt.DisplayRole:
                        textList.append(value)
                        self.addItem(value)


class DeleteDroppedListWidget(QListWidget):
    SelectColumnDropped = pyqtSignal()
    FilterColumnDropped = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.textList = []


    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        source = event.source()
        target = QApplication.widgetAt(self.mapToGlobal(event.pos()))

        mime = event.mimeData()
        if mime.hasText():
            print(mime.text())
        elif mime.hasFormat('application/x-qabstractitemmodeldatalist'):
            self.textList = []
            stream = QDataStream(mime.data('application/x-qabstractitemmodeldatalist'))
            while not stream.atEnd():
                # we're not using row and columns, but we *must* read them
                row = stream.readInt()
                col = stream.readInt()
                for dataSize in range(stream.readInt()):
                    role, value = stream.readInt(), stream.readQVariant()
                    if role == Qt.DisplayRole:
                        self.textList.append(value)
            if isinstance(event.source(), SelectDropableListWidget):
                self.SelectColumnDropped.emit()
            elif isinstance(event.source(), FilterDropableListWidget):
                self.FilterColumnDropped.emit()


class TableModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """

    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.index)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.iloc[index.row()][index.column()])
        return None

    # def headerData(self, col, orientation, role):
    #     if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
    #         return self._data.columns[col]
    #     return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._data.index[col] + 1
        return None

    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        try:
            self.layoutAboutToBeChanged.emit()
            self._data = self._data.sort_values(self._data.columns[Ncol], ascending=not order)
            self.layoutChanged.emit()
        except Exception as e:
            print(e)


class Ui_LoginDialog(QDialog):
    def __init__(self, parent=None):
        super(Ui_LoginDialog, self).__init__(parent)

        self.creds = []
        self.setObjectName("Dialog")
        self.resize(400, 400)
        self.setStyleSheet("background-color: rgb(39, 39, 47);")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(2, 2, 2, 2)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "color:white;\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.149254 rgba(59, 59, 59, 255), stop:0.328358 rgba(60, 60, 60, 255), stop:0.517413 rgba(68, 68, 68, 255), stop:0.716418 rgba(80, 80, 80, 255), stop:1 rgba(115, 115, 115, 255));\n"
                                    "border-style: outset;\n"
                                    "border-width: 0px;\n"
                                    "width:60;\n"
                                    "height:30;\n"
                                    "}\n"
                                    "QLineEdit:hover {\n"
                                    "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0248756 rgba(115, 115, 115, 255), stop:0.353234 rgba(80, 80, 80, 255), stop:0.547264 rgba(68, 68, 68, 255), stop:0.781095 rgba(60, 60, 60, 255), stop:1 rgba(59, 59, 59, 255));\n"
                                    "}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
                                      "color:white;\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.149254 rgba(59, 59, 59, 255), stop:0.328358 rgba(60, 60, 60, 255), stop:0.517413 rgba(68, 68, 68, 255), stop:0.716418 rgba(80, 80, 80, 255), stop:1 rgba(115, 115, 115, 255));\n"
                                      "border-style: outset;\n"
                                      "border-width: 0px;\n"
                                      "width:60;\n"
                                      "height:30;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0248756 rgba(115, 115, 115, 255), stop:0.353234 rgba(80, 80, 80, 255), stop:0.547264 rgba(68, 68, 68, 255), stop:0.781095 rgba(60, 60, 60, 255), stop:1 rgba(59, 59, 59, 255));\n"
                                      "}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
                                      "color:white;\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.149254 rgba(59, 59, 59, 255), stop:0.328358 rgba(60, 60, 60, 255), stop:0.517413 rgba(68, 68, 68, 255), stop:0.716418 rgba(80, 80, 80, 255), stop:1 rgba(115, 115, 115, 255));\n"
                                      "border-style: outset;\n"
                                      "border-width: 0px;\n"
                                      "width:60;\n"
                                      "height:30;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0248756 rgba(115, 115, 115, 255), stop:0.353234 rgba(80, 80, 80, 255), stop:0.547264 rgba(68, 68, 68, 255), stop:0.781095 rgba(60, 60, 60, 255), stop:1 rgba(59, 59, 59, 255));\n"
                                      "}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
                                      "color:white;\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.149254 rgba(59, 59, 59, 255), stop:0.328358 rgba(60, 60, 60, 255), stop:0.517413 rgba(68, 68, 68, 255), stop:0.716418 rgba(80, 80, 80, 255), stop:1 rgba(115, 115, 115, 255));\n"
                                      "border-style: outset;\n"
                                      "border-width: 0px;\n"
                                      "width:60;\n"
                                      "height:30;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0248756 rgba(115, 115, 115, 255), stop:0.353234 rgba(80, 80, 80, 255), stop:0.547264 rgba(68, 68, 68, 255), stop:0.781095 rgba(60, 60, 60, 255), stop:1 rgba(59, 59, 59, 255));\n"
                                      "}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
                                      "color:white;\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.149254 rgba(59, 59, 59, 255), stop:0.328358 rgba(60, 60, 60, 255), stop:0.517413 rgba(68, 68, 68, 255), stop:0.716418 rgba(80, 80, 80, 255), stop:1 rgba(115, 115, 115, 255));\n"
                                      "border-style: outset;\n"
                                      "border-width: 0px;\n"
                                      "width:60;\n"
                                      "height:30;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0248756 rgba(115, 115, 115, 255), stop:0.353234 rgba(80, 80, 80, 255), stop:0.547264 rgba(68, 68, 68, 255), stop:0.781095 rgba(60, 60, 60, 255), stop:1 rgba(59, 59, 59, 255));\n"
                                      "}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white;")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("QLineEdit{\n"
                                      "color:white;\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.149254 rgba(59, 59, 59, 255), stop:0.328358 rgba(60, 60, 60, 255), stop:0.517413 rgba(68, 68, 68, 255), stop:0.716418 rgba(80, 80, 80, 255), stop:1 rgba(115, 115, 115, 255));\n"
                                      "border-style: outset;\n"
                                      "border-width: 0px;\n"
                                      "width:60;\n"
                                      "height:30;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0248756 rgba(115, 115, 115, 255), stop:0.353234 rgba(80, 80, 80, 255), stop:0.547264 rgba(68, 68, 68, 255), stop:0.781095 rgba(60, 60, 60, 255), stop:1 rgba(59, 59, 59, 255));\n"
                                      "}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white;")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("QLineEdit{\n"
                                      "color:white;\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.149254 rgba(59, 59, 59, 255), stop:0.328358 rgba(60, 60, 60, 255), stop:0.517413 rgba(68, 68, 68, 255), stop:0.716418 rgba(80, 80, 80, 255), stop:1 rgba(115, 115, 115, 255));\n"
                                      "border-style: outset;\n"
                                      "border-width: 0px;\n"
                                      "width:60;\n"
                                      "height:30;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0248756 rgba(115, 115, 115, 255), stop:0.353234 rgba(80, 80, 80, 255), stop:0.547264 rgba(68, 68, 68, 255), stop:0.781095 rgba(60, 60, 60, 255), stop:1 rgba(59, 59, 59, 255));\n"
                                      "}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.verticalLayout.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(self)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox.setStyleSheet("color:white;")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "color:white;\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.149254 rgba(59, 59, 59, 255), stop:0.328358 rgba(60, 60, 60, 255), stop:0.517413 rgba(68, 68, 68, 255), stop:0.716418 rgba(80, 80, 80, 255), stop:1 rgba(115, 115, 115, 255));\n"
                                      "border-style: outset;\n"
                                      "border-width: 0px;\n"
                                      "width:65;\n"
                                      "height:40;\n"
                                      "font: 9.5pt \"Calibri\";\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0248756 rgba(115, 115, 115, 255), stop:0.353234 rgba(80, 80, 80, 255), stop:0.547264 rgba(68, 68, 68, 255), stop:0.781095 rgba(60, 60, 60, 255), stop:1 rgba(59, 59, 59, 255));\n"
                                      "    border-style: outset;\n"
                                      "    border-width: 0.5px;\n"
                                      "    border-color: rgb(255, 75, 75);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    border-style: outset;\n"
                                      "    border-width: 0.5px;\n"
                                      "    border-color: rgb(253, 204, 96);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "color:white;\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.149254 rgba(59, 59, 59, 255), stop:0.328358 rgba(60, 60, 60, 255), stop:0.517413 rgba(68, 68, 68, 255), stop:0.716418 rgba(80, 80, 80, 255), stop:1 rgba(115, 115, 115, 255));\n"
                                        "border-style: outset;\n"
                                        "border-width: 0px;\n"
                                        "width:65;\n"
                                        "height:40;\n"
                                        "font: 9.5pt \"Calibri\";\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi()
        self.pushButton.clicked.connect(sys.exit)  # type: ignore
        self.pushButton_2.clicked.connect(self.accept)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.label_3.setText(_translate("Dialog", "Account"))
        self.label_4.setText(_translate("Dialog", "Warehouse"))
        self.label_5.setText(_translate("Dialog", "Database"))
        self.label_6.setText(_translate("Dialog", "Schema"))
        self.label_7.setText(_translate("Dialog", "DSN"))
        self.checkBox.setText(_translate("Dialog", "Remember Details"))
        self.pushButton.setText(_translate("Dialog", "CANCEL"))
        self.pushButton_2.setText(_translate("Dialog", "LOGIN"))
        self.GetCreds()

    def GetCreds(self):

        data = []
        try:
            filename = str(os.getcwd()) + "\CREDS\CRED_" + str(os.getlogin()).upper() + ".txt"
            file1 = open(filename, "r+")
            numoflines = file1.readlines()
            for line in range(0, len(numoflines)):
                data.append(numoflines[line].split(sep=':')[-1].replace('\n', ''))

            self.lineEdit.setText(data[0])
            self.lineEdit_2.setText(data[1])
            self.lineEdit_3.setText(data[2])
            self.lineEdit_4.setText(data[3])
            self.lineEdit_5.setText(data[4])
            self.lineEdit_6.setText(data[5])
            self.lineEdit_7.setText(data[6])

            file1.close()

        except:
            print("File not found!")

    def SetCreds(self):

        filename = str(os.getcwd()) + "\CREDS\CRED_" + str(os.getlogin()).upper() + ".txt"
        line = ''
        try:
            if self.checkBox.isChecked():
                line = 'username:' + self.lineEdit.text() + '\n'
                line = line + 'password:' + self.lineEdit_2.text() + '\n'
                line = line + 'account:' + self.lineEdit_3.text() + '\n'
                line = line + 'warehouse:' + self.lineEdit_4.text() + '\n'
                line = line + 'database:' + self.lineEdit_5.text() + '\n'
                line = line + 'schema:' + self.lineEdit_6.text() + '\n'
                line = line + 'dsn:' + self.lineEdit_7.text() + '\n'

                file1 = open(filename, "w")
                file1.write(line)
                file1.close()

                self.creds.append(self.lineEdit.text())
                self.creds.append(self.lineEdit_2.text())
                self.creds.append(self.lineEdit_3.text())
                self.creds.append(self.lineEdit_4.text())
                self.creds.append(self.lineEdit_5.text())
                self.creds.append(self.lineEdit_6.text())
                self.creds.append(self.lineEdit_7.text())
            else:
                self.creds.append(self.lineEdit.text())
                self.creds.append(self.lineEdit_2.text())
                self.creds.append(self.lineEdit_3.text())
                self.creds.append(self.lineEdit_4.text())
                self.creds.append(self.lineEdit_5.text())
                self.creds.append(self.lineEdit_6.text())
                self.creds.append(self.lineEdit_7.text())
        except:
            print('File not found')
        self.accept()

    def GetInput(self):
        return self.creds


   class Ui_FilterDialog(QDialog):
    def __init__(self, parent=None):
        super(Ui_FilterDialog, self).__init__(parent)
        self.setObjectName("Dialog")
        self.resize(396, 480)
        self.Filters = []
        self.setStyleSheet("background-color: rgb(39, 39, 47);")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(55, 55, 64);")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "color:white;\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.149254 rgba(59, 59, 59, 255), stop:0.328358 rgba(60, 60, 60, 255), stop:0.517413 rgba(68, 68, 68, 255), stop:0.716418 rgba(80, 80, 80, 255), stop:1 rgba(115, 115, 115, 255));\n"
                                    "border-style: outset;\n"
                                    "border-width: 0px;\n"
                                    "width:60;\n"
                                    "height:30;\n"
                                    "}\n"
                                    "QLineEdit:hover {\n"
                                    "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0248756 rgba(115, 115, 115, 255), stop:0.353234 rgba(80, 80, 80, 255), stop:0.547264 rgba(68, 68, 68, 255), stop:0.781095 rgba(60, 60, 60, 255), stop:1 rgba(59, 59, 59, 255));\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.listWidget = QtWidgets.QListWidget(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget.addItem(item)
        self.verticalLayout_2.addWidget(self.listWidget)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(10, 2, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_1 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("QPushButton{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.149254 rgba(59, 59, 59, 255), stop:0.328358 rgba(60, 60, 60, 255), stop:0.517413 rgba(68, 68, 68, 255), stop:0.716418 rgba(80, 80, 80, 255), stop:1 rgba(115, 115, 115, 255));\n"
                                        "border-style: outset;\n"
                                        "border-width: 0px;\n"
                                        "width:63;\n"
                                        "height:40;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0248756 rgba(115, 115, 115, 255), stop:0.353234 rgba(80, 80, 80, 255), stop:0.547264 rgba(68, 68, 68, 255), stop:0.781095 rgba(60, 60, 60, 255), stop:1 rgba(59, 59, 59, 255));\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 0.5px;\n"
                                        "    border-color: rgb(255, 75, 75);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 0.5px;\n"
                                        "    border-color: rgb(253, 204, 96);\n"
                                        "}")
        self.pushButton_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/whiteIcons/featherwhite/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1.setIcon(icon)
        self.pushButton_1.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.149254 rgba(59, 59, 59, 255), stop:0.328358 rgba(60, 60, 60, 255), stop:0.517413 rgba(68, 68, 68, 255), stop:0.716418 rgba(80, 80, 80, 255), stop:1 rgba(115, 115, 115, 255));\n"
                                        "border-style: outset;\n"
                                        "border-width: 0px;\n"
                                        "width:63;\n"
                                        "height:40;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0248756 rgba(115, 115, 115, 255), stop:0.353234 rgba(80, 80, 80, 255), stop:0.547264 rgba(68, 68, 68, 255), stop:0.781095 rgba(60, 60, 60, 255), stop:1 rgba(59, 59, 59, 255));\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 0.5px;\n"
                                        "    border-color: rgb(255, 255, 0);\n"
                                        "    border-color: rgb(0, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 0.5px;\n"
                                        "    border-color: rgb(253, 204, 96);\n"
                                        "}")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/whiteIcons/featherwhite/rotate-ccw.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.149254 rgba(59, 59, 59, 255), stop:0.328358 rgba(60, 60, 60, 255), stop:0.517413 rgba(68, 68, 68, 255), stop:0.716418 rgba(80, 80, 80, 255), stop:1 rgba(115, 115, 115, 255));\n"
                                        "border-style: outset;\n"
                                        "border-width: 0px;\n"
                                        "width:63;\n"
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
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/whiteIcons/featherwhite/arrow-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi()
        self.pushButton_1.clicked.connect(self.close) # type: ignore
        self.pushButton_3.clicked.connect(self.accept)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Filter"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "All"))
        self.listWidget.setSortingEnabled(__sortingEnabled)

    def SetFilters(self):

        for i in range(0, self.listWidget.count()):
            item = self.listWidget.item(i)
            if item.checkState():
                self.Filters.append(item.text())
