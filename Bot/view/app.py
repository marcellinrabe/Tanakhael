import ampalibe
from ampalibe import Payload
from ampalibe.ui import Element, Button
from sre_compile import isstring
from conf import Configuration
from .option import Option
from .search import Search
from .action import Action


app = ampalibe.init(Configuration())
chat = app.chat
query = app.query

class View:

    def __init__(self) -> None:
        self.option = Option(chat)
        self.search = Search(chat)
        self.action = Action(query)

    def getinput(self, sender_id):
        action = "/wantupload"
        self.search.template(sender_id)
        query.set_action(sender_id, action)
    
    def uploadoption(self, sender_id, subtitle: str, verse: str):
        query.set_action(sender_id, None)
        query.set_temp(sender_id, "subtitle", subtitle)
        self.option.upload(sender_id, verse)
    
    def render(self, sender_id, content: str):
        """
            @param str source si c'est un message c'est le verse sinon c'est le nom du fichier
        """
        valids = ["message", "pdf", "textfile", "png"]
        if type not in valids: raise TypeError("output types are message, pdf, text file and png")
        chat.send_message(sender_id, content) if type == 'message' else chat.send_file(sender_id, content)

    def chapters(self, sender_id, chapters: list)->dict:
        render = []
        for chapter in chapters:
            buttons = [
                Button(
                    type="postback",
                    title="tsindrio",
                    payload=Payload("/setcurrent", chapter=chapters[chapter]["sous-titre"])
                )
            ]
            title = chapters[chapter]["nom"] if isstring(chapters[chapter]["nom"]) else chapters[chapter]["nom"][0].capitalize()
            render.append(
                Element(
                    title=title,
                    buttons=buttons
                )
            )
        chat.send_template(sender_id, render, next=True)

    
    
    

    

    
    
