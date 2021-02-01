from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My wonderful store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }
]


# Create a new store
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# Get store by name
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# Get list of all stores
@app.route('/store', methods=['GET'])
def get_store_list():
    return jsonify({'stores': stores})


# Create item in store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    new_item = {
        'name': request_data['name'],
        'price': request_data['price']
    }
    for store in stores:
        if store['name'] == name:
            store['items'].append(new_item)
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


# Get items in store
@app.route('/store/<string:name>/item')
def get_items_int_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
