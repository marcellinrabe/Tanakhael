"""main controller"""

from ampalibe import Model

from collections import namedtuple

from views.user import UserView

from models.book import Book

def parse_object(dictionary, name):
    return namedtuple(f"{name}", dictionary.keys())(*dictionary.values())


class Controller:

    def __init__(self, serve):
        self.serve = serve
        self.query = Model()
        self.views = UserView()
        self.verse_req_datas = {}

    def propose_greeting_keys(self, sender_id, greetings):
        self.views.show_greeting_keys(sender_id, greetings)

    def choice_testament(self, sender_id):
        testaments = self.serve.testaments()
        self.views.prompt_testament(sender_id, testaments)

    def choice_book(self, sender_id, testament):
        books = []

        books_api = self.serve.books(testament)

        for book_api in books_api:
            book = Book(testament, book_api["meta"]["name"], book_api["meta"]["chapter_number"])
            books.append(book)

        self.views.prompt_book(sender_id, books)

    def choice_chapter(self, sender_id, book):
        self.verse_req_datas['book'] = book

        self.views.prompt_chapter(sender_id, book)

    def choice_output(self, sender_id, book, chapter):
        self.verse_req_datas['chapter'] = chapter

        chapter_reference = f"{book.name} {chapter}"
        verse_count = self.serve.verse_number(book, chapter)
        self.views.choice_output(sender_id, chapter_reference, verse_count)

    def get_verse_number(self, sender_id, option, last_index):
        self.views.choice_verse(sender_id, option, last_index)
        self.query.set_action(sender_id, "/verse-text")

    def show_verse(self, sender_id, verse_number):
        self.query.set_action(sender_id, None)
        book, chapter = self.verse_req_datas['book'], self.verse_req_datas['chapter']
        testament_req = "_".join(
            book.testament.split(" ")
        )
        request_format = f"{book.name} {chapter} : {verse_number}"
        verse_dict = self.serve.verse(testament_req, request_format)
        verse = parse_object(verse_dict, "verse")
        self.views.show_verse(sender_id, verse)

    def end_session(self, sender_id):
        self.views.say_goodbye(sender_id)

