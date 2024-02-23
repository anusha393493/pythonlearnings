import requests
from bs4 import BeautifulSoup
import psycopg2
from datetime import date

def extracting_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup.prettify())
    link_url = "https://www.fda.gov/"
    news1_links = []
    news1_link = []

    events = []
    dates=[]
    links = []
    link=[]
    found = 0
    n_found=0
    for tag in soup.find_all(['h2', 'h3','p','a']):
        if tag.name == 'h2':
            if tag.text == "What's New By Topic":
                found = 1
            elif tag.text == "Upcoming Events":
                found = 2
        if found == 1 and tag.name == 'a':
            links = tag.get('href')
            link.append(link_url + links)
        if found == 2:
            break
    news1=link[0]
    #print(news1)
    res1 = requests.get(news1)
    s1 = BeautifulSoup(res1.content, 'html.parser')
    #print(s.prettify())
    for tag in s1.find_all(['h2','a']):
        if tag.name == 'h2':
            if tag.text == "Popular Topics":
                n_found = 1
            elif tag.text == "Features":
                n_found = 2
        if n_found == 1 and tag.name == 'a':
            news1_links = tag.get('href')
            news1_link.append(news1_links)
        if n_found == 2:
            break
    drugs_link=news1_link[0]
    #print(drugs_link)
    res2 = requests.get(drugs_link)
    s2 = BeautifulSoup(res2.content, 'html.parser')
    #print(s2.prettify())
    table=s2.find('table')
    for row in table.find_all('tr'):
        cells=row.find_all(['td','th'])
        row_data=[cell.text.strip() for cell in cells]
        print(row_data)



    return news1_link




if __name__ == "__main__":
    url = "https://www.fda.gov/news-events"
    host = "10.140.189.165"
    database = "Internal"
    username = "postgres"
    password = "techsol"
    port = "5432"
    link=extracting_data(url)
    #print(link)