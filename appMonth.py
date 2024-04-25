from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
class monthApp(QWidget):
    switch_window = QtCore.pyqtSignal(str)
    def __init__(self):
        QWidget.__init__(self)
        width = 300
        heigth = 200
        self.setFixedSize(width, heigth)
        self.resize(500, 500)
        self.setWindowIcon(QtGui.QIcon('config/logo.png'))
        self.setWindowTitle("Oyni tanlang")
        self.monthBox = QComboBox(self)
        month_list = ['Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'Iyun', 'Iyul', 'Avgust', 'Sentabr', 'Oktabr', 'Noyabr', 'Dekabr']
        self.monthBox.addItems(month_list)
        self.refreshWorkers = QPushButton("OK")
        self.refreshWorkers.clicked.connect(self.monthApp)
        layout = QVBoxLayout()
        layout.addWidget(self.monthBox)
        layout.addWidget(self.refreshWorkers)
        self.setLayout(layout)
    def monthApp(self):
        self.switch_window.emit(str(self.monthBox.currentIndex()))

