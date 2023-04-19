"""User views"""

from random import randrange

from ampalibe import Payload, Messenger
from ampalibe.ui import QuickReply, Element, Button, Type


class UserView:

    def __init__(self):
        self.chat = Messenger()

    def show_greeting_keys(self, sender_id, greetings):
        self.chat.send_text(
            sender_id,
            (
                "Mampidira iray @ireto teny ireto mba hanaitra an'i Tanakhael "
                "hitongavany eto hamaly ny fangatahanao : \n\n"
                f"{', '.join(greetings)}"
            )

        )
    def prompt_testament(self, sender_id, testaments):

        testaments_repl = []

        for testament in testaments:
            testaments_repl.append(
                QuickReply(
                    title=f"📚 {testament}",
                    payload=Payload(f"/choice-book", testament=testament)
                )
            )

        self.chat.send_quick_reply(sender_id, testaments_repl, 'Fizarana')

    def prompt_book(self, sender_id, books):
        book_items = []

        for book in books:

            button = Button(
                type=Type.postback,
                title="hamaky",
                payload=Payload("/choice-chapter", book=book, details=True),
            )

            book_items.append(
                Element(
                    title=book.name,
                    image_url="https://i.ibb.co/pjRYvL9/baiboly.jpg",
                    buttons=[button, ],
                )
            )

        self.chat.send_generic_template(
            sender_id,
            book_items,
            next="manaraka",
        )

    def prompt_chapter(self, sender_id, book):
        print(book.chapter_number)
        chapter_items = []
        buttons = []

        for index in range(book.chapter_number):
            chapter = index + 1

            ref = f"{book.name} {chapter}"
            buttons.append(
                Button(
                    type=Type.postback,
                    title=ref,
                    payload=Payload('/output-type', book=book, chapter=chapter)
                )
            )
            if index is not 0 and chapter % 3 == 0:
                chapter_items.append(
                    Element(
                        title="Andininy",
                        buttons=buttons,
                    )
                )
                buttons = []

        self.chat.send_generic_template(
            sender_id,
            chapter_items,
            next="manaraka"
        )

    def choice_output(self, sender_id, chapter_reference, verse_count):
        self.chat.send_text(sender_id, f"{chapter_reference} manana toko {verse_count}")
        options = ["toko iray", "toko mifampitohy"]
        options_repl = []
        for option in options:
            options_repl.append(
                QuickReply(
                    title=option,
                    payload=Payload(f"/verse-number", option=option, last_index=verse_count)
                )
            )
        self.chat.send_quick_reply(sender_id, options_repl, "Toko halaina")

    def choice_verse(self, sender_id, option, last_index):
        """send verse options: one verse or list"""
        if "iray" in option:
            self.chat.send_text(sender_id, f"Mampidira laharana toko iray entre 1 - {last_index}")
        elif "mifampitohy" in option:
            self.chat.send_text(
                sender_id,
                (
                    f"Mampidira ny laharan'ireo toko mifampitohy entre 1 - {last_index}\n"
                    f"Ohatra : {randrange(1, last_index + 1)} - {last_index}"
                )
            )

    def show_verse(self, sender_id, verse):
        self.chat.send_text(
            sender_id,
            (
                f"Eo am-pakana ny {verse.book} {verse.chapter} : {verse.pointer}"
                f"{f'- {verse.end_cursor - 1}' if verse.end_cursor is not None else ''}"
                " ... "
            )
        )

        if verse.end_cursor is None:
            pointer = verse.pointer

            self.chat.send_text(
                sender_id,
                (
                    f"{verse.book} {verse.chapter} : {pointer}\n\n"
                    f"{verse.verses[f'{pointer}']}"
                )
            )
        else:
            for verse_index in range(verse.pointer, verse.end_cursor):
                self.chat.send_text(
                    sender_id,
                    (
                        f"{verse.book} {verse.chapter} : {verse_index}\n\n"
                        f"{verse.verses[f'{verse_index}']}"
                    )
                )

        self.chat.send_text(sender_id, "...")
        self.propose_new_session(sender_id)

    def say_goodbye(self, sender_id):
        self.chat.send_text(sender_id, "Mandram-pihaona ary o 🙂")
        self.chat.send_text(sender_id, "Misaotra betsaka nitsidika. 👉👈")

    def propose_new_session(self, sender_id):
        suggestions_repl = []
        suggestions = ["eny", "aoka izao"]
        for suggestion in suggestions:
            suggestions_repl.append(
                QuickReply(
                    title=f"{suggestion}",
                    payload=Payload(f"/", suggestion={suggestion})
                )
            )

        self.chat.send_quick_reply(sender_id, suggestions_repl, 'Misy andalan-tsoratra Masina hafa tiana jerena ve ?')




