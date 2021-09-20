# import ctypes
#
# myappid = 'file.organizer'  # arbitrary string
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow
from PyQt import Ui_MainWindow


# class Main(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.setupUi(self)
#
#     def browse(self):
#         fname = QFileDialog.getOpenFileName(self, 'Open file',
#                                             'c:\\', "Image files (*.jpg *.gif)")
#         data = fname.read()
#         self.textEdit.setText(data)
#         fname.close()


# if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # window = Main()
    # window.show()
    # sys.exit(app.exec_())
