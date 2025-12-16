---

# Django Pagination & Filtering Project

A Django-based web application demonstrating **server-side pagination and filtering** of data using Django’s built-in tools.

---
---

## 🛠️ Tech Stack

* **Backend:** Django
* **Frontend:** HTML, CSS (Daisy UI )
* **Database:** SQLite (default, can be changed)
* **Language:** Python 3

---

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Leon-glitch-png/paginationAndFilter.git
cd paginationAndFilter
```

### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```


---
# 3. Configuration (`.env`)

Create a `.env` file in the project root . Example:

```
SECRET_KEY="secret_key"
DEBUG='True'

```

The project should load these values using `python-dotenv` in `settings.py`.

### 3️⃣ Install dependencies

```bash

# Install requirements
pip install -r requirements.txt


```

---

### 4️⃣ Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate

# create admin
python manage.py createsuperuser

```

---

### 5️⃣ Run development server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---
