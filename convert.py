import img2pdf
import os

class Convert():
    """
    This class converts images in target folder into a single pdf file
    """
    def __init__(self, target_folder):
        self.target_folder = target_folder
        os.chdir(target_folder)

    def convert_to_pdf(self):
        name = "Document.pdf"
        self.names = os.listdir()
        self.names.sort()
        with open(name, "wb") as f:
            imgs = []
            for f_name in self.names:
                path = os.path.join(self.target_folder, f_name)
                imgs.append(path)
            f.write(img2pdf.convert(imgs))

    def remove_pictures(self):
        for pic in self.names:
            os.remove(pic)

