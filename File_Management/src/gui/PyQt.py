import atexit

from SorterPyqt import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(744, 281)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(ICON), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.label.setPixmap(QtGui.QPixmap(ICON))
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

        self.delete_path = QtWidgets.QPushButton(self.frame)
        self.delete_path.setGeometry(QtCore.QRect(620, 180, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delete_path.setFont(font)
        self.delete_path.setCheckable(False)
        self.delete_path.setObjectName("delete_path")

        self.set_default = QtWidgets.QPushButton(self.frame)
        self.set_default.setGeometry(QtCore.QRect(129, 190, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_default.setFont(font)
        self.set_default.setCheckable(False)
        self.set_default.setObjectName("set_default")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 744, 21))
        self.menuBar.setObjectName("menuBar")

        self.menuTask = QtWidgets.QMenu(self.menuBar)
        self.menuTask.setObjectName("menuTask")

        MainWindow.setMenuBar(self.menuBar)

        create_config_file()

        self.actionActivate_Task = QtWidgets.QAction(MainWindow)
        self.actionActivate_Task.setCheckable(True)
        self.actionActivate_Task.setObjectName("actionActivate_Task")
        self.menuTask.addAction(self.actionActivate_Task)
        self.menuBar.addAction(self.menuTask.menuAction())
        self.actionActivate_Task.setChecked(is_checked(CONFIG_LOCATION))

        self.k = int(config.get(TASK_ACTIVE, 'count'))
        self.isChecked = None

        self.sort.clicked.connect(self.sort_func)
        self.browseBt.clicked.connect(self.setPath)
        self.save_path.clicked.connect(self.show_dialog)
        self.delete_path.clicked.connect(self.delete_path_func)
        self.savedPaths.activated.connect(self.set_combo_path)
        self.set_default.clicked.connect(self.set_default_path)

        self.retranslateUi(MainWindow)
        self.updateComboBox()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        atexit.register(self.when_checked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FIle Organizer"))
        self.label_2.setText(_translate("MainWindow", "File Organizer"))
        self.label_3.setText(_translate("MainWindow", "Path to folder :"))
        self.sort.setText(_translate("MainWindow", "Sort"))
        self.browseBt.setText(_translate("MainWindow", "Browse.."))
        self.label_4.setText(_translate("MainWindow", "Saved paths :"))
        self.save_path.setText(_translate("MainWindow", "Save path"))
        self.delete_path.setText(_translate("MainWindow", "Delete path"))
        self.set_default.setText(_translate("MainWindow", "Set Default Path"))
        self.menuTask.setTitle(_translate("MainWindow", "Task"))
        self.actionActivate_Task.setText(_translate("MainWindow", "Activate Task"))
        self.actionActivate_Task.setShortcut(_translate("MainWindow", "Ctrl+T"))

    def set_default_path(self):
        path = self.path.text()
        self.savedPaths.setItemData(1, path)
        config.set(DEFAULT_PATH, 'path', path)
        write_in_config()

    def when_checked(self):
        if self.actionActivate_Task.isChecked() and self.k == 0:
            self.isChecked = 'True'
            self.k += 1
            create_schedule()

            config.set(TASK_ACTIVE, 'count', str(self.k))
            config.set(TASK_ACTIVE, 'bool', self.isChecked)
        elif not self.actionActivate_Task.isChecked() and self.k == 1:
            self.isChecked = 'False'
            self.k -= 1
            delete_schedule()

            config.set(TASK_ACTIVE, 'count', str(self.k))
            config.set(TASK_ACTIVE, 'bool', self.isChecked)

        write_in_config()

    def getPath(self):
        return self.path.text()

    def setPath(self):
        self.browsedPath = browse()
        self.path.setText(self.browsedPath)

    def sort_func(self):
        download_path = self.getPath()
        try:
            os.chdir(download_path)
            create_folders(download_path)
            create_ext_file(download_path)
            ext_file = create_mapping(download_path)
            sorter(download_path, ext_file)
        except OSError:
            popUpWarning()

    def show_dialog(self):
        Dialog.show()
        path = self.path.text()
        ui_dialog.set_path(path)

    def add_saved_paths(self, name):
        self.savedPaths.addItem(name)

    def updateComboBox(self):
        self.savedPaths.clear()
        self.savedPaths.addItem('Custom')
        self.savedPaths.addItem('Default')
        path_dict, name_list, path_list = create_path_dict(CONFIG_LOCATION)
        for i in range(len(path_dict)):
            self.savedPaths.addItem(name_list[i], path_list[i])

        default_path = config.get(DEFAULT_PATH, 'path')
        self.savedPaths.setItemData(1, default_path)


    def set_combo_path(self, index):
        path = self.savedPaths.itemData(index)
        self.path.setText(path)

    def delete_path_func(self):
        index = self.savedPaths.currentIndex()
        _, name_list, _ = create_path_dict(CONFIG_LOCATION)
        try:
            if index > 2:
                combo_name = name_list[index - 1]
                config.remove_option(SAVED_PATHS, combo_name)
            else:
                config.set(DEFAULT_PATH, 'path', '')

            write_in_config()
            self.path.setText('')
            self.savedPaths.clear()
            self.savedPaths.addItem('Custom')
            self.savedPaths.addItem('Default')
            self.updateComboBox()

        except IndexError:
            pass


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(561, 209)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(ICON)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.dialog_name.setText("")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 51, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.ok_cancel.accepted.connect(lambda: self.save_path(Dialog))
        self.ok_cancel.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Set Name for Path"))
        self.label.setText(_translate("Dialog", "Path:"))
        self.label_2.setText(_translate("Dialog", "Name:"))

    def save_path(self, Dialog):
        self.path = self.dialog_path.text()
        self.name = self.dialog_name.text()

        config_dict, _, _ = create_path_dict(CONFIG_LOCATION)
        values_list = [v for k, v in config_dict.items()]

        if os.path.exists(self.path) and self.path not in values_list:
            config.set(SAVED_PATHS, self.name, self.path)
            ui_main.add_saved_paths(self.name)
            with open(CONFIG_LOCATION, 'w') as f:
                config.write(f)
            ui_main.updateComboBox()
        else:
            popUpWarning()

        Dialog.close()

    def set_path(self, path):
        self.dialog_path.setText(path)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_main = Ui_MainWindow()
    ui_main.setupUi(MainWindow)
    MainWindow.show()

    Dialog = QtWidgets.QDialog()
    ui_dialog = Ui_Dialog()
    ui_dialog.setupUi(Dialog)

    sys.exit(app.exec_())
