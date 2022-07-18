from ampalibe.ui import QuickReply, Button,Element
from ampalibe import Payload
from sre_compile import isstring

def render_search_syntax(sender_id, chat):
    ...
def give_back_way(sender_id, chat):
    research_option = [ 
        QuickReply(
            title="Rechercher",
            payload="/search",
            image_url="https://png.pngtree.com/element_our/20190528/ourlarge/pngtree-magnifying-glass-icon-image_1128382.jpg"
        ),
        QuickReply(
            title="Retour au menu",
            payload="/",
            image_url="https://www.pinclipart.com/picdir/big/44-448226_file-home-icon-svg-wikimedia-commons-free-train.png"
        )
    ]
    chat.send_quick_reply(sender_id, research_option, "Safidy")

def showlist(sender_id, chat, chapters: dict):
    list_items = []
    for chapter in chapters:
        buttons = [
            Button(
                type="postback",
                title="tsindrio",
                payload=Payload("/setcurrent", chapter=chapters[chapter]["sous-titre"])
            )
        ]
        title = chapters[chapter]["nom"] if isstring(chapters[chapter]["nom"]) else chapters[chapter]["nom"][0].capitalize()
        list_items.append(
            Element(
                title=title,
                buttons=buttons
            )
        )
    chat.send_template(sender_id, list_items, next=True)


def options_upload(sender_id, chat, versetstext: str):
    ...
