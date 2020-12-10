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
    tvshow = mongo.db.show
    result = tvshow.find()
    return render_template("index.html", id=result)


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
        return redirect(url_for('profile', username=session["user"]))
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
                    return redirect(url_for(
                        'profile', username=session["user"]))
            else:
                # invalid password
                flash("incorrect username and/ or password")
                return redirect(url_for('login'))
        else:
            # username does not exist
            flash("incorrect username and/ or password")
            return redirect(url_for('login'))
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get user's username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for('login'))


@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for('login'))


@app.route("/search/<searchterm>")
def search(searchterm):
    result = mongo.db.show.find_one(
        {}
    )

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


@app.route('/addreview/<show_id>', methods=['GET', 'POST'])
def addreview(show_id):
    if request.method == "POST":
        reviews = {
            "review_for": show_id,
            "review": request.form.get("review"),
        }
        review = mongo.db.reviews
        review.insert_one(reviews)
        return render_template("addreview.html")


@app.route('/tvshow/<show_id>')
def tvShow(show_id):
    tvshow = mongo.db.show
    result = tvshow.find_one({"_id": ObjectId(show_id)})
    review_coll = mongo.db.reviews
    reviews = review_coll.find_one("review_id": show_id)
    return render_template(
        "tvshow.html", id=result, reviews=reviews)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
