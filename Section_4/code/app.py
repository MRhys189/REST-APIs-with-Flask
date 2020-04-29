from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

items = []

class Items(Resource):
    def get(self,name):
        for item in items:
            if name == item['name']:
                return item
        return {'item':None}
    
    def post(self, name):
        data = request.get_json(force=True)
        item = {'name':name, 'price': data['price']}
        items.append(item)
        return item 

class ItemList(Resource):
    def get(self):
        return{'items': items}
    


api.add_resource(Items, '/item/<string:name>') 
api.add_resource(ItemList, '/items') 

app.run(port=5000)