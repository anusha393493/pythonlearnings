import requests
from bs4 import BeautifulSoup
import psycopg2

def extracting_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    news = []
    events = []
    found = 0

    for tag in soup.find_all(['h2', 'h3']):
        if tag.name == 'h2':
            if tag.text == "What's New By Topic":
                found = 1
            elif tag.text == "Upcoming Events":
                found = 2
            elif tag.text == "Recalls & Alerts":
                found = 3
        if found == 1 and tag.name == 'h3':
            lines=tag.name.split("\n")
        if found == 2 and tag.name == 'h3':
            events.append(tag.text.strip())
        if found == 3:
            break
    return news, events
url="https://www.fda.gov/news-events"