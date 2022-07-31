from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT

from security import authenticate, identify
from Resources.user import UserRegister
from Resources.item import Item, ItemList
from Resources.store import Store, StoreList
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'loc'
api = Api(app)

jwt = JWT(app, authenticate, identify)

@app.before_first_request
def create_table():
    db.create_all()



api.add_resource(Item, '/item/<string:name>') 
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList, '/stores')

# api.add_resource(Student, '/<string:name1>') 

# stores = [
#     {
#         'name':'My Wonderful Store',
#         'items': [
#             {
#                 'name': 'My item',
#                 'price':15.98,
#             }
#         ]
#     }
# ]
# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/', methods=['POST'])
# def create_store():
#     request_data = request.get_json()
#     new_store = {
#         'name': request_data['name'],
#         'items':[],
#     }
#     stores.append(new_store)
#     return jsonify(new_store)

# @app.route('/store/<string:name>')   #http://127.0.0.1:5000/store/some_name
# # GET store/<string:name>
# def get_store(name):
#     for store in stores:
#         if store['name'] == name:
#             return jsonify(store)
#     return jsonify({'message':'store not found'})

# @app.route('/store')   #http://127.0.0.1:5000/store/some_name
# # GET store/<string:name>
# def get_stores():
#     return jsonify({'store': stores})


# @app.route('/store/<string:name>/item', methods = ['POST'])   #http://127.0.0.1:5000/store/some_name
# # GET store/<string:name>
# def create_item_in_store(name):
#     for store in stores:
#         if store['name'] == name:
#             request_data = request.get_json()
#             new_item = {
#                 'name': request_data['name'],
#                 'price': request_data['price'],
#             }
#             store['items'].append(new_item)
#             return jsonify(new_item)
#     return jsonify({'message': 'store not found'})

# @app.route('/store/<string:name>/item', methods = ['GET'])   #http://127.0.0.1:5000/store/some_name
# # GET store/<string:name>
# def get_item_in_store(name):
#     for store in stores:
#         if store['name'] == name:
#             return jsonify({'items':store.items})
#     return jsonify({'message':'store not found'})
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5001)