from SorterPyqt import *

config = ConfigParser()
config.read(CONFIG_LOCATION)

DOWNLOAD_PATH = get_default_path()


def main(download_path):
    setup(download_path)
    dicto = create_mapping(download_path)
    sorter(download_path, dicto)


import contextlib
if __name__ == '__main__':
    with contextlib.suppress(OSError):
        main(DOWNLOAD_PATH)
