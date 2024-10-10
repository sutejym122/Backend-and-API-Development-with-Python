from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory store to hold products
products = {}

# Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Missing product data'}), 400
    
    product_id = data['id']
    if product_id in products:
        return jsonify({'error': 'Product with this ID already exists'}), 409

    products[product_id] = {'name': data['name'], 'price': data['price']}
    return jsonify({'message': 'Product added successfully'}), 201

# Get a specific product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({'error': 'Product not found'}), 404

# Update an existing product by ID
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    if product_id not in products:
        return jsonify({'error': 'Product not found'}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided for update'}), 400
    
    products[product_id].update({
        'name': data.get('name', products[product_id]['name']),
        'price': data.get('price', products[product_id]['price'])
    })
    return jsonify({'message': 'Product updated successfully'}), 200

# Delete a product by ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id in products:
        del products[product_id]
        return jsonify({'message': 'Product deleted successfully'}), 200
    else:
        return jsonify({'error': 'Product not found'}), 404

# Get all products (useful for testing)
@app.route('/products', methods=['GET'])
def get_all_products():
    return jsonify(products), 200

# Handle concurrent requests (Flask is thread-safe by default)
if __name__ == '__main__':
    app.run(debug=True, threaded=True)
