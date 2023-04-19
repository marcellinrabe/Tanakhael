"""Application entry point"""


from controllers.base import BaseController
from routes.base import api

if __name__ == "__main__":
    app = BaseController(api)
    app.run()

