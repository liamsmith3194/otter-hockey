# Otter Hockey

![Am I Responsive](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/images/readme-images/am-i-responsive.PNG)

Welcome to Otter Hockey!

Based on https://www.otterhockey.co.uk

I have been given full permission to use all my static files from the Managing Director Kyle Maroo.

An online E-Commerce store for hockey fans to purchase our products.
From top of the range sticks to a pair a shin pads, we pride ourselves on build quality and use the best materials!

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

### User Stories
[View](https://docs.google.com/spreadsheets/d/19LTRR3Om2SZQ7QQXUBhVAfR0ZMenbPFSQmbzZz1gWek/edit?usp=sharing)
![Google Sheets - User Stories](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/user-stories.PNG)

As a customer/site user ...

1.  I want to be able to *immediately understand the purpose and meaning of the site* so that I can **feel assured that I am on the right site for what I am looking to purchase.**

1.  I want to be able to *be made aware of any deals available* so that I can **make the most on what is on offer, whether it is free delivery or 10% off etc.**

1.  I want to be able to *view the social media account(s)* so that I can **keep up to date with news and offers but also it give me trust in the Company.**

1.  I want to be able to *view a list of all products per category* so that I can **select any product(s) to purchase.**

1.  I want to be able to *select a product and view the product details* so that I can **See an overview of the product showing me the important details such as description, price and rating etc.**

1.  I want to be able to *view product size if applicable* so that I can **select the size of product I wish to purchase (stick size or clothing size).**

1.  I want to be able to *select a quantity choice* so that I can **order 1 or more of the same item.**

1.  I want to be able to *add a product to my bag* so that I can **purchase the item(s) I have selected.**

1.  I want to be able to *be notified of when I have added a product to my bag* so that I can **see that my request to add the item(s) has been successful.**

1.  I want to be able to *be shown an overview of my bag* so that I can **see the product and the important details I have selected to ensure they are correct.**

1.  I want to be able to *see the total price of my bag* so that I can **make sure I don't spend more than I want to.**

1.  I want to be able to *find out how much more I need to spend to receive free delivery* so that I can **see if it is cost effective adding another product(s) to qualify for free delivery.**

1.  I want to be able to *click a button which takes me to my bag and checkout* **proceed with payment easily.**

1.  I want to be able to *register an account* so that I can **I have all the access I require from the site.**

1.  I want to be able to *receive an email confirmation* so that I can **I know my request to register has been received and all I need to do is verify my account.**

1.  I want to be able to *login and out of my account* so that I can **I can ensure my account is safe should I share a computer.**

1.  I want to be able to *reset my password* so that I can **log back in to my account if I have forgotten my password.**

1.  I want to be able to *view previous orders* so that I can **see my purchase history and link to an item I have bought previously.**

1.  I want to be able to *add a default delivery address* so that I can **when I go to checkout my delivery information is already populated, making the process easier.**

1.  I want to be able to *sort the products by certain criteria* so that I can **view the products by a common look such as price lowest to highest etc.**

1.  I want to be able to *search by product category* so that I can **navigate through the products by category e.g. sticks, bags or accessories.**

1.  I want to be able to *search by keyword* so that I can **find the item I specifically looking for to purchase.**

1.  I want to be able to *retrieve all products from a keyword search* so that I can **I am shown a reduced list of products using the keyword as a filter.**

1.  I want to be able to *view all items in my bag* so that I can **I can check my bag and ensure I have all the items and quantities are correct.**

1.  I want to be able to *easily amend any product in my bag* so that I can **add to and reduce the quantity per item.**

1.  I want to be able to *pay for my order* so that I can **process my order and eventually receive my item(s).**

1.  I want to be able to *trust the sites checkout security* so that I can **I feel that personal details are safe and site can be trusted.**

1.  I want to be able to *view my order confirmation after payment* so that I can **I know my order has been processed and provides a final check  should I want to do so.**

1.  I want to be able to *receive an email order confirmation after payment* so that I can **I know my order has been processed and I have the written confirmation to prove it.**

As a administrator/owner ...

1.  I want to be able to *add products to the site* so that I can **add new products to show potential customers.**

1.  I want to be able to *edit/update products* so that I can **amend product details such as name, description, price etc.**

1.  I want to be able to *delete products* so that I can **remove any product that is no longer available.**

### Wireframes

-   Figma Desktop Wireframe - [View](https://www.figma.com/file/IwRdh2KX15cfopZj2ycBZx/Otter-Hockey---Desktop?node-id=0%3A1)

![Figma Desktop Wireframe](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/desktop-wireframes-1.PNG)
![Figma Desktop Wireframe](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/desktop-wireframes-2.PNG)


-   Figma Mobile Wireframe - [View](https://www.figma.com/file/KOF9ARsG0VHTkh4iwZ0QbF/Otter-Hockey---Mobile?node-id=0%3A1)

![Figma Mobile Wireframe](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/mobile-wireframes-1.PNG)

### Flowchart

-   Lucidchart - [View](https://lucid.app/lucidchart/0891e26c-cd6e-4247-ad81-8fbdf35eb7cb/edit?invitationId=inv_4362915e-3638-41ed-b418-d385edae4cff)

![Lucid Flowchart](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/lucid-flowchart.PNG)

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
-   All imagery has been taken from Otter Hockey's site with permission from Kyle as [previously mentioned above](#otter-hockey)
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