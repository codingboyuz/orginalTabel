from PyQt5.QtWidgets import *
from PyQt5 import QtGui


def warning(title, text, path):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(text)
    msg.setWindowTitle(title)
    msg.setWindowIcon(QtGui.QIcon(path))
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    return msg

def info(title, text, path):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(text)
    msg.setWindowTitle(title)
    msg.setWindowIcon(QtGui.QIcon(path))
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()