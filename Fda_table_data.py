import requests
from bs4 import BeautifulSoup
import psycopg2
from datetime import date

def extracting_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    link_url = "https://www.fda.gov/"
    news = []
    events = []
    dates=[]
    links = []
    link=[]
    found = 0
    for tag in soup.find_all(['h2', 'h3','p','a']):
        if tag.name == 'h2':
            if tag.text == "What's New By Topic":
                found = 1
            elif tag.text == "Upcoming Events":
                found = 2
            elif tag.text == "Recalls & Alerts":
                found = 3
        if found == 1 and tag.name == 'h3':
            news.append(tag.text.strip())
        if found == 1 and tag.name == 'a':
            links = tag.get('href')
            link.append(link_url + links)
        if found == 2 and tag.name == 'h3':
            events.append(tag.text.strip())
        if found == 2 and tag.name == 'p':
            dates.append(tag.text.lstrip())

        if found == 3:
            break
    dates =[i for i in dates if i!='']


    return news,link,events,dates

def today_date():
    Current_Date=date.today().strftime('%d/%m/%Y')
    print(Current_Date)
    return Current_Date

def create_table(host, database, username, password, port):
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=username,
            password=password,
            port=port
        )
        cursor = connection.cursor()
        sql_query = """
            CREATE TABLE IF NOT EXISTS FDA_Data (
                id SERIAL PRIMARY KEY,
                CurrentDate TEXT,
                News TEXT,
                Link Text,
                Events TEXT,
                Date TEXT
                
             );
           """
        cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        connection.close()
        print("Table created successfully in PostgreSQL!")
    except psycopg2.Error as error:
        print("Error while connecting to PostgreSQL or creating table:", error)


def insert_into_table(CurrentDate,data_list, host, database, username, password, port):
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=username,
            password=password,
            port=port
        )
        cursor = connection.cursor()
        sql_query = "INSERT INTO FDA_Data (CurrentDate,News,Links, Events, Date) VALUES (%s,%s, %s, %s,%s);"

        max_length = max(len(data_list[0]), len(data_list[1]), len(data_list[2]),len(data_list[3]))
        for i in range(max_length):
            news_item = data_list[0][i] if i < len(data_list[0]) else None
            link_item = data_list[1][i] if i < len(data_list[1]) else None
            events_item = data_list[2][i] if i < len(data_list[2]) else None
            date_item = data_list[3][i] if i < len(data_list[3]) else None

            cursor.execute(sql_query, (CurrentDate,news_item,link_item, events_item, date_item))
            #print(Current_Date)
        connection.commit()
        cursor.close()
        connection.close()
        print("Data inserted successfully into PostgreSQL!")
    except psycopg2.Error as error:
        print("Error while connecting to PostgreSQL or inserting data:", error)


if __name__ == "__main__":
    url = "https://www.fda.gov/news-events"

    data_list = extracting_data(url)
    Current_Date=today_date()
    #dates = extracting_date(url)
    if data_list:
        host = "10.140.189.165"
        database = "Internal"
        username = "postgres"
        password = "techsol"
        port = "5432"
        create_table(host, database, username, password, port)
        insert_into_table(Current_Date,data_list,host, database, username, password, port)
    else:
        print("No data found!")
#today_date()
