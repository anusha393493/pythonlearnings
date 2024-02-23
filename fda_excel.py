import csv
import pandas
import pandas as pd

filepath1=r"C:\Users\anusha.raparthi\Desktop\RPSR23Q4.txt"
filepath2=r"C:\Users\anusha.raparthi\Desktop\OUTC23Q4.txt"
with open(filepath1,'r') as file:
    content=file.read()
data=content.split('$')
data=[item.strip() for item in data if item]
df1=pd.DataFrame(data)
excel1=r"C:\Users\anusha.raparthi\Desktop\texttoexcel.xlsx"
df1.to_excel(excel1)


with open(filepath2,'r') as file:
    content=file.read()
data=content.split('$')
data=content.split('$')
data=[item.strip() for item in data if item]
df2=pd.DataFrame(data)
excel2=r"C:\Users\anusha.raparthi\Desktop\texttoexcel2.xlsx"
df2.to_excel(excel2)


