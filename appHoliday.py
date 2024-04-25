from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
class holidayApp(QWidget):
    switch_window = QtCore.pyqtSignal()
    def __init__(self, text):
        QWidget.__init__(self)
        width = 500
        heigth = 500
        self.setFixedSize(width, heigth)
        self.resize(500, 500)
        self.setWindowIcon(QtGui.QIcon('config/logo.png'))
        self.setWindowTitle("Bayram kunlarini belgilang")
        # self.label =
        self.refreshWorkers = QPushButton("OK" + text)
        self.refreshWorkers.clicked.connect(self.holidayApp)

        layout = QVBoxLayout()
        layout.addWidget(self.refreshWorkers)
        self.setLayout(layout)
    def holidayApp(self):
        self.switch_window.emit()