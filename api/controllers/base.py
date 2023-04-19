"""main controller"""

from uvicorn import run
from os import environ
from dotenv import load_dotenv

load_dotenv()

HOST = environ.get("HOST")
PORT = environ.get("PORT")

class BaseController:

    def __init__(self, api):
        self.api = api

    def run(self):
        """Initialise app and listener"""
        run(self.api, host=f"{HOST}", port=int(PORT))




