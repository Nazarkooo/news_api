
---

# 📰 News API — REST Backend with Django & DRF  

## 📌 About the Project  
**News API** is a RESTful backend for managing news articles and their categories, built with **Django Rest Framework (DRF)**.  

### 🎯 Features  
✅ **CRUD** (Create, Read, Update, Delete) for **News Items**  
✅ **CRUD** for **News Types**  
✅ Filter news by type  
✅ Retrieve a list of all news types  

---

## 🚀 Getting Started  

### 1️⃣ Clone the Repository & Install Dependencies  
```bash
git clone https://github.com/[my_repo]/news_api
cd news_api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2️⃣ Set Up Environment Variables  
Create a `.env` file in the `config` folder and add:  
```bash
SECRET_KEY=<your_secret_key>
DEBUG=<True_or_False>
```

### 3️⃣ Apply Migrations, Create a Superuser & Start the Server  
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 4️⃣ Run Tests  
```bash
python -m pytest api/tests.py
```

### 🐳 Run with Docker  
```bash
docker-compose up --build
```

---

## 📌 API Endpoints  

### 🔹 News Items  
| Method | Endpoint | Description |
|--------|---------|-------------|
| `GET` | `/api/news-items/` | Retrieve all news items |
| `GET` | `/api/news-items/?news_type=<name>` | Filter news by type |
| `GET` | `/api/news-items/<id>/` | Retrieve a specific news item by ID |
| `POST` | `/api/news-items/` | Create a new news item |
| `PUT` | `/api/news-items/<id>/` | Update an existing news item |
| `DELETE` | `/api/news-items/<id>/` | Delete a news item |

#### 🔹 JSON Example for Creating a News Item  
```json
{
    "title": "Example News Title",
    "about": "Short news summary",
    "description": "Full news article text",
    "news_type_name": "Sports",
    "news_type_color": "RED"
}
```

#### 🔹 Response on Successful Creation  
```json
{
    "status": "news item has been created"
}
```

#### 🔹 Response on Deletion  
```json
{
    "status": "news item has been deleted"
}
```

---

### 🔹 News Types  
| Method | Endpoint | Description |
|--------|---------|-------------|
| `GET` | `/api/news-types/` | Retrieve all news types |
| `GET` | `/api/news-types/<id>/` | Retrieve a specific news type by ID |
| `POST` | `/api/news-types/` | Create a new news type |
| `PUT` | `/api/news-types/<id>/` | Update a news type |
| `DELETE` | `/api/news-types/<id>/` | Delete a news type |

#### 🔹 JSON Example for Creating a News Type  
```json
{
    "name": "Politics",
    "color": "BLACK"
}
```

#### 🔹 Response on Successful Creation  
```json
{
    "status": "news type has been created"
}
```

#### 🔹 Response on Deletion  
```json
{
    "status": "news type has been deleted"
}
```
