"""main controller"""

from uvicorn import run


class BaseController:

    def __init__(self, api):
        self.api = api

    def run(self):
        """Initialise app and listener"""
        run(self.api, host="127.0.0.1", port=8000)




