import psycopg2
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# print(soup.prettify())
# print(soup.find_all('a'))
# t=[b['title'] for b in soup.find_all('p') if 'title' in b.attrs]
# print(t)
# print(soup.find_all('p'))
# div class=lcds-card-deck__body
# h3 class =lcds-card__title
# p class=lcds-card__text
# titles = [a['title'] for a in soup.find_all('a') if 'title' in a.attrs]
# for title in titles[5:11]:
# print(title)
def extracting_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    h3_titles = soup.find_all('h3')
    p_titles = soup.find_all('p')[3:-18]
    data_list = []
    for h3, p in zip(h3_titles, p_titles):
        h_data = h3.text.strip()
        p_data = p.text.strip()
        data_list.append((h_data, p_data))
        # data_list=data_list.split(')')
        datalist = [a for a in data_list]
        # print(len(data_list))
    return data_list

def extracting_date(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find_all('h3')
    dates = []
    for row in rows:
        if "FDA Roundup" in row.text:

            date=row.text.strip()
            dates.append(date)
    print(dates)
    return str(dates)


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
        sql_query="""
            CREATE TABLE IF NOT EXISTS WEB_SCRAPPING1 (
                id SERIAL PRIMARY KEY,
                title TEXT,
                description TEXT,
                Date Text
             );
           """
        cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        connection.close()
        print("Table created successfully in PostgreSQL!")

    except (Exception, psycopg2.Error) as error:(
        print("Error while connecting to PostgreSQL or creating table:", error))
        
def insert_into_table(data_list, dates, host, database, username, password, port):
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=username,
            password=password,
            port=port
        )
        cursor = connection.cursor()
        sql_query = "INSERT INTO WEB_SCRAPPING1 (title, description, Date) VALUES (%s, %s, %s);"
        for data_tuple in data_list:
            cursor.execute(sql_query, (*data_tuple, dates))
        connection.commit()
        cursor.close()
        connection.close()
        print("Data inserted successfully into PostgreSQL!")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL or inserting data:", error)



if __name__ == "__main__":
    url = "https://www.fda.gov/news-events"
    data_list = extracting_data(url)
    dates=extracting_date(url)
    if data_list:
        host = "10.140.189.165"
        database = "Internal"
        username = "postgres"
        password = "techsol"
        port = "5432"
        create_table(host, database, username, password, port)
        insert_into_table(data_list,dates,host, database, username, password, port)
    else:
        print("No data found!")