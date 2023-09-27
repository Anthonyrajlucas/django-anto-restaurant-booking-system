# Testing

Back to [README.md](README.md)<br>

## Table of contents
* [User Story and Feature Testing](#user-story-and-feature-testing)
* [Automated View Testing](#automated-view-testing)
* [Browser Testing](#browser-testing)
* [Functionality Testing](#functionality-testing)
* [Code Validation](#code-validation)
* [Bugs](#bugs)

## User Story and Feature Testing
All the user stories were tested manually, that including all the representative features, and were described below with a summary of the steps made for demonstrating the validation of the tests: <br>

### CONTENT AND NAVIGATION

#### 1A: As a user, I want to see a navigation menu so I can easily navigate through website content  
* **Acceptance Criteria:** A site user should always have access to the navigation menu so he can easily switch between pages at any time.
* **Summary:**<br>
    -When a user visits the website he can easily see the navigation menu at the top of the page;<br>
    -Even if switching the pages, the menu is always present at the top and indicates what page is currently active;<br>
    -For the *Home* page, a *Back to top* button is present at the end of the content,(considering screen sizes can vary depending on device used,) and redirects the user to the top of the page where he can access the navigation links;<br>
    -For logged-in clients, the menu contains an additional page, *Booking*, and *Logout* link replaces *Register* and *Login* pages;<br>
       *By testing all these features, it can be affirmed that the user story is accomplished.*<br>
* **Outcome:** Pass

#### 1B: As a user, I want to see relevant information about the restaurant
* **Acceptance Criteria:** A site user should be able to see relevant information about the restaurant.
* **Summary:**   
-When a user first visits the website, he is redirected to the *Home* page and a big cover with a noodle with egg dish background is displayed;
-The cover also displays information about the welcome with name and slogan of the restaurant;
-"About us" is a section on the *Home* page that describes the restaurant and another image of the restaurant interior;
-More information about the restaurant specialities and contact details can be found on the *Menu* and *contact us* pages.

By testing all these features, it can be affirmed that the user story is accomplished.
•	Outcome: Pass


#### 1C: As a user, I want the website to have a nice and intuitive design that will match the restaurant's theme
* **Acceptance Criteria:**  A site user should be able to access the content through an attractive design that would make him want to return to it anytime.
* **Summary:**<br>
    -When a user first visits the website he is redirected to *Home page* where the first impression is created when noticing the well-chosen fonts chosen for the navbar, title and slogan, as well as the cover image<br>
    -The colours of the website were tested to match the contrast requirements and all the colours chosen were generated from the colours' palette of the background cover<br>
    -Throughout the site there are elements created to help the user have a better experience when when navigating through the content<br>
    -On the Home suggest to the user to Register or Login to enjoy all the features of the website;<br>
    -The user gets button popup every time he performs an action such as Registering, Signing In/Signing Out, adding a booking<br><br>

    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br>
* **Outcome:** Pass 

### USER REGISTRATION/AUTENTHICATION
#### 2A: As a user, I want to be able to register on the website
* **Acceptance Criteria:** A site user should be able to create an account by filling in a form on the website.   
* **Summary:**<br>
    -There is a Register page that provides a form with email and password for the user to fill in;<br>
    -When the user submits the form a new entry is created in the Users table;<br>
    -A success message is displayed with the message "Logged in as..." that confirms to the user that he has been registered successfully.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass 

#### 2B: As a user, I want to be able to authenticate using only email and password
* **Acceptance Criteria:** A site user should be able to authenticate at any time with email and password.
* **Summary:**<br>
    -There is a Login page that provides a form with email and password to be filled;<br>
    -The authentication form has a "Remember me" checkbox that will keep the user logged in;<br>
    -A success alert is displayed with the message "Logged in as..." that confirms to the user that he has been logged in successfully.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### 2C: As a user, I want to be able to logout at any time
* **Acceptance Criteria:** A site user should be able to exit current account at any time.
* **Summary:**    
    -There is a Logout modal that can be triggered when clicking on the hyperlink in the navbar. The modal is implemented as part of defensive programming;<br>
    -The logout modal asks the user again if he wishes to exit the current account;<br>
    -A success button message is displayed with the message "You have signed out" that confirms to the user that he has been successfully logged out.<br><br>
    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** pass

### BOOKING
#### 3A: As a logged in user, I want to be able to book a reservation for a specific date, time and number of table
* **Acceptance Criteria:** A logged user should be provided a booking system that generates the table  
* **Summary:**<br> 
    -There is a booking page that can be accessed only by authenticated users, considering that all the booking entries must have the current user as the author;<br>
    -The booking sections appear successive only after the previous ones are validated;<br>
    -The first section contains inputs for Date, Start and End time, for the user to fill in;<br>
    -The validation of these values is very strict to prevent errors when generating the tables section. The following rules are being checked:
    * All the fields must be filled.<br>
    * The Date value should not be less than the current day;<br>
    * The user must choose from the available time slots provided. <br>

    - If the validation is complete, and the user submits the form, a successful feedback in a form of a button message is provided; But if there's no available table for the capacity required a message feedback is also given and the guest cannot proceed with the booking.<br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass


### MENU
#### 4A: As a user, I want to see the restaurant's menu with details about image,description and price, so that I can be completely aware of everything I want to order
* **Acceptance Criteria:** A user should be provided with a list of the menu content, as essential information for a restaurant client.
* **Summary:**<br>
    -There is a *Menu* page that can be accessed by any type of user;<br>
    -A list of meals is displayed and it is visible to any type of user;<br>
    -Every menu item is provided with an image of the meal, name, description and price;<br>
    -All images have the same dimensions, with transparent backgrounds, and prices are in bold, for better visual impact.<br><br>
    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### 5B: As a logged in user, I want to be able to edit or delete my bookings
* **Acceptance Criteria:** A logged in user should be provided a way to edit or delete a booking if he no longer wishes to keep it. 
* **Summary:**<br>
    -In the Bookings page, the user is presented with all the bookings information in a form of a table.
    -All the field information on this table can be updated via an 'edit' button.
    -Bookings can also be deleted via a 'delete' button. 

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

### ADMIN MANAGE BOOKINGS
#### 6A: As a logged in admin member, I want to see the restaurant's upcoming bookings sorted by booking date and time
* **Acceptance Criteria:** A logged in admin member should be able to see all bookings from all the users via admin panel   
* **Summary:**<br>
    -There is a *Manage Bookings* page with all the bookings are visible only for logged-in admin members;<br>
    -The page displays all the bookings for the current day sorted by time, which is very helpful for a staff member that wants to take a look over today's reservations;<br>
    -The bookings are listed in a table and every column represents an important detail such as Date, Time, Number of table, and Customer name;<br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

### CONTACT US
#### 7A: As a user, I want to see the restaurant's opening and closing hours
* **Acceptance Criteria:** A site user should be provided information about opening and closing hours for every day.
* **Summary:**<br>  
    -There is a page called "Where to find us" visible to any type of user;<br>
    -The page displays a container with the timetable for every day of the week;<br>
    -The timetable has a simple and attractive design and the information is clear.<br><br>

     *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 7B: As a user, I want to see location information on the website
* **Acceptance Criteria:** A site user should be provided information about restaurant's location.
* **Summary:**<br>
    -On the "Where to find us" page there is a google map with a marker pointed to the restaurant's location;<br>
    -Also there is an informative text with the address of the restaurant;<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 7C: As a user, I want to see contact information on the website
* **Acceptance Criteria:** A site user should be provided the restaurant's contact information.
* **Summary:**<br> 
    -On the "Where to find us" page there is a section with contact information;<br>
    -The section displays the phone number and contact email for the restaurant.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

### Aditional Manual Testing
  
#### Interface Interaction

* Ensure all interactive elements respond appropriately:
    - **Desktop:**
        - All navbar elements correctly respond to hovering.
        - All buttons correctly respond to hovering.
        - All authentication links correctly respond to hovering
    - **Mobile:**
        - All navbar elements correctly respond to touch.
        - All buttons correctly respond to touch.
        - All authentication links correctly respond to touch

#### Links

* Ensure the external links to social media present in the footer open up in new tabs.

## Functionality testing

Comprehensive testing has been conducted to ensure that all website functionalities are working as intended, providing users with a reliable and enjoyable browsing experience.

| Functionality | What's being tested | Result |
|------|-------------|--------|
| Registration | A new user can create an account successfully. | Pass |
|  | The website displays an appropriate error message with hint when validation fails. | Pass |
|  | The website displays an appropriate message if link is invalid or token expired | Pass |
|  | User is signed in automatically when click confirm button | Pass |
| Admin Panel | Admin can login to admin panel. | Pass |
|  | Admin can add, edit and delete bookings. | Pass |
|  | Admin can add edit and delete menu items. | Pass |
|  | Admin can add and delete tables. | Pass |
|  | Admin can delete users. | Pass|
|  | Admin panel can be accessed by user| Pass |
|Login | A registered user can log in successfully. | Pass |
|  | The website displays an appropriate error message when a user enters an incorrect email or password. | Pass |
|  | A logged-in user can sign out successfully. | Pass |
|  | The website displays an appropriate error message when a user enters invalid data (e.g., date before current day, not allowed charset). | Pass |
|  | A user cannot edit or delete another user's profile | Pass |
|Bookings CRUD | Verify that a logged-in user can create, edit delete his own bookings. | Pass |
|  | Confirmation message is displayed when changes are saved | Pass |
|  | User is asked for confirmation before deleting booking| Pass |
|  | Click on delete confirmation button deletes bookings | Pass |
|  | A user can delete own bookings | Pass |
|  | Only authenticated users can book reservations | Pass |
|  | Confirmation message is displayed when booking is updated or deleted | Pass |
|Menu| A logged-in admin can add, edit or delete menu items. | Pass |

## Code Validation
### HTML

The html code of the website was validated using [W3 Markup Validator](https://validator.w3.org/).<br>

For pages that require authentication, I used the "validate by direct input" method with source code.<br>
At the time of deployment the validation have the following outcome:<br><br>


![html-validation](media/)




The following pages have been tested by direct input:
* Home
* Menu
* booking
* contactus
* Manage bookings
* Login/Register/Logout

| Template | Validation Result |  Final validation
|--------|-----------|---------|
| base.html | no errors | pass|
| menu.html | no errors | pass |
| booking.html | no errors | pass |
| contact.html | no errors | pass|
| signup.html | no errors | pass |
| logout.html | no errors | pass |
| login.html | no errors | pass |

### CSS

The CSS code was validated using [W3 Jigsaw Validator](https://jigsaw.w3.org/css-validator/)<br>
At the time of deployment the validation for *style.css* has the following outcome:<br><br>


![css-validation](media/W3C-css-validation.jpg)

### Python
The python code was tested using [PEP8ci](https://pep8ci.herokuapp.com/) validator.<br>

**Pep8 results:**<br>

<details>
<summary>Main app</summary>

* **settings.py**<br>
![pep8-validation](media/main_settings.py.jpg)

* **urls.py**<br>
![pep8-validation](media/main_urls.py.jpg)
</details>

<details>
<summary>Booking Page</summary>

* **admin.py**<br>
![pep8-validation](media/booking_admin.py.jpg)

* **forms.py**<br>
![pep8-validation](media/booking_form.py.jpg)

* **models.py**<br>
![pep8-validation](media/booking_model.py.jpg)

* **urls.py**<br>
![pep8-validation](media/booking_urls.py.jpg)

* **views.py**<br>
![pep8-validation](media/booking_views.py.jpg)
</details>

<details>
<summary>Contact Page</summary>

* **urls.py**<br>
![pep8-validation](media/contact_urls.py.jpg)

* **views.py**<br>
![pep8-validation](media/contact_views.py.jpg)
</details>
<details>
<summary>Home Page</summary>

* **apps.py**<br>
![pep8-validation]()

* **urls.py**<br>
![pep8-validation]()

* **views.py**<br>
![pep8-validation]()
</details>
<details>
<summary>Menu Page</summary>






