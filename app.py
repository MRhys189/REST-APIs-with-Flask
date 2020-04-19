from flask import Flask, jsonify, request, render_template

app = Flask(__name__)  # to tell that Flask is running
# creates app called Flask with a unique name

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]


    }


]
@app.route('/')
def home():
    return render_template('index.html')

# POST/store data: {name:} create a store with a given name
@app.route('/store', methods=['POST'])
def create_store(request_data, new_store: dict):
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET/store/<string:name>
# get a store for a given name and return some data
@app.route('/store/name/<string:name>')
def get_store(name_of_store):
    for store in stores:  # Iterate over stores
        if name_of_store == store['name']:
            return jsonify(store)  # If the store name matches, return it
    # If none match, return an error message
    return jsonify({'message': 'Store not found'})


# GET/store/ return a list of stores
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST/store/<string:name>/item {name:, price:} create an item in the store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify({new_item})
    return jsonify({'message': 'store not found'})


# GET/store/<string:name>/item {name:, price:} get all items in a specific store
@app.route('/store/<string:name>/item')
def get_items_in_store(store_item):
    for store in stores:
        if store['name'] == store_item:
            return jsonify({'Items': store['item']})
    return jsonify({'message': 'store not found'})


# app.run()
