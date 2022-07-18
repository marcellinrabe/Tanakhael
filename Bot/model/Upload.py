from typing import Text
from utils.constant import *
from utils.Radical import Extension
from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont


class TextFile:

    def __init__(self, path, name) -> None:
        self.path = path
        self.name = name

class Upload:

    def textfile(name: str, verse: str):
        """
            save the verse to a text file
        """
        file = Extension.add("text", name)
        path = const.TEXT_PREFIX+file
        new_file = open(path, "w+")
        new_file.write(verse)
        new_file.close()
        return TextFile(path, name)

    def pdf(name: str, verse: str):
        """
            save the verse to a pdf file
        """
        file = Extension.add("pdf", name)
        path = const.PDF_PREFIX+file
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font("Arial","", const.FONT, uni=True)
        pdf.set_font("Arial","", size = 14)
        pdf.write(8, txt=verse)
        pdf.output(name=path)
        return path
    
    def png(name: str, verse: str):
        """
            save the verse into a png image file 
        """
        # mbola mila fanamboarana
        file = Extension.add("png", name)
        path = const.PNG_PREFIX+file
        outline= bg = "white"
        font = ImageFont.truetype(const.FONT, const.FONT_SIZE)
        width, height = 600, 400
        img = Image.new('RGB', (width+4, height+4), bg)
        d = ImageDraw.Draw(img)
        d.text((2, height/2), verse, fill="black", font=font)
        d.rectangle((0, 0, width+3, height+3), outline=outline)
        img.save(path)
        return path
