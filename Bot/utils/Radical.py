from utils.constant import *


class Prefix:

    @staticmethod
    def image(image: str)->str:
        """
            returns the full path of the image    
        """
        return const.IMAGE_PREFIX+image

class Extension:

    @staticmethod
    def add(type: str, name: str):
        valids = ["text", "pdf", "png"]
        if type not in valids: raise TypeError("valid types are text, pdf and png")
        if type == "text": ext = ".txt"
        elif type == "pdf": ext = ".pdf"
        elif type == "png": ext = ".png"
        return name+ext

