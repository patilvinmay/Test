import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QPushButton, QWidget, QHBoxLayout, QLabel, QListWidgetItem, QVBoxLayout

class ItemWidget(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(1, 1, 1, 1)
        layout.setSpacing(2)

        self.label = QLabel(text, self)  # Set the label text here
        layout.addWidget(self.label)

        self.delete_button = QPushButton('x', self)  # Set the button text here
        self.delete_button.setFixedWidth(30)
        self.delete_button.setFixedHeight(30)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.delete_button.setFont(font)

        layout.addWidget(self.delete_button)
        layout.setStretch(9, 1)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('List Widget with Delete Button and Label')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Create a QVBoxLayout to hold the list widget
        layout = QVBoxLayout(self.central_widget)

        # Create a QListWidget
        self.list_widget = QListWidget(self)
        layout.addWidget(self.list_widget)

        # Add items to the list widget
        for i in range(5):
            item_text = f'Item {i + 1}'

            # Create a custom widget for each item
            item_widget = ItemWidget(item_text)
            item = QListWidgetItem(self.list_widget)
            item.setSizeHint(item_widget.sizeHint())  # Set the item size hint
            self.list_widget.setItemWidget(item, item_widget)

            # Connect the delete button's click signal to the delete_item method
            # item_widget.delete_button.clicked.connect(self.delete_item)
            item_widget.delete_button.clicked.connect(lambda _, item=item: self.delete_item(item))

    # def delete_item(self):
    #     sender = self.sender()  # Get the button that was clicked
    #     item = self.list_widget.itemAt(sender.pos())
    #     if item:
    #         row = self.list_widget.row(item)
    #         self.list_widget.takeItem(row)

    def delete_item(self, item):
        row = self.list_widget.row(item)
        self.list_widget.takeItem(row)


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
