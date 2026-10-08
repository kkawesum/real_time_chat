# real_time_chat

This project is a production-grade WhatsApp clone built with Django, Django REST Framework, Django Channels, React, PostgreSQL, Redis, Docker, and AWS. The goal is to create a scalable, real-time messaging application that demonstrates modern backend and frontend development practices.

Technology Stack

Backend

Python 3.12
Django 5
Django REST Framework
Django Channels (WebSockets)
PostgreSQL
Redis
Celery
JWT Authentication
Pillow (image handling)

Frontend

React
Material UI
Redux Toolkit
Axios
React Router

Infrastructure

Docker & Docker Compose
Nginx
Gunicorn
Daphne (ASGI)
GitHub Actions
AWS EC2
AWS S3 (media storage)
High-Level Architecture
                React Frontend
                     │
        REST API + WebSocket
                     │
             Django Backend
        ┌────────┼────────┐
        │        │        │
 PostgreSQL   Redis   Celery
        │
     Media Storage (S3)
