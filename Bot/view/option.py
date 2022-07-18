from ampalibe import Payload
from ampalibe.ui import QuickReply, Button
from utils.Radical import Prefix
from utils.constant import *


class Option:

    def __init__(self, chat) -> None:
        self.chat = chat
    
    def start(self, sender_id):
        """
            show the menu at the very beginning
        """
        self.chat.get_started()
        menu = [
            QuickReply(
                title="Hanadina",
                payload="/wantsearch",
                image_url= f'https://img.lovepik.com/element/45004/4703.png_860.png'
            ),
            QuickReply(
                title="Hitady",
                payload="/wantbrowse",
                image_url= f'https://cdn3.iconfinder.com/data/icons/vista-general/512/000440-folder-search.png'
            )
        ]
        self.chat.send_quick_reply(sender_id, menu, "Tongasoa")
    
    def upload(self, sender_id, subtitle, verse: str):
        """
            verse rendering options
        """
        image_url = {
            "message": "message-icon.webp",
            "pdf": "pdf-icon.png",
            "textfile": "textfile-icon.png",
            "png": "png-icon.jpg"
        }
        options = [
            QuickReply(
                title ="message",
                payload = Payload("/render", subtitle=subtitle, type="message", versets=verse),
                image_url = f'{const.IMAGE_PREFIX+image_url["message"]}'
            ),
            QuickReply(
                title = "pdf",
                payload = Payload("/render", subtitle=subtitle, type="pdf", verse=verse),
                image_url = f'{const.IMAGE_PREFIX+image_url["pdf"]}'
            ),
            QuickReply(
                title="fichier texte",
                payload= Payload("/render", subtitle=subtitle, type="textfile", versets=verse),
                image_url= f'{const.IMAGE_PREFIX+image_url["textfile"]}'
            ),
            QuickReply(
                title="png",
                payload= Payload("/render", subtitle=subtitle, type="png", versets=verse),
                image_url= f'{const.IMAGE_PREFIX+image_url["png"]}'
            )
        ]
        if 2000 < len(verse): options.pop(0)
        self.chat.send_quick_reply(sender_id, options, "telecharger en tant que")

    def browse(self, sender_id):
        buttons = [
            Button(
                type='postback',
                title='Testameta taloha',
                payload= Payload('/tesmtlist', type="ancient")
            ),
            Button(
                type='postback',
                title='Testameta vaovao',
                payload= Payload('/tesmtlist', type="new")
            ),   
        ]  
        self.chat.send_button(sender_id, buttons, "Testameta")

    