from convert import Convert
from rename import Rename
from extract import Extract
import os
import sys

if __name__ == "__main__":
    path_to_folder = sys.argv[1]
    if os.path.exists(path_to_folder):
        split = os.path.splitext(path_to_folder)
        target_folder = split[0]
        ext_obj = Extract(path_to_folder, target_folder)
        ext_obj.extract_images()
        ren_obj = Rename(target_folder)
        ren_obj.rename_images()
        conv_obj = Convert(target_folder)
        conv_obj.convert_to_pdf()
        conv_obj.remove_pictures()
        filename = os.path.split(path_to_folder)
        new_name = os.path.join(target_folder, filename[1])
        os.rename(path_to_folder, new_name)
    else:
        print("Invalid path")

    