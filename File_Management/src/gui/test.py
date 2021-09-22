from src.gui.SorterPyqt import *

path_dict, name_list, path_list = create_path_dict('config.ini')

config.remove_option('saved_paths', 'dsa')

print(name_list, path_list)
