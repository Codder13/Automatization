import os
import shutil



download_path = "C:\\Users\\Denis\\Desktop\\Downloads\\"

s = os.chdir(download_path)

current = os.getcwd()

files = os.listdir(current)

images = [".jpeg", ".png", ".jpg", ".gif", ".jfif"]  # extensions for images
text = [".doc", ".txt", ".pdf", ".xlsx", ".docx", ".xls", ".rtf", ".md"]  # extensions for text files
videos = [".mp4", ".mkv"]  # extensions for videos
sounds = [".mp3", ".wav", ".m4a"]  # extensions for sounds
applications = [".exe", ".lnk", ".msi"]  # extensions for applications
codes = [".c", ".java", ".py", ".cpp", ".js", ".html", ".css", ".php"]  # extensions for codes
zip_files = [".zip"]
folders = [".Folders", ".Installers", ".Music", ".Other", ".Random Code", ".Saved Pictures", ".Saved Videos", ".Text",
           ".Zip Files"]

extensions = [images, text, videos, sounds, applications, codes, zip_files]

dict = {".Saved Pictures": extensions[0], ".Text": extensions[1],
        ".Saved Videos": extensions[2], ".Music": extensions[3],
        ".Installers": extensions[4], ".Random Code": extensions[5],
        ".Zip Files": extensions[6]}


keys_list = list(dict.keys())

print("Sorting the files...")

for file in files:
    destination = ""

    for i in range(len(keys_list)):
        for ex in dict[keys_list[i]]:
            if file.endswith(ex):
                destination = os.path.join(download_path, keys_list[i])

                if os.path.isfile(os.path.join(destination, file)):
                    shutil.move(file, os.path.join(download_path, ".Other\\.Duplicates"))

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

