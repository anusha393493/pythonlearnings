from Fda_table_data import *
import requests
from bs4 import BeautifulSoup
def extracting_urldata(url1):
    title = []
    description = []
    found = 0
    for tag in soup.find_all(['h2','h3','p']):
        #print(tag.text)
        if tag.name == 'h2':
            if tag.text == "Popular Topics":
                found = 1
            elif tag.text == "Features":
                found = 2
        if found == 1 and tag.name == 'h3':
            title.append(tag.text.strip())
            print(title)
        if found == 1 and tag.name == 'p':
            description.append(tag.text.strip())

        if found == 2:
            break

    print(description)

url="https://www.fda.gov/news-events"
#extracting_data(url)
#print(extracting_data.link[1])
a,b,c,d=extracting_data(url)
#print(a,b,c,d)
url1=(b[0])
#print(url1)
#print(url1)
response=requests.get(url1)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup.prettify())
#extracting_data(url1)
found=0
title=[]
description=[]
for tag in soup.find_all(['h2','h3','p']):
    #print(tag.text)
    if tag.name == 'h2':
        if tag.text == "Popular Topics":
            found = 1
        elif tag.text == "Features":
            found = 2
    if found == 1 and tag.name == 'h3':
        title.append(tag.text.strip())

    if found == 1 and tag.name == 'p':
        description.append(tag.text.strip())
print(title)

