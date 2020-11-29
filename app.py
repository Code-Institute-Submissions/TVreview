import os
from flask import (
    Flask, render_template, url_for, redirect, request, flash, session)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signUp():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            redirect(url_for("signUp"))

        signup = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(signup)

        session["user"] = request.form.get("username").lower()
        flash("Successfully Signed Up")
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # check password matches correctly
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
            else:
                # invalid password
                flash("incorrect username and/ or password")
                return redirect(url_for('login'))
        else:
            # username does not exist
            flash("incorrect username and/ or password")
            return redirect(url_for('login'))
    return render_template("login.html")


@app.route("/addshow")
def addShow():
    return render_template("addshow.html")


@app.route('/submitShow', methods=['POST'])
def submitShow():
    show = {
        "name": request.form.get("name"),
        "years": request.form.get("years"),
        "seasons": request.form.get("seasons"),
        "country": request.form.get("country"),
        "synopsis": request.form.get("synopsis")
    }
    tvshow = mongo.db.show
    tvshow.insert_one(show)
    return redirect(url_for("addShow"))


@app.route('/tvshow')
def tvShow():
    tvshow = mongo.db.show
    result = tvshow.find({}, {"_id": 0, "name": 1})
    return render_template("tvshow.html", test=result)
# @app.route('/tvshow/<show_id>')
# def tvshow(show_id):
    # show = mongo.db.find_one({'_id': ObjectId(show_id)})
    # return render_template("tvshow.html", show=show)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
