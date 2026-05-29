<<<<<<< HEAD
# FoodExpress

FoodExpress is a food delivery API built with FastAPI, SQLAlchemy, and PostgreSQL. It models the core flow of a delivery platform: users, restaurants, dishes, orders, payments, and deliveries.

The project also includes a minimal browser-based test panel so the backend can be exercised quickly without needing Postman or a separate frontend setup.

## Features

- User creation, login, and profile updates
- Restaurant creation and updates
- Dish creation for restaurants
- Order creation with restaurant, dish, quantity, and total price
- Payment record creation with provider, method, amount, status, and currency
- Delivery creation and lookup by ID
- Automatic table creation on app startup
- Minimal HTML/CSS/JavaScript frontend mounted directly in FastAPI
- Interactive API documentation through FastAPI Swagger UI

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn
- HTML, CSS, and vanilla JavaScript

## Project Structure

```text
FoodExpress/
+-- app/
|   +-- delivery/
|   +-- frontend/
|   |   +-- index.html
|   +-- orders/
|   +-- payments/
|   +-- restaurants/
|   +-- users/
|   +-- database.py
|   +-- main.py
|   +-- .env.example
+-- README.md
```

Each domain folder follows a simple layered structure:

- `entity.py`: SQLAlchemy database models
- `schemas.py`: Pydantic request and response models
- `repository.py`: database operations
- `service.py`: business logic
- `routes.py`: FastAPI endpoints

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/FoodExpress.git
cd FoodExpress
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic[email]
```

### 4. Configure the database

Create a PostgreSQL database, then copy the example environment file:

```bash
copy app\.env.example app\.env
```

On macOS/Linux:

```bash
cp app/.env.example app/.env
```

Update `app/.env` with your PostgreSQL connection string:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/postgres
```

### 5. Run the application

```bash
cd app
python -m uvicorn main:app --reload
```

The app will be available at:

```text
http://127.0.0.1:8000
```

## Frontend Test Panel

Open the root URL in your browser:

```text
http://127.0.0.1:8000/
```

The test panel lets you create records through the main food delivery flow:

1. Create a user
2. Create a restaurant
3. Add a dish
4. Create an order
5. Create a payment
6. Create a delivery

Responses from the API are shown directly on the page.

## API Documentation

FastAPI provides interactive API docs automatically:

```text
http://127.0.0.1:8000/docs
```

Alternative ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

## Main Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `POST` | `/users/` | Create a user |
| `POST` | `/users/login` | Log in a user |
| `PUT` | `/users/{user_id}` | Update a user |
| `POST` | `/restaurants/` | Create a restaurant |
| `PUT` | `/restaurants/{restaurant_id}` | Update a restaurant |
| `POST` | `/restaurants/dishes` | Create a dish |
| `POST` | `/orders/` | Create an order |
| `POST` | `/payments/` | Create a payment |
| `POST` | `/deliveries/` | Create a delivery |
| `GET` | `/deliveries/{delivery_id}` | Get a delivery by ID |

## Example Request

Create a restaurant:

```bash
curl -X POST "http://127.0.0.1:8000/restaurants/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Green Bowl",
    "cuisine": "Healthy",
    "phone_number": "+55 11 3333-4444",
    "address": "Av. Paulista, 1000"
  }'
```

## Portfolio Notes

This project demonstrates:

- REST API development with FastAPI
- Relational data modeling with SQLAlchemy
- PostgreSQL integration
- Modular backend architecture
- Request and response validation with Pydantic
- A lightweight frontend for manual API testing

## Future Improvements

- Add authentication tokens
- Add list endpoints for restaurants, dishes, and orders
- Add automated tests
- Add database migrations with Alembic
- Add a production-ready frontend
- Add Docker configuration
=======
# foodexpress
Backend Projects
>>>>>>> cf0d0bf01031b75a87f7c127b125c3b929bfb374
