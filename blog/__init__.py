from flask import Flask
from flask_login import LoginManager
import pytz
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from bson.json_util import dumps 
from bson.objectid import ObjectId
from flask import jsonify
from mailjet_rest import Client

import os
 
app = Flask(__name__,static_url_path='/static')

app.config["CACHE_TYPE"] = "null"
app.config['SECRET_KEY']=''
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
TEMPLATES_AUTO_RELOAD = True

bcrypt=Bcrypt(app)

login_manager=LoginManager(app)
login_manager.login_view='login'
from blog import routes

