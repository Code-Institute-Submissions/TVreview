import os
import requests
import json
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

login_user = False

# Home page


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/search/<searchterm>")
def search(searchterm):
    response = requests.get('https://imdb-api.com/API/SearchSeries/',
    {"apikey": os.environ.get("APIKEY"), "expression": searchterm})
    searchresults = response.json()
    return render_template('search.html', searchresults=searchresults)


@app.route("/searchredirect", methods=["GET", "POST"])
def searchRedirect():
    searchterm = request.form.get("search")
    return redirect(url_for('search', searchterm=searchterm))


# error


@app.route("/error")
def error():
    return render_template("error.html")


# User Login/ signup


@app.route("/signup", methods=["GET", "POST"])
def signUp():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user or existing_email:
            flash("Username/ Email already exists")
            redirect(url_for("signUp"))
        else:
            signup = {
                "username": request.form.get("username").lower(),
                "email": request.form.get("email").lower(),
                "password": generate_password_hash
                (request.form.get("password"))
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
                    global login_user
                    login_user = True
                    return redirect(url_for(
                        'loggedin'))
            else:
                # invalid password
                flash("incorrect username and/ or password")
                return redirect(url_for('login'))
        else:
            # username does not exist
            flash("incorrect username and/ or password")
            return redirect(url_for('login'))
    return render_template("login.html")


@app.route("/loggedin")
def loggedin():
    return render_template("loggedin.html", username=session["user"])


@app.route("/logout")
def logout():
    session.pop("user")
    global login_user
    login_user = False
    return redirect(url_for('login'))


# user profile


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get user's username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    favourites = mongo.db.favourites.find({"user": session["user"]})
    reviews = mongo.db.reviews.find({"review_by": session["user"]})
    if session["user"]:
        return render_template("profile.html",
        username=username, favourites=favourites, reviews=reviews)

    return redirect(url_for('login'))


@app.route("/edit_reviews/<username>/<title>/<show_id>", 
methods=["GET", "POST"])
def edit_reviews(username, title, show_id):
    title = title
    show_id = show_id
    username = username
    if request.method == "POST":
        edited_review = {"$set": {
            "review_for": show_id,
            "title": title,
            "review": request.form.get("edit_review"),
            "review_by": session["user"]
        }}
        old_review = {"review_by": session["user"], "review_for": show_id}
        mongo.db.reviews.update_one(old_review, edited_review)
        flash("Successfully Edited")
        return redirect(url_for('profile', username=session["user"]))
    return render_template("edit.html", 
    title=title, show_id=show_id, username=username)


@app.route("/tvshow/<show_id>")
def tvshow(show_id):
    tvresponse = requests.get('https://imdb-api.com/en/API/Title/',
    {"apikey": os.environ.get("APIKEY"), "id": show_id, "options": "Trailer"})
    show = tvresponse.json()
    session["global_show_id"] = show.get("id")
    session["title"] = show.get("title")
    # show the reviews
    review_coll = mongo.db.reviews
    review_query = {"review_for": show_id}
    reviews = review_coll.find(review_query)
    # show total number of ratings
    rating = mongo.db.ratings.find({"rating_for": show_id})
    rating_count = rating.count()
    # show average rating
    total = 0
    for x in rating:
        total += x.get("rating")
    # find the average
    if rating_count >= 1:
        score = int(total/rating_count)
    else:
        score = 0
    # favourite heart filled in if a favourite
    favourite = "favorite_border"
    global login_user
    if login_user:
        existing_favourite = mongo.db.favourites.find_one(
                {"user": session["user"], "favourite": show_id})
        if existing_favourite:
            favourite = "favorite"
        # Hide ratings and reviews if already done
        existing_rating = mongo.db.ratings.find_one(
                {"rating_by": session["user"], "rating_for": show_id})
        already_reviewed = mongo.db.reviews.find_one(
            {"review_by": session["user"], "review_for": show_id})
        print(login_user)
        return render_template("tvshow.html",
        show=show, reviews=reviews, rating_count=rating_count,
        score=score, favourite=favourite, existing_rating=existing_rating,
        already_reviewed=already_reviewed)
    else:
        print(login_user)
        return render_template("tvshow.html",
        show=show, reviews=reviews, rating_count=rating_count,
        score=score, favourite=favourite)


@app.route('/addreview/<show_id>', methods=['GET', 'POST'])
def addreview(show_id):
    if request.method == "POST":
        try:
            reviews = {
                "review_for": show_id,
                "title": session["title"],
                "review": request.form.get("review"),
                "review_by": session["user"]
            }
            review = mongo.db.reviews
            review.insert_one(reviews)
            return render_template("addreview.html")
        except Exception:
            return redirect(url_for("error"))

# Add the ratings to the database


@app.route('/rating/<show_id>/<rating_no>', methods=['GET', 'POST'])
def rating(show_id, rating_no):
    if request.method == "POST":
        try:
            star = {
                "rating_for": show_id,
                "title": session["title"],
                "rating": int(rating_no),
                "rating_by": session["user"]
            }
            rating = mongo.db.ratings
            rating.insert_one(star)
            return render_template("addreview.html")
        except Exception:
            return redirect(url_for("error"))


# Favourite


@app.route('/favourite/<username>/<show_id>', methods=['GET', 'POST'])
def favourite(username, show_id):
    if request.method == "POST":
        # check if already favourited
        existing_favourite = mongo.db.favourites.find_one(
            {"user": session["user"], "favourite": show_id})
        if existing_favourite:
            flash("this is already on your favourites list")
            return redirect(url_for("tvshow", show_id=show_id))
        else:
            try:
                favourite = {
                    "favourite": show_id,
                    "title": session["title"],
                    "user": session["user"]
                }
                fav = mongo.db.favourites
                fav.insert_one(favourite)
                return redirect(url_for("profile", username=session["user"]))
            except Exception:
                return redirect(url_for("error"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
