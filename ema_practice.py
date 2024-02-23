from tabulate import tabulate
import psycopg2
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date

def today_date():
    return date.today().strftime('%d/%m/%Y')

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
        sql_query = """
            SELECT * FROM EMA_Data
            WHERE CurrentDate=(SELECT MAX(CurrentDate) FROM EMA_Data);
        """
        cursor.execute(sql_query)
        result = cursor.fetchone()
        connection.commit()
        cursor.close()
        connection.close()
        return result
    except psycopg2.Error as error:
        print("Error while connecting to PostgreSQL or executing query:", error)

def comparison(host, database, username, password, port):
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
        rows = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]
        table = tabulate(rows, headers=col_names, tablefmt="html")
        connection.commit()
        cursor.close()
        connection.close()
        return table
    except psycopg2.Error as error:
        print("Error while connecting to PostgreSQL or executing query:", error)

def send_email(table_html):
    sender_email = "noreply.medinquirer@scimaxglobal.com"
    receiver_email = 'rnvanusha@gmail.com'
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

if __name__ == "__main__":
    host = "10.140.189.165"
    database = "Internal"
    username = "postgres"
    password = "techsol"
    port = "5432"

    table_html = comparison(host, database, username, password, port)
    send_email(table_html)
