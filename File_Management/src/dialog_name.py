from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from SorterPyqt import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(561, 209)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)

        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 561, 251))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.ok_cancel = QtWidgets.QDialogButtonBox(self.frame)
        self.ok_cancel.setGeometry(QtCore.QRect(380, 170, 161, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.ok_cancel.setFont(font)
        self.ok_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.ok_cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.ok_cancel.setObjectName("ok_cancel")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 20, 41, 31))
        self.label.setObjectName("label")

        self.dialog_path = QtWidgets.QLineEdit(self.frame)
        self.dialog_path.setGeometry(QtCore.QRect(80, 20, 451, 31))
        self.dialog_path.setText("")
        self.dialog_path.setObjectName("dialog_path")

        self.dialog_name = QtWidgets.QLineEdit(self.frame)
        self.dialog_name.setGeometry(QtCore.QRect(80, 100, 161, 31))
        self.dialog_name.setObjectName("dialog_name")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 51, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.ok_cancel.accepted.connect(Dialog.accept)
        self.ok_cancel.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Set Name for Path"))
        self.label.setText(_translate("Dialog", "Path:"))
        self.label_2.setText(_translate("Dialog", "Name:"))


app = QtWidgets.QApplication(sys.argv)

if __name__ == "__main__":
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

sys.exit(app.exec_())
