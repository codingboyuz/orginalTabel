from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore

import functionTabel


class appNocome(QWidget):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        QWidget.__init__(self)
        width = 500
        heigth = 500
        self.setFixedSize(width, heigth)
        self.resize(500, 500)
        self.setWindowIcon(QtGui.QIcon('config/logo.png'))
        self.setWindowTitle("Istisno holatlarni belgilang")
        self.refreshWorkers = QPushButton("OK")
        self.refreshWorkers.clicked.connect(self.appNocome)
        layout = QVBoxLayout()
        layout.addWidget(self.refreshWorkers)

        self.setLayout(layout)
    def appNocome(self):
        self.close()
        functionTabel.gotonewapplication()
        self.switch_window.emit()
