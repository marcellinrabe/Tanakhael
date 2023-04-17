import ampalibe
from ampalibe import Model

from views.user import UserView

from models.database import Database
from models.collection import Collection
from models.chapter import Chapter
from models.book import Book

views = UserView()
database = Database()
query = Model()


@ampalibe.command('/')
def choice_collection(sender_id, cmd, **ext):
    views.show_collections(sender_id, database.collections)


@ampalibe.command('/collection')
def choice_book(sender_id, cmd, collection_name, **ext):
    query.set_temp(sender_id, 'collection_name', collection_name)
    collection = Collection(database, collection_name)
    books = collection.get_books()
    views.show_books(sender_id, collection, books)


@ampalibe.command('/book')
def choice_chapter(sender_id, cmd, book, **ext):
    query.set_temp(sender_id, 'book_name', book.name)
    views.choice_chapter(sender_id, book)
    query.set_action(sender_id, "/get_chapter")


@ampalibe.action("/get_chapter")
def get_verse_getter(sender_id, cmd, **ext):
    query.set_action(sender_id, None)
    collection_name, book_name, index = (
        query.get_temp(sender_id, 'collection_name'),
        query.get_temp(sender_id, 'book_name'),
        cmd
    )
    collection = Collection(database, collection_name)
    book = Book(collection, book_name)
    chapter = Chapter(book, index)

    query.set_temp(sender_id, 'chapter_name', chapter.index)

    views.choice_verse_getter(sender_id, chapter)


@ampalibe.command("/verse")
def get_verse(sender_id, cmd, option, **ext):
    views.choice_verse(sender_id, option)
    query.set_action(sender_id, "/build")


@ampalibe.action("/build")
def build_request(sender_id, cmd, **ext):
    query.set_action(sender_id, None)
    collection_name, book, index = (
        query.get_temp(sender_id, 'collection_name'),
        query.get_temp(sender_id, 'book_name'),
        query.get_temp(sender_id, 'chapter_name'),
    )
    collection = Collection(database, collection_name)
    book = Book(collection, book)
    chapter = Chapter(book, index)
    result = chapter.get_verse(cmd)
    views.show_verse(sender_id, result)

