from flask import Blueprint

post_file = Blueprint('post_file', __name__)

@post_file.route("/post")
def index():
    return "POST INDEX"
