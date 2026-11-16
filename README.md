# Product API

## About the Project

This is a simple REST API built with Python, Django, and Django REST Framework. It uses serializers to convert product model data into JSON and to validate incoming data. It also includes a user registration API.

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite

## Features

- Register a user
- View all products
- Add a product
- View one product by ID
- Update a product
- Delete a product

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/register/` | Register a user |
| GET | `/api/products/` | Get all products |
| POST | `/api/products/` | Add a product |
| GET | `/api/products/<id>/` | Get one product |
| PUT | `/api/products/<id>/` | Update a product |
| DELETE | `/api/products/<id>/` | Delete a product |

## Product Fields

- `name`
- `price`
- `category`

## Installation and Setup



1. Open the project folder 

2. Install the required packages:

   pip install django djangorestframework
 
4. Apply database migrations:

   python manage.py makemigrations
   python manage.py migrate

5. Start the development server:

   python manage.py runserver

6. Use the API at `http://127.0.0.1:8000/`. The endpoints are listed above.

## Testing

The API endpoints were tested using Postman by sending requests and checking the JSON responses.

## What I Learned

- Creating Django REST Framework API views
- Using ModelSerializer and serializers
- Validating incoming API data
- Performing CRUD operations through API endpoints
- Testing API requests with Postman

## Author

Janish
