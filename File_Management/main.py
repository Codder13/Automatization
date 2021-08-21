import os
import shutil
import pywintypes
from win10toast import ToastNotifier


download_path = "C:\\Users\\Denis\\Downloads\\"

s = os.chdir(download_path)

current = os.getcwd()

files = os.listdir(current)

images = [".jpeg", ".png", ".jpg", ".gif", ".jfif", ".webp"]  # extensions for images
text = [".doc", ".txt", ".pdf", ".xlsx", ".docx", ".xls", ".rtf", ".md"]  # extensions for text files
videos = [".mp4", ".mkv"]  # extensions for videos
sounds = [".mp3", ".wav", ".m4a"]  # extensions for sounds
applications = [".exe", ".lnk", ".msi"]  # extensions for applications
codes = [".c", ".java", ".py", ".cpp", ".js", ".html", ".css", ".php"]  # extensions for codes
zip_files = [".zip"]
folders = [".Folders", ".Installers", ".Music", ".Other", ".Random Code", ".Saved Pictures", ".Saved Videos", ".Text",
           ".Zip Files"]

toast = ToastNotifier()
toast.show_toast("File Organizer", "The process has been started", duration=30)


os.chdir(download_path)

print("Sorting the files...")

for file in files:
    destination = ""
    for ex in images:
        if file.endswith(ex):
            destination = os.path.join(download_path, ".Saved Pictures")
            shutil.move(file, destination)
            break

    for ex in text:
        if file.endswith(ex):
            destination = os.path.join(download_path, ".Text")
            shutil.move(file, destination)
            break

    for ex in sounds:
        if file.endswith(ex):
            destination = os.path.join(download_path, ".Music")
            shutil.move(file, destination)
            break

    for ex in videos:
        if file.endswith(ex):
            destination =  os.path.join(download_path, ".Saved Videos")
            shutil.move(file, destination)
            break

    for ex in applications:
        if file.endswith(ex):
            destination = os.path.join(download_path, ".Installers")
            shutil.move(file, destination)
            break

    for ex in codes:
        if file.endswith(ex):
            destination = os.path.join(download_path, ".Random Code")
            shutil.move(file, destination)
            break

    for ex in zip_files:
        if file.endswith(ex):
            destination = os.path.join(download_path, ".Zip Files")
            shutil.move(file, destination)
            break
    if os.path.isfile(file):
        if destination == "":
            shutil.move(file, os.path.join(download_path, ".Other"))

    if os.path.isdir(file):
        if file not in folders:
            shutil.move(file, os.path.join(download_path, ".Folders"))

print("Sorting Completed...")
