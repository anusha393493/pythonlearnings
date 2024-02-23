import requests
from bs4 import BeautifulSoup
r=requests.get('https://www.geeksforgeeks.org/python-programming-language/')
#print(r.content)
#print(r.url)
#print(r.status_code)
soup=BeautifulSoup(r.content,'html.parser')
#print(soup.prettify())
#print(soup.title)
#print(soup.title.name)
#print(soup.title.parent.name)
#s=soup.find('div',class_='entry-content')
#content=s.find_all('p')
#print(s)
#print(content)
#s=soup.find('div',id='main')
#leftbar=s.find('ul',class_='leftBarList')
#content=leftbar.find_all('li')
#print(content)
#for line in content:
#    print(line.text)
for link in soup.find_all('a'):
    print(link.get('href'))
