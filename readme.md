# Revuu-IT Flask App
MS3. Project Code Institute - Flask-Revuu-IT - Flask Framework Review app with Login + Register

<img src="" style="margin: 0;">

### [GitHub Live Heroku Hosted Website](https://github.com/Dermomurphy/Flask-Revuu-It)

Milestone 3 Project: Code Institute: Revuu-IT

 
## Table of Contents
1. [**Project overview**](#project-overview)
2. [**UX**](#ux)
   - [**Wireframe**](#wireframe)
 
3. [**Features**](#features)
   - [**Existing Features**](#existing-features)
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
User: admin 
password: 12345

 
## UX

- The user can add a review by clicking the 'New Review' menu link. They can select a category for their review, a Title , paste an image url hyperlink and add a content edited review description that uses the CKEDITOR. The user must agree to the terms & Conditions and can add a star rating based on their review. Submitting will add the review to the Reviews Page.
- Popular reviews - Any Reviews with a star rating of 4 or above are displayed on this page
- Recent Reviews - Any Review added recently based on the Object_Id in MongoDB are displayed. Most recent are on top.
- Register - A user may register with Revuu-IT using a chosen Username/Email and password. If the username or email is already in the DB an already exists warning is displayed
- Login - A user may login to the app using their registered username and password.


### Initial Concept
Link to Initial concept:
- [Wireframe](https://dermomurphy.github.io/MS3-Mockup/)

## Features

**Main Home Page** - Main Content Cards for Home Brews Selected |  ABV and IBU Selection sliders with Get Recipe Buttons | Random Beer Recipe Generated on page refresh.

**Brew Calculator Page** - 2 Brewing Calcuators one for ABV calcuation the other for Priming sugar calculation.

**Contact Page** - Main Contact form for Contacting Brewpunk with message ,reply email, first name and last name fields.
 
### Existing Features
- **Links to Sections** - Quick Navbar + Bottom right corner pop out links to Each Page. Also on Footer.
- **Reandom Beer Recipe Generated** - Featured Beer Recipe randomly generated on page refresh.
- **ABU Slider** - ABU slider operational to choose deisred Alcohol by volume %.
- **IBU Slider** - IBU slider operational to choose deisred Bitterness Level.
- **Get Recipe Buttons** - Each button links to Generated Card Content based on IBU and ABV selection levels. Data fetched from PunkAPI
- **Contact Form** - A way to send a suggestion  or send a generic message to us.
- **Footer Section** - Showcases Company Bio - Page links and Social media content
- **Social Media Links** - Links to all social media content in footer.
- **Made With Materialize** - Link in footer to Materialize framework Documentation



### Features Left to Implement
- Reply to Reviews section

## Technologies Used

1. [Bulma](https://bulma.io)
    - Built with Bulma CSS framework. 
2. ![jQuery](https://img.shields.io/badge/jQuery-3.5.1-yellowgreen)
    - [jQuery](https://jquery.com/) - is a fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling, animation. The project uses **JQuery** to simplify DOM manipulation as part of Materialize framework.
3. [MongoDB]()
4. [Flask]()

4.  [Visual Studio Code](https://code.visualstudio.com/): Programming code editor created by Microsoft.
5.  ![Chrome Developer Tools](https://img.shields.io/badge/Chrome%20Dev%20Tools-Google%20Chrome-blue)
    - [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) -  web developer tools built directly into the Google Chrome web browser.
6.  ![Git](https://img.shields.io/badge/Git-----fast--version--control-orange)
    - [Git](https://git-scm.com/) - open source distributed version control system.
7.  ![GitHub](https://img.shields.io/badge/GitHub-Git%20repository%20hosting%20service-lightgrey)
    - [GitHub](https://github.com/) - Web-based hosting service for version control using Git.
8.  [W3CMarkupValidation](https://validator.w3.org/) Tools to assess CSS and HTML validation.
9.  [Metatags](https://metatags.io/) Generation of Meta tag content for social media sharing and SEO.
10. [GoogleFonts](https://fonts.google.com/) - font families from Google.
11. [CKEDITOR](https://www.ckeditor.com/) - Javascript library for adding rich content editing abilities.
13. ![HTML5](https://img.shields.io/static/v1?label=HTML&message=5&color=E34F26&logo=html5&logoColor=ffffff)
    - [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - used for Hyper text markup language.
14. ![CSS3](https://img.shields.io/static/v1?label=CSS&message=3&color=1572B6&logo=css3&logoColor=ffffff)
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
Testing done on VSCode Using Live server.- Mobile responsiveness also tested live

- All page/card/footer links were tested to open in seperate window.
- Navigation Buttons and Navbar links tested to navigate to specific pages.
- Various screen sizes also tested from large screen to mobile.
- Scrollable categories tested for each section.
- Caclulator/Main page - stacking of elements on smaller screens.
- Navbar Hamburger menu showing on mobile.

1. Main/Index Page:
    1. Slide ABU slider to see if Get Recipe (yellow) button updates values - Get Recipes button Generates Media Cards with Brewdog recipes for all ABU > than the selected values of ABV %
    2. Slide IBU slider to see if Get Recipe (Red) button updates values - Get Recipes button Generates Media Cards with Brewdog recipes for all ABU > than the selected values of IBU Bitterness level
    3. Slide ABU slider & IBU slider to see if Get Recipe (Green) button updates values - Get Recipes button Generates Media Cards with Brewdog recipes for all ABU > & IBU > than the selected values of ABV + IBU combined.

2. Brew Calculator Page - ABV Calc:
    1. Add initial gravity and final gravity readings. Number content only. Text content generates red error
    2. Calculate ABV % generates correct Alcohol %age based on IG and FG readings.
    3. Reset ABV button generates alert and removes any values present on input fields and textarea
3. Brew Calculator Page - Priming Sugar Calc:
    1. Add initial volume of Beer in Gallons / Temperature of Beer and Volumes of C02 based on style table volumes. Number content only. Text content generates red error
    2. Dropdown menu for sugarType displays correctly and is fed into Priming sugar calculator. Switch case function used to selext Sugar Factor.
    3. Calculate Priming Sugar in Grams generates correct sugar volume based on chosen sugar type.
    4. Reset ABV button generates alert and removes any values present on input fields and textarea

4. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears ....TODO!
    3. Try to submit the form with an invalid email address type and verify that a relevant error appears
    4. Try to submit the form with all inputs valid and verify that a the form Success page message appears. email is sent to my personal email address.
 
**Media Queries**
Media Queries Break Screens smaller than 960px:
- Main Page Header Text reduces in size on smaller screens
- Materialize Framework handles many resizing of Rows and colums based on s/m factors chosen on page HTML.

**Issues**
- Current: Priming sugar Calculator only calculates in imperial measurements currently.
- Resolved: Banner text was impeded display download of DIYDOg recipeds pdf. Media Query added to reduce text size.


## Deployment
Deployed using GitHub Pages accessed via the link below
 - https://dermomurphy.github.io/BrewPunk-CI/
 index.html is main content page - all other navigatable via this webpage

  **Process**
   1. Created a Github account at https://github.com My account: https://github.com/Dermomurphy

   2. Synced folder on local machine to Github Repo via VsCode: https://github.com/Dermomurphy/BrewPunk-CI

   3. To publish the project to see it on the web go to Settings on Repo , scroll down to the heading, GitHub Pages. Under the Source setting, Use drop-down menu to select master branch as a publishing source and save. Refreshed the github page, and you are then given a url where your page is published; The site is now published on gitHub pages at https://dermomurphy.github.io/BrewPunk-CI/

   4. To run this code on your local machine, you would go to my respository at https://github.com/Dermomurphy/BrewPunk-CI and on the home page on the right hand side just above all the files, you will see a green button that says, "Clone or download", this button will give you options to clone with HTTPS, open in desktop or download as a zip file. Then --> click the clipboard item to copy the Https address of the repo.
   Open Git Bash/Terminal: 
   CD the working directory to the location where you want the cloned directory to be made.you can use mkdir command to make a new directory, then cd into it.Type git clone, and then paste the URL: https://github.com/Dermomurphy/BrewPunk-CI.git Press Enter. The clone is created.
   For more information about the above process; https://help.github.com/en/github/using-git/which-remote-url-should-i-use

## Credits

### Content
- Main Text Written by Dermot Murphy
- 
- Google Fonts for font styles; https://fonts.google.com/
- [Bulma CSS Framework](https://bulma.io/)
- W3schools.com: for code used on contact form page and implementation if necessary.[W3Schools](https://www.w3schools.com/)

### Media
- The photos used in this site were obtained  [Unsplash](https://unsplash.com/) [Markusspiske](https://unsplash.com/@markusspiske) + [DIY DOG](https://www.brewdog.com/uk/community/diy-dog)
- Main Images on Recipe Cards taken from PunkAPI.


### Acknowledgements
- PunkAPI - MAin API for generation of content
- https://www.brewersfriend.com/beer-priming-calculator/ - Aided in formula for generation of Priming sugar calculator

- Mentor Adegbenga Adeye:  for site layout inspiration, constructive advice. Github : https://github.com/deye9

- Code Institute : for instructional videos and Tutoring/support slack channel. https://codeinstitute.net/