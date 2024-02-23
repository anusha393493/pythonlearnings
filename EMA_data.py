import requests
from bs4 import BeautifulSoup
import psycopg2
from datetime import date
import smtplib, ssl
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def sending_data(link):
    href1 = "https://www.ema.europa.eu/"
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    #found=0
    table=soup.find('table')
    table_data=[]
    #print(table.text)
    #print(soup.prettify())
    for row in table.find_all('tr'):
        row_data=[]
        for cell in row.find_all(['td']):
            cell_text=cell.get_text().strip()
            anchor_tag=cell.find('a')
            if anchor_tag:
                href2=anchor_tag.get('href')
                href2=href1+href2
                row_data.append((cell_text,href2))
            else:
                row_data.append(cell_text)

        table_data.append(row_data)
    #print(table_data)


    return table_data
def extract_data(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    found=0
    table=soup.find('table')
    table_data=[]
    #print(table.text)
    #print(soup.prettify())
    for row in table.find_all('tr'):
        row_data=[]
        for cell in row.find_all(['td']):
            row_data.append(cell.get_text().strip())
        table_data.append(row_data)
    #print(table_data)

    data_count=len(table_data)
    data_count=data_count-1
    #print(length)
    return data_count

def today_date():
    Current_Date=date.today().strftime('%d/%m/%Y')
    #print(Current_Date)
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
            CREATE TABLE IF NOT EXISTS EMA_Data (
                CurrentDate TEXT,
                data_count INTEGER
                );
           """
        sql_query1 ="""
            CREATE TABLE IF NOT EXISTS EMA_content (
                content_date TEXT,
                Content Text,
                URL Text,
                Status Text
                );
        """
        cursor.execute(sql_query)
        cursor.execute(sql_query1)
        connection.commit()
        cursor.close()
        connection.close()
        print("Table created successfully in PostgreSQL!")
    except psycopg2.Error as error:
        print("Error while connecting to PostgreSQL or creating table:", error)

def getting_data(host, database, username, password, port):
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=username,
            password=password,
            port=port
        )
        cursor = connection.cursor()
        sql_query = """(
            SELECT * FROM EMA_Data
            WHERE CurrentDate=(SELECT MAX(CurrentDate) FROM EMA_Data)
             );
           """
        cursor.execute(sql_query)
        result=cursor.fetchone()
        connection.commit()
        cursor.close()
        connection.close()
        #print("select!")
        return result
    except psycopg2.Error as error:
        print("Error while connecting to PostgreSQL or creating table:", error)


def insert_into_table(CurrentDate,data_count, host, database, username, password, port):
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=username,
            password=password,
            port=port
        )
        cursor = connection.cursor()
        sql_query = "INSERT INTO EMA_Data (CurrentDate,data_count) VALUES (%s,%s);"
        cursor.execute(sql_query, (CurrentDate,data_count))
            #print(Current_Date)
        connection.commit()
        cursor.close()
        connection.close()
        print("Data inserted successfully into PostgreSQL!")
    except psycopg2.Error as error:
        print("Error while connecting to PostgreSQL or inserting data:", error)
def insert_into_table1(table_data, database, username, password, port):
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=username,
            password=password,
            port=port
        )
        cursor = connection.cursor()
        for row in table_data:

            if len(row) >= 3:
                content = row[1][0]
                url = row[1][1]

                cursor.execute("INSERT INTO EMA_content(content_date, Content, URL, Status) VALUES (%s, %s, %s, %s)",
                               (row[0], content, url, row[2]))
            else:
                pass
        connection.commit()
        cursor.close()
        connection.close()
        print("Data inserted successfully into PostgreSQL!")
    except psycopg2.Error as error:
        print("Error while connecting to PostgreSQL or inserting data:", error)


def comparision(host, database, username, password, port):
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=username,
            password=password,
            port=port
        )
        cursor = connection.cursor()
        query = """
                    SELECT * FROM EMA_content 
                    WHERE content_date IN (
                        SELECT DISTINCT content_date 
                        FROM EMA_content 
                        ORDER BY content_date DESC 
                        LIMIT 7
                    )
                    ORDER BY content_date DESC;
                """
        cursor.execute(query)
        rows=cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]
        table = tabulate(rows, headers=col_names, tablefmt="html")
        #print(results)
        connection.commit()
        cursor.close()
        connection.close()
        return table
    except psycopg2.Error as error:
        print("Error while connecting to PostgreSQL or executing query:", error)


def send_email(table_html,host, database, username, password, port):
    previous_date = getting_data(host, database, username, password, port)
    current_date = today_date()
    if previous_date[0] != current_date:
        print("not same!")
        sender_email = "noreply.medinquirer@scimaxglobal.com"
        receiver_email = 'rapolarjun@gmail.com'
        password = input("Enter your email password:")
        message = MIMEMultipart("alternative")
        message["Subject"] = "EMA UPDATES"
        message["From"] = sender_email
        message["To"] = receiver_email
        html = f"""\
        <html>
          <body>
            <p>Hi team,
              Here are the updates of EMA:
            </p>
            {table_html}
            <p>
            Regards,
            Analytics Team.
            </p>
          </body>
        </html>
        """

        part = MIMEText(html, "html")
        message.attach(part)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
    else:
        print("same")

if __name__ == "__main__":
    url = "https://www.ema.europa.eu/en/homepage"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    href = "https://www.ema.europa.eu/"
    # print(soup.prettify())
    found = 0
    for tag in soup.find_all('a'):
        found = 1
        if found == 1 and tag.text == "What's new":
            link = tag.get('href')

    link = href + link

    Current_Date = today_date()
    # dates = extracting_date(url)
    data_count=extract_data(link)
    table_data=sending_data(link)
    if data_count:
        host = "10.140.189.165"
        database = "Internal"
        username = "postgres"
        password = "techsol"
        port = "5432"
        create_table(host, database,  username, password, port)
        result = getting_data(host, database, username, password, port)
        table_html=comparision(host, database, username, password, port)

        send_email(table_html,host, database,  username, password, port)
        insert_into_table(Current_Date, data_count, host, database, username, password, port)
        insert_into_table1(table_data, database, username, password, port)

        #print(result[0])
    else:
        print("No data found!")






























