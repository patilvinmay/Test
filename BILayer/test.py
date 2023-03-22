n = 6
student = [4,9,5,3,2,10]

if __name__ == '__main__':
    print(0, end=' ')
    for i in range(1, n):
        t = 0
        for j in range(1, i):
            if student[j] >= student[i]:
                t += 1
        print(t, end=' ')


# import sys
#
# from PyQt5.QtCore import Qt, QMimeData
# from PyQt5.QtGui import QDrag
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QGridLayout, QScrollArea, QMainWindow, QSlider
#
#
# class Stroj:
#
#     def __init__(self, rok, naziv, trajanje):
#         self.rok = rok
#         self.naziv = naziv
#         self.trajanje = trajanje
#
#
# class Button(QPushButton):
#     drag = 0
#
#     def __init__(self, title, parent):
#         super().__init__(title, parent)
#
#     def mouseMoveEvent(self, e):
#
#         if e.buttons() != Qt.LeftButton:
#             return
#
#         mimeData = QMimeData()
#         mimeData.setText(self.text())
#
#         self.drag = QDrag(self)
#         self.drag.setMimeData(mimeData)
#         self.drag.setPixmap(self.grab())
#         self.drag.setHotSpot(self.rect().center())
#
#         dropAction = self.drag.exec_(Qt.MoveAction)
#
#
# class MainWindow(QMainWindow):
#     layout = QGridLayout()
#     btns = []
#     snd = ""
#     i = 0
#     j = 0
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         self.setAcceptDrops(True)
#         self.scroll = QScrollArea()
#         self.widget = QWidget()
#         self.drag = QDrag(self)
#
#         SL = []
#         for x in range(30):
#             self.btns.append(x)
#
#         for x in range(30):
#
#             self.btns[x] = Button(str(x), self)
#             self.btns[x].setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
#             self.layout.addWidget(self.btns[x], self.i, self.j)
#             if(self.j > 5):
#                 self.j = 0
#                 self.i += 1
#             else:
#                 self.j += 1
#
#         self.widget.setLayout(self.layout)
#         self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
#         self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
#         self.scroll.setWidgetResizable(True)
#         self.scroll.setWidget(self.widget)
#
#         self.setCentralWidget(self.scroll)
#
#         self.setWindowTitle('Raspored')
#         self.setGeometry(350, 75, 950, 750)
#
#     def dragEnterEvent(self, e):
#         e.accept()
#
#     def dragMoveEvent(self, e):
#         source = e.source()
#         target = QApplication.widgetAt(self.mapToGlobal(e.pos()))
#         print(source)
#         print(target)
#         if (isinstance(e.source(), Button) and isinstance(target, Button) and target != source):
#             e.accept()
#         else:
#             e.ignore()
#
#     def dropEvent(self, e):
#         source = e.source()
#         target = QApplication.widgetAt(self.mapToGlobal(e.pos()))
#         if (not isinstance(source, Button) or not isinstance(target, Button)
#                 or target == source):
#             return
#         layout = self.widget.layout()
#
#         sourceIndex = layout.indexOf(source)
#         sourcePos = layout.getItemPosition(sourceIndex)
#
#         targetIndex = layout.indexOf(target)
#         targetPos = layout.getItemPosition(targetIndex)
#
#         layout.addWidget(source, *targetPos)
#         layout.addWidget(target, *sourcePos)
#
#         e.accept()
#
#
# def main():
#
#     app = QApplication(sys.argv)
#     main = MainWindow()
#     main.show()
#     app.exec_()
#
#
# if __name__ == '__main__':
#     main()