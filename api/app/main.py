"""Application entry point"""


from api.app.controllers.base import BaseController
from api.routes.base import api

if __name__ == "__main__":
    app = BaseController(api)
    app.run()

