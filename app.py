from flask import Flask,request,jsonify
from flask_restful import Resource, Api,reqparse
from flask_jwt import JWT,jwt_required
from securitywithdb import  authenticate,identity
from resources.Item import Item,Item_List,ItemListOfStore
from resources.Store import  StoreList,Store
from resources.User import UserReister
from db import db
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key="jose"
@app.before_first_request
def create_tables():
    db.create_all()
api=Api(app)
jwt=JWT(app, authenticate, identity) #/auth
api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(Item_List,'/items')
api.add_resource(ItemListOfStore,'/<string:name>/items')
api.add_resource(StoreList,'/stores')

api.add_resource(UserReister,'/user/register')

if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)
