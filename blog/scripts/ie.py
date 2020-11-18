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



def indianexpress(key,tmk,cm):
    arr=[]
    count=0
    pageindex=1
    exitscr=0
    keyer=[]
    if type(tmk)==str:
                
        tmk=datetime.datetime.strptime(tmk,'%d/%m/%Y')
    if ' ' in key:
        key=key.replace(" ",'+')
    
    url="https://indianexpress.com/page/"
    while(count<cm):
        url=url+str(pageindex)+"/?s="+str(key)
        
        response=requests.get(url)
        content=BeautifulSoup(response.content,"html.parser")
        
        h1=content.findAll("h3")
        h2=content.findAll("time")
        h3=content.findAll("p")
        if len(h1)==0:
            return arr
        
        for i,j,k in zip(h1,h2,h3):
            counter=0
            time=str(j.get_text())
            tm=time.split(" ")
            mon=str(tm[len(tm)-6])
            
            title=str(i.find('a').get_text())
            more=str(k.get_text())

            if mon.lower()=='january':
                        month=1
            elif mon.lower()=='february':
                        month=2
            elif mon.lower()=='march':
                        month=3
            elif mon.lower()=='april':
                        month=4
            elif mon.lower()=='may':
                        month=5
            elif mon.lower()=='june':
                        month=6
            elif mon.lower()=='july':
                        month=7
            elif mon.lower()=='august':
                        month=8
            elif mon.lower()=='september':
                        month=9
            elif mon.lower()=='october':
                        month=10
            elif mon.lower()=='november':
                        month=11
            elif mon.lower()=='december':           
                        month=12
            date=str(tm[len(tm)-5]).replace(",",'')+"/"+str(month)+"/"+str(tm[len(tm)-4])
            start_time = datetime.datetime.strptime(str(date),'%d/%m/%Y')
            # start_time=datetimeobject.strftime('%d/%m/%Y')
            
                
            if count<cm and start_time>=tmk:
                count+=1
                
                arr.append(i.find('a')['href'])
            else:
                exitscr=1
            
        if exitscr==1:
            return arr  
        pageindex=int(pageindex)+1
        url="https://indianexpress.com/page/"
    return arr
    