from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
from datetime import timedelta
from api import api
from database import database

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=1)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # removes a warning 
app.register_blueprint(api, ulr_prefix="/api")
app.register_blueprint(database, ulr_prefix="/")

# HOME PAGE
@app.route('/home')
@app.route('/')
def home():
	return render_template("index.html")

# LOGIN APGE
@app.route('/login', methods=["POST", "GET"])
def login():
	# POST 
	if request.method == "POST":
		session.permanent = False
		user = request.form["nm"]
		session["user"] = user

		found_user = users.query.filter_by(name=user).first()
		if found_user:
			session["email"] = found_user.email
		else:
			usr = users(user, "")
			db.session.add(usr)
			db.session.commit()

		flash(f"You have been logged in, {user}", "info")
		return redirect(url_for("user"))
	# GET
	else:
		if "user" in session:
			return redirect(url_for("user"))
		else:
			return render_template("login.html")

@app.route('/user', methods=["POST", "GET"])
def user():
	email = None
	if "user" in session:
		user = session["user"]

		if request.method == "POST":
			email = request.form["email"]
			session["email"] = email
			found_user = users.query.filter_by(name=user).first()
			found_user.email = email
			db.session.commit()
			flash(f"Email was saved!")
		else:
			if "email" in session:
				email = session["email"]

		return render_template("user.html", user=user, email=email)
	else:
		return redirect(url_for("login"))

@app.route('/view')
def view():
	return render_template("view.html", values=users.query.all())

@app.route('/reservation')
def reservation():
	return render_template("reservation.html")

@app.route('/drugs')
def drugs():
	return render_template("drugs.html")

@app.route('/employees')
def employees():
	return render_template("employees.html")

@app.route('/history')
def history():
	return render_template("history.html")

@app.route('/offices')
def offices():
	return render_template("offices.html")

@app.route('/logout')
def logout():
	if "user" in session:
		user = session["user"]
		flash(f"You have been logged out, {user}", "info")
	session.pop("user", None)
	session.pop("email", None)
	return redirect(url_for("login"))

if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)