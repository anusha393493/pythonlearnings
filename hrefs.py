import psycopg2
import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.fda.gov/news-events"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
valid_links=[]
print(soup.prettify())
url="https://www.fda.gov/"
for h3 in soup.find_all('h3'):
    links=soup.find_all('a')
    for link in links:
        href=link.get('href')
        if href==None:
            pass
        else:
            href = url+href
            href=href.replace("#","")
            #print(href)
            valid_links.append(href)

#print(valid_links)








