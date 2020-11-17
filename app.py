import os
from flask import Flask, render_template, flash, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
   import env


app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get("MONGODB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_reviews")
def get_reviews():
    reviews = list(mongo.db.reviews.find())
    
    return render_template("reviews.html", reviews=reviews)


@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        # Check if hte username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
        existing_email = mongo.db.users.find_one({
            "email": request.form.get("email").lower()
        })

        if existing_user or existing_email:
            flash('Username or Email Already Exists!')
            return redirect(url_for('register'))
        # current date and time
        now = datetime.now()
        timestamp = datetime.timestamp(now)
       

        new_user_submit = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash( request.form.get("password"),method='pbkdf2:sha256', salt_length=8),
            "ts": timestamp
        }

        mongo.db.users.insert_one(new_user_submit)

        # Add the new user inito 'session' cookie
        session["user"] = request.form.get('username').lower()

        flash('Registration Successful!')
        return redirect(url_for('profile', username=session["user"]))



    return render_template("register.html")


@app.route('/profile/<username>', methods=["GET", "POST"])
def profile(username):
    #Get the session username from DB
    username = mongo.db.users.find_one(
        {'username': session["user"]})['username']

    email = mongo.db.users.find_one(
        {'username': session["user"]})['email'] 
    timestamp = mongo.db.users.find_one(
        {'username': session["user"]})['ts'] 

    date_time = datetime.fromtimestamp(timestamp)
    readable_dt = date_time.strftime("Created: %m/%d/%Y @ Time: %H:%M:%S")
	
    if session["user"]:
       return render_template('profile.html', username=username, email=email, readable_dt=readable_dt)
    #shoul be redirext to login change
    return redirect(url_for('get_reviews'))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
