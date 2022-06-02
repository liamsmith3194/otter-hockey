# Otter Hockey

![Am I Responsive](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/am-i-responsive.PNG)

Welcome to Otter Hockey!

Based on https://www.otterhockey.co.uk

An online E-Commerce store for hockey fans to purchase our products.
From top of the range sticks to a pair a shin pads.

## Our Story

> "Whilst at University our founder, Kyle, broke his hockey stick and had not budgeted to purchase another. The idea of making hockey sticks premium but affordable then formed. Upon our start in 2018, we originally planned to make one range of sticks, but in April 2019 the community wanted more, we gave you more. Fast forward two years later and our sticks were at the Tokyo 2020 Olympics, used by Melanie Garcia of Spain. Showcasing to the world how Hockey can be Premium, but Affordable. Keep an eye out, we've got more to come."

## Permission

I have been given full permission to use all my static files and product information from the Managing Director of Otter Hockey, Kyle Maroo.
![Email Permission](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/permission-email.PNG)

## Links

### Live Site
[Heroku Project](https://otter-hockey.herokuapp.com/)

### Repository
[GitHub Repository](https://github.com/liamsmith3194/otter-hockey)

# Table of Contents

1.  [Planning & Requirements](#agile-methodology---planning--requirements)
    -   [User Stories](#user-stories)
    -   [Wireframes](#wireframes)
    -   [Flowchart](#flowchart)
    -   [Databases](#databases)
2.  [Design](#agile-methodology---design)
    -   [Colour Scheme](#colour-scheme)
    -   [Typography](#typography)
    -   [Imagery](#imagery)
3.  [Features](#features)
    -   [Layout](#layout)
    -   [Navigation Bar](#navigation-bar)
    -   [Allauth](#allauth)   
    -   [Boostrap Alerts](#boostrap-alerts)
    -   [Bootstrap Nav Pills](#boostrap-nav-pills)
    -   [Book a Table](#book-a-table)
    -   [Manage Booking](#manage-booking)
    -   [Django Admin Site](#django-admin-site)
4.  [Implementation](#agile-methodology---implementation)
    -   [Programs](#programs)
5.  [Testing](#agile-methodology---testing)
    -   [Validation Testing](#validation-testing)
    -   [Manual Testing](#manual-testing)
    -   [Continued Testing](#continued-testing)   
    -   [Glitches](#glitches)
    -   [Issues](#issues)
6.  [Deployment](#deployment)
    -   [Heroku & Gitpod](#heroku--gitpod)
    -   [Updated Heroku Deployment Via Terminal](#updated-heroku-deployment-via-terminal)
7.  [Evaluation](#agile-methodology---evaluation)
    -   [Site Visitor Goals](#site-visitor-goals-1)
    -   [Admin User/Owner Goals](#admin-userowner-goals-1)
    -   [Future Features](#future-features)   
8.  [References](#references)
    -   [Code](#code)
9.  [Conclusion](#conclusion)
    -   [Content](#content)
    -   [Mentions](#mentions)

## Agile Methodology - Planning & Requirements

-   GitHub Issues - [View](https://github.com/liamsmith3194/otter-hockey/issues)
![GitHub Issues](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/github-issues-1.PNG)
![GitHub Issues](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/github-issues-2.PNG)

-   Project Planning Board - [View](https://github.com/liamsmith3194/otter-hockey/projects/1)
![GitHub Project Planning Board](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/github-project-planning-board.PNG)

### User Stories
[View](https://docs.google.com/spreadsheets/d/19LTRR3Om2SZQ7QQXUBhVAfR0ZMenbPFSQmbzZz1gWek/edit?usp=sharing)
![Google Sheets - User Stories](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/user-stories-google-sheets.PNG)

As a customer/site user ...

#### Customer Viewing

1.  I want to be able to *immediately understand the purpose and meaning of the site* so that I can **feel assured that I am on the right site for what I am looking to purchase.**

1.  I want to be able to *be made aware of any deals available* so that I can **make the most of what is on offer, whether it is free delivery or 10% off etc.**

1.  I want to be able to *view the social media account(s)* so that I can **keep up to date with news and offers, but also it gives me trust in the Company.**

#### Products

1.  I want to be able to *view a list of all products per category* so that I can **select any product(s) to purchase.**

1.  I want to be able to *select a product and view the product details* so that I can **see an overview of the product showing me the important details such as description, price and rating etc.**

1.  I want to be able to *view product size if applicable* so that I can **select the size of product I wish to purchase (stick size or clothing size).**

1.  I want to be able to *select a quantity choice* so that I can **order one or more of the same item.**

1.  I want to be able to *add a product to my bag* so that I can **purchase the item(s) I have selected.**

#### Notifications

1.  I want to be able to *be notified of when I have added a product to my bag* so that I can **see that my request to add the item(s) has been successful.**

1.  I want to be able to *be shown an overview of my bag* so that I can **see the product and the important details I have selected to ensure they are correct.**

1.  I want to be able to *see the total price of my bag* so that I can **make sure I don't spend more than I want to.**

1.  I want to be able to *find out how much more I need to spend to receive free delivery* so that I can **see if it is cost-effective adding another product(s) to qualify for free delivery.**

1.  I want to be able to *click a button which takes me to my bag and checkout* so that I can **proceed with payment easily.**

#### Registration

1.  I want to be able to *register an account* so that I can **I have all the access I require from the site.**

1.  I want to be able to *receive an email confirmation* so that I can **know my request to register has been received and all I need to do is verify my account.**

1.  I want to be able to *login and out of my account* so that I can **ensure my account is safe should I share a computer.**

1.  I want to be able to *reset my password* so that I can **log back in to my account if I have forgotten my password.**

1.  I want to be able to *view previous orders* so that I can **see my purchase history and link to an item I have bought previously.**

1.  I want to be able to *add a default delivery address* so that I can **when I go to checkout, my delivery information is already populated, making the process easier.**

#### Sorting & Searching

1.  I want to be able to *sort the products by certain criteria* so that I can **view the products by a common look such as price lowest to highest etc.**

1.  I want to be able to *search by product category* so that I can **navigate through the products by category e.g. sticks, bags or accessories.**

1.  I want to be able to *search by keyword* so that I can **find the item I am specifically looking for to purchase.**

1.  I want to be able to *retrieve all products from a keyword search* so that I can **be shown a reduced list of products using the keyword as a filter.**

#### Checkout

1.  I want to be able to *view all items in my bag* so that I can **check my bag and ensure I have all the items and quantities are correct.**

1.  I want to be able to *easily amend any product in my bag* so that I can **add to and reduce the quantity per item.**

1.  I want to be able to *pay for my order* so that I can **process my order and eventually receive my item(s).**

1.  I want to be able to *trust the sites' checkout security* so that I can **I feel that personal details (especially banking information) are safe, and the site can be trusted.**

1.  I want to be able to *view my order confirmation after payment* so that I can **I know my order has been processed and provides a final check  should I want to do so.**

1.  I want to be able to *receive an email order confirmation after payment* so that I can **trust my order has been processed, and I have the written confirmation to prove it.**

#### Company Information

1.  I want to be able to *find out more information about the company* so that I can **look into their background and develop an understanding of the business.**

1.  I want to be able to *review the FAQ's* so that I can **should I have a question, I can see if it has already been answered.**

1.  I want to be able to *contact them directly* so that I can **ensure my query/question can be answered.**

1.  I want to be able to *read through the privacy policy* so that I can **know my personal information is secure.**

1.  I want to be able to *subscribe to the sites mailing list* so that I can **recieve all the latest deals, offers and news.**

As an administrator/owner ...

#### Admin Rights

1.  I want to be able to *add products to the site* so that I can **add new products to show potential customers.**

1.  I want to be able to *edit/update products* so that I can **amend product details such as name, description, price etc.**

1.  I want to be able to *delete products* so that I can **remove any product that is no longer available.**

### Wireframes

-   Figma Desktop Wireframe - [View](https://www.figma.com/file/IwRdh2KX15cfopZj2ycBZx/Otter-Hockey---Desktop?node-id=0%3A1)

![Figma Desktop Wireframe](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/desktop-wireframes-1.PNG)
![Figma Desktop Wireframe](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/desktop-wireframes-2.PNG)
![Figma Desktop Wireframe](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/desktop-wireframes-3.PNG)
![Figma Desktop Wireframe](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/desktop-wireframes-4.PNG)
![Figma Desktop Wireframe](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/desktop-wireframes-5.PNG)
![Figma Desktop Wireframe](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/desktop-wireframes-6.PNG)


-   Figma Mobile Wireframe - [View](https://www.figma.com/file/KOF9ARsG0VHTkh4iwZ0QbF/Otter-Hockey---Mobile?node-id=0%3A1)

![Figma Mobile Wireframe](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/mobile-wireframes-1.PNG)
![Figma Mobile Wireframe](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/mobile-wireframes-2.PNG)

### Flowchart

-   Lucidchart Flowchart - [View](https://lucid.app/lucidchart/0891e26c-cd6e-4247-ad81-8fbdf35eb7cb/edit?invitationId=inv_4362915e-3638-41ed-b418-d385edae4cff)

![Lucid Flowchart](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/lucid-flowchart.PNG)

### Databases

-   Lucidchart Database Models - [View](https://lucid.app/lucidchart/d2cd8bee-d86e-490a-9f4b-8ca0156f4ffe/edit?viewport_loc=-474%2C38%2C3136%2C1334%2C0_0&invitationId=inv_b6c90e1f-5889-4a79-82c4-13073bf97b4f#)

![Lucid Database Models](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/lucid-database-models.PNG)

The site is connected to Heroku's Postgres Database.

The Entity-Relationship Diagram below shows how the database models and how they relate to each other.

#### Products
The Products model is used to add products to the site. Only the site owner/admin can add, edit, and delete products. All other users are able to view the products on the site.

#### Category
The Category model is used so that the site owner/admin can assign products to a Category. This ensures the products are in the correct location for users to find. The product category links to the Category name.

#### Order
The Order model is used for the order details (when an order is placed by a user). The user profile of the order model is linked to the User Profile model providing the user is registered.

#### Order Line Items
Used for the checkout details. This is linked to the Order Line Items model which contains the products (and products model) ordered by the user.

#### User Profile
The User Profile stores the default delivery details again, assuming the user is registered and chose to save their delivery details.

## Agile Methodology - Design

### Colour Scheme

-   The site colour scheme is minimalistic but effective.

-   #6D6D6D - Grey
    -   The grey is used throughout the site, for the logo, navigation bar, footer and some action buttons such as "Add to Basket"
    -   All the sticks on offer on the site have a 'progress bar' used for power and control, this uses our main grey against a lighter grey for the background.

-   #000000 - Black
    -   Black is used for the vast majority of the text
    -   The navigation bar items carry a hover & active black pseudo-class to highlight where the cursor is and current page to the user.
    -   A black banner is used to show the free delivery offer and provides a nice contrast from the navigation bar.

-   #FFFFFF - White
    -   The header containing the logo, search bar and account/basket buttons.
    -   The navigation menu items are white at the default state.
    -   The 'free delivery offer' text against the black background is drawn to the users attention.

### Typography

-   Orbitron
    -   I have chosen to use the same typeface as used on https://www.otterhockey.co.uk for the logo and product names on the product detail pages. This is a conscious choice to increase the continuity on the site with regards to the product images.
    -   The logo uses the bold style, but also carrys a subtle dropshadow to make it stand out.
    -   The product name uses the regular style.
    -   As a couple of products contain the letter O and a zero this typeface provides a completely different look making it easier for the user to understand the product name.

-   Montserrat (light, medium & bold) 
    -   A large majority of text on the site uses Montserrat.
    -   This is a very popular font for web design because of its readability.
    -   The uses of light, medium and bold varies and highlights certain details. For example the order confirmation uses the light style for the field names, the medium for the field values and the bold for the sub-headings.
    -   This make it more appealing to the user and easier to read or quickly check.

-   Bebas Neue
    -   This typeface is used sparcely but provides a strong contrast between Orbitron and Montserrat
    -   It is used for the navigation items and the basket total.
    -   Increased letter spacing makes the font more legible for the users.

### Imagery
-   All imagery has been taken from Otter Hockey's site with permission from Kyle as [previously mentioned above](#permission)
-   The hero image has been taken from the Otter Hockey Instagram page .... add more info when chosen
-   All the other imagery used on the site show the products on offer.

# TO BE COMPLETED AFTER BUILD

## Features
Below is a brief overview showing the main features of the site.

### Layout
-   Using the grid set up from Bootstrap, 12 columns split into 3 for the navigation and 9 for the content.
-   The hero image covers the "content" side of the screen and lays behind the transparent window.
-   All the page titles use a consistent theme.
-   All page content including forms, buttons and text is presented inside the window.

### Navigation Bar
-   Located on the left side of screen, which includes the logo, menu items, opening times information and social media links.

![Navigation Bar - Standard](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/nav-bar-new-user.PNG)

-   The navigation bar automatically collapses at a screen width of 767px. This produces the "Hamburger button" to open and close the nav bar on a click.

![Navigation Bar - Hamburger button](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/nav-bar-hamburger-button.PNG)

-   More menu items are available and shown after a user has signed in or registers for the first time. For example, 'Book A Table' and 'Manage Booking'.

![Navigation Bar - User logged in](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/nav-bar-existing-user.PNG)

### Allauth
-   Allauth has been installed to enable users to create, login and sign out of their accounts.
-   The register form has been amended to include first and last name.
-   All the user details are submitted and saved to the database.

![Allauth - Register Form](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/allauth-register-page.PNG)

### Boostrap Alerts
-   When the user logs in, an alert appears in the navigation bar to show the user they have successfully signed in.
-   The alert is also triggered when the user logs outs.

![Boostrap - Alert](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/bootstrap-alert.PNG)

### Boostrap Nav Pills
-   The menu page uses the bootstrap component nav pills.
-   By default it shows the starters but choices span across the window showing the mains, sides and desserts. Clicking on any of these options changes the data correspondingly.

![Menu Page - Nav pills](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/menu-page.PNG)

### Book A Table
-   The booking form self populates with the user's first name, last name and email address, taken from the registration form.

![Booking Page - Form](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/booking-page.PNG)

-   Bookings must be submitted one day in advance and maximum 30 days prior.
-   On a successful submission, the user will receive an automated email confirmation, showing the location, date and time and the number of guests.
-   Also on a successful submission, the user will be redirected to the 'Manage Booking' page.
-   If the date and time isn't available on submit, the user is greeted with a validation error "Date and/or time not available, please try again."
-   If the user already has a booking that hasn't expired, they will be forced to either amend or delete their reservation by clicking on the 'Manage Booking' button.

![Existing Booking Page](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/existing-booking-page.PNG)

### Manage Booking
-   The booking data is presented only showing the critical details such as date and time, location  and number of guests.
-   The user has two clear buttons to amend or delete the booking.
-   Clicking the amend button produces the booking form again with the previously entered booking data.
-   When the user amends the booking and saves, the database is updated and when redirected, the manage booking page is updated to show the change(s).
-   If the user clicks the delete button, they are asked to confirm this, "Are you sure you want to delete your booking?". This is displayed alongside two options "No, Cancel" and "Yes, Delete"
-   Clicking on either of the buttons redirects the user back to the 'Manage Booking' Page, whether the booking is still seen is determined by which button the user clicked.
-   If the user doesn't have a booking in the database, they are notified by a simple paragraph "There is no booking currently in the database" and shown a button linking them to the 'Book A Table'.

![Manage Booking](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/manage-booking-page.PNG)

### Django Admin Site

![Django Admin - Overview](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/django-admin-overview.PNG)

-   The admin site is username and password protected for obvious reason. Only a "Superuser" or "Staff status" have access.

![Django Admin - Login](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/django-admin-login.PNG)

-   The "recent actions" panel shows the last 10 changes to users or bookings.
-   The pencil icon indicates a change.
-   The cross icon indicates a deletion.

![Django Admin - Recent Actions](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/django-admin-recent-actions.PNG)

-   They have the ability to add and amend users, including changing their names, email address, username and even their password and permissions.

![Django Admin - Amend User](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/django-admin-amend-user.PNG)

-   It also shows the user's activity in terms of their last login and when they registered.

-   Finally, users can be deleted by an admin user.

![Django Admin - User Important Dates](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/django-admin-user-dates.PNG)

-   As an admin user you have the ability to create manual bookings "ADD BOOKING"
-   The form uses a dropdown menu to select the username, ensure the user has created an account in order to make a reservation.
-   The location and number of guests use the same options as the site, keeping it consistent.

![Django Admin - Add Booking](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/django-admin-add-booking.PNG)

-   An admin user is also able to amend any booking and any piece of information from that booking, for example; date and time, location and number of guests.
-   A booking can also be deleted as a batch or individually.

![Django Admin - Edit Booking](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/django-admin-edit-booking.PNG)

## Agile Methodology - Implementation

### Programs
### Created by using:

-   HTML5
-   CSS3
-   JavaScript
-   Python
-   Django

### Programs including:

-   [Heroku](https://www.Heroku.com/) was used to share the site online.
-   [AWS](https://aws.amazon.com/) was used to store static files. 
-   [Bootstrap](https://getbootstrap.com/) was used to create the framework for the site, including the grid set up and other components such as buttons, toasts and progress bars.
-   [Font Awesome](https://fontawesome.com/) was used for the social media icons within the footer.
-   [Google Fonts](https://fonts.google.com/) was used to import the 'Orbitron', 'Bebas Neue' and 'Montserrat' into the style.css file.
-   [GitPod](https://gitpod.io/) was used to create and update the website throughout, via the terminal to push changes to GitHub.
-   [GitHub](https://github.com/) was used to commit changes during development and ensure no work was lost.
-   [Figma](https://figma.com/) was used to create the wireframes during the design process.
-   [Lucidchart](https://lucidchart.com/) was used to create the step by step workflow to visualise how the user can book and manage their reservation.

### Search Engine Optimisation (SEO)

TO BE COMPLETED

In order to find the relevant keywords for my project I made the following searches on Google and Word Tracker along with a few combinations:

## Agile Methodology - Testing

TO BE REPLACED 

### Validation Testing

The W3C Markup Validator and W3C CSS Validator Services were used to ensure there were no syntax errors in the project.

- [W3C HTML Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fotter-hockey.herokuapp.com%2F)
    -   Script type warnings - The suggested code from Bootstrap and EmailJS included script type="text/javascript".
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fotter-hockey.herokuapp.com)
    -   The only errors/warnings from the validation were seen in Bootstrap styles, not the developer's css.
- [Jshint JavaScript linter](https://jshint.com/) - No errors were found
- [PEP8](http://pep8online.com/) Python linter was used to ensure there were no syntax errors in the project.
Checking all individual files separately produced numerous errors. On the first use my code produced over 30 warnings and/or errors including:
    - "line too long (127 > 79 characters)"
    - "blank line contains whitespace"
    - "indentation is not a multiple of four"

These have now all be rectified.

- [Bookings App - URLS](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/booking_urls_result.txt)

- [Bookings App - Models](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/booking_models_result.txt)

- [Bookings App - Views](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/booking_views_result.txt)

### Manual Testing

TO BE REPLACED 

- Responsive Testing
    - The site has been tested on an iMac, PC, Laptop, iPad and iPhone X.
    - At mobile phone width the 'hamburger bars' are shown, in order to shrink and expand the navigation bar.

- Index Page
    - [x] Ace of Steaks logo link 
        - Links to from every page successfully.
    - [x] Individual page links
        - All pages link to one another from any page.
    - [x] Social media links open in new tab
        - All three social media sites are linked to open new tabs, this can be done from any web page.
    - [x] Window link to menu page
        - See menu button successfully links to the menu page showing the default data; starters.

- Register Page
    - [x] Username already exists
        - Attempting to create a user with the same username produces a validation error, "A user with that username already exists."

        ![User exists](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/user-exists.PNG)

    - [x] All fields required except email address (optional)
        - The form does not submit unless all the fields have been completed with valid data.
    - [x] Not a recognised email address
    - [x] Passwords don't match
        - When creating a user and the passwords don't match, a validation error is presented. "You must type the same password each time."

        ![Passwords don't match](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/password-dont-match.PNG)

    - [x] Password not secure
        - If the password isn't strong enough, another validation error is shown. "This password is too short. It must contain at least 8 characters. This password is too common."

        ![Password not strong enough](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/password-too-short.PNG)

    - [x] Sign in link
        - The link redirects the user to the sign-in form as expected, autofilling if the user uses the 'remember me' feature.

- Login Page
    - [x] Invalid credentials
        - Attempting to sign in as a user that has not been registered I am greeted with an error message, "The username and/or password you specified are not correct."

        ![Invalid credentials](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/invalid-user.PNG)

    - [x] Remember me
        - The 'remember me' checkbox works correctly, after logging in with one user, clicking the checkbox and signing out. The username produced was the last used. This was tested on multiple user accounts.
    - [x] Register link "sign up"
        - The link redirects the user to the register form as expected.

- Logout Page
    - [x] Logout link
        - The logout button works from any page on the site.

- Booking Page
    - [x] All fields required
        - The booking will not submit unless all the fields have been completed with valid input.
    - [x] Date unavailable before or on the day of booking
        - The calendar ensure the invalid dates can not be selected.

        ![Today's date unavailable](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/todays-date-unavailable.PNG)

    - [x] No bookings will be taken after 30 days in advance
        - The calendar ensure the user is unable to select a date 30 days in advance of today's' date.
    - [x] Double booking
        - The booking will not submit if the date and time is the same as an existing booking in the database.

        ![Date unavailable](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/date-unavailable.PNG)

    - [x] All account details coming through
        - Tested 3 different users and all pulled through user credentials (first name, last name & email address) when going to book a table.

- Manage Booking Page (Overview)
    - [x] All data matches user input
        - Made numerous bookings under different users and all the data synced correctly.
    - [x] Old bookings are removed from view
        - Bookings passed the date of reservation are being deleted from the user's manage booking page. Giving them the ability to book a new table.

- Manage Booking Page (Update)
    - [x] Form loads user entry
        - The form autopopulates with the data taken from the booking made.
        - The date and time field does not autopopulate. [See below](#issues)
    - [x] Date unavailable before or on the day of booking
        - The same restriction remains on the calendar to ensure the invalid dates can not be selected.
    - [x] No bookings will be taken after 30 days in advance
        - The same checks are in place to ensure the user is unable to select a date 30 days in advance of today's' date.
    - [x] Double booking
        - The new booking still checks to ensure the date and time doesn't clash with any other booking in the database.
    - [x] Booking change saved and updated in overview and database
        - After saving the changes to the booking, the manage booking page is updated.
        - Whether one field or multiple are changed, the view from the user is updated along with the database.

![Manage booking - Update](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/edit-booking.PNG)

- Manage Booking Page (Delete)
    - [x] Cancel button keeps booking and returns the user to the manage booking page
        - When clicking the cancel button, the user is redirected to the manage booking page with the booking intact and editable.
    - [x] Delete button removes booking from user's view and from the database
        - After clicking the delete button the user is redirected to the manage booking page, the booking has been removed from view and removed from the system.
        - As there is no booking in the database for the user, they are able to book a table. 

![Manage booking - Delete](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/delete-booking.PNG)

- Menu Page
    - [x] All links show correct data
        - All four navigation tabs open the correct information, and it doesn't matter what order the tabs are clicked in.

### Lighthouse Testing

TO BE REPLACED 

- Desktop Results

![Lighthouse Desktop Results](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/lighthouse-desktop.PNG)

- Mobile Results

![Lighthouse Mobile Results](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/lighthouse-mobile.PNG)

### Continued Testing

TO BE REPLACED 

- The Website was tested on Google Chrome and Microsoft Edge.
- The website has been displayed on various devices such as Desktop PC, iMac, Laptop, iPhone X & iPad Pro
- Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Glitches

Glitches here

## Issues

Issues here

## Deployment

### Heroku & GitPod

Heroku & GitPod were the program used to share and deploy the app, it was accomplished by using the following steps:

1. Log in to Heroku. On your dashboard, click "New" and then click "Create new app".

2. Fill in the field for App name - It must be a unique name to Heroku. 
    -   Then select the region of Europe and click "Create app".

![Heroku - New app](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/heroku-create-app.PNG)

3. In the "Resources" tab, scroll down to "Add-ons" and search for "Heroku Postgres".
    -   Once selected and saved in the "Settings" tab click "Reveal Config Vars", this produces a database url.

![Heroku - Add Heroku Postgres](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/heroku-resources.PNG)

4. In GitPod set up an env.py file in the repository.
    -   Create an environment variable for "DATABASE_URL" and paste the value from Heroku.
    -   Create an environment variable for "SECRET_KEY" and create your key using any characters available.

5.  Copy the secret key to Heroku by adding the variable in the "Config Vars" section.

6.  In the settings.py file import:
    -   os
    -   dj_database_url
-   Add the if statement:
    -   if os.path.isfile('env.py'): import env

7.  Amend the secret key variable to the secure key created earlier:
    -   "SECRET_KEY = os.environ.get('SECRET_KEY')

8.  Add our Heroku host name into the allowed hosts, this is your Heroku app name followed by herokuapp.com.
    -   Add "localhost" too, so the app can be ran locally.

9.  Scroll down to the "DATABASES" section
    -   'Comment out' the default code and add the "DATABASE_URL" variable created earlier:
    -   DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

10. Create a Procfile
    -   It must be named like so; "Procfile" and sit inside the root directory.
    -   Within the file add "web: gunicorn" followed by the app name .wsgi.
    -   For example: "web: gunicorn aceofsteaks.wsgi".

11. Scroll back and click the tab "Deploy".
    -   Choose "GitHub" as the Deployment method.
    -   Enter the GitHub repository name and click "Search".
    -   The repository should appear below, then click "Connect".

![Heroku - Deployment method](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/heroku-deploy-section.PNG)

12.  Then click the "Deploy Branch" button in the "Manual deploy" section. This way you can see the code being written.

![Heroku - Manual deployment](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/heroku-manual-deploy.PNG)

13. Once that is complete, a message will appear with "Your app was successfully deployed" and a "View" button. This will take you to the app directly.

![Heroku - Successfully Deployed](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/heroku-deployed-successfully.PNG)

-   On final deployment the project must be set up in the following way:
    -   DEBUG is set to false in settings.py file
    -   staticcollect=1 from Config Vars in Heroku deleted.

### Updated Heroku Deployment Via Terminal

During the timeframe of this project Heroku had to change security settings internally which meant disabling automatic deployment. Therefore deployment to Heroku had to be completed in the following way:
1.  Via the terminal in GitPod, login in to Heroku using the command: "heroku login -i"
2.  Enter the email address linked the Heroku user.
3.  Enter your password, if your password doesn't work use the API key which is found in Heruko under the account settings towards the bottom of the page.
4.  The terminal prints "Logged in as (email address)"
5.  You then select the applicaion you want to deploy with the command: "heroku git:remote -a (app name)"
6.  Successfully identifying the app, the terminal will show this message "set git remote heroku to `https://git.heroku.com/(app name).git`"
7.  The final command: "git push heroku main".

## Agile Methodology - Evaluation

### Site Visitor Goals

QUESTIONS TO BE ANSWERED

As a customer/site user ...

1.  I want to be able to *immediately understand the purpose and meaning of the site* so that I can **feel assured that I am on the right site for what I am looking to purchase.**

1.  I want to be able to *be made aware of any deals available* so that I can **make the most of what is on offer, whether it is free delivery or 10% off etc.**

1.  I want to be able to *view the social media account(s)* so that I can **keep up to date with news and offers, but also it gives me trust in the Company.**

1.  I want to be able to *view a list of all products per category* so that I can **select any product(s) to purchase.**

1.  I want to be able to *select a product and view the product details* so that I can **see an overview of the product showing me the important details such as description, price and rating etc.**

1.  I want to be able to *view product size if applicable* so that I can **select the size of product I wish to purchase (stick size or clothing size).**

1.  I want to be able to *select a quantity choice* so that I can **order one or more of the same item.**

1.  I want to be able to *add a product to my bag* so that I can **purchase the item(s) I have selected.**

1.  I want to be able to *be notified of when I have added a product to my bag* so that I can **see that my request to add the item(s) has been successful.**

1.  I want to be able to *be shown an overview of my bag* so that I can **see the product and the important details I have selected to ensure they are correct.**

1.  I want to be able to *see the total price of my bag* so that I can **make sure I don't spend more than I want to.**

1.  I want to be able to *find out how much more I need to spend to receive free delivery* so that I can **see if it is cost-effective adding another product(s) to qualify for free delivery.**

1.  I want to be able to *click a button which takes me to my bag and checkout* so that I can **proceed with payment easily.**

1.  I want to be able to *register an account* so that I can **I have all the access I require from the site.**

1.  I want to be able to *receive an email confirmation* so that I can **know my request to register has been received and all I need to do is verify my account.**

1.  I want to be able to *login and out of my account* so that I can **ensure my account is safe should I share a computer.**

1.  I want to be able to *reset my password* so that I can **log back in to my account if I have forgotten my password.**

1.  I want to be able to *view previous orders* so that I can **see my purchase history and link to an item I have bought previously.**

1.  I want to be able to *add a default delivery address* so that I can **when I go to checkout, my delivery information is already populated, making the process easier.**

1.  I want to be able to *sort the products by certain criteria* so that I can **view the products by a common look such as price lowest to highest etc.**

1.  I want to be able to *search by product category* so that I can **navigate through the products by category e.g. sticks, bags or accessories.**

1.  I want to be able to *search by keyword* so that I can **find the item I am specifically looking for to purchase.**

1.  I want to be able to *retrieve all products from a keyword search* so that I can **be shown a reduced list of products using the keyword as a filter.**

1.  I want to be able to *view all items in my bag* so that I can **check my bag and ensure I have all the items and quantities are correct.**

1.  I want to be able to *easily amend any product in my bag* so that I can **add to and reduce the quantity per item.**

1.  I want to be able to *pay for my order* so that I can **process my order and eventually receive my item(s).**

1.  I want to be able to *trust the sites' checkout security* so that I can **I feel that personal details are safe, and the site can be trusted.**

1.  I want to be able to *view my order confirmation after payment* so that I can **I know my order has been processed and provides a final check  should I want to do so.**

1.  I want to be able to *receive an email order confirmation after payment* so that I can **trust my order has been processed, and I have the written confirmation to prove it.**

As an administrator/owner ...

1.  I want to be able to *add products to the site* so that I can **add new products to show potential customers.**

1.  I want to be able to *edit/update products* so that I can **amend product details such as name, description, price etc.**

1.  I want to be able to *delete products* so that I can **remove any product that is no longer available.**

### Future Features

TO BE CONFIRMED

## References

### Code

CODE REFERENCES

- Boutique Ado:
header
body height calculation - height: calc(100vh - 164px);
overlay


## Conclusion

### Content

-   The majority of content was written by the developer. 
-   The product information was taken from [Otter Hockey](https://www.otterhockey.co.uk) but again I was given permission to use this by [Kyle](#permission).

### Mentions

-   My Mentor Narender
    -   Numerous video calls
    -   A lot of questions via Slack.
    -   Introduced me to Pylint.