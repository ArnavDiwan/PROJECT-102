import os
import shutil

from_dir = "C:/Users/dell/Downloads"
to_dir = "C:/Users/dell/Downloads"

list_of_files = os.listdir(from_dir)
print("list of files:- ",list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print("Name of file:- ",name)
    print("Extension of file:- ",extension)

    if extension in ['.pdf', '.docx', '.doc', '.txt']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Text files"
        path3 = to_dir + '/' + "Text files" + '/' + file_name
        print("path1:-  " , path1)
        print("path2:-  ", path3)
        print("path3:-  ", path3)

        if os.path.exists(path2):
            print("Moving " + file_name + ".....")
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("Moving " + file_name + ".....")
            shutil.move(path1, path3)