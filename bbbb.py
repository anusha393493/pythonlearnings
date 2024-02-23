from bs4 import BeautifulSoup
import requests
import re
def extracting_news(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content, 'html.parser')
    #print(soup.prettify())
    new_url="https://www.fda.gov/"
    news=[]
    events=[]
    date=[]
    links=[]
    link=[]
    found=0
    for tag in soup.find_all(['h2','h3','p','a']):
        if tag.name=='h2':
            if tag.text=="What's New By Topic":
                found=1
            elif tag.text=="Upcoming Events":
                found=2
            elif tag.text=="Recalls & Alerts":
                found=3
        if found==1 and tag.name=='h3':
            news=tag.text.strip()
        if found==1 and tag.name=='a':
            links=tag.get('href')
            link.append(new_url+links)

        if found == 2 and tag.name == 'h3':
            events = tag.text.strip()
            #print(events)
        if found==2 and tag.name=='p':
            date=tag.text
            #print(date)
        if found==3:
            break
    print(news)

url="https://www.fda.gov/news-events"
extracting_news(url)


