from flask_restful import Resource
from Models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'store': store.json()}, 200

        return {'message': "store not found"}, 404

    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'message': "store already exists"}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        
        except:
            return {'message': 'A error occured during creating store'}, 500
        
        return {'store': store.json()}, 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete()
        
        return {'message': 'Store deleted'}

class StoreList(Resource):
    def get(self, name):
        pass
