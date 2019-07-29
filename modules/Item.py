from db import db
from resources.Store import StoreModel
class ItemModel(db.Model):
    __tablename__='items'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String((80)))
    price=db.Column(db.Float(precision=2))

    store_id=db.Column(db.Integer,db.ForeignKey('stores.id'))
    store=db.relationship('StoreModel')


    def __init__(self,_id,name, price,store_id):
        self.id=_id
        self.name = name
        self.price = price
        self.store_id=store_id

    def __init__(self,name,price,store_id):

        self.name=name
        self.price=price
        self.store_id=store_id

    def json(self):
        return {"store_id":self.store_id,"name":self.name,"price":self.price}


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    def findByName(name):
        return ItemModel.query.filter_by(name=name).first()

    @classmethod
    def getItemsByStoreName(cls,name):
        store=StoreModel.find_by_name(name)
        return {"items:": [item.json() for item  in  ItemModel.query.filter_by(store_id=store.id).all()]}


        #multiples things ItemModel.query.filter_by(name=name).filter_by(id=2)
    # multiples things ItemModel.query.filter_by(name=name,id=2)