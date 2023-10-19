from flask import Blueprint, current_app, jsonify
from .repository import User


blueprint = Blueprint("api", __name__, url_prefix="/api")


@blueprint.route("/users/", methods=("GET",))
def get_users():
    users: list[User] = current_app.users.get_all()

    return jsonify(users)


@blueprint.route("/users/<id>", methods=("GET",))
def get_user(id):
    user: User = current_app.users.get_one(id)

    return jsonify(user)
