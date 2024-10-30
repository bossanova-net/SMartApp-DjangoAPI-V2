# Django REST API Project

This project is a Django REST API for managing project data using Django REST Framework 3.15.2.

## Project Structure

```
project/
├── api/
│   ├── management/
│   │   └── commands/
│   │       └── populate_db.py
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
5. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Populate the database with fake data:
   ```
   python manage.py populate_db
   ```
7. Run the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

- GET /api/projects/ - List all projects
- POST /api/projects/ - Create a new project
- GET /api/projects/{id}/ - Retrieve a specific project
- PUT /api/projects/{id}/ - Update a specific project
- DELETE /api/projects/{id}/ - Delete a specific project

You can test these endpoints using tools like curl, Postman, or by accessing them in your web browser (for GET requests).