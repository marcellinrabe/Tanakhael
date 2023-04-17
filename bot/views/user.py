"""User views"""
from ampalibe import Payload, Messenger, Model

from ampalibe.ui import QuickReply, Element, Button, Type

from models.book import Book


class UserView:

    def __init__(self):
        self.chat = Messenger()
        self.query = Model()

    def show_collections(self, sender_id, collections):

        collections_repl = []

        for collection in collections:
            collection_split = collection.split("_")
            collection_string = " ".join(collection_split)
            collections_repl.append(
                QuickReply(
                    title=collection_string,
                    payload=Payload(f"/collection", collection_name=collection, ref=collection)
                )
            )

        self.chat.send_quick_reply(sender_id, collections_repl, 'Misafidiana ary ny testameta tianao jerena')

    def show_books(self, sender_id, collection, books):

        book_items = []

        for document in books:
            book = Book(collection, document["meta"]["name"])

            buttons = [
                Button(
                    type=Type.postback,
                    title="hijery",
                    payload=Payload("/book", book=book),
                )
            ]

            book_items.append(
                Element(
                    title=book.name,
                    image_url="https://i.ibb.co/pjRYvL9/baiboly.jpg",
                    buttons=buttons,
                )
            )

        # next=True for displaying directly next page button.
        self.chat.send_generic_template(sender_id, book_items, next=True)

    def choice_chapter(self, sender_id, book):
        self.chat.send_text(sender_id, f"Miisa {book.chapters_count} ny isan'ireo andininy amin'ny boky {book.name}")
        self.chat.send_text(sender_id, "Misafidiana laharana andininy iray amin'izy ireo")

    def choice_verse_getter(self, sender_id, chapter):
        self.chat.send_text(sender_id, f"Miisa {chapter.verse_count} ny isan'ireo toko amin'ilay andininy")
        buttons = [
            Button(
                type=Type.postback,
                title='iray',
                payload=Payload('/verse', option="one")
            ),
            Button(
                type=Type.postback,
                title='mifampitohy',
                payload=Payload('/verse', option="many")
            ),
        ]

        self.chat.send_button(sender_id, buttons, "Firy ny toko hovakianao ?")

    def choice_verse(self, sender_id, option):
        """send verse options: one verse or list"""
        if option == "one":
            self.chat.send_text(sender_id, "Misafidiana laharana toko iray amin'izy ireo")
        elif option == "many":
            self.chat.send_text(
                sender_id,
                (
                    "Mampidira ny laharan'ireo toko mifampitohy \n"
                    "Ohatra : 1 - 2"
                )
            )

    def show_verse(self, sender_id, result):
        if result["end_cursor"] is None:
            pointer = result["pointer"]

            self.chat.send_text(
                sender_id,
                (
                    f"{result['book']} {result['chapter']} : {pointer}\n\n"
                    f"{result['verses'][f'{pointer}']}"
                )
            )
            return None

        for verse_index in range(result["pointer"], result["end_cursor"]):
            self.chat.send_text(
                sender_id,
                (
                    f"{result['book']} {result['chapter']} : {verse_index}\n\n"
                    f"{result['verses'][f'{verse_index}']}"
                )
            )




