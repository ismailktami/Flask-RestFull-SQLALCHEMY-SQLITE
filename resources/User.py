import sqlite3
from flask_restful import Resource,reqparse,request
from modules.User import UserModel

class UserReister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',required=True, help="this field cannot be left blank")
    parser.add_argument('password',type=str,required=True, help="this field cannot be left blank")



    def post(self):
        data =self.parser.parse_args()
        user= UserModel.findBy_username(data['username'])
        if user is None:
            user=UserModel(data['username'],data['password'])
            user.add_user()
            message={"id":1,"messgae": "Use created succesfully"}
        else:
            message={"id":2,"messgae": "Can t add user with this username"}
        return message,201 if message.get("id")==1 else 400