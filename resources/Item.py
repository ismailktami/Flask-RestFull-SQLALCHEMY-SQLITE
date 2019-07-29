from flask_restful import Resource,reqparse
from flask_jwt import JWT,jwt_required
import  sqlite3
from modules.Item import ItemModel
from modules.Store import StoreModel
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price', type=float,
        required=True, help="this field cannot be left blank")

    parser.add_argument(
        'store_id', type=int,
        required=True, help="this field cannot be left blank")

    def get(self):
        return {"You should have a token": 404},403

    @jwt_required()
    def get(self,name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "select * from items where name=?"
        row = cursor.execute(query, (name,)).fetchone()
        if row:
            return {"item":{"name":row[1],"price":row[2]}},201

        else:
            item = None
        connection.close()
        return item


    @jwt_required()
    def post(self,name):
        if ItemModel.findByName(name):
            return {'message':'this name already exists'},404
        else:
            data = self.parser.parse_args()
            item=ItemModel(name,data['price'],data['store_id'])
            item.save_to_db()
            return item.json(),200




    @jwt_required()
    def delete(self,name):
        item=ItemModel.findByName(name)
        if item:
            item.delete_from_db()

        return {"message":"item deleted"}

    @jwt_required()
    def put(self,name):
        data=self.parser.parse_args()
        item=ItemModel.findByName(name)
        if item is None:
            #  item=ItemModel(name,data['price'],data['store_id'])
            item=ItemModel(name,**data)

            item.save_to_db()
            return item.json(), 201

        else :
            item.price=data['price']
            item.save_to_db()
            return item.json()


class Item_List(Resource):
    def get(self):
        #   return {'items':list(map(lambda x:x.json(),ItemModel.query.all()))}

        return {"items":[x.json() for x in ItemModel.query.all()]}

class ItemListOfStore(Resource):
    def get(self,name):
        return ItemModel.getItemsByStoreName(name)