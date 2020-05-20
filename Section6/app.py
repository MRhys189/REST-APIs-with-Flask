from flask import Flask
from flask_restful import Api 
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import ItemList, Item
from resources.store import Store, StoreList

app = Flask(__name__)
# doesn't have to be SQLite; can be oracle postgresql, mongoDB etc...
app.config['SQLALCHEMY_DATABASE_URI '] = 'sqlite:///data.db'
# To allow flask propagating exception even if debug is set to false on app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False
# To allow flask propagating exception even if debug is set to false on app
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'rhys'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all


jwt = JWT(app, authenticate, identity)


api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores ')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)  # important to mention debug=True
