<h1 align="center"><strong>Anto-Restaurant-Booking-System</strong></h1>

<h3 align="center">Full-Stack Project (HTML5, CSS3, Bootstrap, Django, Python, JavaScript, jQuery, PostgreSQL, Cloudinary)</h3>

<br>

**Developer:** Anthony Raj 

**[View live website here]()**  :computer:

# Table of Content
 * [Overview](#overview)
  * [UX](#ux)
    + [Strategy](#strategy)
    + [Scope](#scope)
    + [Structure](#structure-hr-)
    + [Skeleton](#skeleton-hr-)
    + [Surface](#surface-hr-)
      - [Color Scheme](#color-scheme)
      - [Fonts](#fonts)
  * [Agile Methodology](#agile-methodology)
  * [Features](#features)
    + [Existing Features](#existing-features)
      - [Create bookings](#create-bookings)
      - [ContactUs](#contactus)
      - [Menu](#menu)
      - [Profiles](#profiles)
      - [Admin bookings management](#admin)
    + [Future Feature Considerations](#future-feature-considerations)
  * [Responsive Layout and Design](#responsive-layout-and-design)
  * [Tools Used](#tools-used)
    + [Python packages](#python-packages)
  * [Testing](#testing)
  * [Deployment](#deployment)
    + [Deploy on heroku](#deploy-on-heroku)
    + [FORK THE REPOSITORY](#fork-the-repository)
    + [CLONE THE REPOSITORY](#clone-the-repository)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Code](#code)
  * [Acknowledgements](#acknowledgements)


# Overview :

Anto-Restaurant-Booking-System Website was created as Portfolio Project #4 (Full-Stack Toolkit) for Diploma in Full Stack Software Development at [Code Institute](https://www.codeinstitute.net).

Project purpose was to build a full-stack site using agile methodology to plan and design web application using MVC framework and related contemporary technologies. Appplication offers users full CRUD (create, read, update, delete) functionality.

This is a project designed and developed to create a complete experience for the clients of Anto-Restaurant. The clients/guests are given opportunity to create an account, manage their account, create a booking and Edit, Delete.

This project is very much a personal one. This website look exactly as how I imagine my dream restaurant located in my hometown would look like.


## UX
This site was created respecting the Five Planes Of Website Design:<br>
### Strategy<hr>
**User Stories:** <br>

|   EPIC                                |ID|                                User Story                                                   |
| :-------------------------------------|--|:------------------------------------------------------------------------------------------- |
|**CONTENT AND NAVIGATION**             |  ||
|                                       |1A| As a user, I want to see a menu so I can easily navigate through website content |             
|                                       |1B| As a user, I want to see relevant information about the restaurant|
|                                       |1C| As a user, I want the website to have a nice and intuitive design that will match the restaurant's theme|
|**USER REGISTRATION/AUTENTHICATION**   |  || 
|                                       |2A| As a user, I want to be able to register on the website|
|                                       |2B| As a user, I want to be able to authenticate using only email and password|
|                                       |2C| As a user, I want to be able to log out at any time|
|**BOOKING**                            |  ||
|                                       |3A| As a logged-in user, I want to be able to find the available tables for a specific date and time|
|                                       |3B| As a logged-in user, I want to be able to select the table that I want to reserve|
|**MENU**                               |  ||
|                                       |4A| As a user, I want to see the restaurant's menu with details about description, category and price, so that I can make an informed decision|                                  
|**USER PROFILE**                       |  ||
|                                       |5A| As a logged-in user, I want to view a list of my upcoming bookings|
|                                       |5B| As a logged-in user, I want to be able to edit my bookings|
|                                       |5C| As a logged-in user, I want to be able to delete my bookings|
|**ADMIN MANAGE BOOKINGS**              |  ||
|                                       |6A| As a logged-in admin member, I want to see the restaurant's upcoming bookings for the current day sorted by time|
|                                       |6B| As a logged-in admin member, I want to be able to filter bookings by date|
|**CONTACT**                            |  ||
|                                       |7A| As a user, I want to see the restaurant's opening and closing hours|
|                                       |7B| As a user, I want to see location information on the website|
|                                       |7C| As a user, I want to see contact information on the website|

**Project Goal:**<br>
To create a website for Anto-Restaurant that will be beneficial for both clients and staff members which aims to maximise clients/customers experience and staff productivity, ultimately maximising the restaurant's revenue and customer satisfaction

**Project Objectives:**<br> 
* To create a website with a simple and intuitive User Experience design;
* To add relevant content that aims to create a better image/branding of the restaurant;
* To differentiate between client and staff member accounts;
* To implement fully functional features that will ease the staff members' tasks and upgrade clients' experience with the restaurant services;
* To make the website fully responsive, and available and functional on every device.<br><br>

### Scope<hr>
**Simple and intuitive User Experience**<br>
* Ensure the navigation menu is visible and functional at every step;
* Ensure every page has a suggestive name that fits its content;
* Ensure the users will get visual cues and feedback when navigating through pages;
* Create a design that  is clear, precise, engaging and matches the restaurant theme.

**Relevant content**<br>
* Add information about restaurant name, location and contact data;
* Make a clear beautifully designed presentation of the menu elements;
* Create a booking section that is easy to navigate;

**Different client and staff member Accounts**<br>
* Allow clients to add, update or delete bookings their own bookings;
* Allow admin and staff members to add, update or delete bookings;
* Allow admin and staff members to add, update or delete menu items;
* Allow signed in clients access to Profile page;
* Allow access to Manage Bookings page only for staff members type of users;


**Responsiveness**<br>
* Create a responsive design for desktop, tablet and mobile devices.<br><br>

### Structure<hr>
The structure of the website is divided into seven pages but with content depending on authentication and client/admin status <br>
-**Register/Login** pages give the user the possibility to create an account and authenticate for accessing different features. <br>
-**Logout** feature is a modal that helps user exit their current account; <br>
-The **Home** page is visible for both types of users and includes details about the restaurant, and appropriate links to different pages; <br>
-The **Menu** page displays menu details and a food description and Category and price <br>
-The **Booking** page is only available for logged-in users, both clients and staff members; <br>
-**Contact us** contains relevant information visible to all users;

* FLOWCHARTS <br>
The Flowchart for my program was created using <b>pencil</b> and it visually represents how the system works.<br>

[![N|Solid](media/flowchart.png)](media/flowchart.png)<br>

### Skeleton<hr>
**Wireframes**<br>

The wireframes below were created the start of the project building.

The wireframes for mobile and desktop were created with [Balsamiq](https://balsamiq.com/) tool.

**Home Page**

![homepage-mobile](static/wireframes/homepage-wireframe-mobile.png)
![homepage-desktop](static/wireframes/homepage-wireframe-desktop.png)

**Menu Page**

![menu-page-mobile](static/wireframes/menu-wireframe-mobile.png)
![menu-page-desktop](static/wireframes/menu-wireframe-desktop.png)

**Bookings Page**

![bookings-page-mobile](static/wireframes/booking-wireframe-mobile.png)
![bookings-page-desktop](static/wireframes/booking-wireframe-desktop.png)

**Database**<br>

The project uses a cloud-based PostgreSQL database provided by [ElephantSQL](https://www.elephantsql.com/) as a service. ElephantSQL is known for its ease of use, and reliability, and is a popular choice for Django projects that require a PostgreSQL database. It offers a web interface with a console for SQL queries. Database URL including API key is stored as an environment variable in Heroku.
<br>

<summary>Initial Schema</summary>

The diagram below was created before the actual development of the website which led to some changes to the attributes and tables for finding the most relevant and useful ones to be kept. Due to time constraint, I was not able to make an updated version on time, but I will make sure to update this on future releases.

![schema-diagram](media/)

### Surface<hr>
#### Color Scheme
All the colors were selected using the hero image to generate color scheme using coolors (https://coolors.co/generate)

![Colour Scheme](media/colorscheme.jpg)

For consistency and convenience, I created css root variables that I used throughout the project.

![Colour Scheme-root-variables](media/colors_root_variable.jpg)

#### Fonts
* The fonts I used for this site were imported from [Google Fonts](https://fonts.google.com/):<br>
The [Roboto](('https://fonts.googleapis.com/css?family=Roboto:100,200,300,400,500,600,700|Exo:100,200,300,400,500,600,700');) font is the main font used throughout the whole website with Sans Serif as the fallback. Roboto is a clean, modern looking and well known font. It is sourced from Google fonts and it's linked to css document via @import method.

## Agile Methodology

This project was developed utilising the Agile Methodology.
This is the first time I used Agile methodology when planning full-stack Django website with a focus on delivering the basic app functionalities. I prioritized features by labelling them as "must-have" or "could-have" These stories helped to define the features and functionalities that were most important to project's target audience.

As a student solo developer who was learning a lot during development, I faced challenges in estimating the time required for each task and only had a basic concept of what I would create. Therefore, I kept things simple and focused on achievable goals. Aiming for Minimum Viable Product, or MVP.

To keep track of progress, I used Github Projects(https://github.com/users/Anthonyrajlucas/projects/4/views/1). I used a kanban board (https://github.com/users/Anthonyrajlucas/projects/4/views/1?layout=board) 


By using agile methodology, I was able to stay organized and focused on delivering the most important features, while also allowing flexibility for future development. This experience gave me valuable insight and lessons that I can apply to future projects.

![agile-table](media/agile_table.jpg)
![agile-board](media/agile_board.jpg)

## Features
### Existing Features<hr>

### Navbar and main menu

Bootstrap navbar component was used to create the navigation bar. It is always visible and stays fixed at the top of the screen. The navbar consists of the Restaurant logo and links to the main areas of the site (home, menu, contact pages, Login, and Register). 

![navbar-1](media/navbar1.jpg)<br><br>

After Login user can view booking and logout navbar 

![navbar-2](media/navbar2.jpg)<br><br>

### Home page

The user is welcomed with an image of one of the restaurant's favorite menu. Down the page to be greeted with a welcome message and information about the restaurant. And another image of the restaurant interior is present to entice the user even further. All these design were implemented aiming to meet the project goal of building a simple but intuitive and user friendly application.

![homepage](media/home_page.jpg)
<br><br>

#### Create bookings

Every user that is authenticated can access the *Make aBooking* page for making a reservation. This feature provides a form with multiple input fields that appear successively, as steps in completing the booking.

The inputs are validated after the following rules:
  - The Date value should not be less than the current day.
  - Fields cannot be empty.
  - User must choose total table for booking.

    ![create-booking](media/create_booking.jpg)


Upon successful booking, a button confirming the reservation appears to give feedback to the user.

  ![create-booking-success](media/create_booking_success.jpg)

  The user wish to edit and delete the booking 

  ![edit-booking](media/edit_booking.jpg)
  ![delete-booking](media/delete_booking.jpg)

#### Menu 
* On the *Menu* page there is a list with all the menu elements. Every item represents a meal with details such as *Name*, *Image*, *Price*, and *Description*. The list design is simple and attractive.<br>

![menu](media/menu.jpg)

#### Profiles
The users' accounts have been created using the **django allauth** module. This way, information about the current user can be accessed from the template and displayed to confirm that the authentication was successful.<br>
Considering that the website is created for a restaurant, the profile of the user is created to display essential information such as name and email.<br>

![profile](media/profilelogin.jpg)
![profiel-login-success-msg](media/profile_login_success_msg.jpg)

### Footer

The footer consists of copyright info and quick navigation to social media links with icons, allowing guests to connect with the brand on popular social media platforms.
<br><br>
![footer](media/footer.jpg)<br>


## Responsive Layout and Design
The project design has been adapted to all types of devices using Bootstrap predefined breakpoints. For intermediate devices where the design didn't fit accordingly, custom breakpoints were used.

**Breakpoints:**

    - max-width:280px
    - max-width:768px
    - max-width:992px
    - max-width:1024px

**Tested devices:**

    - iPhone SE 
    - iPhone XR 
    - iPhone 11 
    - Samsung Galaxy S20 Ultra 
    - Samsung Galaxy S8 
    - Galaxy Note 2 
    - Galaxy Tab S4

## Tools Used

[GitHub](https://github.com/) - used for hosting the source code of the program<br>
[gitpod](https://gitpod.io/workspaces) - for writing and testing the code locally<br>
[Heroku](https://dashboard.heroku.com/) - used for deploying the project<br>
[Balsamiq](https://balsamiq.com/wireframes/) - for creating the wireframes<br>
[Pencil](https://pencil.evolus.vn/Features.html) - used for creating the Flowchart and Database relational schema<br>
[Favicon.io](https://favicon.io/) - used for generating the website favicon<br>
[Diffchecker](https://www.diffchecker.com/) - used for comparing the code<br>
[TinyPNG](https://tinypng.com/) - for compressing the images<br>
[Grammarly](https://app.grammarly.com/) - for correcting text content<br>
[Font Awesome](https://fontawesome.com/) - for creating atractive UX with icons<br>
[Bootstrap5](https://getbootstrap.com/) - for adding predifined styled elements and creating responsiveness<br>
[Google Fonts](https://fonts.google.com/) - for typography<br>
[JsHint](https://jshint.com/) - used for validating the javascript code<br>
[PEP8 Validator](http://pep8online.com/) - used for validating the python code<br>
[HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - used for validating the HTML<br>
[CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - used for validating the CSS<br>
[Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - for debugging the project<br>
[W.A.V.E.](https://wave.webaim.org/) - for testing accessibility<br>
[Cloudinary](https://cloudinary.com/) - for storing static data<br>
LightHouse - for testing performance<br>

### Python packages

* django 
* gunicorn 
* dj-database-url
* psycopg2
* dj3-cloudinary-storage 
* pylint-django 
* whitenoise
* jinja2 
* django-allauth
* django-crispy-forms 
* django-filter
* pylint 
* dateutils 
* black

## Deployment

The app was deployed to heroku for the first time as soon as  django 
installation was completed to make sure that everything is working correctly.

## Database (ElephangSQL)

1. Navitate to [ElephantSQL website](https://www.elephantsql.com/), log in to your account
2. In top-right corner click on green button "Create New Instance".
3. Enter database name, leave plan field as is, optionaly enter tags.
4. Select region, click on "Review" and then on "Create instance".
5. Go to your dashboard, find newly created database instance, click on it.
6. Copy URL starting with "postgress://"
7. Paste this URL into env.py file as DATABASE_URL value and save the file.

  ```python
  os.environ["DATABASE_URL"] = "postgres://yourLinkFromDatabaseDashboard"
  ```

## Cloudinary

1. Navigate to [https://cloudinary.com/](https://cloudinary.com/) and log in to your account.
2. Navigate to dashboard/console [https://console.cloudinary.com/console/](https://console.cloudinary.com/console/) and copy API Enviroment variable starting with "cloudinary://".
3. Paste copied url into env.py file as CLOUDINARY_URL value and save the file.

```python
os.environ["CLOUDINARY_URL"] = "cloudinary://yourLinkFromCloudinaryDashboard"
```

## Django secret key

In order to protect django app secret key it was set as an environment variable and stored in env.py. Please change your password accordingly.

```python
os.environ["SECRET_KEY"] = "yourSecretKey"
```

## GitHub and Gitpod

Note: Repository was created using Code Institute template: [https://github.com/Code-Institute-Org/gitpod-full-template](https://github.com/Code-Institute-Org/gitpod-full-template)

1. Login to Github and navigate to repository: [https://github.com/Anthonyrajlucas/django-anto-restaurant-booking-system](https://github.com/Anthonyrajlucas/django-anto-restaurant-booking-system)

2. Click on "Fork button" in the upper-right corner and create a new form in your own account.

3. Open your repository in local IDE or using Gitpod. The preferred way is to use [Chrome Gitpod Extension](https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki). When you install an extension, green "Gitpod" button appears in your repository. Click on it to cread a new workspace.

4. Go to workspace terminal and install all requirements using command: "pip install -r requirements.txt". All te packages will be installed. requirements.txt content:

    ```python
    asgiref==3.6.0
    cloudinary==1.32.0
    crispy-bootstrap5==0.7
    dj-database-url==0.5.0
    dj3-cloudinary-storage==0.0.6
    Django<4
    django-allauth==0.52.0
    django-crispy-forms==2.0
    django-social-share==2.3.0
    django-summernote==0.8.20.0
    django-taggit==3.1.0
    gunicorn==20.1.0
    oauthlib==3.2.2
    psycopg2==2.9.5
    PyJWT==2.6.0
    python3-openid==3.2.0
    pytz==2022.7.1
    requests-oauthlib==1.3.1
    sqlparse==0.4.3
    ```

5. Local env.py file should be configured as on example below:

    ```python
    import os

    # Env vars
    os.environ["DATABASE_URL"] = "postgres://yourLinkCopiedFromElephantSQLDashboard"
    os.environ["SECRET_KEY"] = "YourSecretKey"
    os.environ["CLOUDINARY_URL"] = "cloudinary://yourLinkCopiedFromCloudinaryDashboard"


6. In order to save django changes in database migration needs to be made.

7. Use terminal commands:

    ```text
    python3 manage.py makemigrations --dry-run
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

8. Create superuser to access admin area using terminal command (email is optional, password won't be visible when typing, confirm password twice):

    ```text
    python3 manage.py createsuperuser
    ```

9. App can be run in gitpod enviroment using terminal command:

    ```text
    python3 manage.py runserver
    ```

10. Go to Heroku and follow further instructions below.


### Deploy on Heroku

## Heroku

1. Navigate to [https://heroku.com/](https://heroku.com/) login to your account and open dashboard. Click button "New" and select "Create new app" button.

2. Enter app name, I used "django-anto-restaurant-booking"", chose your region and click on "Create app" button.

3. Click on newly created app and go to "Deploy" tab and then to "Deployment method" section. Authorize and connect your GitHub account, then find and select your repository.

4. Go to the "Settings" tab, click on "Reveal Config Vars" and add the following keys and values (all values should be strings without any quotation marks):

    NOTE: DISABLE_COLLECTSTATIC variable should be set to "1" for initial deployment. Before final deployment it should be removed.

    | Key                    | Value                                                            |
    |------------------------|------------------------------------------------------------------|
    | CLOUDINARY_URL         | cloudinary url beginning with cloudinary://                      |
    | DATABASE_URL           | postgress url beginning with postgress://                        |
    | DISABLE_COLLECTSTATIC  | 1                                                                |
    | PORT                   | 8000                                                             |
    | SECRET_KEY             | YourSecretKey, the same as in env.py                             |


5. Return to your Gitpod workspace and navigate to the file"anto_restaurant/settings.py Change allowed hosts including the name of the app that you created in previous steps. In my case, it was django-anto-restaurant-booking.herokuapp.com save the file 

6. Procfile required to run project on Heroku was already created but if you change your app's name please make sure that this change is reflected in Procfile. It can be found in your project's main directory. In my case Procfile looks as below:

    ```python
    web: gunicorn anto_restaurant.wsgi
    ```

7. After adding enviromental variables and editing Procfile project is ready for deployment. In Heroku app's dashboard navigate to "Deploy" tab, scroll down to "Manual deploy" section. Select main branch from dropdown menu and click on "Deploy Branch".

8. **Step required for final deployment:** Navigate again to app's settings, reveal config vars and delete DISABLE_COLLECTSTATIC entry if it was set before.

9. After build is done, you should be able to see the button with the link leading to deployed app. In my case...

### Fork the repository
For creating a copy of the repository on your account and change it without affecting the original project, use<b>Fork</b> directly from GitHub:
- On [My Repository Page](https://github.com/Anthonyrajlucas/django-anto-restaurant-booking-system), press <i>Fork</i> in the top right of the page
- A forked version of my project will appear in your repository<br></br>

### Clone the repository
For creating a clone of the repository on your local machine, use<b>Clone</b>:
- On [My Repository Page](https://github.com/Anthonyrajlucas/django-anto-restaurant-booking-system), click the <i>Code</i> green button, right above the code window
- Chose from <i>HTTPS, SSH and GitClub CLI</i> format and copy (preferably <i>HTTPS</i>)
- In your <i>IDE</i> open <i>Git Bash</i>
- Enter the command <code>git clone</code> followed by the copied URL
- Your clone was created
<hr>

## Credits

- Code Institute [Code Institute course and learning platform](https://codeinstitute.net/) specifically "I Think Therefore I Blog" and "To Do App"

- I use this website to resize my images: (https://picresize.com/)
- W3schools (https://www.w3schools.com/)
- Black - Black is a PEP8-compliant opinionated formatter. Used to format code.

## Media

Images used on the project are taken from here:
- pexels.com
- cloudinary 


## Learning resources

- [Code Institute course and learning platform](https://codeinstitute.net/)
- [The book "Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction To Programming"](https://nostarch.com/pythoncrashcourse2e)
- [Slack](https://codeinstitute.net/de//)
- [W3Schools](https://www.w3schools.com/python/default.asp)
- [Django](https://www.djangoproject.com/) - Django documentation.
- [Bootstrap](https://blog.getbootstrap.com/2022/11/22/bootstrap-5-2-3/) - Bootstrap documentation.
- Documentation of python modules and libraries used in the project.

## Acknowledgements

- My mentor Derek McAuley for helpful feedback and guidance at all stages of the project.
- Code Institute Slack Community for being invaluable knowledge base.

## Disclaimer

- Anto-Restaurant-Booking-System Website was created for educational purposes only.




























