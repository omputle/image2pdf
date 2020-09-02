import os

class Rename():
    """
    This class renames images in target folder for easy sorting
    """
    def __init__(self, target_folder):
        os.chdir(target_folder)
    
    def rename_images(self):
        images = os.listdir()
        images.sort()
        for f in images:
            f_name, f_ext = os.path.splitext(f)
            f_parts = f_name.split('_')
            f_parts[4] = f_parts[4].zfill(2)
            new_name = '{}{}'.format(f_parts[4], f_ext)
            os.rename(f, new_name)