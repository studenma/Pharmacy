from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

database = Blueprint("database", __name__, static_folder="static", template_folder="templates")

database.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
database.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # removes a warning 

db = SQLAlchemy(database)

class users(db.Model):
	_id = db.Column("id", db.Integer, primary_key=True)
	name = db.Column("name", db.String(100))
	email = db.Column("email", db.String(100))

	def __init__(self, name, email):
		self.name = name
		self.email = email

@second.route("/home")
def home():
	render_templates("home.html")