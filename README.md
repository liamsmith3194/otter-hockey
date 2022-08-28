# Otter Hockey

![Am I Responsive](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/am-i-responsive.PNG)

Welcome to Otter Hockey!

Based on https://www.otterhockey.co.uk
(Before website update in mid July)
![Otter Hockey - Home](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/otter-hockey-home.PNG)
![Otter Hockey - Products](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/otter-hockey-products.PNG)
![Otter Hockey - Sticks](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/otter-hockey-sticks.PNG)

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

## Last Minute Addition

### All Products
- On the 23/08/22 - One week before submission, I decided to implement an all products view.
- It's been something that I have changed my mind on continuously, however now constructed, I have been able to give it, its own page heading and the sort by dropdown using the 'Category A-Z' & 'Category Z-A'

![Desktop - All Products](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/products-all-products-desktop.PNG)

- The navigation bar has been amended to include an 'All Products' link, both on large screens and smaller devices.
- You will notice that all the screenshots from the site do not contain the updated navigation bar.

![Mobile - Updated - Navigation Bar](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/updated-mobile-nav.PNG)

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
    -   [Layout - Desktop](#layout-desktop)
    -   [Layout - Mobile](#layout-mobile)
    -   [Index Page](#index-page)
    -   [Products Page](#products-page)
    -   [All Products](#all-products)
    -   [Product Detail Page](#product-detail-page)
    -   [Basket - Desktop](#basket-desktop)
    -   [Basket - Mobile](#basket-mobile)
    -   [Check Out](#check-out-desktop)
    -   [Order Confirmation](#order-confirmation-desktop)
    -   [My Profile](#my-profile)
    -   [Product Management Page](#product-management-page)
    -   [Product Management - Via Products](#product-management---via-products)
    -   [Allauth Pages](#allauth-pages-register-login-logout-etc)   
    -   [Bootstrap Alerts(Toasts)](#bootstrap-alerts-toasts)
    -   [About Us](#about-us)
    -   [FAQ's](#faqs)
    -   [Privacy Policy](#privacy-policy)
    -   [Contact Us](#contact-us)
    -   [Error 404](#error-404---page-not-found)
    -   [Django Admin Site](#django-admin-site)
        -   [Login](#login)
        -   [Create Order](#create-order)
        -   [Amend Order](#amend-order)
        -   [Amend Product](#amend-product)
        -   [Amend User](#amend-user)
        -   [User Activity](#user-activity)
        -   [Recent Actions](#recent-actions)
4.  [Implementation](#agile-methodology---implementation)
    -   [Programs](#programs)
    -   [Web Marketing](#web-marketing)
5.  [Testing](#agile-methodology---testing)
    -   [Validation Testing](#validation-testing)
    -   [Manual Testing](#manual-testing)
        - [Responsive](#responsive-testing)
        - [Index Page](#index-page-1)
        - [Register Page](#register-page)
        - [Login Page](#login-page)
        - [Products](#products-page-1)
        - [Product Details](#product-details-page)
        - [Basket](#basket)
        - [Check Out](#check-out-1)
        - [Stripe](#stripe)
        - [Order Confirmation](#order-confirmation)
        - [My Profile](#my-profile-1)
        - [Product Management](#product-management)
        - [FAQ's](#faqs-1)
        - [Contact](#contact)
        - [Subscribe](#subscribe)
    -   [Continued Testing](#continued-testing)   
    -   [Glitches](#glitches)
    -   [Issues](#issues)
6.  [Deployment](#deployment)
    -   [Heroku & Gitpod](#heroku--gitpod)
    -   [Amazon S3](#amazon-S3)
        - [Create a Bucket](#create-a-bucket)
        - [Properties](#properties)
        - [Permissions](#permissions)
    -   [Amazon IAM](#amazon-iam)
    -   [Update settings.py](#update-settingspy)
    -   [Create customstorages.py](#create-customstoragespy)
    -   [Updated Heroku Deployment Via Terminal](#heroku-deployment-via-terminal)
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

1.  I want to be able to *view the social media account(s)* so that I can **keep up to date with news and offers, but also it gives me trust in the company.**

#### Products

1.  I want to be able to *view a list of all products per category* so that I can **select any product(s) to purchase.**

1.  I want to be able to *select a product and view the product details* so that I can **see an overview of the product showing me the important details such as description, price and rating etc.**

1.  I want to be able to *view product size if applicable* so that I can **select the size of product I wish to purchase (stick size or clothing size).**

1.  I want to be able to *select a quantity choice* so that I can **order one or more of the same item.**

1.  I want to be able to *add a product to my basket* so that I can **purchase the item(s) I have selected.**

#### Notifications

1.  I want to be able to *be notified of when I have added a product to my basket* so that I can **see that my request to add the item(s) has been successful.**

1.  I want to be able to *be shown an overview of my basket* so that I can **see the product and the important details I have selected, to ensure they are correct.**

1.  I want to be able to *see the total price of my basket* so that I can **make sure I don't spend more than I want to.**

1.  I want to be able to *find out how much more I need to spend to receive free delivery* so that I can **see if it is cost-effective adding another product(s) to qualify for free delivery.**

1.  I want to be able to *click a button which takes me to my basket and check out* so that I can **proceed with payment easily.**

#### Registration

1.  I want to be able to *register an account* so that I can **I have all the access I require from the site.**

1.  I want to be able to *receive an email confirmation* so that I can **know my request to register has been received and all I need to do is verify my account.**

1.  I want to be able to *login and out of my account* so that I can **ensure my account is safe should I share a computer.**

1.  I want to be able to *reset my password* so that I can **log back in to my account if I have forgotten my password.**

1.  I want to be able to *view previous orders* so that I can **see my purchase history and link to an item I have bought previously.**

1.  I want to be able to *add a default delivery address* so that **when I go to check out, my delivery information is already populated, making the process easier.**

#### Sorting & Searching

1.  I want to be able to *sort the products by certain criteria* so that I can **view the products by a common look such as price lowest to highest etc.**

1.  I want to be able to *search by product category* so that I can **navigate through the products by category e.g. sticks, bags, clothes or accessories.**

1.  I want to be able to *search by keyword* so that I can **find the item I am specifically looking for to purchase.**

1.  I want to be able to *retrieve all products from a keyword search* so that I can **be shown a reduced list of products using the keyword as a filter.**

#### Check Out

1.  I want to be able to *view all items in my basket* so that I can **check my basket and ensure I have all the items and quantities are correct.**

1.  I want to be able to *easily amend any product in my basket* so that I can **add to and reduce the quantity per item.**

1.  I want to be able to *pay for my order* so that I can **process my order and eventually receive my item(s).**

1.  I want to be able to *trust the sites' check out security* so that I can **I feel that personal details (especially banking information) are safe, and the site can be trusted.**

1.  I want to be able to *view my order confirmation after payment* so that **I know my order has been processed and provides a final check should I want to do so.**

1.  I want to be able to *receive an email order confirmation after payment* so that I can **trust my order has been processed, and I have the written confirmation to prove it.**

#### Company Information

1.  I want to be able to *find out more information about the company* so that I can **look into their background and develop an understanding of the business.**

1.  I want to be able to *review the FAQ's* so that **should I have a question, I can see if it has already been answered.**

1.  I want to be able to *contact them directly* so that I can **ensure my query/question can be answered.**

1.  I want to be able to *read through the privacy policy* so that I **know my personal information is secure.**

1.  I want to be able to *subscribe to the site's mailing list* so that I can **receive all the latest deals, offers and news.**

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

The Entity-Relationship Diagram below shows the database models and how they relate to each other.

#### Products
The Products model is used to add products to the site. Only the site owner/admin can add, edit, and delete products. All other users are able to view the products on the site.

#### Category
The Category model is used so that the site owner/admin can assign products to a Category. This ensures the products are in the correct location for users to find. The product category links to the Category name.

#### Order
The Order model is used for the order details (when an order is placed by a user). The user profile of the order model is linked to the User Profile model, providing the user is registered.

#### Order Line Items
Used for the check out details. This is linked to the Order Line Items model, which contains the products (and products model) ordered by the user.

#### User Profile
The User Profile stores the default delivery details again, assuming the user is registered and has chosen to save their delivery address.

## Agile Methodology - Design

### Colour Scheme

-   The site colour scheme is minimalistic but effective.

-   #6D6D6D - Grey
    -   The grey is used throughout the site, for the logo, navigation bar, footer and some action buttons such as "Add to Basket"
    -   All the sticks on offer on the site have a 'progress bar' used for power and control, this uses our main grey against a lighter grey for the background.

-   #000000 - Black
    -   Black is used for the vast majority of the text
    -   The navigation bar items carry a hover & active black pseudo-class to highlight where the cursor is and current page to the user.
    -   A black banner is used to show the free delivery offer and provides a nice contrast from the navigation bar.

-   #FFFFFF - White
    -   The header containing the logo, search bar and account/basket buttons.
    -   The navigation menu items are white at the default state.
    -   The 'free delivery offer' text against the black background is drawn to the user's attention.

### Typography

-   Orbitron
    -   I have chosen to use the same typeface as used on https://www.otterhockey.co.uk for the logo and product names on the product detail pages. This is a conscious choice to increase the continuity on the site in regard to the product images.
    -   The logo uses the bold style, but also carries a subtle drop shadow to make it stand out.
    -   The product name uses the regular style.
    -   As a couple of products contain the letter O and a zero, this typeface provides a completely different look, making it easier for the user to understand the product name.

-   Montserrat (light, medium & bold) 
    -   A large majority of text on the site uses Montserrat.
    -   This is a very popular font for web design because of its readability.
    -   The site uses light, medium and bold font weights in order to highlight certain details. For example, the order confirmation uses the light style for the field names, the medium for the field values and the bold for the subheadings.
    -   This make it more appealing to the user and easier to read or quickly check.

-   Bebas Neue
    -   This typeface is used sparsely, but provides a strong contrast between Orbitron and Montserrat
    -   It is used for the navigation items and the basket total.
    -   Increased letter spacing makes the font more legible for the users.

### Imagery
-   All imagery has been taken from Otter Hockey's site with permission from Kyle as [previously mentioned above](#permission)
-   The hero image has been taken from the Otter Hockey Instagram page .... add more info when chosen
-   All the other imagery used on the site show the products on offer.

## Features
Below is an overview showing the main features of the site.

### Layout (Desktop)
- The site uses the grid set up from Bootstrap, twelve columns split into various different ways across all pages.
- The logo features in the left corner on every page across the site.
- A convenient search bar is placed in the centre of the screen.
- On the right side features ‘My Account’ button containing a dropdown including register and login etc.
- The shopping trolley icon links to the user's basket, which shows the total amount already added.
- The navigation bar sits below the search bar on its own row, centered and spanning half the width of the screen.
- The free delivery offer also spans across the width of the page
but uses a black background and white text, contrasting nicely against the grey on white.
- The vast majority of pages follow a similar theme in terms of page title and subheading(s) if there is one.
- Finally, the footer contains three columns separated clearly by their subheadings.
- More information presents links to three separate pages about us, FAQ’s and privacy policy.
- Subscribe shows an email input field in order to sign up to the fictional newsletter using Mail Chimp.
- The Contact us section contains a further link to an internal page where users can contact customer services via the form. Below the link, the social media icons open new tabs independently (Twitter and Instagram and live genuine links to Otter Hockey).

### Layout (Mobile)
- On smaller devices, the navigation bar is broken down into the collapsable menu via the 'hamburger button'
- The search feature is activated by clicking the icon with the search bar spanning the width of the screen.
- The 'My Account' and trolley icon buttons remain visually identical, except equidistant spacing.
- The footer items are listed in one column, flowing from one to subheading to the next.

![Layout - Mobile](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/index-page-mobile.PNG)

### Index Page
- The hero image covers the width of any screen viewing the site.
- The welcome message is set on a transparent rounded box which focuses the visitor's attention on the welcome message, tag line and button.

![Index Page](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/index-page-desktop.PNG)

### Products Page
- The products page displays two products per row on a desktop and a single product on smaller devices.
- Each product page (Sticks, Bags, Clothes, Accessories) carries its own page title and product count.
- The sort by dropdown contains four options to filter on, such as "Price (low to high)" and "Rating (high to low)".
- The product name is displayed in the logo typeface (Orbitron)
- Shows a brief/cut down product description
- When viewing the Sticks page, the user is shown the power/control score via Bootstrap progress bars.
- The rating values are displayed alongside the star icon and showing the user it is out of 10.
- With the price displayed in a bolder font, the user is immediately aware of the product cost.

![Desktop - Products - Sticks](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/products-sticks-desktop.PNG)
![Desktop - Products - Others](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/products-others-desktop.PNG)

![Mobile - Products - Sticks](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/products-sticks-mobile.PNG)
![Mobile - Products - Others](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/products-others-mobile.PNG)

### Product Detail Page
- A bigger product image covers the left column, and on click opens the linked image in a new tab.
- The full description is revealed.
- Select size dropdown options (if applicable):
    - Sticks - 35.5", 36.5", 37.5", 38.5",
    - Clothes &  Accessories - XS, S, M, L, XL
- The plus and minus button enable the user to adjust quantity before adding the product to the basket.
- Return to result OR KEEP SHOPPING

![Desktop - Product Details - Sticks](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/product-details-sticks-desktop.PNG)
![Desktop - Product Details - Others](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/product-details-others-desktop.PNG)

- All action elements such as size dropdowns, the quantity selector, add to basket button and keep shopping button all layout in single columns, full width of the container.

![Mobile - Product Details - Sticks](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/product-details-sticks-mobile.PNG)
![Mobile - Product Details - Others](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/product-details-others-mobile.PNG)

### Basket (Desktop)
- The table format works well for larger devices containing a larger image, product details such as product name, rating, size selected and sku reference. 
- The next column contains the price per item
- As a user, you are able to adjust the quantity of each item in the basket. This is activated via the plus and minus buttons and then by clicking 'update'.
- Making any changes to the quantity of an item will adjust the subtotal.
- The final column displays a bin icon used to remove an item from the basket.

![Desktop Basket 1](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/basket-1-desktop.PNG)

- All the costs are contained in their own row, including the basket total (no delivery cost), delivery total and grand total.
- All three totals are split out and easy to differentiate based on the various fonts.
- The check out button uses another icon from FontAwesome and follows the same button theme.

![Desktop Basket 2](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/basket-2-desktop.PNG)

- The free delivery offer uses an icon to display to the user if they have qualified for the deal.
- When the basket is below £100 hovering off the cross icon, produces a pop-up with the amount needed to add to the basket for free delivery.

![Delivery pop-over](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/delivery-popover.PNG)

- An Empty basket present a different basket look, informing the user there are no items to check out and provides a handy link to the sticks page.

![Empty Basket](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/empty-basket.PNG)

### Basket (Mobile)

- Viewing the basket on a mobile/smaller devices shows a very different layout.
- All the basket details are spread across the width of the screen.
- The product image is at the top of the screen and centered followed by product name, rating, size and sku all left aligned.
- The price is centered and bold
- The quantity selector is on the following row
- Followed by the subtotal copying the price styling.
- The bin icon is the last graphic centered below the subtotal.

![Mobile Basket 1](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/basket-1-mobile.PNG)

- After scrolling past the final item in the basket, the user is shown the final costs along with the secure check out button.

![Mobile Basket 2](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/basket-2-mobile.PNG)

### Check Out (Desktop)

- The check out page follows a similar theme, with the check out form covering the left side of the screen (on larger devices).
- The same inset border has been used along with the placeholders.
- Split into three sections; Personal Details, Delivery Details and Card Details.
- The Personal Details are quite standard, with full name and email address. Invalid email addresses will produce a validation error and will stop confirmation.  
- If the user has created an account and is logged in, they can either manually enter their delivery address in and save it to their profile using the tick box, or enter their details in the 'my profile' page [(as seen below)](#my-profile) to enable the autofill.
- If this is a new user without an account instead of seeing a save tick box, they are shown two links, one to create an account (linking to the registration page) the other to login.
- The final section shows an input field used for the user's card number, expiry date and security code.
- Just like the email field, a validation error will appear should any card details be incorrect
- The final charge amount is displayed at the bottom of the page below the card input field. Providing further assurance to the user that the correct amount will be processed.
- The order summary on the right side provides a list of the items in the basket including their key details such as name, size, quantity and subtotal, along with a small image.
- When the summary contains multiple items pushing past the check out form, a scroll bar then appears to keep the page to a sensible scrolling size.
- The costs are presented in the same way as the basket page.
- Next to the confirm order button is a return to basket formatted in the secondary button theme.

![Check Out](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/checkout.PNG)

### Order Confirmation (Desktop)

- The order confirmation page is almost identical to the check out page, but instead of input fields, all the check out data is written with the user input in bold. This includes all delivery details and final costings.
- The order number is randomly generated with a string of 32 characters.
- From the order confirmation, the user is able to link to their profile (assuming the user is registered)

![Order Confirmation](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/order-confirmation.PNG)

### My Profile
- The 'My Profile' tab is only available once a user has created an account and logged in.
- From this page they are able to add and amend default delivery details which are copied through to check out page to save the user repeating their information.
- Order history provides a list of confirmed orders from the logged-in user.
- It shows the order number, linked to the order confirmation.
- The date the order was submitted, items from the order and the subtotal are also on view.

![My Profile](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/my-profile.PNG)

- A toast notification appears to make the user aware that this is a previous order
- From the order confirmation, the user is able to return to the profile using the action button.

![My Profile - Order Confirmation](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/my-profile-order-confirmation.PNG)

### Product Management - (Page)
- As an admin user, under the product management tab, you are able to add products to the database using the form displayed.
- Ensuring the required fields contain valid data you are able to submit the product adding to the database and the site for users to view.
- Creating a product that doesn't yet have a product image will display the Otter Hockey logo by default.

![Product Management - Add Product](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/add-product.PNG)

### Product Management - (Via Products)
- When an admin user is logged on, they have the permission to edit and/or delete any product on the site.
- When clicking the edit link, the user is redirected to the product management form, autofilled with the product details from the database in order to amend on save.
- After the admin user has saved their changes, they are redirected back to the product detail page of that product.

![Product Management - Edit Product](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/edit-product.PNG)

### Allauth Pages (Register, Login, Logout etc)
- The majority of Allauth pages contain a form or form element.
- The input fields are spread across half the screen on large devices and full width on smaller devices.
- The use of 'inset' black and grey borders carry more of a visual impact than standard or no border at all.
- Action button(s) use the consistent grey and white theme. 

![Sign In](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/sign-in.PNG)

![Sign Up](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/sign-up.PNG)

### Bootstrap Alerts (Toasts)
- Positioned on the right side of the screen underneath the basket total.
- The toasts are a consistent feature across the site, triggered by various actions such as login, logout, adding an item to the basket and check out confirmation amongst others.

![Toast - Sign In](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/toast-sign-in.PNG)
![Toast - Log Out](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/toast-log-out.PNG)
![Toast - Add to Basket](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/toast-add-to-basket.PNG)
![Toast - Remove from Basket](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/toast-remove-from-basket.PNG)
![Toast - Order Confirmation](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/toast-order-confirmation.PNG)

### About us
- The about us content has been taken from [Otter Hockey](https://www.otterhockey.co.uk) displayed in simple block paragraphs with subheadings.

![About Us](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/about-us.PNG)

### FAQ’s
- The FAQ's are presented via a Bootstrap accordions, separated into three sections; Orders, Delivery and Returns.

![FAQ's](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/faqs.PNG)

### Privacy Policy
- The privacy policy has been created using [Terms Feed](https://www.termsfeed.com/privacy-policy-generator/) and displayed in a similar format to the about us page using block paragraphs and subheadings.

![Privacy Policy](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/privacy-policy.PNG)

### Contact Us
- Contact form continues the style theme from the Allauth pages in terms of black/grey inset borders.
- On the right side is an interactive map showing the location of Otter Hockey HQ.
- When the user submits the form, they are ensured success through the toast notification.

![Contact Us](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/contact-us.PNG)

### Error 404 - Page not found
- The error page uses the index page as a template, replacing the welcome message and tag line to page not found and a suggestion.
- Leaving the sticks button intact.

![Error 404](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/error-404.PNG)

### Django Admin Site

![Django Admin - Overview](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/django-admin-overview.PNG)

#### Login

-   The admin site is username and password protected for obvious reason. Only a "Superuser" or "Staff status" have access.

![Django Admin - Login](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/django-admin-login.PNG)

#### Create Order

-   As an admin user you have the ability to create manual orders "ADD ORDER"
-   The form uses a dropdown menu to select the user profile to ensure the user has created an account in order to make a reservation.
-   The user details are at the top page such as delivery address and then basket products at the bottom producing a list of database items
-   The size field is available on all products and accepts stick sizes and clothes sizes.
-   Adjusting the quantity will change the line item total on save. 

![Django Admin - Create Order](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/django-admin-create-order.PNG)

#### Amend Order

- Via the orders tab, an admin user is able to amend any order in the database, ranging from the personal details such as the delivery address to line items like adding and removing products and amending sizes and quantities.

![Django Admin - Amend Order](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/django-admin-amend-order.PNG)

#### Amend Product

- Amending an existing product is a simple task, after clicking on the product link the form is autofilled with product details.
- After changing a field or fields, clicking save at the bottom of the page updates the database and therefore the site.

![Django Admin - Amend Product](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/django-admin-amend-product.PNG)

#### Amend User

- They have the ability to add and amend users, including changing their names, email address, username and even their password and permissions.

![Django Admin - Amend User](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/django-admin-amend-user.PNG)

#### User Activity

- It also shows the user's activity in terms of their last login and when they registered.
- Finally, users can be deleted by an admin user.

![Django Admin - User Important Dates](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/django-admin-user-dates.PNG)

#### Recent Actions

- The "recent actions" panel shows the last 10 changes to any database on the admin site.
- The pencil icon indicates a change.
- The cross icon indicates a deletion.

![Django Admin - Recent Actions](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/django-admin-recent-actions.PNG)

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
-   [Stripe](https://stripe.com/en-gb) was used to enable users to make a transaction.
-   [Bootstrap](https://getbootstrap.com/) was used to create the framework for the site, including the grid set up and other components such as buttons, toasts, progress bars and the accordian.
-   [Font Awesome](https://fontawesome.com/) was used for the social media icons within the footer.
-   [Google Fonts](https://fonts.google.com/) was used to import the 'Orbitron', 'Bebas Neue' and 'Montserrat' into the style.css file.
-   [GitPod](https://gitpod.io/) was used to create and update the website throughout, via the terminal to push changes to GitHub.
-   [GitHub](https://github.com/) was used to commit changes during development and ensure no work was lost.
-   [Figma](https://figma.com/) was used to create the wireframes during the design process.
-   [Lucidchart](https://lucidchart.com/) was used to create the step by step workflow to visualise how the user can book and manage their reservation.

### Web Marketing

-   A Facebook page has been created in order to promote the company, site and products.

![Facebook Page 1](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/facebook-page-1.PNG)
![Facebook Page 2](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/facebook-page-2.PNG)

-   The Facebook page has now been removed (28/08/22), therefore the footer link, reddirects the user to the Facebook login page. 

-   Another use of web marketing is the use of MailChimp, this has set up to connect the user to a fictional monthly newsletter.

### Search Engine Optimisation (SEO)

In order to find the relevant keywords for my project I made the following searches on Google and [Word Tracker](https://www.wordtracker.com/). Below is a list of keywords used:
- Hockey sticks
- Premimum hockey sticks
- Hockey equipment
- Hockey bags
- Hockey accessories
- Hockey gifts

After making these searches I discovered that because of what Americans would call hockey (Ice Hockey), I should add 'Field' to my searches.

- Field Hockey sticks
- Premimum field hockey sticks
- Field hockey equipment
- Field Hockey bags
- Field Hockey accessories
- Field Hockey gifts

The results were very dissapointing with hockey brands coming back as alternative searches, such as
- Grays field hockey sticks
- Adidas field hockey sticks
- TK hockey sticks
- Osaka field hockey sticks

Using this feedback I added all 'field' combinations to my metadata keywords.
It also shows that the target market for hockey products, especially sticks, are aware of the brands and know what type of stick they would like to purchase.
It seems it is all about brand awareness!

## Agile Methodology - Testing

### Validation Testing

The W3C Markup Validator and W3C CSS Validator Services were used to ensure there were no syntax errors in the project.

- [W3C HTML Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fotter-hockey.herokuapp.com%2F)
    -   "Element li not allowed as child of element nav in this context. (Suppressing further errors from this subtree.)"
    -   I tried different options to eliminate this error, but everything attempting broke the dropdown links.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fotter-hockey.herokuapp.com)
    -   The only warning produces from the developer's CSS was pointing to the 'cut-down' description shown on the products page. However, due to this being a [reference](#references) and it working correctly on all devices, the code remains.
![CSS Warnings](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/css-warning.PNG)
-   The only warnings from the validation were seen from Mailchimp and Bootstrap styles, not the developer's css.
- [Jshint JavaScript Linter](https://jshint.com/)
- All the Javascript files have been tested and validated through jshint.
    - 'stripe_element.js' returned just two warnings pointing to the same statment - " 'template literal syntax' is only available in ES6 (use 'esversion: 6')."
    - It appeared to not recognise the backtick. 

- [PEP8](http://pep8online.com/) Python linter was used to ensure there were no syntax errors in the project.
Checking all individual files separately produced numerous errors. The vast majority looking at easily fixed issues, such as:
    - "line too long"
    - "blank line contains whitespace"
    - "too many blank lines (2)"
    - "indentation is not a multiple of four"

These have now all be rectified.
Below are links to all indivdual Pep8 results

#### Otter_Hockey App

- [urls.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/otter_hockey_urls_results.txt)

- [views.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/otter_hockey_views_results.txt)

#### Home App

- [urls.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/home_urls_results.txt)

- [views.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/home_views_results.txt)

#### Products App

- [admin.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/products_admin_results.txt)

- [forms.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/products_forms_results.txt)

- [models.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/products_models_results.txt)

- [urls.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/products_urls_results.txt)

- [views.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/products_views_results.txt)

#### Bag App

- [context.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/bag_context_results.txt)

- [urls.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/bag_urls_results.txt)

- [views.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/bag_views_results.txt)

#### Checkout App

- [admin.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/checkout_admin_results.txt)

- [forms.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/checkout_forms_results.txt)

- [models.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/checkout_models_results.txt)

- [urls.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/checkout_urls_results.txt)

- [views.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/checkout_views_results.txt)

- [webhook_handler.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/checkout_webhook_handler_results.txt)

- [webhooks.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/checkout_webhooks_results.txt)

#### Profiles App

- [forms.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/profiles_forms_results.txt)

- [models.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/profiles_models_results.txt)

- [urls.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/profiles_urls_results.txt)

- [views.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/profiles_views_results.txt)

#### Company App 

- [urls.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/company_urls_results.txt)

- [views.py](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/pep8/company_views_results.txt)

### Manual Testing

#### Responsive Testing
- The site has been tested on an iMac, PC, Laptop, iPad and iPhone X.
- At mobile phone width the 'hamburger bars' are shown, in order to shrink and expand the navigation bar.
![Hamburger bars](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/hamburger-bars.PNG)
- All forms are spread across the width of the screen on smaller devices
- The vast majority of buttons are also spread across the width and stacked above one another.
- The footer elements are displayed in a singe column on smaller devices, with all content centered.

#### Index Page
- [x] Otter Hockey logo link 
    - Links to the home page from every page successfully.
- [x] Search bar results
    - Produces results when keyword found with number of results.
    - Zero results found on any keyword not in the database '0 Products found for "test"'
![No results found](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/no-results.PNG)
- [x] Individual page links
    - All pages link to one another from any page.
- [x] Social media links open in new tab
    - All three social media sites are linked to open new tabs, this can be done from any web page.
- [x] Window links to the sticks products page
- Window button 'View all Sticks' successfully links to the sticks products page.

#### Register Page
- [x] Email address already exists
    - Attempting to create a user with the same email address produces a validation error, "A user is already registered with this e-mail address."

![Email address exists](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/username-exists.PNG)

- [x] Username already exists
        - Attempting to create a user with the same username produces a validation error, "A user with that username already exists."

![Username exists](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/username-exists.PNG)

![Username & email address exists](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/username-email-exists.PNG)

- [x] All fields are required
    - The form does not submit unless all the fields have been completed with valid data.
- [x] Not a recognised email address.
    - A common validation error could be the follow:
        'Please use an '@' in the email address'.
- [x] Passwords don't match
    - When creating a user and the passwords don't match, a validation error is presented. "You must type the same password each time."

![Passwords don't match](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/password-dont-match.PNG)

- [x] Password not secure
    - If the password isn't strong enough, another validation error is shown. "This password is too short. It must contain at least 8 characters. This password is too common."
    - Using a purely numerical password also isn't allowed. "This password is entirely numeric."

![Password invalid](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/password-invalid.PNG)

- [x] Sign in link
    - The link redirects the user to the sign-in form as expected, autofilling if the user uses the 'remember me' feature.

#### Login Page
- [x] Invalid credentials
    - Attempting to sign in as a user that has not been registered I am greeted with an error message, "The username and/or password you specified are not correct."

![Invalid credentials](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/invalid-user.PNG)

- [x] Remember me
    - The 'Remember Me' checkbox works correctly, after logging in with one user, clicking the checkbox and signing out. The username produced was the last used. This was tested on multiple user accounts.
- [x] Register link "sign up"
    - The link redirects the user to the register form as expected.

#### Logout Page
- [x] Logout link
    - The logout button works from any page on the site.

#### Products Page
- [x] View products by category
    - The navigation bar provides a very easy and convenient way to view the products by category.
- [x] Product count
    - Each category shows the amount of products on offer.
- [x] Product name links to product detail page
    - As the product range is small, I have been able to test all product links via the product name.
- [x] Product image links to product detail page
    - As the product range is small, I have been able to test all product links via the product image.
- [x] Sort by filter
    - Each filter has been tested on every category page and works as expected.
- [x] Stick parameters
    - As expected, the stick parameters are only visible on the sticks category page. All the values match the database input figures.
- [x] Return to top of the page
    - The back to top button is visible on all product pages and sends the user back to the first row of products.

#### Product Details Page
- [x] Larger product image in new tab
    - Every product image opens in a new tab linked to S3, where the images are stored.
- [x] Stick parameters
    - Only the stick products display the power and control progress bars.
- [x] Size dropdown
    - All products have been checked ensuring the sticks use the stick sizes, all clothes use the clothes sizes and the bags don't show a size selector.
    - All the accessories except the chamois grip use clothes sizes.
    - All the products that have a size options are required in order to the item to the basket.
![Size required](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/size-required.PNG)
- [x] Quantity buttons
    - All the products show the quantity selector option.
    - It is impossible to add another below 1 to the basket
    - The quantity selector is always right aligned whether a sizes field is required or not.
- [x] Add to basket button
    - Providing all the fields are filled in correctly, every product can added to the basket.
- [x] Keep shopping button
    - The keep shopping button returns the user to the all products page on every product detail page tested.

#### Basket
- [x] Correct product image
    - Every product added to the basket produced the correct image.
- [x] Correct product name
    - Every product added to the basket produced the correct product name.
- [x] Correct product rating
    - Every product added to the basket produced the correct product rating.
- [x] Correct product sku
    - Every product added to the basket produced the correct product sku.
- [x] Correct product price
    - Every product added to the basket produced the correct product price.
- [x] Correct selected quantity
    - Every product added to the basket produced the quantity input from the product detail page.
- [x] Adjust basket
    - When amending any product in the basket, like increasing or decreasing quanity the sub total of each product was recalculated to match along with all the totals.
- [x] Basket total
    - To ensure the basket total was correct I added numerous products to the basket multiple times and added them up using a calculator.
- [x] Delivery offer icon
    - The delivery offer icon changes everytime I go over the £100 mark as expected.
- [x] Delivery pop-over calculation
    - The pop-over calculation was tested a number of times with different amounts in the basket and then manually calculated.
- [x] Delivery total
    - The delivery total automatically updates when the basket is over £100 to £0.00
    - By default the delivery total is £5.00
- [x] Grand total
    - To ensure the grand total was correct I added numerous products to the basket multiple times and added them up using a calculator.
    - I also made sure to edit the basket continuously to update the basket total and delivery total.
- [x] Secure check out button
    - The check out button links successfully.
- [x] Empty basket
    - The empty basket page is displayed correctly when nothing is in the basket and when all items have been manually removed from the basket.

#### Stripe
- [x] All events created successfully
    - Logging into Stripe, I was able to see all events for checkout were successfully created and processed with HTTP status codes of 200.

![Stripe - Events](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/stripe-events.PNG)

- [x] All webhooks created successfully
    - Viewing the webhooks section, all three webhooks were created, again all with HTTP status codes of 200. 

![Stripe - Webhooks](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/stripe-webhooks.PNG)


#### Check Out
- [x] All '*' fields are required
    - Only the fields with a '*' in the placeholder are required, not filling these fields in will not submit the order.
    - Every other delivery field can be left blank, and the order will be submitted successfully.
- [x] Email address is valid
    - The email address field follows the same checks on the check out page as when a user registers.
- [x] User details autofill
    - The user's delivery details auto-populate providing the user has created an account and filled in their profile information.
    - They also update when amending from the 'My Profile' page, even when there are items already in the basket.
- [x] Create and log in links
    - The create and log in links only appear when a user hasn't logged in to their account.
![Create an account or login](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/check out-create-account-login.PNG)
    - Both links redirect to the correct pages.
- [x] Save checkbox is available
    - The save details checkbox is present only when a user has created an account and is signed in.
![Save to profile](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/check out-save-to-profile.PNG)
    - Creating a number of users and clicking the option updated as expected.
    - Leaving the option unticked leaves the default values as the last saved input credentials, either from the check out page or 'My Profile'.
- [x] Card details verification
    - The card input field has built in verification from Stripe, this notifies the user if the card number, expiry date or security code is invalid.
    - The error message is displayed underneath the input field.
![Card verification](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/card-verification.PNG)
- [x] Charge amount is correct.
    - The charge amount has been calculated manually and matches the grand total.
- [x] Order summary matches basket
    - The order summary is an exact match to what has been shown in the basket every time.
- [x] Basket total
    - The basket total has never differed from the value shown on the basket page.
- [x] Delivery offer icon
    - The delivery offer icon remains in place with the icons used
- [x] Delivery pop-over calculation
    - The pop-over calculation also remains in place with the same calculation shown to the user, matching the basket calculation.
- [x] Delivery total
    - The delivery total copies through from the basket as expected with only two outcomes £5.00 or £0.00
- [x] Grand total
    - Again, the grand total is an exact match to the grand total shown on the basket page.
    - To ensure this is correct, I have manually calculated the grand total numerous times.
- [x] Confirm order button
    - As stated above, providing the required fields have been filled in and the bank details are valid, the confirm order button works as expected and the user is redirected to the order confirmation page.
- [x] Return to basket button
    - The return to basket sends the user back to the basket with all items intact to amend or add to.

#### Order Confirmation 
- [x] Email confirmation has been sent to email address from check out
    - The email address, highlighted in bold, corresponds to the email input field on the check out page.
    - Checked out using multiple users, with email confirmations successfully received.
- [x] Order number has been randomly generated
    - The order number randomly generated from a mixture of 32 characters. 
    - Duplicates are almost impossible.
- [x] Order date is correct
    - The order date shown is correct to the GMT (Greenwich Mean Time)
    - This includes BST (British Summer Time) UTC +1
- [x] All delivery information matches the check out fields
    - The delivery address are the same details as input on the check out page.
- [x] order total matches basket total from check out
    - For the third page in a row, the basket total is a direct copy and has been manually calculated.
- [x] Delivery total matches check out
    - For the third page in a row, the delivery total copies through as expected with only two outcomes £5.00 or £0.00
    - No need for the free delivery icon on this page.
- [x] Grand total matches check out
    - For the third page in a row, the grand total is a match to all previous two pages and has been manually calculated to ensure the maths are correct.
- [x] Purchased products matches Order summary from check out
    - The purchase summary matches the check out page with the same product details pulling through.
- [x] Return home button
    - The return home button redirects the user to the index page as expected, whether the user is logged in or out.
- [x] View account button
    - Clicking the view account button provides two different outcomes depending on if the user is logged in or not
    - If the user **is** logged in, they will be sent to the 'My Profile' page where they will be able to see the order they have just placed, and any past orders should there be any.
    - If the user **is not** logged in, clicking the button will force the user to sign in or register as a new user.

#### My Profile 
- [x] Default address fields placeholders
    - All the placeholders are visible to every logged-in user.
- [x] Country dropdown
    - A full list of countries are presented
    - The option of "Country" is used as a placeholder
    - However, this option will not work for the check out page, ensuring it can't be missed, and the validation error will appear.
- [x] Update details
    - With none of the fields being required, the form saves via the click of the button
    - Every time the profile is updated the check out delivery address is changed
    - This includes going from an input address to removing it completely.
- [x] Order history
    - Logging in as various users, the order history is only showing orders relating to that logged-in user.
- [x] Order data
    - The order data shown in the history relates to the user's order
    - Proving the order number, the date ordered, the items and the total.
- [x] Order link
    - The order number underlined produces a link to the confirmation order and links through to any user order.
- [x] Previous order known to user
    - A toast notification is raised when the order confirmation is shown, for example, "This is a past confirmation for order number 29AEDBC9DEDA48659494F13C75564175."
![Previous order](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/previous-order.PNG)
- [x] Order Confirmation
    - The order confirmation shown from the profile link matches the order confirmation shown to the user from the standard check out procedure.
- [x] Return to profile
    - The return to profile button is present on all order history links and is only displayed to the user via the 'My Profile' page.

#### Product Management
- [x] Required fields
    - The required fields are marked up with asterisks to notify the user that they need to contain valid data.
- [x] category dropdown
    - The category dropdown contains the options taken from the site using the friendly name and ensure the new product is located in the correct category.
- [x] Invalid price
    - The price field is set to two decimal places and maximum of 6 figures.
    - Entering a price for example like "100.999" is not submitted
    - A validation error is shown, "Please enter a valid value".
- [x] Invalid rating
    - Similarly, the rating field only uses integers and therefore decimal places are not allowed.
    - Like the price field producing a validation error.
- [x] No image
    - When no image has been specified, the default image (Otter Hockey logo) is used as the product image
    - This is shown on the products page and inside the product details.
- [x] Select image
    - Conversely, selecting an image to use is displayed as expected.
- [x] return home button
    - The return home button cancels the product creation and redirects the user back to the index page.
- [x] Add product
    - Using a valid product form and clicking the add product button, creates the product in the database and redirects the user to the newly created item.
    - All details filled in from the form are carried through, for example name, description, price, rating and stick parameters (category permitting).

#### FAQ'S
- [x] Accordions
    - Every combination of the accordions has been checked.
    - Only one question per section can be opened at once.
    - Opening another question from the same section will close the first opened accordion.

#### Contact
- [x] Required fields
    - All the contact fields are required, leaving any fields blank will result in the form not being submitted.
- [x] Email address is valid
    - Like all email fields, the email address input must be valid, for example uses a "@".
- [x] Message sent
    - The send button is activated when all the fields having been field in
    - On a successful post, the user is redirected to the home page with a toast notification - "Your message has been sent, we will contact you via ... as soon as possible."

#### Subscribe
- [x] Email address is valid
    - Attempting to submit an invalid email address, produces a validation error, "Please enter a valid email address."
- [x] Success message displayed
    - Assuming a valid email address has been entered, after clicking the subscribe button the user receives a success message "Thank you for subscribing!"

### Lighthouse Testing
On first testing, the lighthouse performance results were below par at around 70-75 (url dependent). Pointing to various oppertunities such as:
-   Eliminate render-blocking resources
-   Reduce unused JavaScript
-   Enable text compression
Although there isn't much I can do about the Stripe and Bootstrap components, I can ensure my CSS doesn't contain unused code.
- Desktop Results

![Lighthouse Desktop Results](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/lighthouse-desktop.PNG)

- Mobile Results

![Lighthouse Mobile Results](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/lighthouse-mobile.PNG)

### Continued Testing

TO BE REPLACED 

- The Website was tested on Google Chrome and Microsoft Edge.
- The website has been displayed on various devices such as Desktop PC, iMac, Laptop, iPhone X & iPad Pro
- Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Glitches

- Viewing the site on my mobile, the navigation bar appears to be transparent and therefore on a scroll the content container is viewable over the nav.
    - This doesn't occur using the Google Chrome developer tool.

## Issues

Adjust bag - Size is removed.

## Deployment

### Heroku & GitPod

Heroku & GitPod were the program used to share and deploy the app, it was accomplished by using the following steps:

1. Log in to Heroku. On your dashboard, click "New" and then click "Create new app".
2. Fill in the field for App name - It must be a unique name to Heroku. 
    -   Then select the region of Europe and click "Create app".

![Heroku - New app](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/heroku-create-app.PNG)

3. In the "Resources" tab, scroll down to "Add-ons" and search for "Heroku Postgres".
    -   Once selected and saved in the "Settings" tab click "Reveal Config Vars", this produces a database url.

![Heroku - Add Heroku Postgres](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/heroku-resources.PNG)

4. In GitPod set up an env.py file in the repository.
    -   Create an environment variable for "DATABASE_URL" and paste the value from Heroku.
    -   Create an environment variable for "SECRET_KEY" and create your key using any characters available.
5.  Copy the secret key to Heroku by adding the variable in the "Config Vars" section.
6.  In the settings.py file import:
    -   os
    -   dj_database_url
-   Add the if statement:
```
if os.path.isfile('env.py'): import env
```
7.  Amend the secret key variable to the secure key created earlier:
```
SECRET_KEY = os.environ.get('SECRET_KEY')
```
8.  Add our Heroku host name into the allowed hosts, this is your Heroku app name followed by herokuapp.com.
    -   Add "localhost" too, so the app can be ran locally.
9.  Scroll down to the "DATABASES" section
    -   'Comment out' the default code and add the "DATABASE_URL" variable created earlier:
```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```
10. Create a Procfile
    -   It must be named like so; "Procfile" and sit inside the root directory.
    -   Within the file add "web: gunicorn" followed by the app name .wsgi.
    -   For example: "web: gunicorn otter_hockey.wsgi".
11. Scroll back and click the tab "Deploy".
    -   Choose "GitHub" as the Deployment method.
    -   Enter the GitHub repository name and click "Search".
    -   The repository should appear below, then click "Connect".

![Heroku - Deployment method](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/heroku-deploy-section.PNG)

12.  Then click the "Deploy Branch" button in the "Manual deploy" section. This way you can see the code being written.

![Heroku - Manual deployment](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/heroku-manual-deploy.PNG)

13. Once that is complete, a message will appear with "Your app was successfully deployed" and a "View" button. This will take you to the app directly.

![Heroku - Successfully Deployed](https://raw.githubusercontent.com/liamsmith3194/otter-hockey/main/static/readme-images/heroku-deployed-successfully.PNG)

### Amazon S3
Amazon S3 was used to store all media and static file for the site. It was set up using the following steps after creating an Amazon Web Service account:
- Search for S3 under the services tab

#### Create a Bucket
1.  Click the orange 'Create a Bucket' button. Give the bucket a name, I used "otter-hockey"
2.  I then selected my closest region "EU (London) eu-west-2" and changed the 'Object Ownership' setting to ACLs enabled. 
3.  Finally, I unticked the 'Block all public access' box and ticked the 'I acknowledge that the current settings might result in this bucket and the objects within becoming public.' box and clicked on the 'Create Bucket' button.

#### Properties
1.  On the properties tab, scroll to the bottom of the page and turned on static website hosting. 
2.  Fill in the index and error document fields with the default values as they won't be used and click save.
-   This provides a new endpoint that can be used to access it from the internet.

#### Permissions
1.  On the permissions tab, scroll down to 'Cross-origin resource sharing (CORS)' section and paste in the following CORS configuration:
```
[
{
    "AllowedHeaders": [
    "Authorization"
    ],

    "AllowedMethods": [
    "GET"
    ],

    "AllowedOrigins": [
    "*"
    ],

    "ExposeHeaders": []
}
]
```
-   This provides access between our Heroku app and this S3 bucket.

2.  Next, click on the 'Bucket Policy' tab and click 'Policy Generator'
3.  Policy type is "S3 Bucket Policy", In the principal field add a "*" which will allow all. Using the actions dropdown, select "GetObject"
4.  Copy the ARN, which can be found in 'Properties' tab, under 'Bucket Overview' and paste into the 'ARN' field.
5.  Click 'Add Statement', then 'Generate Policy' and then select and copy the policy.
6.  Paste the policy into the 'Bucket policy' editor
7.  To allow access to all resources in this bucket, add a "/*" to the end of the "Resource" line ``` "Resource": "arn:aws:s3:::otter-hockey/*"``` and click 'Save'.
8.  Lastly, under the 'Access control list (ACL)' section, click edit and enable 'List' for 'Everyone (public access)' and accept the warning box.

### Amazon IAM
- To access the bucket you need to create a user, this is where Amazon IAM (Identify and Access Management) comes in.
- Search for IAM under the services tab

1.  Create a User group - Click on 'User Groups' and then click button 'Create Group' giving it the name "manage-otter-hockey".
2.  Create the Policy used to access our bucket by clicking 'Policies' and then click button 'Create Policy'. 
3.  Click on the JSON tab and select 'Import managed policy' to import a pre-built AWS policy for full access to S3. Then click 'Import'.
4.  Inside the JSON editor, we need to amend the "Resource" line again to give access to the bucket. (You may need to go back to S3 and copy the ARN again)
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "arn:aws:s3:::otter-hockey",
                "arn:aws:s3:::otter-hockey/*"
            ]
        }
    ]
}
```
-   The "arn:aws:s3:::otter-hockey/*" allows access to all files and folders in the bucket.

5.  The click 'Review policy'. Provide a name and a description. I used "otter-hockey-policy" with a description of "Access to S3 bucket for Otter Hockey static files".
6.  Next, attach the policy to the Group by clicking 'User Groups', selecting the group name "manage-otter-hockey" and clicking on the 'permissions' tab.
7.  Then click on the button that says 'Add permissions' and click 'Attach policies'.
8.  Select the policy "otter-hockey-policy" and click 'Add permissions' at the bottom of the page.
9.  Finally, create a user clicking 'User' User's page and clicking 'Add users' button. Give the user a name, I called mine "otter-hockey-staticfiles-user" I created a user named clay-and-fire-static-files-user and gave them 'Programmatic access'. Click 'Next'.
10. Select the group you want to assign the user to by ticking the box and click 'Next'. Keeping clicking until you reach 'Create user', click one more time and download the CSV file.
11. This file contains the User's Access Key and Secret Access Key, both of which are used later in the settings.py file but first need adding to the "Config Vars" in Heroku:
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
12. While in the "Config Vars" add with a new variable:
- USE_AWS = True

### Update settings.py

1.  In order to connect Django to the newly created S3 bucket, install two packages and freeze them:
- boto3
- django-storages
2.  In settings.py add 'storages' to the list of 'INSTALLED_APPS'
3.  Under the static files information towards the bottom of the page, we need to add the following if statement:
```
if 'USE_AWS' in os.environ:
            
    AWS_STORAGE_BUCKET_NAME = 'otter-hockey'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
     
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
4.  I then added the following to our 'Config Vars' on Heroku:
- USE_AWS = True
- AWS_ACCESS_KEY_ID, taken from the new user credentials
- AWS_SECRET_ACCESS_KEY, taken from the new user credentials

5.  The next step is to tell Django that in production we want to use S3 to store our static files whenever someone runs collectstatic and that we want any uploaded product images to go there also. To do that, I created a file called custom_storages.py.

### Create custom_storages.py

1.  To store the static files in S3 during production, we need to create a new file called 'custom_storages.py'
2.  First import settings from django.conf and the s3boto3 storage class from Django Storages.
3.  Then create a custom class 'StaticStorage' and 'MediaStorage' and set the location to use the 'USE_AWS' if statement from settings.py
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

### Heroku Deployment Via Terminal

Code and site updates pushed to Heroku were conducted in the following way:
1.  Via the terminal in GitPod, login in to Heroku using the command: "heroku login -i"
2.  Enter the email address linked to the Heroku user.
3.  Enter your password, if your password doesn't work use the API key which is found in Heroku under the account settings towards the bottom of the page.
4.  The terminal prints "Logged in as (email address)"
5.  You then select the application you want to deploy with the command: "heroku git:remote -a (app name)"
6.  Successfully identifying the app, the terminal will show this message "set git remote heroku to `https://git.heroku.com/(app name).git`"
7.  The final command: "git push heroku main".

-   On final deployment, the project **must** be set up in the following way:
    -   DEBUG is set to false in settings.py file
    -   staticcollect=1 from Config Vars in Heroku deleted.

## Agile Methodology - Evaluation

### Site Visitor Goals

As a customer/site user ...

#### Customer Viewing

1.  I want to be able to *immediately understand the purpose and meaning of the site* so that I can **feel assured that I am on the right site for what I am looking to purchase.**

    - With the hero image advertising a stick product and the name ‘Otter Hockey’ shown for the logo, it is abundantly clear what the site is selling, even as someone who doesn’t play the sport.

1.  I want to be able to *be made aware of any deals available* so that I can **make the most of what is on offer, whether it is free delivery or 10% off etc.**
    - The use of the banner is a great way to advertise deals, in this case free delivery over £100.
    - The colour scheme of white on black provides a good contrast to the navigation bar.

1.  I want to be able to *view the social media account(s)* so that I can **keep up to date with news and offers, but also it gives me trust in the company.**
    - All the social media links are located at the bottom of the page, and broken down into their own sections, which breaks down the footer nicely.

#### Products

1.  I want to be able to *view a list of all products per category* so that I can **select any product(s) to purchase.**

    - The navigation bar allows me to view products by category really easily, with the links taking me straight to the product in question.
    - Each product category page uses a subtitle such as ‘Full range of sticks’, giving me reassurance that I have followed the correct link. 

1.  I want to be able to *select a product and view the product details* so that I can **see an overview of the product showing me the important details such as description, price and rating etc.**

    - I am able to see the vast majority of important product details from the products page.
    - Nicely presented with different typography displaying different pieces of data.
    - The use of the ‘progress bars’ adds something different to the sticks category page, and coloured in the grey used throughout the site, which fits in with the theme.

1.  I want to be able to *view product size if applicable* so that I can **select the size of product I wish to purchase (stick size or clothing size).**

    - The size selector dropdown is easily identified, with the ‘Select Size’ placeholder
    - The size options are dependent on product category, and anything without a size doesn’t have the dropdown menu to view.

1.  I want to be able to *select a quantity choice* so that I can **order one or more of the same item.**

    - The plus/minus boxes are presented well in order to change the quantity
    - Clicking the buttons changes the quantity value accordingly. Also, the ability to never add anything lower than 1, provides a clever ‘safety net’.

1.  I want to be able to *add a product to my basket* so that I can **purchase the item(s) I have selected.**

    - Providing the required fields contain valid data, I am able to add any product to my basket with a click of a button.
    
#### Notifications

1.  I want to be able to *be notified of when I have added a product to my basket* so that I can **see that my request to add the item(s) has been successful.**

    - Every item added to the basket, displays a handy notification, ensuring me that the basket has been successfully updated.
    
1.  I want to be able to *be shown an overview of my basket* so that I can **see the product and the important details I have selected to ensure they are correct.**

    - The notification overview displays the name, item size, should the item have a size and quantity.

1.  I want to be able to *see the total price of my basket* so that I can **make sure I don't spend more than I want to.**

    - The total price is located at the bottom of the notification pop-up as soon as an item has been added.

1.  I want to be able to *find out how much more I need to spend to receive free delivery* so that I can **see if it is cost-effective adding another product(s) to qualify for free delivery.**

    - After adding items to the basket, I am able to see the amount needed for free delivery change, providing me with an amount remaining.
    - When my basket reached the delivery threshold, the paragraph was removed as expected.

1.  I want to be able to *click a button which takes me to my basket and check out* so that I can **proceed with payment easily.**

    - The toast notification provides a handy link to the basket in order for me to check out, with the button standing out from the notification block.

#### Registration

1.  I want to be able to *register an account* so that I can **I have all the access I require from the site.**

    - The registration process is very easy with only a couple of fields to fill in, and even some of those are duplicates to confirm.

1.  I want to be able to *receive an email confirmation* so that I can **know my request to register has been received and all I need to do is verify my account.**

    - Almost immediately after signing up, an automated email was sent to my address asking me to confirm my user via the confirm button and then signing in.

1.  I want to be able to *login and out of my account* so that I can **ensure my account is safe should I share a computer.**

    - The login in and out links are found under the 'My Account' dropdown.
    - Both actions were shown to me by the notifications section.

1.  I want to be able to *reset my password* so that I can **log back in to my account if I have forgotten my password.**

    - Resetting my password was just as easy as registering.
    - Following the links, I was sent an email which provided me with a 'Change password' page. 

1.  I want to be able to *view previous orders* so that I can **see my purchase history and link to an item I have bought previously.**

    - Following the 'My profile' link, I was able to view my order history listed with all the key details.
    - With the order number linking to the order confirmation.

1.  I want to be able to *add a default delivery address* so that **when I go to check out, my delivery information is already populated, making the process easier.**

    - Staying on the 'My profile' page, I added my delivery address and after saving, when going to make a purchase the fields were pre-filled to make the process easy and quicker.

#### Sorting & Searching

1.  I want to be able to *sort the products by certain criteria* so that I can **view the products by a common look such as price lowest to highest etc.**

    - Through any of the navigation links, each page contains a dropdown in order to filter.
    - This includes price and rating, low to high and high to low are both options.

1.  I want to be able to *search by product category* so that I can **navigate through the products by category e.g. sticks, bags, clothes or accessories.**

    - Searching by category is made even easier with the navigation bar links, with a helpful title per category page, for example "Full range of sticks". 

1.  I want to be able to *search by keyword* so that I can **find the item I am specifically looking for to purchase.**

    - Any keyword typed in the search bar was feed back to me, whether there were results found or not.

1.  I want to be able to *retrieve all products from a keyword search* so that I can **be shown a reduced list of products using the keyword as a filter.**

    - As mentioned above, all results were displayed to me, and I was able to look through the products that contained my keyword.
    - The number count from the search word (in quotes) provides a nice summary.

#### Check Out

1.  I want to be able to *view all items in my basket* so that I can **check my basket and ensure I have all the items and quantities are correct.**

    - Viewing the basket, I can see all the product details I need along with product images.
    - The 'list' type display on mobile devices is very easy to scroll through and check.

1.  I want to be able to *easily amend any product in my basket* so that I can **add to and reduce the quantity per item.**

    - I am able to amend any product in my basket using the quantity buttons and then clicking update
    - This updated the sub total as expected as well as all of the total in the lower section.

1.  I want to be able to *pay for my order* so that I can **process my order and eventually receive my item(s).**

    - From the checkout page, I was able to pay for my items in my basket, using the fields from the form, including bank details.
    - I was also able to double-check my basket using the order summary section.

1.  I want to be able to *trust the sites' check out security* so that I can **I feel that personal details (especially banking information) are safe, and the site can be trusted.**

    - The use of a padlock icon along with 'Secure Checkout' made me feel comfortable proceeding to checkout.
    - Also when entering bank details, which were invalid, I was made aware of that from the site. 

1.  I want to be able to *view my order confirmation after payment* so that **I know my order has been processed and provides a final check should I want to do so.**

    - After my payment was successful, I was shown my order confirmation, providing me the assurance my order had been received
    - Similarly, I was able to check the Purchased products section to ensure everything was correct.

1.  I want to be able to *receive an email order confirmation after payment* so that I can **trust my order has been processed, and I have the written confirmation to prove it.**

    - Along with the site order confirmation, I received an email confirmation of my order too, which again made me trust the company more.

#### Company Information

1.  I want to be able to *find out more information about the company* so that I can **look into their background and develop an understanding of the business.**
    - With all the company information at the bottom of each page, it is very easy to navigate to each section
    - The about us page provides an easy-to-read overview of the company, separated into two sections.

1.  I want to be able to *review the FAQ's* so that I can, **should I have a question, see if it has already been answered.**
    - The FAQ's are displayed cleanly with the topics broken down
    - I agree with the choice of neutral colours being used for this page, as the blocks may have been overpowering in the site grey.

1.  I want to be able to *contact them directly* so that I can **ensure my query/question can be answered.**
    - The contact form provides a direct way to contact the company, with only a small amount of input.
    - Through testing, I am aware that I am unable to send a message without filling in the fields first.
    - The map showing the location is great for someone that is local to the area and able to pop in.

1.  I want to be able to *read through the privacy policy* so that I **know my personal information is secure.**
    - The privacy policy is displayed in a similar way to the about page with small sections, which I felt made it easier to read through.

1.  I want to be able to *subscribe to the site's mailing list* so that I can **receive all the latest deals, offers and news.**
    - After submitting my email address, I can immediately see my request has been successful with the “Thank You” message displayed.

As an administrator/owner ...

#### Admin Rights

1.  I want to be able to *add products to the site* so that I can **add new products to show potential customers.**
    - Using admin access, adding a new product is very easy using the product management form.

1.  I want to be able to *edit/update products* so that I can **amend product details such as name, description, price etc.**
    - From any product and/or product detail page, I am shown a link in order to edit the product.
    - After clicking the link I am presented the product management form with all the details filled in ready to amend and save.

1.  I want to be able to *delete products* so that I can **remove any product that is no longer available.**
    - Similarly to the edit link, the delete link is shown on the same pages.
    - As soon as the delete button is clicked, the product is removed.

### Future Features

-   Discount codes
    - I would have liked to be able to set discount codes, an input field that when entered, if it matched a secret discount, reduced the basket total. 
-   Customer reviews
    - Another feature I would have liked to implement would have been customers posting their own reviews on products. These reviews would generate the rating shown for each item.

## References

### Code

The large majority of functionality was replicated from the Boutique Ado walkthrough project.

Footer position - https://dev.to/domysee/keeping-the-footer-at-the-bottom-with-css-flexbox-5h5f
- This has been used to ensure the footer is stuck to the bottom of the screen on any device.

Responsive iframes - https://www.benmarshall.me/responsive-iframes/ 
- This is enabled me to adjust the map on the contact page to adjust based on screen size.

Cut down description - https://stackoverflow.com/questions/30110455/paragraph-overflow-with-ellipsis
- Used for the products page, when the description was too long, the paragraph is cut short and the ellipses are used.

Return to previous url - https://stackoverflow.com/questions/27325505/how-to-get-the-previous-url-from-a-post-in-django#:~:text=You%20can%20do%20that%20by,get()%20notation%20instead.
- This is been used inside the product detail template and returns the user to the search results

Contact form - Codemy - https://www.youtube.com/watch?v=w4ilq6Zk-08
- This video tutorial was used to ensure the contact form was fully functioning. 

Error 404 Page - https://www.youtube.com/watch?v=3SKjPppM_DU
- This video tutorial was used to ensure the custom 404 page was displayed when an invalid url was input.

## Conclusion

### Content

-   The majority of content was written by the developer. 
-   The product information was taken from [Otter Hockey](https://www.otterhockey.co.uk) but again I was given permission to use this by [Kyle](#permission).

### Mentions

-   Code Institute tutor assistance
    - Special mention to John, without him (19/08/22), the ability to adjust the items in the basket wouldn't have worked.

-   My Mentor Narender
    -   Numerous video calls
    -   A lot of questions via Slack.