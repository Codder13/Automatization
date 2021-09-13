import os
import shutil
import pywintypes
from win10toast import ToastNotifier
import getpass

UserName = getpass.getuser()
download_path = f"C:\\Users\\{UserName}\\Downloads\\"



s = os.chdir(download_path)

current = os.getcwd()

files = os.listdir(current)

folders = [".Folders", ".Installers", ".Music", ".Other", ".Random Code", ".Saved Pictures", ".Saved Videos", ".Text",
           ".Zip Files"]

for folder in folders:
    if folder not in files:
        os.mkdir(os.path.join(download_path, folder))

Folder_files = os.listdir(os.path.join(download_path, ".Folders"))

ext_file = "Extensions_file.txt"

if ext_file not in Folder_files:
    with open(os.path.join(download_path, ".Folders\\Extensions_file.txt"), 'a') as ex_file:
        ex_file.write(
            "images = .jpeg, .png, .jpg, .gif, .jfif\ntext = .doc, .txt, .pdf, .xlsx, .docx, .xls, .rtf, .md\n"
            "videos = .mp4, .mkv, .webp, .webm\nsounds = .mp3, .wav, .m4a\napplications = .exe, .lnk, .msi\n"
            "codes = .c, .java, .py, .cpp, .js, .html, .css, .php, .rar\nzip_files = .zip"
        )


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


dict = {".Saved Pictures": extensions[0], ".Text": extensions[1],
        ".Saved Videos": extensions[2], ".Music": extensions[3],
        ".Installers": extensions[4], ".Random Code": extensions[5],
        ".Zip Files": extensions[6]}

keys_list = list(dict.keys())

toast = ToastNotifier()
toast.show_toast("File Organizer", "The process has been started",
                 'C:\\Users\\Denis\\Programing\\.GitHub_Programing\\GithHub_Automatization\\File_Management\\Organizer.ico')


os.chdir(download_path)

print("Sorting the files...")

for file in files:
    destination = ""

    for i in range(len(keys_list)):
        for ex in dict[keys_list[i]]:
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
        if file not in folders:
            shutil.move(file, os.path.join(download_path, ".Folders"))

print("Sorting Completed...")

toast.show_toast("File Organizer", "Finished organizing",
                 'C:\\Users\\Denis\\Programing\\.GitHub_Programing\\GithHub_Automatization\\File_Management\\Organizer.ico')
