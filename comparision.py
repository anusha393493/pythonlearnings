import psycopg2
import requests
from bs4 import BeautifulSoup
import pandas as pd
import smtplib,ssl
import numpy as np
url1="https://www.w3.org/"
url2="https://www.google.com/"
response1=requests.get(url1)
response2=requests.get(url2)
soup1=BeautifulSoup(response1.content,'html.parser')
soup2=BeautifulSoup(response2.content,'html.parser')
t1=soup1.get_text()
t2=soup2.get_text()
if t1==t2:
    print("same!")
    comparision=("Both urls are  same")
else:
    print("not same")
    comparision=("Both urls are not same")





smtp_server="smtp.gmail.com"
port=587
sender_email="noreply.medinquirer@scimaxglobal.com"
password=input("enter your Password:")
receiver_email='rapolarjun@gmail.com'
message=comparision
context=ssl.create_default_context()
try:
  server=smtplib.SMTP(smtp_server,port)
  server.ehlo()
  server.starttls(context=context)
  server.ehlo()
  server.login(sender_email,password)
  server.sendmail(sender_email,receiver_email,message)
  print("sent successfully")
except Exception as e:
  print(e)
finally:
  server.quit()