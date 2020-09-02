import zipfile
import os

class Extract():
    """
    This class extracts mages in zip file and puts the in target folder
    """
    def __init__(self, path, target_folder):
        self.path = path
        self.target_folder = target_folder
    
    def extract_images(self):
        with zipfile.ZipFile(self.path) as zip_ref:
            zip_ref.extractall(self.target_folder)
