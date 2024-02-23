import feedparser
import psycopg2

url="https://classic.clinicaltrials.gov/ct2/results/rss.xml?rcv_d=14&lup_d=&sel_rss=new14&count=10000"
feed=feedparser.parse(url)
#print(feed)
#print(feed.feed.summary)

for entry in feed.entries:
    print("Entry Title:", entry.title)
    print("Entry Link:", entry.link)
    print("Entry Published Date:", entry.published)
    print("Entry Summary:", entry.summary)
    print("\n")
'''

def extract_data(feed):
  for entry in feed.entries:
      title=entry.title
      link=entry.link
      published=entry.published
      summary=entry.summary
  print(title,link,published,summary)



if __name__ == "__main__":
    host = "10.140.189.165"
    database = "Internal"
    username = "postgres"
    password = "techsol"
connection = psycopg2.connect(
    host=host,
    database=database,
    user=username,
    password=password
)
cursor = connection.cursor()
sql_query = """
            CREATE TABLE IF NOT EXISTS RSS (
                    title VARCHAR,
                    link VARCHAR,
                    published VARCHAR,
                    summary VARCHAR
                );
            """
cursor.execute(sql_query)
connection.commit()
title,link,published,summary=extract_data(feed)
print(title,link,published,summary)

'''
