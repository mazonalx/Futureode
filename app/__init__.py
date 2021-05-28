from flask import Flask,session
from flask_session import Session
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)

app.config.from_object(Config)
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQLAlchemy(app)
migrate = Migrate(app,db)
from app import routes,models,errors,systems,books

