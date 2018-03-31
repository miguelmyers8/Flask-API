from flask import Blueprint

users_file = Blueprint('users_file', __name__)

@users_file.route("/users", methods=["GET"])
def index():
    return "USERS INDEX"

@users_file.route('/user/<user_id>', methods=["GET"])
def show(user_id):
    return: "SHOW"

@users_file.route('/user/new', methods=["POST"])
def new():
    return "NEW"
