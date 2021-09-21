import ctypes
import sys
from PyQt import *
from SorterPyqt import *
from dialog_name import Ui_Dialog

myappid = 'file.organizer'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


def mainWindow():
    """
        Sets up the Main Window
    """
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_main = Ui_MainWindow()
    ui_main.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


def DialogWindow():
    """
        Sets up the dialog Window
    """
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


def main():
    mainWindow()
    DialogWindow()


if __name__ == "__main__":
    main()
