from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#cors = CORS(app, resources={r"/quiz/api/v1.0/*": {"origins": "*"}})
cors = CORS(app)

import os.path
def mkpath(p):
    return os.path.normpath(
        os.path.join(
        os.path.dirname( __file__ ),
        p))
app.config["SQLALCHEMY_DATABASE_URI"] = ("sqlite:///"+mkpath("../quizz.db"))

db = SQLAlchemy(app)

app.config["SECRET_KEY"] = "550fcef2-a94c-4673-a8c3-bd315daf4726"