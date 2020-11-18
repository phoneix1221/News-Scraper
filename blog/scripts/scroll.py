from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request
from flask_pymongo import pymongo
import urllib.parse
from flask_cors import CORS,cross_origin
from bson.json_util import dumps
from datetime import date
import datetime 
import requests
import GetOldTweets3 as got
from facebook_scraper import get_posts
from bs4 import BeautifulSoup 
import requests
import datetime
import os
import smtplib
from email.message import EmailMessage
from apiclient.discovery import build



def scrollin(key,tm,cm):
    arr=[]
    count=0
    pageindex=1
    exitscr=0
    keyer=[]
    if type(tm)==str:
                
        tm=datetime.datetime.strptime(tm,'%d/%m/%Y')
    if ' ' in key:
        key=key.replace(" ",'%20')
    url="https://scroll.in/search?q="+key
    while(count<cm):
        url=url+str("&page=")+str(pageindex)
        
        response=requests.get(url)
        content=BeautifulSoup(response.content,"html.parser")
        h1=content.find("div",{"class":"row-stories column scroll-box"})
        if len(h1)==0:
            return arr     
        z=h1.findAll('li')
        for i in z:
            dt=str(i.find('time'))
            date=dt[dt.rindex("-")+1:dt.rindex("-")+3]+dt[dt.index("-"):dt.rindex("-")]+"-"+dt[dt.index("-")-4:dt.index("-")]
            start_time = datetime.datetime.strptime(str(date),'%d-%m-%Y')
            # start_time=datetimeobject.strftime('%d/%m/%Y')    
            if count<cm and start_time>=tm:
                count+=1
                arr.append(i.find('a')['href'])
            else:
                exitscr=1
            
            
        if exitscr==1:
            return arr  
        pageindex=int(pageindex)+1
        url="https://scroll.in/search?q="+key
    return arr





