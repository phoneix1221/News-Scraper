# News-Scraper

  News-Scraper is a flask based webapplication used for scraping news from different india news websites with the help of beautiful soup and mongodb .
# Features

1) user login and signup with email in which user will get the news from the sites he added into the webapp

2) user can add/edit/update/delete news websites and keywords for which he want to scrap news from 

3) user will automatically get a text file with added keywords from added websites on their mail (interval based on cron job )

4) user can run the scraping process whenever he wants to 



#Requirements

Install all requirements from requirements.txt

#Procedure

Install all requirements and add monogoatlas credientials in routes,models,script3.py files run flask app .For regular interval emails send to user use cron job and run script3.py
set the cron job time .scripts of websites can be found in scripts folder.
I have only added 9 or 10 scripts only those websites will work whos scripts are available . Create your own scripts if you want more webistes.
