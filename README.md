
# Flask API Project

This is a Flask-based RESTful API for managing product data. The API supports basic CRUD (Create, Read, Update, Delete) operations, and data is stored in an in-memory structure.

## Features
- Add a new product (POST)
- Retrieve a product by ID (GET)
- Update a product by ID (PUT)
- Delete a product by ID (DELETE)
- Retrieve all products (GET)

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/your-username/flask-api-project.git
cd flask-api-project
```

### 2. Create a Virtual Environment
Create a virtual environment to keep dependencies isolated:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install the required dependencies (Flask) using pip:
```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application
Run the Flask application locally:
```bash
python app.py
```

The API will start running on `http://127.0.0.1:5000/`.

## Usage Instructions

### Add a Product (POST request)
To add a new product, send a POST request to the `/products` endpoint.
```bash
curl -X POST http://127.0.0.1:5000/products -H "Content-Type: application/json" -d '{"id": 1, "name": "Product A", "price": 100}'
```

### Retrieve a Product (GET request)
To retrieve a product by ID, send a GET request to `/products/<product_id>`.
```bash
curl -X GET http://127.0.0.1:5000/products/1
```

### Update a Product (PUT request)
To update a product, send a PUT request to `/products/<product_id>`.
```bash
curl -X PUT http://127.0.0.1:5000/products/1 -H "Content-Type: application/json" -d '{"price": 150}'
```

### Delete a Product (DELETE request)
To delete a product, send a DELETE request to `/products/<product_id>`.
```bash
curl -X DELETE http://127.0.0.1:5000/products/1
```

### Get All Products (GET request)
To retrieve all products, send a GET request to `/products`.
```bash
curl -X GET http://127.0.0.1:5000/products
```

## Error Handling
The API includes proper error handling for the following cases:
- 404 Not Found: When a product with the given ID does not exist.
- 400 Bad Request: When the request payload is missing required data.
 
