from flask import Flask
from post import post_file
from users import users_file
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)
#path to this file
basedir = os.path.abspath(os.path.dirname(__file__))
#you need to tell your app how to connect to your database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
#pass app to database
db = SQLAlchemy(app)

#tables------------

# user table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

# post table
class post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    user_id = db.Column(db.Integer)

#register post.py
app.register_blueprint(post_file)
#register users.py
app.register_blueprint(users_file)

if __name__ == '__main__':
    app.run(debug=True)
