import os

Folder_files = os.listdir("C:\\Users\\Denis\\Desktop\\Downloads\\.Folders\\")

ext_file = "Extensions_file.txt"

if ext_file not in Folder_files:
    with open(ext_file, 'a') as ex_file:
        ex_file.write(
            "images = .jpeg, .png, .jpg, .gif, .jfif\ntext = .doc, .txt, .pdf, .xlsx, .docx, .xls, .rtf, .md\n"
            "videos = .mp4, .mkv, .webp, .webm\nsounds = .mp3, .wav, .m4a\napplications = .exe, .lnk, .msi\n"
            "codes = .c, .java, .py, .cpp, .js, .html, .css, .php, .rar\nzip_files = .zip"
        )

