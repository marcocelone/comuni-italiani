from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'enrico'
api = Api(app)


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, '/comuni/<string:name>')
api.add_resource(StoreList, '/comuni')
# api.add_resource(Store, '/store/<string:name>')
# api.add_resource(StoreList, '/stores')
#api.add_resource(Item, '/item/<string:name>')
#api.add_resource(ItemList, '/items')
#api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
