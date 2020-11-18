from blog import login_manager
from datetime import datetime
from flask_login import UserMixin
from flask_pymongo import pymongo
import urllib.parse
from bson import ObjectId

 
@login_manager.user_loader
def load_user(user_id):
    # define username and password of mongoatlas
    mongopass=urllib.parse.quote_plus("")
    mongouser=urllib.parse.quote_plus("")
    client = pymongo.MongoClient('mongodb+srv://%s:%s@mongodb1-vla9b.mongodb.net/test?retryWrites=true&w=majority' % (mongouser,mongopass))
    dbs = client.get_database('scrapper')
    user_collection = pymongo.collection.Collection(dbs,'users')
    user_json = user_collection.find_one({'_id': ObjectId(user_id)})
    return User(user_json)


class User(UserMixin):
    def __init__(self, user_json):
        self.user_json = user_json
        self.username=user_json['username']
        self.email=user_json['Email']    

    # Overriding get_id is required if you don't have the id property
    # Check the source code for UserMixin for details
    def get_id(self):
        object_id = self.user_json.get('_id')
        return str(object_id)
    def __repr__(self):
        return f"User('{self.username}','{self.email}')"

