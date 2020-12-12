# Revuu-IT Flask App
MS3. Project Code Institute - Flask-Revuu-IT - Flask Framework Review app with Login + Register

<img src="https://github.com/Dermomurphy/Flask-Revuu-It/blob/main/static/images/amIresponsiveRevuuIT.png" style="margin: 0;">

### [GitHub Live Heroku Hosted Website](https://github.com/Dermomurphy/Flask-Revuu-It)

Milestone 3 Project: Code Institute: Revuu-IT

 
## Table of Contents
1. [**Project overview**](#project-overview)
2. [**UX**](#ux)
   - [**Concept**](#concept)
 
3. [**Features**](#features)
   - [**Features Left to Implement**](#Features-Left-to-Implement)
 
4. [**Technologies Used**](#technologies-used)

5. [**Testing**](#testing)
   - [**Viewports/Responsiveness**](#Viewports-Responsiveness)
   - [**Functional Testing**](#funtional-testing)
 
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
- User: admin 
- password: 12345

 
## UX

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

 ### Schema
 <img src="https://github.com/Dermomurphy/Flask-Revuu-It/blob/main/static/images/schmea.png" style="margin: 0;">
 


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
    - [jQuery](https://jquery.com/) - is a fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling, animation. The project uses **JQuery** to simplify DOM manipulation as part of Materialize framework.
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
9.  [Metatags](https://metatags.io/) Generation of Meta tag content for social media sharing and SEO. ***TODO***
10. [GoogleFonts](https://fonts.google.com/) - font families from Google.
11. [CKEDITOR](https://www.ckeditor.com/) - Javascript library for adding rich content editing abilities.
12. ![HTML5](https://img.shields.io/static/v1?label=HTML&message=5&color=E34F26&logo=html5&logoColor=ffffff)
    - [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - used for Hyper text markup language.
13. ![CSS3](https://img.shields.io/static/v1?label=CSS&message=3&color=1572B6&logo=css3&logoColor=ffffff)
    - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used for cascading stylesheets.

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

### Functional Testing 
Testing done on VSCode Using Live server.- Mobile responsiveness also tested live via Heroku Live Hosted app.

- All page/card/footer links were tested to open.
- Navigation Buttons and Navbar links tested to navigate to specific pages.
- Various screen sizes also tested from large screen to mobile.
- Scrollable categories tested for each section.
- Reviews Main page - stacking of elements on smaller screens.
- Navbar Hamburger menu showing on mobile.
 
**Media Queries**
Media Queries Break Screens based on Bulma Framework Breakpoints :
- Main Page Header Text reduces in size on smaller screens
- Bulma Framework handles many resizing of Rows and colums based on s/m factors chosen on page HTML.

**PEP8 Compliance**
Python code was checked for PEP8 compliance using [PEP8 Checker](http://pep8online.com/)
**Issues**



## Deployment
Deployed using Heroku accessed via the link below
 - https://flask-revuu-it.herokuapp.com/
    - all content is navigatable via this webpage. You must register and login to access adding/editing reviews
    - Admin user Can access Manage Categories section also.

  **Process**
   1. Created a Github account at https://github.com My account: https://github.com/Dermomurphy

   2. Synced folder on local machine to Github Repo via VsCode: https://github.com/Dermomurphy/Flask-Revuu-It automatic deployment on Heroku
     - Configure Procfie to have web: python app.py

   3. Set environment variables in env.py and on Heroku
       -  ("IP", "0.0.0.0")
       -  ("PORT" , "5000")
       -  ("SECRET_KEY" ,  <USER_SET>)
       -  ("MONGO_URI", <MONGOURI>)
       -  ("MONGO_DBNAME" ,"revuu_data")
       -  ("MAIL_USERNAME" , <USER_EMAIL>)
       -  ("MAIL_PASSWORD" , <USER_PASSWORD>)

   4. Mail Config Settings
       - If you use Gmail as an smtp server you can login with your own username and password. Note third party app access must be granted
       ### SMTP Flaskmail config - Can be found in app.py
       
  



## Credits

### Content
- Main Text Written by Dermot Murphy
- Dublin 360 - [Dublin 360 website](https://dublin-360.com/) for content and images also. (My own Website)
- Google Fonts for font styles; https://fonts.google.com/
- [Bulma CSS Framework](https://bulma.io/)
- W3schools.com: for code used on contact form page and implementation if necessary.[W3Schools](https://www.w3schools.com/)

### Media
- The photos used in this site were mainly originaly obtained from  [Unsplash](https://unsplash.com/) 



### Acknowledgements

- Mentor Adegbenga Adeye:  for site layout inspiration, constructive advice. Github : https://github.com/deye9

- Code Institute : for instructional videos and Tutoring/support slack channel. https://codeinstitute.net/