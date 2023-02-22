import sys
from PyQt5.QtWidgets import QComboBox, QListWidget, QMainWindow
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5 import QtCore, QtGui, QtWidgets
# import ConTest as ct
import resource_rc


class CheckableComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self._changed = False

        self.view().pressed.connect(self.handleItemPressed)

    def setItemChecked(self, index, checked=False):
        item = self.model().item(index, self.modelColumn())  # QStandardItem object

        if checked:
            item.setCheckState(Qt.Checked)
        else:
            item.setCheckState(Qt.Unchecked)

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)

        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)
        self._changed = True

    def hidePopup(self):
        if not self._changed:
            super().hidePopup()
        self._changed = False

    def itemChecked(self, index):
        item = self.model().item(index, self.modelColumn())
        return item.checkState() == Qt.Checked


class CheckableListWidgt(QListWidget):
    def __init__(self):
        super().__init__()
        self._changed = False

        self.clicked.connect(self.handleItemPressed)

    # def setItemChecked(self, index, checked=False):
    #     item = self.model().item(index, self.modelColumn()) # QStandardItem object
    #
    #     if checked:
    #         item.setCheckState(Qt.Checked)
    #     else:
    #         item.setCheckState(Qt.Unchecked)

    def handleItemPressed(self, index):

        item = self.itemFromIndex(index)

        if self.currentRow() == 0:
            if item.checkState() == Qt.Checked:
                item.setCheckState(Qt.Unchecked)
                for i in range(self.count()):
                    self.item(i).setCheckState(Qt.Unchecked)
            else:
                item.setCheckState(Qt.Checked)
                for i in range(self.count()):
                    self.item(i).setCheckState(Qt.Checked)
        else:
            if item.checkState() == Qt.Checked:
                item.setCheckState(Qt.Unchecked)
                self.item(0).setCheckState(Qt.Unchecked)
            else:
                item.setCheckState(Qt.Checked)
                flg = False
                for i in range(1, self.count()):
                    if self.item(i).checkState() == Qt.Checked:
                        flg = True
                    else:
                        flg = False
                        break
                if flg:
                    self.item(0).setCheckState(Qt.Checked)
                else:
                    self.item(0).setCheckState(Qt.Unchecked)
        self._changed = True

    # def hidePopup(self):
    #     if not self._changed:
    #         super().hidePopup()
    #     self._changed = False

    # def itemChecked(self, index):
    #     item = self.model().item(index, self.modelColumn())
    #     return item.checkState() == Qt.Checked


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


class Ui_QueryWindow(object):
    def setupUi(self, QueryWindow):
        QueryWindow.setObjectName("QueryWindow")
        QueryWindow.resize(500, 900)

        self.centralwidget = QtWidgets.QWidget(QueryWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 476, 776))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        self.CtextEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.CtextEdit.setFont(font)
        self.CtextEdit.setObjectName("CtextEdit")
        self.verticalLayout.addWidget(self.CtextEdit)

        self.TtextEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.TtextEdit.setObjectName("TtextEdit")
        self.verticalLayout.addWidget(self.TtextEdit)

        self.FtextEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.FtextEdit.setObjectName("FtextEdit")
        self.verticalLayout.addWidget(self.FtextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        QueryWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(QueryWindow)
        QtCore.QMetaObject.connectSlotsByName(QueryWindow)

    def retranslateUi(self, QueryWindow):
        _translate = QtCore.QCoreApplication.translate
        QueryWindow.setWindowTitle(_translate("QueryWindow", "QueryWindow"))


class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(416, 324)
        self.creds = []
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(39, 39, 47);\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(4, 4, 4, 4)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("color: white;\n"
                                 "font: 12pt \"Calibri\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(55, 55, 64);\n"
                                    "font: 63 14pt \"Calibri\";\n"
                                    "border-style: none;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("color: white;\n"
                                   "font: 12pt \"Calibri\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(55, 55, 64);\n"
                                      "font: 63 14pt \"Calibri\";\n"
                                      "border-style: none;")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setStyleSheet("color: white;\n"
                                   "font: 12pt \"Calibri\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(55, 55, 64);\n"
                                      "font: 63 14pt \"Calibri\";\n"
                                      "border-style: none;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("color: white;\n"
                                   "font: 12pt \"Calibri\";")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(55, 55, 64);\n"
                                      "font: 63 14pt \"Calibri\";\n"
                                      "border-style: none;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setStyleSheet("color: white;\n"
                                   "font: 12pt \"Calibri\";")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(55, 55, 64);\n"
                                      "font: 63 14pt \"Calibri\";\n"
                                      "border-style: none;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setStyleSheet("color: white;\n"
                                   "font: 12pt \"Calibri\";")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(55, 55, 64);\n"
                                      "font: 63 14pt \"Calibri\";\n"
                                      "border-style: none;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setStyleSheet("color: white;\n"
                                   "font: 12pt \"Calibri\";")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(55, 55, 64);\n"
                                      "font: 63 14pt \"Calibri\";\n"
                                      "border-style: none;")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)

        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "color: white;\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(lambda: MainWindow.close())
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "color: white;\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.149254 rgba(59, 59, 59, 255), stop:0.328358 rgba(60, 60, 60, 255), stop:0.517413 rgba(68, 68, 68, 255), stop:0.716418 rgba(80, 80, 80, 255), stop:1 rgba(115, 115, 115, 255));\n"
                                      "border-style: outset;\n"
                                      "border-width: 0px;\n"
                                      "width:50;\n"
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
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.SetCreds)
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 8)
        self.verticalLayout.setStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def SetCreds(self):

        line = ''
        try:
            line = 'username:' + self.lineEdit.text() + '\n'
            line = line + 'password:' + self.lineEdit_2.text() + '\n'
            line = line + 'account:' + self.lineEdit_3.text() + '\n'
            line = line + 'warehouse:' + self.lineEdit_4.text() + '\n'
            line = line + 'database:' + self.lineEdit_5.text() + '\n'
            line = line + 'role:' + self.lineEdit_6.text() + '\n'
            line = line + 'dsn:' + self.lineEdit_7.text() + '\n'

            file1 = open("Creds.txt", "w")
            file1.write(line)
            file1.close()

            self.creds.append(self.lineEdit.text())
            self.creds.append(self.lineEdit_2.text())
            self.creds.append(self.lineEdit_3.text())
            self.creds.append(self.lineEdit_4.text())
            self.creds.append(self.lineEdit_5.text())
            self.creds.append(self.lineEdit_6.text())
            self.creds.append(self.lineEdit_7.text())
        except:
            print('File not found')

        self.pushButton_2.click()

    def GetCreds(self):

        data = []
        try:
            file1 = open("Creds.txt", "r+")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "Account"))
        self.label_4.setText(_translate("MainWindow", "Warehouse"))
        self.label_5.setText(_translate("MainWindow", "Database"))
        self.label_6.setText(_translate("MainWindow", "Role"))
        self.label_7.setText(_translate("MainWindow", "DSN"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.GetCreds()
