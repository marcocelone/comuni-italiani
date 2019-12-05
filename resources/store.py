from flask_restful import Resource
from models.store import StoreModel
from flask_jwt import jwt_required


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Comune non trovato not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "Comune con nome '{}' gia' esistente.".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "Errore di creazione comune."}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Comune elimminato'}


class StoreList(Resource):
    def get(self):
        return {'comuni': list(map(lambda x: x.json(), StoreModel.query.all()))}