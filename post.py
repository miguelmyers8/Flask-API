from api import app
from flask import request, jsonify
from models import Post
import os


@app.route('/upload', methods=['POST'])
def upload_file():
    data = request.get_json()

    new_post = Post(
    image_filename = data['image_filename']
    )
    data.save(secure_filename(files.filename))

    db.session.add(new_post)

    db.session.commit()

    return jsonify({"message": "new post created!"})
