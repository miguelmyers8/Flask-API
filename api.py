from flask import Flask, request, jsonify
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)
#path to this file
basedir = os.path.abspath(os.path.dirname(__file__))
#you need to tell your app how to connect to your database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
#pass app to database
db = SQLAlchemy(app)

#tables------------------------------------

# user table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

# post table
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    user_id = db.Column(db.Integer)


#routes-----------------------------------

    #index_____________
@app.route('/users', methods=["GET"])
def index():
    #get all users from SQLAlchemy
    users = User.query.all()
    #turn SQLAlchemy results to json
    output = []
    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.append(user_data)
    return jsonify({'users':output})


    #show_________________
@app.route('/user/<public_id>', methods=["GET"])
def show(public_id):
    #find user by public id
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message : No user found!'})
    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['name'] = user.name
    user_data['password'] = user.password
    user_data['admin'] = user.admin
    return jsonify({"user": user_data })


    #new__________________
@app.route('/user/new', methods=["POST"])
def new():
    #get data in json
    data = request.get_json()
    # hased password
    hased_password = generate_password_hash(data['password'], method='sha256')
    #create new user
    new_user = User(
    public_id=str(uuid.uuid4()), #string verion of uuid
    name=data['name'], #data name
    password=hased_password,
    admin=False #default is false
    )
    #add the user to db
    db.session.add(new_user)
    #commit user
    db.session.commit()
    return jsonify({"message": "new user created!"})

    #update_____________________
@app.route('/user/<public_id>', methods=["PUT"])
def update(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message : No user found!'})
    return "Update"


    #delete______________________
@app.route('/user/<public_id>', methods=["DELETE"])
def delete(public_id):
    return  "Delete"

if __name__ == '__main__':
    app.run(debug=True)
