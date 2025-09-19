# 🎬 Django 3-Tier Movie App

A simple Django project to manage movies and their ratings. The frontend mimics a **Prime-style layout**, and data is stored in a single SQLite database. The app can be run manually with Django, via Docker, or with Docker Compose. You can also simulate traffic with `movie_traffic.py`.  

---
🏗 3-Tier Architecture

Frontend: HTML + CSS templates served by Django.

Backend: Django views and forms handle requests and database operations.

Database: SQLite (persisted with Docker volume).

---

## 1 Project Requirements

- Python 3.12+  
- Django >= 4.2  
- Optional for traffic simulation:
  - `requests`
  - `beautifulsoup4`

---

## 2 PCreate a Python virtual environment:
```
python -m venv venv
source venv/bin/activate          # Linux/Mac
venv\Scripts\activate             # Windows
```
## 3 Install requirements:
```
pip install -r requirements.txt
```
## 4 Run migrations:
```
python manage.py migrate
```
## 5 Run the development server:
```
python manage.py runserver 0.0.0.0:8000
```
## 6 Access the app:
Open in browser: http://127.0.0.1:8000/ (or your EC2 public IP if running on cloud).

## 7 Optional: Access Django admin:
```
python manage.py createsuperuser
```
Then visit http://127.0.0.1:8000/admin/.

---

Running with Docker
```
docker build -t movieapp .
docker run -dit -p 8000:8000 --name movie_container movieapp
```
Access the app: http://<EC2-PUBLIC-IP>:8000.

---

Running with Docker Compose
```
docker-compose up -d
```
Stop app:
```
docker-compose down
```
View logs:
```
docker-compose logs -f
```
Note: SQLite DB is persisted in Docker volume movie_db. Deleting the container will not delete the DB unless the volume is removed:
```
docker volume rm movie_project_movie_db
```
----
Simulating Traffic (movie_traffic.py)
Use the Python script to automatically add and delete movies, and refresh the homepage multiple times to simulate traffic.
```
pip install requests beautifulsoup4
python movie_traffic.py
```
The script will ask:
```
How many movies to create? 5
How many movies to delete? 2
```
---
⚡ Notes

CSS and static files work automatically when using volumes: .:/app in Docker Compose.

Always make sure your EC2 security group allows port 8000 to access the app externally.

For production, consider switching to PostgreSQL instead of SQLite.
