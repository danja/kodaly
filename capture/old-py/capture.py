# 'ui-images/sf-0-do.png'

import sys
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMainWindow, QApplication, QLabel


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = "Load image in PySide2"
        self.setWindowTitle(self.title)

        label = QLabel(self)
        pixmap = QPixmap('ui-images/sf-0-do.png')
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
