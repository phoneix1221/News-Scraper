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



def bline(key,tm,cm):
    arr=[]
    count=0
    pageindex=0
    exitscr=0
    if type(tm)==str:
                
        tm=datetime.datetime.strptime(tm,'%d/%m/%Y')
   
    if ' ' in key:
        key=key.replace(" ",'+')
    url="https://www.thehindubusinessline.com/search/?order=DESC&page="
    while(count<cm):
        url=url+str(pageindex)+str("&q=")+key+str("&sort=publishdate")
        response=requests.get(url)
        content=BeautifulSoup(response.content,"html.parser")
        h1=content.findAll("article")
        # h2=content.findAll("div",{"class":"views-field views-field-php-2"})
        # h3=content.findAll("div",{"class":"text-details"})
        if len(h1)==0:
            return arr

        c=0
        for i in h1:
            c=c+1
            p=i.find('div')
            z=i.find('span')
            
            dt=str(z.get_text())
            
            
            mon=dt[dt.index(" ")+1:dt.index(",")]
            counter=0
           
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
            
            date=str(dt[:dt.index(" ")]).strip()+"/"+str(month)+"/"+str(dt[dt.rindex(" ")+1:]).strip()
            
            start_time = datetime.datetime.strptime(str(date),'%d/%m/%Y')
            # start_time=datetimeobject.strftime('%d/%m/%Y')    
            if count<cm and start_time>=tm:
                count+=1
                arr.append(p.find('a')['href'])
            else:
                exitscr=1
            counter=0
            if c==20:
                break
            
        if exitscr==1:
            return arr  
        pageindex=int(pageindex)+1
        url="https://www.thehindubusinessline.com/search/?order=DESC&page="
    return arr

