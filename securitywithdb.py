from resources.User import UserModel

from werkzeug.security import safe_str_cmp



def authenticate(username,password):
    user=UserModel.findBy_username(username)
    if user and safe_str_cmp(user.password,password):
        return user


def identity(payload):
    userid=payload['identity']
    return UserModel.findBy_id(userid)