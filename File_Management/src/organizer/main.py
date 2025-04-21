import getpass
import os
import shutil
import errno
from win10toast import ToastNotifier
import contextlib

USER_NAME = getpass.getuser()
DEFAULT_DOWNLOAD_PATH = f"C:\\Users\\{USER_NAME}\\Downloads\\"
RESOURCES = f"C:\\Users\\{USER_NAME}\\.organize\\resources\\"
FOLDERS = [",Folders", ".Installers", ".Music", ".Other", ".Code", ".Pictures", ".Videos", ".Text",
           ".Zip Files"]

# Ensure resources directory exists
os.makedirs(RESOURCES, exist_ok=True)

toast = ToastNotifier()


def toastNotifier(message):
    icon_path = os.path.join(RESOURCES, "icon.ico")
    # Use default notification if icon doesn't exist
    if not os.path.exists(icon_path):
        icon_path = None
    
    try:
        toast.show_toast("File Organizer", message, icon_path, 2)
    except Exception:
        # Fallback if toast notification fails
        print(f"Notification: {message}")


def setup(download_path):
    create_folders(download_path)
    create_ext_file(download_path)


def create_folders(download_path):
    try:
        # Get current files in download path
        current_files = os.listdir(download_path)
        
        # Create required folders if they don't exist
        for folder in FOLDERS:
            folder_path = os.path.join(download_path, folder)
            if folder not in current_files and not os.path.exists(folder_path):
                os.makedirs(folder_path, exist_ok=True)
        
        # Create .Duplicates folder inside .Other folder
        duplicates_path = os.path.join(download_path, ".Other", ".Duplicates")
        if not os.path.exists(duplicates_path):
            os.makedirs(duplicates_path, exist_ok=True)
    except Exception as e:
        print(f"Error creating folders: {e}")


def create_ext_file(download_path):
    try:
        # Default extensions in case the model file doesn't exist
        default_extensions = """images = .jpeg, .png, .jpg, .gif, .jfif
text = .doc, .txt, .pdf, .xlsx, .docx, .xls, .rtf, .md
videos = .mp4, .mkv, .webp, .webm
sounds = .mp3, .wav, .m4a
applications = .exe, .lnk, .msi
codes = .c, .java, .py, .cpp, .js, .html, .css, .php
zip_files = .zip, .rar, .7z"""

        # Try to read extensions from model file
        model_file = os.path.join(RESOURCES, "Extensions_file.txt")
        extensions = default_extensions
        if os.path.exists(model_file):
            with open(model_file, 'r') as file:
                extensions = file.read()
        
        # Make sure folders directory exists
        folders_dir = os.path.join(download_path, ",Folders")
        if not os.path.exists(folders_dir):
            os.makedirs(folders_dir, exist_ok=True)
            
        # Check if extension file already exists
        ext_file = os.path.join(folders_dir, "Extensions_file.txt")
        if not os.path.exists(ext_file):
            with open(ext_file, 'w') as ex_file:
                ex_file.write(extensions)
    except Exception as e:
        print(f"Error creating extensions file: {e}")


def create_mapping(download_path):
    try:
        ext_file_path = os.path.join(download_path, ",Folders", "Extensions_file.txt")
        
        # Make sure the extensions file exists
        if not os.path.exists(ext_file_path):
            # Create it if it doesn't exist
            create_ext_file(download_path)
        
        # Create default extension lists in case of problems
        default_extensions = [
            ['.jpeg', '.png', '.jpg', '.gif', '.jfif'],
            ['.doc', '.txt', '.pdf', '.xlsx', '.docx', '.xls', '.rtf', '.md'],
            ['.mp4', '.mkv', '.webp', '.webm'],
            ['.mp3', '.wav', '.m4a'],
            ['.exe', '.lnk', '.msi'],
            ['.c', '.java', '.py', '.cpp', '.js', '.html', '.css', '.php'],
            ['.zip', '.rar', '.7z']
        ]
        
        # Try to read and parse the extension file
        with open(ext_file_path, 'r') as file:
            images = file.readline()
            text = file.readline()
            videos = file.readline()
            sounds = file.readline()
            applications = file.readline()
            codes = file.readline()
            zip_files = file.readline()
        
            extensions = [images, text, videos, sounds, applications, codes, zip_files]
            
            # Parse each line into a list of extensions
            for i, j in enumerate(extensions):
                try:
                    j = j.split(', ')
                    j[0] = j[0].split('= ')[1]
                    j[-1] = j[-1].split('\n')[0]
                    extensions[i] = j
                except (IndexError, ValueError):
                    # If parsing fails, use default extensions
                    extensions[i] = default_extensions[i]
        
        # Create the extension dictionary with correct folder names
        ext_dict = {".Pictures": extensions[0], ".Text": extensions[1],
                    ".Videos": extensions[2], ".Music": extensions[3],
                    ".Installers": extensions[4], ".Code": extensions[5],
                    ".Zip Files": extensions[6]}
                    
        return ext_dict
    
    except Exception as e:
        print(f"Error creating extension mapping: {e}")
        # Return default mapping if something goes wrong
        return {
            ".Pictures": ['.jpeg', '.png', '.jpg', '.gif', '.jfif'],
            ".Text": ['.doc', '.txt', '.pdf', '.xlsx', '.docx', '.xls', '.rtf', '.md'],
            ".Videos": ['.mp4', '.mkv', '.webp', '.webm'],
            ".Music": ['.mp3', '.wav', '.m4a'],
            ".Installers": ['.exe', '.lnk', '.msi'],
            ".Code": ['.c', '.java', '.py', '.cpp', '.js', '.html', '.css', '.php'],
            ".Zip Files": ['.zip', '.rar', '.7z']
        }


def sorter(download_path, ext_dict):
    try:
        # Make sure we're in the right directory
        os.chdir(download_path)
        print("Sorting the files...")
        
        # Get the current files (fresh list)
        files_to_sort = os.listdir(download_path)
        keys_list = list(ext_dict.keys())
        
        # Map folder names in ext_dict to FOLDERS names to ensure consistency
        folder_mapping = {
            ".Saved Pictures": ".Pictures",
            ".Random Code": ".Code",
            ".Saved Videos": ".Videos"
        }

        # Process each file in the directory
        for file in files_to_sort:
            # Skip the folders we created
            if file in FOLDERS:
                continue
                
            destination = ""
            file_path = os.path.join(download_path, file)
            
            # Skip files that no longer exist (might have been moved by another process)
            if not os.path.exists(file_path):
                continue

            # Try to find the right destination based on file extension
            for i in range(len(keys_list)):
                for ex in ext_dict[keys_list[i]]:
                    if file.endswith(ex):
                        # Map to the correct folder name if needed
                        folder_name = keys_list[i]
                        if folder_name in folder_mapping:
                            folder_name = folder_mapping[folder_name]
                            
                        destination = os.path.join(download_path, folder_name)
                        
                        # Handle duplicates
                        if os.path.isfile(os.path.join(destination, file)):
                            try:
                                duplicates_folder = os.path.join(download_path, ".Other", ".Duplicates")
                                # Ensure the duplicates folder exists
                                if not os.path.exists(duplicates_folder):
                                    os.makedirs(duplicates_folder, exist_ok=True)
                                    
                                # Try to move the file to duplicates folder
                                with contextlib.suppress(shutil.Error):
                                    shutil.move(file_path, duplicates_folder)
                                
                                # If move failed, try renaming the file
                                if os.path.exists(file_path):
                                    new_name = os.path.join(duplicates_folder, f"DUP_{file}")
                                    # Ensure we don't override existing files
                                    counter = 1
                                    while os.path.exists(new_name):
                                        new_name = os.path.join(duplicates_folder, f"DUP_{counter}_{file}")
                                        counter += 1
                                    os.rename(file_path, new_name)
                            except (OSError, IOError) as e:
                                print(f"Error handling duplicate file {file}: {e}")
                        else:
                            # Move file to its destination folder
                            try:
                                shutil.move(file_path, destination)
                            except (OSError, IOError) as e:
                                print(f"Error moving file {file} to {destination}: {e}")
                        
                        # We found a match, no need to check other extensions
                        break
                
                # If we found a destination, no need to check other categories
                if destination:
                    break

            # Handle files with no matching extension
            if os.path.exists(file_path):  # Check if file still exists
                if os.path.isfile(file_path) and not destination:
                    try:
                        shutil.move(file_path, os.path.join(download_path, ".Other"))
                    except (OSError, IOError) as e:
                        print(f"Error moving file {file} to .Other folder: {e}")
                
                elif os.path.isdir(file_path) and file not in FOLDERS:
                    folders_dir = os.path.join(download_path, ",Folders")
                    # Check if a folder with the same name already exists in the ,Folders directory
                    if os.path.exists(os.path.join(folders_dir, file)):
                        try:
                            # This folder already exists in ,Folders, move to .Duplicates
                            duplicates_folder = os.path.join(download_path, ".Other", ".Duplicates")
                            # Ensure the duplicates folder exists
                            if not os.path.exists(duplicates_folder):
                                os.makedirs(duplicates_folder, exist_ok=True)
                                
                            # Try to move the folder to duplicates
                            target_path = os.path.join(duplicates_folder, file)
                            
                            # If target already exists, create a unique name
                            if os.path.exists(target_path):
                                counter = 1
                                while os.path.exists(os.path.join(duplicates_folder, f"DUP_{counter}_{file}")):
                                    counter += 1
                                target_path = os.path.join(duplicates_folder, f"DUP_{counter}_{file}")
                            
                            # Move folder to duplicates
                            shutil.move(file_path, target_path)
                            print(f"Moved duplicate folder '{file}' to .Duplicates")
                        except (OSError, IOError) as e:
                            print(f"Error moving duplicate folder {file} to .Duplicates: {e}")
                    else:
                        # Normal case - move to ,Folders
                        try:
                            shutil.move(file_path, folders_dir)
                        except (OSError, IOError) as e:
                            print(f"Error moving directory {file} to ,Folders: {e}")
        
        print("Sorting Completed...")
        toastNotifier("Finished organizing")
        
    except Exception as e:
        print(f"Error during sorting: {e}")
        toastNotifier("Error during organizing")


def main(download_path):
    setup(download_path)
    dicto = create_mapping(download_path)
    sorter(download_path, dicto)


if __name__ == '__main__':
    main(DEFAULT_DOWNLOAD_PATH)
