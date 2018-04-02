from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug import secure_filename


app = Flask(__name__)
#path to this file
basedir = os.path.abspath(os.path.dirname(__file__))
#you need to tell your app how to connect to your database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
#pass app to database
db = SQLAlchemy(app)



from users import *
from post import *

if __name__ == '__main__':
    app.run(debug=True)
