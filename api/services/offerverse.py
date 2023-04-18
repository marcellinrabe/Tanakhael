"""Offer verse service"""


class VerseService:

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def _parse_json_dict(self, cursor):
        return [doc for doc in cursor]

    def _parse_verse_dict(self, cursor):
        """Parse documents object from pymongo to FastAPI JSON supported argument"""
        documents = []

        for chapter in cursor:
            for verse_index in chapter:
                documents.append(chapter[f"{verse_index}"])
        return documents[0]

    def show_collection_list(self):
        cursor = self.db_connection.db.list_collection_names()
        testaments_database = self._parse_json_dict(cursor)
        output = []
        for testament_database_name in testaments_database:
            testament = " ".join(
                testament_database_name.split("_")
            )
            output.append(testament)
        return output

    def show_verse(self, collection_name, meta):
        """deliver verset text according to uri"""
        collection = self.db_connection.db[collection_name]
        cursor = collection.find(meta['filters']["arg_1"], meta['filters']["arg_2"])
        verses = self._parse_verse_dict(cursor)
        return {
            "book": meta["book"],
            "chapter": meta["chapter"],
            "pointer": meta["pointer"],
            "end_cursor": meta["end_cursor"],
            "verses": verses
        }

    def offer_collection_books(self, testament):
        fields_filter = {
            "meta.name": 1,
            "meta.chapter_number": 1,
            "_id": 0
        }
        collection = self.db_connection.db[testament]
        cursor = collection.find({}, fields_filter)
        return self._parse_json_dict(cursor)

    def count_verse(self, testament, book, chapter) -> int:
        search_filter = {
            "meta.name": book,
            f"{chapter}": {
                "$exists": True
            }
        }
        collection = self.db_connection.db[testament]
        document = collection.find_one(search_filter)
        return len(document[f"{chapter}"])

