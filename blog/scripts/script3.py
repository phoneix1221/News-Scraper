
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
import sys
from it import indiatoday 
from ie import indianexpress
from thehindu import hindu
from toi import timesOfIndia
from oneind import oneindia
from scroll import scrollin
from businessline import bline
from dkoding import dk

#add username password of mongoatlas
mongopass=urllib.parse.quote_plus("")
mongouser=urllib.parse.quote_plus("")

CONNECTION_STRING = "mongodb+srv://%s:%s@mongodb1-vla9b.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient('mongodb+srv://%s:%s@mongodb1-vla9b.mongodb.net/test?retryWrites=true&w=majority' % (mongouser,mongopass))
dbs = client.get_database('scrapper')
currentuser=str(sys.argv[2])
user_collection = pymongo.collection.Collection(dbs,'users')
website_Collection=pymongo.collection.Collection(dbs,'websites')
webview_Collection=pymongo.collection.Collection(dbs,'views')

def get():
        cu=currentuser.strip()
        if cu=='':
            cu=''
        ex=0
        len_of_keywords=0
        user=user_collection.find_one({'username':cu})
        websites=website_Collection.find({"username":cu})
        print(websites)
        email=user['Email']
        filename=user['username']+".txt"
        file1 = open(filename,"w") 
        for website in websites:
            print(website)
            keywords=webview_Collection.find({"username":cu,"website_name":website['website_name']})

            if str(website['website_name']).lower()=='ndtv':
                
                len_of_keywords+=1
                
                if keywords.count()==0:
                    ex=ex+1


                file1.write("\nNDTV \n")
                links=["https://www.ndtv.com/india/page-","https://www.ndtv.com/world-news/page-","https://www.ndtv.com/cities/page-","https://www.ndtv.com/education/page-","https://www.ndtv.com/business/latest/page-","https://gadgets.ndtv.com/mobiles/news/page-",'https://gadgets.ndtv.com/telecom/news/page-','https://gadgets.ndtv.com/entertainment/news/page-','https://gadgets.ndtv.com/games/news/page-','https://gadgets.ndtv.com/tv/news/page-','https://gadgets.ndtv.com/laptops/news/page-','https://gadgets.ndtv.com/apps/news/page-','https://gadgets.ndtv.com/tablets/news/page-','https://gadgets.ndtv.com/science/news/page-']
                for keyword in keywords:
                    
                    breaker=0
                    sept=0
                    count=0
                    pageindex=1
                    
                    dt=keyword['datefrom']
                    file1.write("\n"+str(keyword['keyword'])+"\n")
                    url="https://www.ndtv.com/latest/page-"
                    
                    while(count<int(keyword['total_no_of_post'])):
                        url=url+str(pageindex)
                        
                        response=requests.get(url)
                        movetonext=0
                        if sept==0 or sept==1 or sept==2 or sept==3 or sept==4 or sept==5 :
                            content=BeautifulSoup(response.content,"html.parser")
                            h1=content.findAll("div",{"class": "nstory_header"})
                            h2=content.findAll("div",{"class":"nstory_intro"})
                            h3=content.findAll("div",{"class":"nstory_dateline"})
                        
                            for i,j,k in zip(h1,h2,h3):
                                dmm=datecon(str(k.text))
                                
                                dmm=datetime.datetime.strptime(dmm,'%d/%m/%Y')
                                dtm=datetime.datetime.strptime(dt,'%d/%m/%Y')
                                if dmm<dtm:

                                   
                                    movetonext=1
                                key=str(keyword['keyword'])
                                if ' ' in key.strip():
                                    co=0
                                    split=key.split(' ')
                                    for m in split:
                                        if m.lower() in  i.text.lower()  or m.lower() in j.text.lower():
                                            co=co+1
                                    if co==len(split):
                                        if count<int(keyword['total_no_of_post']):
                                            count+=1
                                            file1.write(str(i.find('a')['href'])+"\n")

                                else:

                                    if keyword['keyword'].lower() in i.text.lower() or keyword['keyword'].lower() in j.text.lower():
                                        if count<int(keyword['total_no_of_post']):
                                            count+=1
                                            file1.write(str(i.find('a')['href'])+"\n")

                        elif  sept==6 or sept==7 or sept==8 or sept==9 or sept==10 or sept==11 or sept==12 or sept==13 or sept==14 :
                            content=BeautifulSoup(response.content,"html.parser")
                            h1=content.findAll("div",{"class": "caption_box"})
                            h2=content.findAll("div",{"class": "dateline"})
                            for i,j in zip(h1,h2):
                                dmt=datecon1(str(j.text))
                                
                                dmt=datetime.datetime.strptime(dmt,'%d/%m/%Y')
                                dtk=datetime.datetime.strptime(dt,'%d/%m/%Y')
                                
                                if dmt<dtk:
                                    
                                    movetonext=1
                                st=i.find('span',{"class": "news_listing"}).text
                                key=str(keyword['keyword'])
                                if ' ' in key.strip():
                                    co=0
                                    split=key.split(' ')
                                    for m in split:
                                        if m.lower() in st.lower():
                                            co+=1
                                    if co==len(split):
                                        if count<int(keyword['total_no_of_post']):
                                            count+=1
                                            file1.write(str(i.find('a')['href'])+"\n")           
                                else:

                                    if keyword['keyword'].lower() in st.lower():
                                        if count<int(keyword['total_no_of_post']):
                                            count+=1
                                            file1.write(str(i.find('a')['href'])+"\n")

                           

                        pageindex+=1
                        if movetonext==1 and sept<14:
                            
                            
                            pageindex=1
                            if sept==13:
                                sept=sept+1
                                movetonext=0
                                break
                            else:
                                sept=sept+1    
                                url=links[sept]
                                movetonext=0
                        if pageindex>8 and sept==0 :
                            pageindex=1
                            sept=1
                            url=links[0]
                        if sept==1 or sept==2 or sept==3 or sept==4 or sept==5:
                            if pageindex>14:
                                pageindex=1
                                url=links[sept]
                                sept=sept+1

                        if sept>=6 and sept<14:
                            if pageindex>10:
                                pageindex=1
                                url=links[sept]
                                sept=sept+1
                        if pageindex>10 and sept>13:
                            break

                            
                            
                        sep='-'
                        url = url.split(sep, 1)[0]
                        url=url+"-"

            if str(website['website_name']).lower()=='youtube':
                
                file1.write("\nYOUTUBE\n")
                api_key = ""
                len_of_keywords+=1
                if keywords.count()==0:
                    ex=ex+1
                for keyword in keywords:
                    st=keyword['datefrom']
                    file1.write("\n"+keyword['keyword']+"\n")
                    youtube=build('youtube','v3',developerKey=api_key)
                    datetimeobject = datetime.datetime.strptime(str(st),'%d/%m/%Y')
                    start_time=datetimeobject.strftime('%Y-%m-%dT%H:%M:%SZ')
                    req=youtube.search().list(q=keyword['keyword'], part="snippet", type="video",maxResults=keyword['total_no_of_post'], publishedAfter=start_time)
                    res=req.execute()
                    for i in res['items']:
                        
                        string=i['snippet']['publishedAt']
                        url = i['id']['videoId']     
                        string=string[:10]
                        file1.write("https://www.youtube.com/watch?v="+url+"\n")
            

            if str(website['website_name']).lower().strip()=='indiatoday' or str(website['website_name']).lower().strip()=='india today':
                file1.write("\nIndia today\n")
                
                len_of_keywords+=1
                if keywords.count()==0:
                    ex=ex+1
                
                for keyword in keywords:
                     st=keyword['datefrom']
                     tot=int(keyword['total_no_of_post'])
                     file1.write("\n"+keyword['keyword']+"\n")
                     res=indiatoday(str(keyword['keyword']),st,tot)
                     for i in res:
                         file1.write(i+"\n")
            
            if str(website['website_name']).lower().strip()=='indianexpress' or str(website['website_name']).lower().strip()=='indian express' or str(website['website_name']).lower()=='the indian express':
                file1.write("\nIndian Express\n")
                
                len_of_keywords+=1
                if keywords.count()==0:
                    ex=ex+1
                for keyword in keywords:
                     st=keyword['datefrom']
                     tot=int(keyword['total_no_of_post'])
                     file1.write("\n"+keyword['keyword']+"\n")
                     res=indianexpress(str(keyword['keyword']),st,tot)
                     for i in res:
                         file1.write(i+"\n")
            
            if str(website['website_name']).lower().strip()=='thehindu' or str(website['website_name']).lower().strip()=='the hindu':
                file1.write("\nThe hindu\n")
                
                len_of_keywords+=1
                if keywords.count()==0:
                    ex=ex+1
                for keyword in keywords:
                     st=keyword['datefrom']
                     tot=int(keyword['total_no_of_post'])
                     file1.write("\n"+keyword['keyword']+"\n")
                     res=hindu(str(keyword['keyword']),st,tot)
                     for i in res:
                         file1.write(i+"\n")


            if str(website['website_name']).lower().strip()=='times of india' or str(website['website_name']).lower().strip()=='timesofindia':
                file1.write("\nTimes Of India\n")
                
                len_of_keywords+=1
                if keywords.count()==0:
                    ex=ex+1
                for keyword in keywords:
                     st=keyword['datefrom']
                     tot=int(keyword['total_no_of_post'])
                     file1.write("\n"+keyword['keyword']+"\n")
                     res=timesOfIndia(str(keyword['keyword']),st,tot)
                     for i in res:
                         file1.write(i+"\n")

            if str(website['website_name']).lower().strip()=='oneindia' or str(website['website_name']).lower().strip()=='one india':
                file1.write("\nOneindia\n")
                len_of_keywords+=1
                if keywords.count()==0:
                    ex=ex+1
               
                for keyword in keywords:
                     st=keyword['datefrom']
                     tot=int(keyword['total_no_of_post'])
                     file1.write("\n"+keyword['keyword']+"\n")
                     res=oneindia(str(keyword['keyword']),st,tot)
                     for i in res:
                         file1.write(i+"\n")

            if str(website['website_name']).lower().strip()=='scroll.in' or str(website['website_name']).lower().strip()=='scroll':
                file1.write("\nscroll.in\n")
                len_of_keywords+=1
                if keywords.count()==0:
                    ex=ex+1
                
                for keyword in keywords:
                     st=keyword['datefrom']
                     tot=int(keyword['total_no_of_post'])
                     file1.write("\n"+keyword['keyword']+"\n")
                     res=scrollin(str(keyword['keyword']),st,tot)
                     for i in res:
                         file1.write(i+"\n")
                
            if str(website['website_name']).lower().strip()=='businessline' or str(website['website_name']).lower().strip()=='business line':
                file1.write("\nbusiness line\n")
                
                len_of_keywords+=1
                if keywords.count()==0:
                    ex=ex+1
                for keyword in keywords:
                     st=keyword['datefrom']
                     tot=int(keyword['total_no_of_post'])
                     file1.write("\n"+keyword['keyword']+"\n")
                     res=bline(str(keyword['keyword']),st,tot)
                     for i in res:
                         file1.write(i+"\n")
            
            if str(website['website_name']).lower().strip()=='dkoding' :
                file1.write("\ndkoding\n")
                
                len_of_keywords+=1
                if keywords.count()==0:
                    ex=ex+1
                for keyword in keywords:
                     st=keyword['datefrom']
                     tot=int(keyword['total_no_of_post'])
                     file1.write("\n"+keyword['keyword']+"\n")
                     res=dk(str(keyword['keyword']),st,tot)
                     for i in res:
                         file1.write(i+"\n")
            

                

        
        
                        
        file1.close()
        msg=EmailMessage()
        today = date.today()
        do=today.strftime("%d/%m/%Y")
        msg['Subject']='Online news '+do
        msg['From']=''
        msg['To']=email
        msg.set_content("kindly find the attachment")
        with open(filename,'rb') as f:
            file_data=f.read()
            file_name=f.name

            msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:

            #add smtp credientials here
            smtp.login('', '')

            smtp.send_message(msg)
        print("mail send")
            


                        

def datecon(dt):
    dt=dt.strip()
    if "|" in dt:
        dt=dt[dt.index("|")+2:]
        if dt.count(',')==2:
            rdex=dt.rindex(',')
            ldex=dt.index(',')
            yr=dt[ldex+2:rdex]
            da=dt[ldex-2:ldex]
            sp=dt.index(" ")
            mon=dt[sp+1:ldex-3]
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
            da=da.strip()
            yr=yr.strip()
            date=da+"/"+str(month)+"/"+yr
            
            return date

        elif dt.count(',')==1:
                yr=dt[dt.rindex(',')+2:]
                yr=yr.strip()
                dat=dt[dt.rindex(',')-2:dt.rindex(',')]
                dat=dat.strip()
                mon=dt[dt.index(' '):dt.rindex(',')-2]
                mon=mon.strip()
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
                date=dat+"/"+str(month)+"/"+yr
                
                return date
        
        elif dt.count(',')==3:
                
                mt=dt.find(',',2)
                yr=dt[mt+2:mt+6]
                yr=yr.strip()
                dat=dt[mt-2:dt.find(',')]
                dat=dat.strip()
                mon=dt[dt.index(' '):mt-2]
                mon=mon.strip()
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
                date=dat+"/"+str(month)+"/"+yr
                
                return date
        else:
            return '20/80/1990'
    else:
        
        if dt.count(',')==2:
            rdex=dt.rindex(',')
            ldex=dt.index(',')
            yr=dt[ldex+2:rdex]
            da=dt[ldex-2:ldex]
            sp=dt.index(" ")
            mon=dt[sp+1:ldex-3]
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
            da=da.strip()
            yr=yr.strip()
            date=da+"/"+str(month)+"/"+yr
           
            return date

        elif dt.count(',')==1:
                yr=dt[dt.rindex(',')+2:]
                yr=yr.strip()
                dat=dt[dt.rindex(',')-2:dt.rindex(',')]
                dat=dat.strip()
                mon=dt[dt.index(' '):dt.rindex(',')-2]
                mon=mon.strip()
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
                date=dat+"/"+str(month)+"/"+yr
                
                return date
        
        elif dt.count(',')==3:
                
                mt=dt.find(',',2)
                yr=dt[mt+2:mt+6]
                yr=yr.strip()
                dat=dt[mt-2:dt.find(',')]
                dat=dat.strip()
                mon=dt[dt.index(' '):mt-2]
                mon=mon.strip()
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
                date=dat+"/"+str(month)+"/"+yr
                
                return date
        else:
             
            return '20/80/1990'



def datecon1(val):
        if val.count(',')==1:
                yr=val[val.rindex(' ')+1:]
                yr=yr.strip()
                dt=val[val.index(',')+2:val.index(',')+4]
                dt=dt.strip()
                
                st=val[:val.rindex(' ')]
                mon=st[st.rindex(' ')+1:]
                mon=mon.strip()
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
                date=dt+"/"+str(month)+"/"+yr
                
                return date
        
        else:
            return '20/08/1990'
            



get()        






