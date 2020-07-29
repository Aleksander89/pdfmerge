import os

def is_valid_directory(directory):
    if os.name == 'nt':
        if "\\" not in directory:
            raise Exception(directory + ' is not a valid path. Try --help for more information.')

    return os.path.isdir(directory)
