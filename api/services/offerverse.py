"""Offer verse service"""


class VerseService:

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def show_collection_list(self):
        collections = self.db_connection.db.list_collection_names()
        for collection in collections:
            print(collection)

    def show_verse(self, collection_name, db_search_filter):
        """deliver verset text according to uri"""
        collection = self.db_connection.db[collection_name]
        cursor = collection.find(db_search_filter["arg_1"], db_search_filter["arg_2"])
        documents = [doc for doc in cursor]
        return documents

