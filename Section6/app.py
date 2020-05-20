from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import ItemList,Item
from flask_sqlalchemy import SQLAlchemy
from models.item import ItemModel 

# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=db, ItemModel=ItemModel)

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS ']=False # To allow flask propagating exception even if debug is set to false on app
app.config['SQLALCHEMY_DATABASE_URI ']='sqlite:///data.db' #doesn't have to be SQLite; can be oracle postgresql, mongoDB etc...
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'rhys'
api = Api(app)

jwt = JWT(app, authenticate, identity)
 

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__': 
    from db import db 
    db.init_app(app)
    app.run(debug=True)  # important to mention debug=True
