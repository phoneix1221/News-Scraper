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



def dk(key,tm,cm):
    arr=[]
    count=0
    pageindex=1
    exitscr=0
    if type(tm)==str:
                
        tm=datetime.datetime.strptime(tm,'%d/%m/%Y')
    keyer=[]
    if ' ' in key:
        key=key.replace(" ",'+')
    url="https://www.dkoding.in/page/"
    while(count<cm):
        url=url+str(pageindex)+"/?s="+key
        
        response=requests.get(url)
        content=BeautifulSoup(response.content,"html.parser")
        h1=content.findAll("h5",{"class":"entry-title"})
        h2=content.findAll("div",{"class":"time"})
        if len(h1)==0:
            return arr
        for i,j in zip(h1,h2):
            
            dt=str(j.get_text())
            dt=dt[:dt.index(" ")]
            dt=dt.strip()
            

            datetimeobject = datetime.datetime.strptime(str(dt),'%d/%m/%Y')
            
            if count<cm and datetimeobject>=tm:
                count+=1
                arr.append(i.find('a')['href'])
            else:
                exitscr=1
                
            
            
        if exitscr==1:
            return arr  
        pageindex=int(pageindex)+1
        url="https://www.dkoding.in/page/"
    return arr


