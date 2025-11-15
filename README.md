1️⃣ Project Title & Summary

Project Title: Django E-Commerce Website with Stripe Payment & Admin Dashboard
Short Summary:
This is a fully functional e-commerce web application built with Django. It includes product management, shopping cart, checkout system, Stripe payment integration, order tracking, coupon system, and an advanced admin dashboard.

2️⃣ Features Overview
🛒 User Features

Browse products by category

Search products

View product details

Add/remove products from cart

Update cart quantity

Checkout

Save shipping/billing addresses

Stripe payment system

View past orders

Order confirmation page

User profile page

🔑 Admin Features

(Admin login required: @staff_member_required)

Admin Dashboard (overview + statistics)

Manage Products (CRUD)

Manage Orders (update status: delivered, received, refund)

Manage Users (edit: activate/deactivate account, set staff role)

Manage Coupons (CRUD)

Manage Payments (view history)

Manage Refunds (approve/deny)

3️⃣ System Architecture

Explain the layers:

Backend

Django Class-Based Views (CBV)

Stripe API integration

Django ORM Models:

Item (Product)

OrderItem

Order

Address

Payment

Coupon

Refund

UserProfile

Frontend

HTML / CSS / Bootstrap

Django Template System

4️⃣ Key Functionalities (Explain each)
✔ Add to Cart

Checks if active order exists

Adds or increases product quantity

✔ Checkout

User can:

Use default address

Enter new address

Save address as default

Billing and shipping logic

Payment method selection

✔ Stripe Payment

Save card

One-click payment

Process charges through Stripe API

Handle exceptions (CardError, RateLimitError, etc.)

✔ Admin Dashboard Statistics

Total orders

Total revenue

Pending orders

New users

Recent activity

5️⃣ Pages

Add these slides:

Home page

Product detail page

Cart page

Checkout page

Payment page

Order confirmation

Admin dashboard

Product CRUD

Order management

User management

6️⃣ Technology Stack
Backend

Python 3

Django

Django ORM

Payment

Stripe API

Database

MySQL / SQLite

Frontend

HTML

CSS

Bootstrap

Django Templates

8️⃣ Conclusion

Explain what you learned:

How to structure a Django project

Working with Class-Based Views

Integrating Payment Gateway

Building admin dashboards

Handling real-world business logic


Add a README.md
---

# Django E-commerce

This is a very simple e-commerce website built with Django.

---

## Project Summary

The website displays products. Users can add and remove products to/from their cart while also specifying the quantity of each item. They can then enter their address and choose Stripe to handle the payment processing.


---

## Running this project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```

**Note** if you want payments to work you will need to enter your own Stripe API keys into the `.env` file in the settings files.

---


## Support

If you'd like to support this project and all the other open source work on this organization, you can use the following options

### Option 1: GitHub Sponsors

https://github.com/sorurng-kosorl/django-final-year4


---



Card Number: 4242 4242 4242 4242
Expiry: 12/34
CVC: 123
ZIP: 10001 (any)

# django-final-year4
