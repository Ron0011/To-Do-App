# 📝 To-Do List App (FastAPI + SQLite)

## 📌 Project Overview  
A simple **To-Do List web application** built with **FastAPI (Python), SQLite, HTML, and CSS**.  
This project demonstrates **CRUD operations** (Create, Read, Update, Delete) using SQLAlchemy ORM and provides a clean front-end with Jinja2 templates.  

The app allows users to:  
- ➕ Add new tasks  
- ✔ Mark tasks as completed (toggle status)  
- 🔄 Undo completed tasks  
- 🗑 Delete tasks  

---

## 🚀 Tech Stack  
- **Backend:** FastAPI (Python)  
- **Database:** SQLite (SQLAlchemy ORM)  
- **Frontend:** HTML, CSS (Jinja2 templates)  
- **Server:** Uvicorn  

---

## 📂 Project Structure  
todo-app/
│── main.py # FastAPI entry point
│── models.py # SQLAlchemy models
│── schemas.py # Pydantic schemas
│── crud.py # Database CRUD functions
│── database.py # DB connection/session
│── templates/
│ └── index.html # Frontend HTML (Jinja2 template)
│── static/
│ └── index.css # Styling
│── README.md # Project documentation


---

## ⚡ Features  
- 📝 Task management (Add / Delete / Update)  
- ✔ Mark tasks as completed / undo  
- 💾 Data stored in SQLite database  
- 🎨 Simple and responsive UI with custom CSS  

---

## ▶️ How to Run Locally  

1. **Clone the repository**  
git clone https://github.com/your-username/todo-fastapi.git
cd todo-fastapi
Create a virtual environment

python -m venv venv
Activate the virtual environment

Windows:

venv\Scripts\activate

Install dependencies
fastapi==0.111.0
uvicorn==0.30.1
SQLAlchemy==2.0.31
pydantic==2.8.2
jinja2==3.1.4
pip install -r requirements.txt

Run the server
uvicorn main:app --reload

Open in browser
👉 http://127.0.0.1:8000

uvicorn main:app --reload
Open in browser
👉 http://127.0.0.1:8000
