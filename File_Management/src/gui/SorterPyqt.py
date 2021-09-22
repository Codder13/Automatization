import getpass
import os
import shutil
from win10toast import ToastNotifier
from configparser import ConfigParser
import ctypes
import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox

"""Variables"""
USER_NAME = getpass.getuser()
DEFAULT_DOWNLOAD_PATH = 'C:\\Users\\Denis\\Desktop\\test'
CONFIG_LOCATION = '../../resources/config.ini'
RESOURCES = f"C:\\Users\\{USER_NAME}\\.organize\\resources\\"
FOLDERS = [".Folders", ".Installers", ".Music", ".Other", ".Random Code", ".Saved Pictures", ".Saved Videos", ".Text",
           ".Zip Files"]
ICON = os.path.join(RESOURCES, 'icon.ico')
"""_________________________________________________________________________________________________________________"""

"""Other stuff"""
toast = ToastNotifier()

config = ConfigParser()
config.read(CONFIG_LOCATION)
SECTION = 'saved_paths'
myappid = 'file.organizer'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

"""_________________________________________________________________________________________________________________"""

"""Library of functions"""


def create_path_dict(config_path):
    config.read(config_path)
    path_dict = dict(config.items('saved_paths'))
    name_list = [x for x, v in path_dict.items()]
    path_list = [v for x, v in path_dict.items()]

    return path_dict, name_list, path_list


def create_config_file():
    """
        Creates the config file
    """
    sections = config.sections()
    section = 'saved_paths'
    if section not in sections:
        config.add_section(section)
        with open('../../resources/config.ini', 'w') as f:
            config.write(f)


def write_in_config():
    """
        This function is the one writing the changes in the config file
    """
    with open(CONFIG_LOCATION, 'w') as f:
        config.write(f)


def toastNotifier(message):
    """
        this one defines the toast notifier(windows notifications)
    """
    toast.show_toast("File Organizer", message, os.path.join(RESOURCES, "icon.ico"), 2)


def setup(download_path):
    """
        this one prepares everything before sorting
    """
    os.chdir(download_path)
    create_folders(download_path)
    create_ext_file(download_path)


def create_folders(download_path):
    """
        creates the necessary folders
    """
    os.chdir(download_path)
    current = os.getcwd()
    files = os.listdir(current)
    for folder in FOLDERS:
        if folder not in files:
            os.mkdir(os.path.join(download_path, folder))


def create_ext_file(download_path):
    """
    creates the extension file
    """
    os.chdir(download_path)
    model_file = os.path.join(RESOURCES, "Extensions_file.txt")
    with open(model_file, 'r') as file:
        extensions = file.read()
    Folder_files = os.listdir(os.path.join(download_path, ".Folders"))
    ext_file = os.path.join(download_path, ".Folders\\Extensions_file.txt")
    if 'Extensions_file.txt' not in Folder_files:
        with open(ext_file, 'w') as ex_file:
            ex_file.write(extensions)


def create_mapping(download_path):
    """
    creates the mapping between the extension and the folders
    """
    os.chdir(download_path)
    with open(os.path.join(download_path, ".Folders\\Extensions_file.txt"), 'r') as file:
        images = file.readline()
        text = file.readline()
        videos = file.readline()
        sounds = file.readline()
        applications = file.readline()
        codes = file.readline()
        zip_files = file.readline()

    extensions = [images, text, videos, sounds, applications, codes, zip_files]

    for i, j in enumerate(extensions):
        j = j.split(', ')
        j[0] = j[0].split('= ')[1]
        j[-1] = j[-1].split('\n')[0]
        extensions[i] = j

    ext_dict = {".Saved Pictures": extensions[0], ".Text": extensions[1],
                ".Saved Videos": extensions[2], ".Music": extensions[3],
                ".Installers": extensions[4], ".Random Code": extensions[5],
                ".Zip Files": extensions[6]}

    return ext_dict


def sorter(download_path, ext_dict):
    """
        sorts the files
    """
    os.chdir(download_path)
    print("Sorting the files...")
    keys_list = list(ext_dict.keys())
    current = os.getcwd()
    files = os.listdir(current)

    for file in files:
        destination = ""

        for i in range(len(keys_list)):
            for ex in ext_dict[keys_list[i]]:
                if file.endswith(ex):
                    destination = os.path.join(download_path, keys_list[i])

                    if os.path.isfile(os.path.join(destination, file)):
                        try:
                            shutil.move(file, os.path.join(download_path, ".Other\\.Duplicates"))
                        except shutil.Error:
                            new_path_file = os.path.join(download_path, ".Other\\.Duplicates")
                            os.rename(file, os.path.join(new_path_file, f"DUP {file}"))
                    else:
                        shutil.move(file, destination)

                    break

        if os.path.isfile(file):
            if destination == "":
                shutil.move(file, os.path.join(download_path, ".Other"))

        if os.path.isdir(file):
            if file not in FOLDERS:
                shutil.move(file, os.path.join(download_path, ".Folders"))

    print("Sorting Completed...")

    toastNotifier("Finished organizing")


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


def main_sorter(download_path):
    setup(download_path)
    dicto = create_mapping(download_path)
    sorter(download_path, dicto)


if __name__ == '__main__':
    main_sorter(DEFAULT_DOWNLOAD_PATH)
