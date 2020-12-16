# Revuu-IT Flask App
MS3. Project Code Institute - Flask-Revuu-IT - Flask Framework Review app with Login + Register

<img src="https://github.com/Dermomurphy/Flask-Revuu-It/blob/main/static/images/amIresponsiveRevuuIT.png" style="margin: 0;">

### [GitHub Repo](https://github.com/Dermomurphy/Flask-Revuu-It)
### [Heroku Live Deployed App](https://flask-revuu-it.herokuapp.com/)

Milestone 3 Project: Code Institute: Revuu-IT

 
## Table of Contents
1. [**Project overview**](#project-overview)
2. [**UX**](#ux)
   - [**Concept**](#concept)
   - [**Database**](#database)
   - [**Schema**](#schema)
 
3. [**Features**](#features)
   - [**Features Left to Implement**](#Features-Left-to-Implement)
 
4. [**Technologies Used**](#technologies-used)

5. [**Testing**](#testing)
   - [**Viewports/Responsiveness**](#Viewports-Responsiveness)
   - [**Functional Testing**](#funtional-testing)
   - [**Database CRUD Operations**](#database-crud-operations)
   - [**Compliance**](#compliance)
   - [**Issues**](#issues)
 
6. [**Deployment**](#deployment)
 
7. [**Credits**](#credits)
   - [**Content**](#content)
   - [**Media**](#media)
   - [**Acknowledgements**](#acknowledgements)
 
---
## Project Overview

A Site developed for MS3 Project in Code Institute. The site consists of a review app based on the Flask Framework.
Users may Register with their own username, email and password. Data is stored in an Atlas MongoDb cluster. Once registered the user may login. A logged in user has the ability to add a new review based on a category of choice. The user may only edit or Delete their own reviews.
The Admin user has the ability to add edit and delete categories and any reviews they may submit.
For demonstration purposese the admin can login using the details below:

 
## UX

### User Stories:
As as User I have the ability to :
1. See Reviews of local places, movies, books, points of interest and any rental accommodation in my area.
2. I Can login to the site creating a  username and secure password.
3. Once logged in I can see my user profile and time and date created . 
4. As a logged in user I have the ability to add any new REviews.  I can select a title, Image URL and write a description using the content editor provided. I can also give this review a star rating out of 5 stars, 5 being the highest mark. I have to agree to our terms of service to post the new review.
5. If I have made a misttake or wish to delete or edit my review I can do so on the reviews page or user profile page to see my reviews. There I have the option to edit or delete any review I have created.

### Admin Stories:
As an Admin I have the ability to : 
1. I can login to the site using the admin username and password.
2. I have the ability to add or delete any reviews I make.
3. I have the credentials to add /Edit or delete Review Categories. Using the manage categories tab.
4. Have the ability to Edit any Category and choose the appropriate styling for that category.

### User Journey:

- The user can add a review by clicking the 'New Review' menu link. They can select a category for their review, a Title , paste an image url hyperlink and add a content edited review description that uses the CKEDITOR. The user must agree to the terms & Conditions and can add a star rating based on their review. Submitting will add the review to the Reviews Page.
- Popular reviews - Any Reviews with a star rating of 4 or above are displayed on this page
- Recent Reviews - Any Review added recently based on the Object_Id in MongoDB are displayed. Most recent are on top.
- Register - A user may register with Revuu-IT using a chosen Username/Email and password. If the username or email is already in the DB an already exists warning is displayed.
- Login - A user may login to the app using their registered username and password.
- If a user tries to access a page they do not have access to they are redirected to the login page.
- If a user is not logged in they cannot see the add review page and profile page. A user not logged in can see the login and register icons and only view reviews. The categories sidebar is also hidden from view.
- If a user is logged in they can see the add review page and profile page. The login and Register icons are also hidden and a logout button is present. The categories sidebar is visible.




### Initial Concept
Link to Initial concept:
- [Concept](https://dermomurphy.github.io/MS3-Mockup/)
  - Bulma framework was used on this project as I had already used Materialize in the MS2 Project. Bulma does lack some UX features that Materialise has like sticky Nav. I still feel it was beneficial to learn a new framework even though it may be lacking in some areas.

## Database
The mongoDB BSON based Collection uses the the online Cloud DB Atlas from Mongo DB trial. The database is based off one database called revuu_data filled with 4 collections: Namely
 - categories
 - newsletter
 - reviews
 - users 

 A JSON representation of each collection can be found here [Schema JSON](https://github.com/Dermomurphy/Flask-Revuu-It/tree/main/static/schema)

 ### Schema 
 <img src="https://github.com/Dermomurphy/Flask-Revuu-It/blob/main/static/images/schema.png" style="margin: 0;">
 


## Features

**Main Review Page** - Review Content with Header Image on each review, Card title, star rating visible in number of stars and review content description.

**Register** - A user may register with the app providing a username/email and password assuming the existing username/email is not already present in database.

**Login** - A user may login providing the correct username and password combination. Access is denied if provided false data. Passwords are hashed in the db using sha256 encrpytion.

**Newsletter Signup** - A user many sign up for Our newsletter. The details are stored in the db and a confirmation email is sent via python to the using flask_mail module.

**Popular Reviews** - A list of popular reviews with a star rating of greater than 3. Limited to 50 Reviews

**Recent Reviews** - A list of Recent reviews sorted by most recent review. Limited to 50 Reviews

**Your Reviews** - Once logged in on users profile the user can see a list of their published reviews.

**Edit/Delete Review** - If a user has created a review they have the ability to edit or delete that review. Once the user session matches the current username. A red icon on each review is shown to the user for deletion with confirmation dialog. A review is deleted from the db if confirmed. The ability to edit a review is also available. In Edit mode all content can be edited and updated on the chosen review only if the user has initially created the review.

**Manage Categories** - Admin User only - Specific to adminstrator only. Admin can see current categories can choose to add edit or delete each category from the database.

**Add/Edit/Delete Category** - Add Category takes the admin to an Add Category Page where they can add the Category name and Tag Colour accordingly based on Bulma Presets. Edit Category can change name and styling of each category. Delete Category with Confirmation dialog to delete the category from the database.





### Features Left to Implement
- Reply to Reviews section - Allow the user to comment on each review.

## Technologies Used

1. [Bulma](https://bulma.io)
    - Built with Bulma CSS framework. 
2. ![jQuery](https://img.shields.io/badge/jQuery-3.5.1-yellowgreen)
    - [jQuery](https://jquery.com/) - is a fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling, animation. The project uses **JQuery** to simplify DOM manipulation.
3.  [MongoDB](https://www.mongodb.com/) - Cloud based Database using BSON format.
4.  [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Python app framework

4.  [Visual Studio Code](https://code.visualstudio.com/): Programming code editor created by Microsoft.
5.  ![Chrome Developer Tools](https://img.shields.io/badge/Chrome%20Dev%20Tools-Google%20Chrome-blue)
    - [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) -  web developer tools built directly into the Google Chrome web browser.
6.  ![Git](https://img.shields.io/badge/Git-----fast--version--control-orange)
    - [Git](https://git-scm.com/) - open source distributed version control system.
7.  ![GitHub](https://img.shields.io/badge/GitHub-Git%20repository%20hosting%20service-lightgrey)
    - [GitHub](https://github.com/) - Web-based hosting service for version control using Git.
8.  [W3CMarkupValidation](https://validator.w3.org/) Tools to assess CSS and HTML validation.
9.  [GoogleFonts](https://fonts.google.com/) - font families from Google.
10. [CKEDITOR](https://www.ckeditor.com/) - Javascript library for adding rich content editing abilities.
11. ![HTML5](https://img.shields.io/static/v1?label=HTML&message=5&color=E34F26&logo=html5&logoColor=ffffff)
    - [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - used for Hyper text markup language.
12. ![CSS3](https://img.shields.io/static/v1?label=CSS&message=3&color=1572B6&logo=css3&logoColor=ffffff)
    - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used for cascading stylesheets.
13. [Visual Paradigm](https://online.visual-paradigm.com/) - Schema Diagrams
14. [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Jinja - Templating language.
15. [Python V3.6.9](https://www.python.org/) - Python Programming language.


## Testing
### Viewports Responsiveness
http://ami.responsivedesign.is/  Used to Test site across multiple viewports:

Desktop
    1600x992px scaled down to scale(0.3181)

Laptop
    1280x802px scaled down to scale(0.277)

Tablet
    768x1024px scaled down to scale(0.219)

Mobile
    320x480px scaled down to scale(0.219) 

**Media Queries**
Media Queries Break Screens based on Bulma Framework Breakpoints :
- Main Page Header Text reduces in size on smaller screens
- Bulma Framework handles many resizing of Rows and colums based on s/m factors chosen on page HTML.

### Functional Testing 
Testing done on VSCode Using Live server - Mobile responsiveness also tested live via Heroku Live Hosted app.

- All page/card/footer links were tested to open.
- Database CRUD operations using PyMongo.
- Navigation Buttons and Navbar links tested to navigate to specific pages.
- Various screen sizes also tested from large screen to mobile.
- Scrollable categories tested for each section.
- Reviews Main page - stacking of elements on smaller screens.
- Navbar Hamburger menu showing on mobile.
- Add Review form Adding reviews to database and listing on reviews page
- Edit Review and Delete buttons showing for relevant logged in users.
- Admin Menu for Categories editing and adding showing and functions for Admin user.
- Popular Reviews shows reviews with rating > 3
- Recent Reviews shows the latest reviews added chronologically.
- Newsletter singup adding to DB and Email confirmation sent to user.
- Logout Button only shown to logged in users.
- Only Logged in users can update or delete their relevant reviews.
- Only Admin can see Categories section and update/Add/Delete Categories.

### Database CRUD Operations

#### Read Operations:
- On the main Get_reviews page an article container is loaded for each review document in the database
- On the popular reviews page an article container is loaded for each review document in the database > 3 stars.
- On the recent reviews page lists all Reviews added chronologically sorted by most recent.
- See All Reviews on Users Profile page lists all Reviews added by that specific users Username.
- Categories are listed on the left sidebar once a user is logged in. Generated from Catgories Collection.

#### Create Operations:
-  When a user signs up, a new user is created in the users collection with username password stored in sha256 format and their associated email and timestamp.
-  When a user adds a new Review the relevant fields are populated from the Add Review View into the database.
-  When the admin user creates a new category  and tag style this is added to the categories collection.
-  MongoDB autopopulates each document with a unique ObjectID BSON object (_id)

#### Update Operations:
- When a user tries to Edit one of their reviews this allows them to edit any data added within the Edit Review Form. 
- An edited review updates the relevant fields within the database and the new content is shown on the main reviews page.
- The Admin user can edit any Categories already listed , change the Category name and tag style associated with it.

#### Delete Operations:
- When a user deletes their review the review is removed from the database.
- When the Admin deletes a category the category is removed from the database.
 
### Compliance

**PEP8 Compliance**
Python code was checked for validity using PEP8 compliance : [PEP8 Checker](http://pep8online.com/)

### Features Left to Implement
 - User can add infinte newsletter singup emails to Database if already exists in database.
 - Admin needs to be able to delete all Reviews.
 - Should have initialised python environment in a penv to minimise requirements file.
 - UserID in users should match created_by in reviews collection not the username for better verificiation and collection data retrieval.
 - Category ID should match to Review Category_id  instead of category_name for better data retrieval.



## Deployment
Deployed using Heroku accessed via the link below
 - https://flask-revuu-it.herokuapp.com/
    - all content is navigatable via this webpage. You must register and login to access adding/editing reviews
    - Admin user Can access Manage Categories section also.

  ### Process
   #### 1: Created a Github account at https://github.com My account: https://github.com/Dermomurphy

   #### 2: Setup Heroku for hosting App.
   1. Create a Heroku account
   2. Create a new app [must have a unique name] and select your region

   #### 3: Synced folder on local machine to Github Repo via VsCode: https://github.com/Dermomurphy/Flask-Revuu-It automatic deployment on Heroku.
   -  Synced folder on local machine to Github Repo via VsCode: https://github.com/Dermomurphy/Flask-Revuu-It

   - To run this code on your local machine, you would go to my respository at https://github.com/Dermomurphy/Flask-Revuu-It and on the home page on the right hand side just above all the files, you will see a green button that says, "Clone or download", this button will give you options to clone with HTTPS, open in desktop or download as a zip file. Then --> click the clipboard item to copy the Https address of the repo.
   - **Open Git Bash/Terminal:**
   - CD into the working directory to the location where you want the cloned directory to be made.you can use mkdir command to make a new directory, then cd into it.
   - Type `git clone`, and then paste the URL: https://github.com/Dermomurphy/Flask-Revuu-It.git Press Enter. The clone is created.
   - For more information about the above process; https://help.github.com/en/github/using-git/which-remote-url-should-i-use


   - Configure Procfile to have content `web: python app.py` in order to deploy app using python on Heroku. 

   #### 4: Set environment variables in env.py locally and on Heroku config variables.
   - Create an env.py file in the apps root directory.
   - Add the env.py file to your .gitignore file
   - In order to deploy in Heroku set Config vars located in settings to below. Click Reveal config vars to input these variables.

   **Set a (KEY, VALUE)**
   - ("IP","0.0.0.0")
   - ("PORT" , "5000")
   - ("SECRET_KEY" ,  **<USER_SECRETKEY>**)
   - ("MONGO_URI", mongodb+srv://root:**<USER_PASSWORD>**@**<USER_CLUSTER>**.tto0e.mongodb.net/**<USER_DB_NAME>**?retryWrites=true&w=majority)
   - ("MONGO_DBNAME" ,**<USER_DB_NAME>**)  current 'revuu_data'
   - ("MAIL_USERNAME" , **<USER_EMAIL>**)
   - ("MAIL_PASSWORD" , **<USER_MAIL_PASSWORD>**)

   #### 5: Mail Config Settings.
   - If you use Gmail as an smtp server you can login with your own username and password. 
   - Note third party app access must be granted.
   - SMTP Flaskmail config :Can be found in [app.py](https://github.com/Dermomurphy/Flask-Revuu-It/blob/main/app.py)
   
   #### 6: Requirements.
   1. Using a terminal window command prompt input  `pip3 freeze --local > requirements.txt` to create a requirements.txt file in order for Heroku to install all requirements necessary.


   #### 7: Pushing files to Heroku hosted. 
   1. In the terminal window type in `heroku login` and fill in your heroku credentials and password
   2. Commit all your files and type in the same terminal window `git push heroku master`. 

   #### 8: Open Deployed App in Heroku.
   1. Click on **Open app** in the Heroku account, the application will open in a new tab within the browser
  

   #### 9: How to Run the App locally.
   1. Open your terminal command window
   2. Syncing from Github - As outlined above in Process 3
   3. Install the requirements by typing `pip3 install -r requirements.txt` in your CLI
   4. Create a Database in MongoDB:
        Create or login to a MongoDB account.
        Create a new project Name.
        Add a new cluster to this prpoject give it a unique name.
        - create a new database, name it accordingly (revuu_data) and create these three collections:
            * categories
            * users
            * reviews
            * newsletter
        - Populate the categories collection with Key Value pairs outlined below:
            * category_name: (String)
            * tag_style: (String)
        - Populate the reviews collection with key value pairs outlined below:
            * category_name: (String)
            * review_title: (String)
            * review_description: (String)
            * ts: (Double)
            * star_rating: (Int32)
            * images: (Object of Strings)
                * image_url: (String)
            * created_by: (String)
            * agree_terms(String)
        -  Populate the users collection with the key value pairs outlined below:
            * username: (String)
            * email: (String)
            * password: (String)
            * ts: (double)
        -  Populate the newsletter collection with the key value pairs outlined below:
            * first_name: (String)
            * last_name:(String)
            * newsletter_email:(String)
            * newsletter_terms: (String)
            * registered: (String)
            * created_by: (String)         
   5. Adding local enviroment varibales:
    - Go to MongoDB and copy the srv link to your database (go to "Command Line Tools", "Connect Instruction", "Connect your application" and copy the link).
    - To the env.py add the secret key and MongoDB URI:
    - add the environment variables below to your env.py file:

        * os.environ.setdefault("IP", "0.0.0.0")
        * os.environ.setdefault("PORT", "5000")
        * os.environ.setdefault("MONGODB_URI", "mongodb+srv://root:**<USER_PASSWORD>**@**<USER_CLUSTER>**.tto0e.mongodb.net/**<USER_DB_NAME>**?retryWrites=true&w=majority")
        * os.environ.setdefailt("SECRET_KEY"], <SECRET_KEY>)
        * os.environ.setdefault("MAIL_USERNAME", <USER_EMAIL>)
        * os.environ.setdefault("MAIL_PASSWORD", <USERMAIL_PASSWORD>)



   6. Type in `python3 app.py` in the CLI to run the app. Open a web browser and point it to localhost 0.0.0.0:5000 (port 5000)
       
  
## Credits

### Content
- Main Text Written by Dermot Murphy
- Dublin 360 - [Dublin 360 website](https://dublin-360.com/) for content and images also. (My own Website)
- Google Fonts for font styles; https://fonts.google.com/
- [Bulma CSS Framework + Themes](https://bulma.io/)
- W3schools.com: for code used on contact form page and implementation if necessary.[W3Schools](https://www.w3schools.com/)

### Media
- The photos used in this site were mainly originaly obtained from  [Unsplash](https://unsplash.com/) 



### Acknowledgements

- Mentor Adegbenga Adeye:  for site layout inspiration, constructive advice. Github : https://github.com/deye9

- Code Institute : for instructional videos and Tutoring/support slack channel. https://codeinstitute.net/