import os
from flask import Flask, render_template, flash, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from flask_mail import Mail, Message
from functools import wraps
import time
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
   import env


app = Flask(__name__)

mail= Mail(app)

app.config['MONGO_DBNAME'] = os.environ.get("MONGODB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
#smtp Flaskmail config
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

mongo = PyMongo(app)



#Main reviews View
@app.route("/")
@app.route("/get_reviews")
def get_reviews():
    # Get all reviews from Database
    reviews = mongo.db.reviews.find()
    categories = mongo.db.categories.find()
    
    return render_template("reviews.html", reviews=reviews, categories=list(categories))


# custom template filter for timestamp
@app.template_filter('ctime')
def timectime(s):
    return time.ctime(s) # datetime.datetime.fromtimestamp(s)


#Register
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
       
        #submit new user object
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


#Login decorator - To disable pages for non logged in users.
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" in session:
            return f(*args, **kwargs)
        else:
            flash("Please Login to Access")
            return redirect(url_for("login", next=request.url))
    return decorated_function


#Profile based on username
@app.route('/profile/<username>', methods=["GET", "POST"])
@login_required
def profile(username):
    #Get the session username from DB
    username = mongo.db.users.find_one(
        {'username': session["user"]})['username']

    email = mongo.db.users.find_one(
        {'username': session["user"]})['email'] 
    timestamp = mongo.db.users.find_one(
        {'username': session["user"]})['ts'] 

    date_time = datetime.fromtimestamp(timestamp)
    readable_dt = date_time.strftime("Created: %m/%d/%Y @ Time: %H:%M:%S") # display readable date and Time
	# render profile if user logged in
    if session["user"]:
       return render_template('profile.html', username=username, email=email, readable_dt=readable_dt)
    #direct to login page if not in session
    return redirect(url_for('login'))

#Login
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

#logout
@app.route("/logout")
@login_required
def logout():
    flash("You are now Logged Out!")
    #Remove user from the session cookies
    session.pop("user")
    return redirect(url_for("login"))

#Add a new review
@app.route("/add_review", methods=["GET", "POST"])
@login_required
def add_review():
    

    if request.method == "POST":
        now = datetime.now()
        # Review object - Get data from Form
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

#popular Reviews
@app.route("/popular")
def popular():
    #display popular reviews greater than 3 Limit to 50 Reviews
    popular_reviews = mongo.db.reviews.find(
        {"star_rating":{"$gt":3}}
    ).limit(50)
    
    categories = mongo.db.categories.find()

    return render_template('popular.html', reviews=popular_reviews,categories=list(categories))

#Your Reviews
@app.route("/your_reviews")
@login_required
def your_reviews():
    #display users reviews
    your_reviews = mongo.db.reviews.find(
        {"created_by": session["user"].lower()}
    )
    categories = mongo.db.categories.find()

    return render_template('your_reviews.html', reviews=your_reviews,categories=list(categories))

#Recent Reviews
@app.route("/recent")
def recent():
    latest_reviews = mongo.db.reviews.find().sort("_id",-1).limit(50);
    categories = mongo.db.categories.find()
     
    return render_template('recent.html', reviews=latest_reviews, categories=list(categories))

#edit a review
@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
@login_required
def edit_review(review_id):
    if request.method == "POST":
        now = datetime.now()
        # get submit data from edit form
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
        #updated edited review
        mongo.db.reviews.update({"_id":ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")
        return redirect(url_for("get_reviews"))
    
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    categories = mongo.db.categories.find().sort('category_name', 1)
    return render_template("edit_review.html", review=review, categories=categories)

#Delete a review
@app.route("/delete_review/<review_id>", methods=["GET","POST"])
@login_required
def delete_review(review_id):
    if request.method == "POST":
        # confirm deletion
        if request.form.get("deleteConfirm") == "Yes":
            mongo.db.reviews.remove({"_id":ObjectId(review_id)})
            flash("Review Successfully Deleted")
            return redirect(url_for("get_reviews"))
        else:
            flash("Operation Cancelled")
            return redirect(url_for("get_reviews"))
       

#Show Categories
@app.route("/get_categories")
@login_required
def get_categories():
    categories = mongo.db.categories.find().sort('category_name',1)
    return render_template("categories.html", categories=categories )

#Add a category
@app.route("/add_category", methods=["GET", "POST"])
@login_required
def add_category():
    # Tag Styles for Categories
    tag_styles = {
        "Blue": "is-info",
        "Black": "is-black",
        "Dark": "is-dark",
        "Light": "is-light",
        "White": "is-white",
        "Primary": "is-primary",
        "Link": "is-link",
        "Success": "is-success",
        "Yellow": "is-warning",
        "Red": "is-danger",
    }

    if request.method == "POST":
        category =  {
            "category_name": request.form.get("category_name").lower(),
            "tag_style": request.form.get("tag_style").lower()
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for('get_categories'))

    return render_template("add_category.html", tag_styles=tag_styles)

#Edit Category based on ID
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
@login_required
def edit_category(category_id):
    # Category Styles
    tag_styles = {
        "Blue": "is-info",
        "Black": "is-black",
        "Dark": "is-dark",
        "Light": "is-light",
        "White": "is-white",
        "Primary": "is-primary",
        "Link": "is-link",
        "Success": "is-success",
        "Yellow": "is-warning",
        "Red": "is-danger",
    }

    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "tag_style": request.form.get("tag_style").lower()
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit )
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template('edit_category.html', category=category, tag_styles=tag_styles)


#Delete a review
@app.route("/delete_category/<category_id>", methods=["GET","POST"])
@login_required
def delete_category(category_id):
    if request.method == "POST":
        #Delete Confirmation
        if request.form.get("deleteConfirm2") == "Yes":
            mongo.db.categories.remove({"_id":ObjectId(category_id)})
            flash("Category Successfully Deleted")
            return redirect(url_for("get_categories"))
        else:
            flash("Operation Cancelled")
            return redirect(url_for("get_categories"))
      


#Newsletter signup and Mail confirmation
@app.route("/newsletter", methods=["GET", "POST"])
def newsletter():
        # check if session user exists
    try:
        if session["user"]:
            created_by = session["user"]
            user_email = mongo.db.users.find_one({"username":created_by})["email"]
    except:
            created_by = "Not Registered"
            user_email = ""
  
    
    
    if request.method == "POST":
        submit = {
                "first_name": request.form.get("first_name").lower(),
                "last_name": request.form.get("last_name").lower(),
                "newsletter_email": request.form.get("newsletter_email").lower(),
                "newsletter_terms": request.form.get("newsletter_terms"),
                "registered": request.form.get("registered"),
                "created_by": created_by
            }

        mongo.db.newsletter.insert_one(submit)
        flash("Newsletter Signup Successful")
        # Send Email to  Email on form newsletter
        send_to = request.form.get('newsletter_email')
        msg = Message('Hello', sender = 'info@dublin-360.com', recipients = [send_to])
        msg.body = "Hello {} {} ,Thank you for registering to Revvuu-IT".format(request.form.get('first_name'),request.form.get('last_name'))
        mail.send(msg)
        flash("Mail Sent to {}".format( request.form.get('newsletter_email') ))
        

    return render_template('newsletter.html', user_email=user_email)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
