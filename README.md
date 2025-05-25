
# 🛒 TechKart - E-commerce Web App (In Progress)

TechKart is a custom-built full-stack e-commerce web application using *Django* for the backend and HTML/CSS/JavaScript for the frontend. It is designed to sell electronics and features a user-friendly shopping experience.

---

## 🚧 Project Status

This project is currently in development. The following features have been completed:

- Product listing
- Product detail page
- Add to Cart functionality
- Cart page with quantity and total price
- Checkout view and template created
- URL routing and basic error handling setup

---

## ⚙ Tech Stack

- *Backend*: Django (Python)
- *Frontend*: HTML, CSS, JavaScript
- *Database*: SQLite (default for development)
- *Templating*: Django Template Language

---

## 📁 Project Structure

TechKart/
├── shop/ # Django app handling store logic
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── ...
├── templates/ # Global templates folder
│ ├── cart.html
│ └── checkout.html
├── techkart/ # Django project settings
│ └── settings.py
├── db.sqlite3
└── manage.py


---
Here’s a clean and clear README.md for your e-commerce project, up to the current stage (Add to Cart, Cart Page, Checkout View & Templates, Basic Routing):

markdown
Copy
Edit
# 🛒 TechKart - E-commerce Web App (In Progress)

TechKart is a custom-built full-stack e-commerce web application using **Django** for the backend and HTML/CSS/JavaScript for the frontend. It is designed to sell electronics and features a user-friendly shopping experience.

---

## 🚧 Project Status

This project is currently in development. The following features have been completed:

- Product listing
- Product detail page
- Add to Cart functionality
- Cart page with quantity and total price
- Checkout view and template created
- URL routing and basic error handling setup

---

## ⚙️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default for development)
- **Templating**: Django Template Language

---

## 📁 Project Structure

TechKart/
├── shop/ # Django app handling store logic
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── ...
├── templates/ # Global templates folder
│ ├── cart.html
│ └── checkout.html
├── techkart/ # Django project settings
│ └── settings.py
├── db.sqlite3
└── manage.py

yaml
Copy
Edit

---

## 🛠 Setup Instructions :

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/techkart.git
   cd techkart
Create a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install django
Run migrations

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Run the server

bash
Copy
Edit
python manage.py runserver
Visit the app
Open your browser and go to http://127.0.0.1:8000/

✅ Features Implemented So Far are
Home page displaying products

Add to cart button on product pages

View cart with list of added items and total cost

Checkout page view (placeholder)

📌 Upcoming Features include
User authentication (login, signup)

Checkout form and payment integration

Search and filter products

Order summary and confirmation

Admin dashboard

🧑‍💻 Author
Developed by [Varshitha Reddy,Rozal Binish, Sachi Tiwari ]

📄 License
This project is licensed under the MIT License.


