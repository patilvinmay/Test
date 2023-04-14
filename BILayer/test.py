import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices

class MyTable(QTableWidget):
    def __init__(self, data):
        super().__init__()

        self.setColumnCount(len(data.columns))
        self.setRowCount(len(data.index))

        # Add column labels
        for i, column in enumerate(data.columns):
            item = QTableWidgetItem(str(column))
            self.setHorizontalHeaderItem(i, item)

        # Add data to table
        for i in range(len(data.index)):
            for j in range(len(data.columns)):
                cell_data = str(data.iloc[i, j])
                if cell_data.startswith("http"):
                    item = QTableWidgetItem(cell_data)
                    item.setData(Qt.UserRole, QUrl(cell_data))
                else:
                    item = QTableWidgetItem(cell_data)
                self.setItem(i, j, item)

        self.cellDoubleClicked.connect(self.openLink)

    def openLink(self, row, column):
        item = self.item(row, column)
        if item and item.data(Qt.UserRole):
            QDesktopServices.openUrl(item.data(Qt.UserRole))

if __name__ == '__main__':
    app = QApplication([])
    data = pd.DataFrame({
        'Column 1': [1, 2, 3],
        'Column 2': ['http://www.example.com', 'B', 'http://www.google.com'],
        'Column 3': [True, False, True]
    })
    table = MyTable(data)
    table.show()
    app.exec_()
