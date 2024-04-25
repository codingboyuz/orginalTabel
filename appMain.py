import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
import appMonth
import test

import function
import functionLate
import functionNocome
import functionOntime
import functionTabel
import functionUpdateworkers


class DialogApp(QWidget):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        QWidget.__init__(self)
        width = 500
        heigth = 500
        self.setFixedSize(width, heigth)
        self.resize(500, 500)
        self.setWindowIcon(QtGui.QIcon('config/logo.png'))
        self.setWindowTitle("Innovatsiya texnologiyalar markazi MChJ")
        self.calendar = QCalendarWidget(self)
        self.calendar.setGeometry(50, 50, 50, 50)
        self.refreshWorkers = QPushButton("Ишчиларни янгилаш")
        self.refreshWorkers.clicked.connect(functionUpdateworkers.get_new_workers)

        self.checkLate = QPushButton("Кеч қолганлар (pdf)")

        self.checkLate.clicked.connect(functionLate.get_checked_late)

        self.checkCome = QPushButton("Келмаганлар (pdf)")
        self.checkCome.clicked.connect(functionNocome.get_checked_come)

        self.timeCome = QPushButton("Вақтида келганлар (pdf)")
        self.timeCome.clicked.connect(functionOntime.get_checked_timecome)

        self.tabel = QPushButton("Табелни шакллантириш")
        self.tabel.clicked.connect(self.appMain)



        layout = QVBoxLayout()
        layout.addWidget(self.refreshWorkers)
        layout.addWidget(self.calendar)
        layout.addWidget(self.checkLate)
        layout.addWidget(self.checkCome)
        layout.addWidget(self.timeCome)
        layout.addWidget(self.tabel)
        self.setLayout(layout)

    def appMain(self):
        self.switch_window.emit()

    def selectDate(self):
        date = self.calendar.selectedDate()
        return date
