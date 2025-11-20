# Django Polls App — README

This project is built by following the official **Django Documentation Tutorial**. It demonstrates Django fundamentals such as models, views, templates, forms, admin configuration, testing, and deployment.

---

## 📌 Features

* Create and manage poll questions.
* Allow users to vote on choices.
* Display poll results.
* Fully integrated Django Admin interface.
* Includes automated tests.

---

## 📂 Project Structure

```
mysite/
├─ manage.py
├─ mysite/        # Project settings and configuration
└─ polls/         # Main app created in the tutorial
   ├─ migrations/
   ├─ static/polls/
   ├─ templates/polls/
   ├─ admin.py
   ├─ apps.py
   ├─ models.py
   ├─ tests.py
   └─ views.py
```

---

## 🚀 Getting Started

### 1️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 2️⃣ Install Dependencies

```bash
pip install django
```

### 3️⃣ Run Migrations

```bash
python manage.py migrate
```

### 4️⃣ Create a Superuser

```bash
python manage.py createsuperuser
```

### 5️⃣ Start the Server

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/polls/`

---

## 🛠 How It Works

### **Models**

Defines `Question` and `Choice` models.

```python
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
```

### **Views**

Includes views for listing, detail page, results page, and voting logic.

### **Templates**

Uses Django's template language to render HTML pages.

### **Admin Panel**

Register models for easy CRUD operations.

### **Routing**

`urls.py` maps URLs to views.

---

## 🧪 Running Tests

```bash
python manage.py test
```

Example tested behavior:

* Index page shows "No polls are available." when empty
* Detail page returns 404 for future questions
* Voting redirects correctly

---

## 📦 Static Files

Static files like CSS are stored in:

```
polls/static/polls/
```

Django collects them using:

```bash
python manage.py collectstatic
```

---

## 📤 Deployment Notes

* Use `DEBUG=False` in production
* Set `ALLOWED_HOSTS`
* Use a real DB (PostgreSQL recommended)
* Configure static files for production

---

## 📚 References

* Django Documentation: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
* Official Tutorial: Polls App

---

## ✔️ License

This project follows the Django tutorial and is free to use and modify.
