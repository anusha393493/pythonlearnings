import feedparser
import psycopg2

url="file:///C:/Users/anusha.raparthi/AppData/Local/Temp/09652dc5-cf02-47fc-8b91-f1e80bd509b9_faers_xml_2023Q3.zip.9b9/XML/1_ADR23Q3.xml"
feed=feedparser.parse(url)
#print(feed)
#print(feed.feed.summary)

for entry in feed.entries:
    print("Entry Summary:", entry.summary)
    print("\n")