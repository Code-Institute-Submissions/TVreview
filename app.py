import os
from flask import Flask, render_template, url_for, redirect, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
