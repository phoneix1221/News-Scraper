from blog.models import User
from flask import render_template,url_for,flash,redirect
from blog.forms import Registrationform,loginform,websiteform,viewform
from blog import app
from blog import bcrypt
from flask_login import login_user,current_user,logout_user,login_required
from mailjet_rest import Client
from flask_pymongo import pymongo
from bson.json_util import dumps 
from bson.objectid import ObjectId
from flask import jsonify,request 
import os
import urllib.parse
import subprocess
import sys
from datetime import date
import threading
from subprocess import call
from flask_talisman import Talisman
import razorpay

# Talisman config
csp = {
     'default-src': '\'self\'',
    
    'style-src': ['\'unsafe-inline\' \'self\'','https://ajax.googleapis.com/','https://code.jquery.com/','https://cdnjs.cloudflare.com/','https://stackpath.bootstrapcdn.com/'],
    'script-src':[ '\'unsafe-inline\' \'self\'','https://ajax.googleapis.com/','https://code.jquery.com/','https://cdnjs.cloudflare.com/'],
    'img-src':[ '\'self\' data:','*'],
    'font-src':'*'
    
}


Talisman(app,content_security_policy=csp,force_https_permanent=True)


name=''

#add a=mongoatlas username and password
mongopass=urllib.parse.quote_plus("")
mongouser=urllib.parse.quote_plus("")

# data=[{'blog_title':'first blog',
#         'blog_date':'12/10/2019',
#         'blog_author':'mayank',
#          'blog_content':'this is second blog'
#         },
#         {
#         'blog_title':'second blog',
#         'blog_date':'20/10/2019',
#         'blog_author':'atul',
#         'blog_content':'this is second blog'
#         } 
#     ]
  

CONNECTION_STRING = "mongodb+srv://%s:%s@mongodb1-vla9b.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient('mongodb+srv://%s:%s@mongodb1-vla9b.mongodb.net/test?retryWrites=true&w=majority' % (mongouser,mongopass))

#database name change according to your requirement
dbs = client.get_database('scrapper')

#collection names  change according to your requirement
user_collection = pymongo.collection.Collection(dbs,'users')
website_Collection=pymongo.collection.Collection(dbs,'websites')
webview_Collection=pymongo.collection.Collection(dbs,'views')


#routes
@app.route("/",methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=loginform()
    if form.validate_on_submit():
        user_json=user_collection.find_one({'Email':form.email.data})
        
        if user_json and bcrypt.check_password_hash(user_json['password'],form.password.data):
            loginuser = User(user_json)
            
            login_user(loginuser,remember=form.remember.data)
            flash(f'login successfully for user {form.email.data}!','success')
            return redirect(url_for('home'))
        else:
            flash(f'login failed please enter correct Email and Password !','danger')
    return render_template('login.html',form=form)

    
 

@app.route("/register", methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        form=Registrationform()
        if form.validate_on_submit():
            existing_user = user_collection.find_one({"Email":form.email.data})
            existing_user1=user_collection.find_one({"username":form.username.data})
            if existing_user is None and existing_user1 is None and form.password.data==form.password.data:
                hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                usname=str(form.username.data).strip()
                email=str(form.email.data).strip()

                user_collection.insert_one({"username":usname,"Email":email,"password":hashed_password})
                flash(f'Account created successfully for user {form.username.data}!','success')
                return redirect(url_for('login'))
            if existing_user is not None:    
                flash(f'Email already exist {form.email.data}!','error')
            elif existing_user1 is not None:
                flash(f'username already exist {form.username.data}!','error')   
        if form.password.data!=form.confirm_password.data:
            flash(f'passwords dont match {form.confirm_password.data}!','error')              
        return render_template('register.html',form=form)

@app.route("/home",methods=['POST','GET'])
@login_required
def home():
    if current_user.is_authenticated:
        fetch_data=website_Collection.find({'username':current_user.username})    
        form=websiteform()
        if form.validate_on_submit():
            website_Collection.insert_one({"username":current_user.username,"website_name":form.websitename.data,"website_url":form.websiteurl.data})
        return render_template('home.html',form=form,data=fetch_data)
        
            
    else :
        return redirect(url_for('login'))
         


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/account")
@login_required
def account():
   return render_template('account.html',title="Account")




@app.route("/profile")
@login_required
def user_profile():
    return render_template('user_profile.html') 





@app.route("/load/<name>",methods=['GET'])
@login_required
def load(name):
    fetch_data=webview_Collection.find({'username':current_user.username,'website_name':name})
    return render_template('websiteviews.html',data=fetch_data)




@app.route("/loadform/<name>",methods=['POST','GET'])
@login_required
def loadform(name):
    form=viewform()
    if form.validate_on_submit():
        keyword=form.keyword.data
        datefrom=form.datefrom.data
        if datefrom==None:
           
            today = date.today()
            datefrom=today.strftime("%d/%m/%Y")
        else:
            datefrom=datefrom.strftime('%d/%m/%Y')
        tot=form.total_no_post.data
        # language=form.language.data
        # if language==None:
        #     print("empty lang")
        #     language='na'
             
        webview_Collection.insert_one({"username":current_user.username,"website_name":name,"keyword":keyword,"datefrom":datefrom,"total_no_of_post":tot})
    name=str(name).upper()
    return render_template('websiteForm.html',data=name,form=form)

@app.route("/loadwithoutform",methods=['POST','GET'])
@login_required
def loadwithoutform():
    form=viewform()
    if form.validate_on_submit():
        keyword=form.keyword.data
        datefrom=form.datefrom.data
        if datefrom==None:
            
            today = date.today()
            datefrom=today.strftime("%d/%m/%Y")
        else:
            datefrom=datefrom.strftime('%d/%m/%Y')
        tot=form.total_no_post.data

        fetch_data=website_Collection.find({'username':current_user.username})
        
        
        for i in fetch_data:
            print(i['website_name'])
            webview_Collection.insert_one({"username":current_user.username,"website_name":str(i['website_name']),"keyword":keyword,"datefrom":datefrom,"total_no_of_post":tot})   

    return render_template('websiteForm.html',form=form)


@app.route("/del",methods=['POST'])
@login_required
def delete():
    if request.method == "POST":
        global name
        name=request.json['newwebget']
        name=name.lstrip()
        name=name.rstrip()

        website_Collection.delete_one({'username':current_user.username,'website_name':name})
        webview_Collection.delete_many({'username':current_user.username,'website_name':name})
        message={
             'status':200,
             'message':'successful'+request.url
        }
        resp=jsonify(message)  
        resp.status_code=200
        return resp
         
    else:
        message={
             'status':400,
             'message':'failed'+request.url
        }
        resp=jsonify(message)  
        resp.status_code=400  
        return resp


      

@app.route("/delview/<name>/<keyword>",methods=['GET'])
@login_required
def deleteview(name,keyword):
        webview_Collection.delete_one({'username':current_user.username,'website_name':name,'keyword':keyword}) 
        fetch_data=webview_Collection.find({'username':current_user.username,'website_name':name})
        return render_template('websiteviews.html',data=fetch_data)
  

@app.route("/runscrapping")
def runscrapping():
    us=current_user.username
    
    command=["python",'/app/blog/scripts/script3.py',"-a",us]
    # p = subprocess.Popen([sys.executable,'F:/projects/blog1/blog/script3',], 
                                    # stdout=subprocess.PIPE, 
                                    #  stderr=subprocess.STDOUT)
    subprocess.Popen(command,cwd='/app')
    
    return redirect(url_for('home'))


@app.route('/genorderid',methods=['POST','GET'])
def genorderid():
    cl = razorpay.Client(auth=("", ""))
    _json=request.json
    _receiptid=_json['receipt']
    _amount=_json['amount']
    DATA = {
    "amount":_amount,
    "currency":"INR",
    "receipt": _receiptid,
    "payment_capture":1
    }
    id=cl.order.create(data=DATA)
    gid=id['id']
    grecpid=id['receipt']
    message={
            'orderid':gid,
            'receipt':grecpid
        }
    resp=jsonify(message)  
    resp.status_code=200
    return resp
    
