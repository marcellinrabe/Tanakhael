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
