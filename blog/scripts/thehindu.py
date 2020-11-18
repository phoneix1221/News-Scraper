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



def hindu(key,tmk,cm):
    arr=[]
    count=0
    pageindex=1
    exitscr=0
    keyer=[]
    if type(tmk)==str:
                
        tmk=datetime.datetime.strptime(tmk,'%d/%m/%Y')
    if ' ' in key:
        key=key.replace(" ",'%20')
    url="https://www.thehindu.com/search/?q="
    while(count<cm):
        url=url+str(key)+"&order=DESC&sort=publishdate&page="+str(pageindex)
        
        response=requests.get(url)
        content=BeautifulSoup(response.content,"html.parser")
        h1=content.findAll("a",{"class":"story-card75x1-text"})
        h2=content.findAll("span",{"class":"light-gray-color story-card-33-text hidden-xs"})
        h3=content.findAll("span",{"class":"dateline"})
        if len(h1)==0:
            return arr
        for i,j,k in zip(h1,h2,h3):
            counter=0
            link=i['href']
            date=str(k.get_text())
            date=date.strip()
            mon=date[:date.index(" ")]
            day=date[date.index(" "):date.index(",")]
            day=day.strip()
            year=date[date.rindex(" "):]


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
            dt=day+"/"+str(month)+"/"+str(year).strip()
            start_time = datetime.datetime.strptime(str(dt),'%d/%m/%Y')
            # start_time=datetimeobject.strftime('%d/%m/%Y')
            
            
            if count<cm and start_time>=tmk:
                count+=1
                arr.append(link)
            else:
                exitscr=1
            counter=0
            if exitscr==1:
                return arr  
        pageindex=int(pageindex)+1
        url="https://www.thehindu.com/search/?q="
    return arr

