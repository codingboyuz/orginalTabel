import os
import shutil

def remove_folder():
    folder_path = 'database/'

    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        os.makedirs(folder_path)
    else:
        os.makedirs(folder_path)
