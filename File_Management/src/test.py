# import ctypes
#
# myappid = 'file.organizer'  # arbitrary string
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
import os
import getpass

USER_NAME = getpass.getuser()
DOWNLOAD_PATH = f"C:\\Users\\{USER_NAME}\\Downloads\\"


model_file = r"C:\Users\Denis\.organize\resources\Extensions_file.txt"

with open(model_file, 'r') as file:
    extensions = file.read()
    Folder_files = os.listdir(os.path.join(DOWNLOAD_PATH, ".Folders"))
    ext_file = os.path.join(DOWNLOAD_PATH, ".Folders\\Extensions_file.txt")
    if ext_file not in Folder_files:
        with open(ext_file, 'w') as ex_file:
            ex_file.write(extensions)
