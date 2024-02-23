import requests
from bs4 import BeautifulSoup
import psycopg2
from datetime import date
url="https://www.fda.gov/news-events/fda-newsroom/press-announcements"
response=requests.get(url)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup.prettify())
current_date=date.today()
current_month=current_date.strftime("%B")
current_year=current_date.year
date=(current_month+" "+str(current_year))
months=[]
links=[]
#print(date)
for tag in soup.find_all(['h3','a']):
    if tag.name=='h3':
        months.append(tag.text.strip())
        month=months[0]

#print(month)


#print(months[0])

