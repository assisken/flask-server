from flask import Flask

from .api import blueprint as api
from .repository import Users


def create_app(con) -> Flask:
    app = Flask(__name__)

    app.users = Users(con)

    app.register_blueprint(api)

    return app
