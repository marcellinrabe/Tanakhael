from fastapi import FastAPI
from fastapi.responses import JSONResponse

from os import environ
from dotenv import load_dotenv

from api.database.connection import DBConnection

from api.app.models.uri import Uri

from api.services.offerverse import VerseService

load_dotenv()

DB_URL = environ.get("DB_URL")
DB_NAME = environ.get("DB_NAME")


api = FastAPI()
db_connection = DBConnection(DB_URL, DB_NAME)
verse_service = VerseService(db_connection)


@api.get("/verse/{verse}")
def search_verse(verse: str, collection: str):
    uri = Uri(verse)

    if not uri.is_conform():
        return None

    db_search_filter = uri.build_filter()
    documents = verse_service.show_verse(collection, db_search_filter)
    return JSONResponse(content=documents)


@api.get("/collection/list")
def collections():
    documents = verse_service.show_collection_list()
    return JSONResponse(content=documents)


@api.get("/collection/books")
def collection_book(collection: str):
    documents = verse_service.offer_collection_books(collection)
    return JSONResponse(content=documents)


@api.get("/book/chapter/count")
def book_chapters(collection: str, book: str):
    return verse_service.count_book_chapters(collection, book)


@api.get("/chapter/verse/count")
def chapter_verses(collection: str, book: str, index: int):
    return verse_service.count_chapter_verses(collection, book, index)
