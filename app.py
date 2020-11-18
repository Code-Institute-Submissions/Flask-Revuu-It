import os
from flask import Flask, render_template, flash, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
import time
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
    reviews = mongo.db.reviews.find()
    categories = mongo.db.categories.find()
    
    return render_template("reviews.html", reviews=reviews, categories=categories)


# custom template filter for timestamp
@app.template_filter('ctime')
def timectime(s):
    return time.ctime(s) # datetime.datetime.fromtimestamp(s)



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
    #direct to login page if not in session
    return redirect(url_for('login'))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if the user exists in the db
        existing_user = mongo.db.users.find_one({
            "username": request.form.get("username").lower()
        })

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                # put user in session cookie
                session["user"] = request.form.get("username").lower() 
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    'profile', username=session["user"]
                ))
            else:
                #invalid Password Match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            #username doesnt exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You are now Logged Out!")
    #Remove user from the session cookies
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    

    if request.method == "POST":
        now = datetime.now()

        review = {
        "category_name" : request.form.get('category_name').lower(),
        "review_title" : request.form.get('review_title'),
        "review_description" : request.form.get('review_description'),
        "ts" : datetime.timestamp(now),
        "star_rating": int(request.form.get('star_rating')),
        "images":{"image_url": request.form.get('image_url')},
        "created_by": session["user"],
        "agree_terms": request.form.get('agree_terms')
        }

        mongo.db.reviews.insert_one(review)
        flash("Review Added Successfully")
        return redirect(url_for('get_reviews'))

    categories = mongo.db.categories.find().sort('category_name',1)
    return render_template("add_review.html", categories=categories)


@app.route("/popular")
def popular():
    popular_reviews = mongo.db.reviews.find(
        {"star_rating":{"$gt":4}}
    )
    categories = mongo.db.categories.find()
    return render_template('popular.html', reviews=popular_reviews,categories=categories)


@app.route("/recent")
def recent():
    latest_reviews = mongo.db.reviews.find().sort("_id",-1).limit(50);
    categories = mongo.db.categories.find()
    return render_template('recent.html', reviews=latest_reviews, categories=categories)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        now = datetime.now()
        submit = {
            "category_name" : request.form.get("category_name").lower(),
            "review_title": request.form.get("review_title"),
            "review_description": request.form.get("review_description"),
            "ts" : datetime.timestamp(now),
            "star_rating": int(request.form.get("star_rating")),
            "images": {"image_url": request.form.get("image_url")},
            "created_by": session["user"],
            "agree_terms": request.form.get("agree_terms"),
        }
        mongo.db.reviews.update({"_id":ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")
    
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    categories = mongo.db.categories.find().sort('category_name', 1)
    return render_template("edit_review.html", review=review, categories=categories)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id":ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("get_reviews"))




if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
