import os
import imghdr


import shutil





def create_folders(path, folders):
    """Creates standard folders in selected path"""

    for folder in folders:
        dir = path + folder
        try:
            os.mkdir(dir)
        except FileExistsError:
            pass


def arrange_files(path, folders):
    """Arranges files into standard folders depending on their extension""" 

    def move_file(folder):
        try:
            shutil.move(path + f, path + folder + "/" + f)
        except shutil.Error:
             pass


    files = os.listdir(path)
    for f in files:
        
        name, ext = os.path.splitext(path + f)

        if f not in folders:

            if imghdr.what(path + f) != None:
                move_file(folders[0])

            elif ext == ".avi" or ext == '.mov' or ext == '.mp4':
                move_file(folders[1])

            elif ext == ".mp3" or ext == ".wav":
                move_file(folders[2])

            elif ext == ".azw3":
                move_file(folders[3])
            
            elif ext == ".pdf":
                move_file(folders[4])

            elif ext == ".rar" or ext == ".zip":
                move_file(folders[5])

            else:
                move_file(folders[6])



def main():
    """Executes the main program"""
    
    path = "C:/Users/alexf/Downloads/"
    folders = ["Imagenes", "Videos", "Audio", "Ebooks", "pdf", "comprimidos", "otros"]

    create_folders(path, folders)
    arrange_files(path, folders)