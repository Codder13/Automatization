from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import sys
from SorterPyqt import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(744, 269)
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
        self.sort.setGeometry(QtCore.QRect(290, 200, 181, 41))
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

        self.savedPaths = QtWidgets.QComboBox(self.frame)
        self.savedPaths.setGeometry(QtCore.QRect(130, 150, 161, 31))
        self.savedPaths.setObjectName("savedPaths")
        self.savedPaths.addItem("")

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 111, 31))
        self.label_4.setObjectName("label_4")

        self.save_path = QtWidgets.QPushButton(self.frame)
        self.save_path.setGeometry(QtCore.QRect(620, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save_path.setFont(font)
        self.save_path.setCheckable(False)
        self.save_path.setObjectName("save_path")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.sort.clicked.connect(self.sort_func)
        self.browseBt.clicked.connect(self.setPath)
        self.save_path.clicked.connect(self.add_saved_path)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FIle Organizer"))
        self.label_2.setText(_translate("MainWindow", "File Organizer"))
        self.label_3.setText(_translate("MainWindow", "Path to folder :"))
        self.sort.setText(_translate("MainWindow", "Sort"))
        self.browseBt.setText(_translate("MainWindow", "Browse.."))
        self.savedPaths.setItemText(0, _translate("MainWindow", "Custom"))
        self.label_4.setText(_translate("MainWindow", "Saved paths :"))
        self.save_path.setText(_translate("MainWindow", "Save path"))

    def getPath(self):
        return self.path.text()

    def setPath(self):
        self.browsedPath = browse()
        self.path.setText(self.browsedPath)

    def sort_func(self):
        DOWNLOAD_PATH = self.getPath()
        try:
            os.chdir(DOWNLOAD_PATH)
            create_folders(DOWNLOAD_PATH)
            create_ext_file(DOWNLOAD_PATH)
            EXT_FILE = create_mapping(DOWNLOAD_PATH)
            sorter(DOWNLOAD_PATH, EXT_FILE)
        except OSError:
            popUpWarning()

    def add_saved_path(self):
        pass


def browse():
    try:
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        options |= QFileDialog.DontUseCustomDirectoryIcons

        dialog = QFileDialog()
        dialog.setOptions(options)

        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            path = dialog.selectedFiles()[0]  # returns a list
            return path
        else:
            return ''
    except TypeError:
        pass


def popUpWarning():
    font = QtGui.QFont()
    font.setFamily("Calibri")
    font.setPointSize(13)

    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(os.path.join(RESOURCES, "icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    warning = QMessageBox()
    warning.setWindowTitle('Invalid path')
    warning.setWindowIcon(icon)
    warning.setFont(font)
    warning.setText("You need to chose a valid path.")
    warning.setIcon(QMessageBox.Information)

    warning.exec_()
