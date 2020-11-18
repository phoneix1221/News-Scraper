from datetime import date
import datetime 
import requests
from bs4 import BeautifulSoup 


def timesOfIndia(key,tmk,cm):
    arr=[]
    count=0
    pageindex=1
    exitscr=0
    keyer=[]
    if type(tmk)==str:
                
        tmk=datetime.datetime.strptime(tmk,'%d/%m/%Y')
    if ' ' in key:
        key=key.replace(" ",'-')
    # print(key)
    url="https://timesofindia.indiatimes.com/topic/"
    while(count<cm):
        url = url+str(key)+"/"+str(pageindex)
        # print(url)
        response=requests.get(url)
        content=BeautifulSoup(response.content,"html.parser")
        
        h1 = content.find_all('span', class_="title")
        h2 = content.find_all('span', class_="meta")
        h3 = content.find_all('div', class_="content")
        if len(h1)==0:
            return arr
        
        
        
        for i,j,k in zip(h1,h2,h3):
            
            
            # print(title)
            date = str(j.get_text())
            if '-' in date:
                date=date.replace("-","/")
                date=date[:date.rindex("/")+3]
                date = date.strip()
                start_time = datetime.datetime.strptime(date, '%Y/%m/%d')
                # start_time = datetimeobject.strftime('%d/%m/%Y')
            else:
                date=date.replace(" ","/")
                mon=date[date.index("/")+1:date.rindex("/")]
                # print(mon)
                if mon.lower()=='jan':
                            month=1
                elif mon.lower()=='feb':
                            month=2
                elif mon.lower()=='mar':
                            month=3
                elif mon.lower()=='apr':
                            month=4
                elif mon.lower()=='may':
                            month=5
                elif mon.lower()=='jun':
                            month=6
                elif mon.lower()=='jul':
                            month=7
                elif mon.lower()=='aug':
                            month=8
                elif mon.lower()=='sep':
                            month=9
                elif mon.lower()=='oct':
                            month=10
                elif mon.lower()=='nov':
                            month=11
                elif mon.lower()=='dec':           
                            month=12
                date=date[:date.index("/")]+"/"+str(month)+date[date.rindex("/"):]
                date = date.strip()
                start_time = datetime.datetime.strptime(date,'%d/%m/%Y')
                # start_time = datetimeobject.strftime('%d/%m/%Y')


            # print(start_time)
            # print(start_time,">",tmk)
            if count<cm and start_time>=tmk:
                count+=1
                arr.append("https://timesofindia.indiatimes.com/topic"+k.find('a')['href'])
            else:
                exitscr=1
        
        if exitscr==1:
            return arr  
        pageindex=int(pageindex)+1
        url = "https://timesofindia.indiatimes.com/topic/"
    return arr


    
