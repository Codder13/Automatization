import os.path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import ctypes
import sys
from SorterPyqt import *

myappid = 'file.organizer'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(744, 269)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(RESOURCES, "icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 741, 241))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(320, 20, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
        self.label_2.setObjectName("label_2")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(270, 20, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(os.path.join(RESOURCES, "icon.ico")))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 121, 31))
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
        self.label_3.setObjectName("label_3")

        self.path = QtWidgets.QLineEdit(self.frame)
        self.path.setGeometry(QtCore.QRect(130, 90, 481, 31))
        self.path.setObjectName("path")

        self.sort = QtWidgets.QPushButton(self.frame)
        self.sort.setGeometry(QtCore.QRect(290, 180, 181, 55))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sort.setFont(font)
        self.sort.setObjectName("sort")

        self.browseBt = QtWidgets.QPushButton(self.frame)
        self.browseBt.setGeometry(QtCore.QRect(620, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.browseBt.setFont(font)
        self.browseBt.setObjectName("browseBt")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionSave_Path = QtWidgets.QAction(MainWindow)
        self.actionSave_Path.setObjectName("actionSave_Path")

        self.actionChange_Mode = QtWidgets.QAction(MainWindow)
        self.actionChange_Mode.setObjectName("actionChange_Mode")

        self.actionSave_Path_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_Path_2.setObjectName("actionSave_Path_2")

        self.sort.clicked.connect(sort)
        self.browseBt.clicked.connect(self.browse)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FIle Organizer"))
        self.label_2.setText(_translate("MainWindow", "File Organizer"))
        self.label_3.setText(_translate("MainWindow", "Path to folder :"))
        self.sort.setText(_translate("MainWindow", "Sort"))
        self.browseBt.setText(_translate("MainWindow", "Browse.."))
        self.actionSave_Path.setText(_translate("MainWindow", "Save Path"))
        self.actionChange_Mode.setText(_translate("MainWindow", "Change Mode"))
        self.actionSave_Path_2.setText(_translate("MainWindow", "Save Path"))
        self.actionSave_Path_2.setShortcut(_translate("MainWindow", "Ctrl+S"))

    def getPath(self):
        return self.path.text()

    def setPath(self, ):
        pass

    def browse(self):
        try:
            filename = QFileDialog.getOpenFileName(None, 'Chose Directory', '.')
            fname = open(filename)
            data = fname.read()
            self.path.setText(data)
            fname.close()
        except TypeError:
            pass


def sort():
    DOWNLOAD_PATH = ui.getPath()
    try:
        os.chdir(DOWNLOAD_PATH)
        create_folders(DOWNLOAD_PATH)
        create_ext_file(DOWNLOAD_PATH)
        EXT_FILE = create_mapping(DOWNLOAD_PATH)
        sorter(DOWNLOAD_PATH, EXT_FILE)
    except OSError:
        popUpWarning()


def popUpWarning():
    font = QtGui.QFont()
    font.setFamily("Calibri")
    font.setPointSize(11)

    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(os.path.join(RESOURCES, "icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    warning = QMessageBox()
    warning.setWindowTitle('Invalid path')
    warning.setWindowIcon(icon)
    warning.setText("You need to chose a valid path.")
    warning.setIcon(QMessageBox.Information)
    warning.setFont(font)

    warning.exec_()


app = QtWidgets.QApplication(sys.argv)

if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

sys.exit(app.exec_())
