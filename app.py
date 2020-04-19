from flask import Flask

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

# POST/store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET/store/<string:name>
@app.route('/store/name/<string:name>', methods=['GET'])
def get_store(name):
    pass

# GET/store/
@app.route('/store/name', methods=['GET'])
def get_stores():
    pass

# POST/store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    pass


# GET/store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['GET'])
def get():
    pass


app.run()
