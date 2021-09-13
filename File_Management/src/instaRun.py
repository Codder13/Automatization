import getpass
import os
import shutil
from win10toast import ToastNotifier

USER_NAME = getpass.getuser()
DOWNLOAD_PATH = f"C:\\Users\\{USER_NAME}\\Downloads\\"
FOLDERS = [".Folders", ".Installers", ".Music", ".Other", ".Random Code", ".Saved Pictures", ".Saved Videos", ".Text",
           ".Zip Files"]


toast = ToastNotifier()
os.chdir(DOWNLOAD_PATH)
current = os.getcwd()
files = os.listdir(current)


def toastNotifier(message):
    toast.show_toast("File Organizer", message,
                     'C:\\Users\\Denis\\Programing\\.GitHub_Programing\\' +
                     'GithHub_Automatization\\File_Management\\resources\\Organizer.ico', 2)


def setup(download_path):
    create_folders(download_path)
    create_ext_file(download_path)


def create_folders(download_path):
    for folder in FOLDERS:
        if folder not in files:
            os.mkdir(os.path.join(download_path, folder))


def create_ext_file(download_path):
    Folder_files = os.listdir(os.path.join(download_path, ".Folders"))
    ext_file = "../resources/Extensions_file.txt"
    if ext_file not in Folder_files:
        with open(os.path.join(download_path, ".Folders\\Extensions_file.txt"), 'a') as ex_file:
            ex_file.write(
                "images = .jpeg, .png, .jpg, .gif, .jfif\ntext = .doc, .txt, .pdf, .xlsx, .docx, .xls, .rtf, .md\n"
                "videos = .mp4, .mkv, .webp, .webm\nsounds = .mp3, .wav, .m4a\napplications = .exe, .lnk, .msi\n"
                "codes = .c, .java, .py, .cpp, .js, .html, .css, .php, .rar\nzip_files = .zip, .rar, .7z"
            )


def create_mapping(download_path):
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
    os.chdir(download_path)
    print("Sorting the files...")
    keys_list = list(ext_dict.keys())

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


def main(download_path):
    setup(download_path)
    dicto = create_mapping(download_path)
    sorter(download_path, dicto)


if __name__ == '__main__':
    main(DOWNLOAD_PATH)
