'''
#from urllib.request import urlretrieve
from six.moves import urllib
#url=r"https://fis.fda.gov/content/Exports/faers_ascii_2023Q4.ZIP"
#urlretrieve(url)
urllib.request.urlretrieve(r"https://fis.fda.gov/content/Exports/faers_ascii_2023Q4.ZIP")
'''
import pandas as pd
df=pd.read_csv(r"C:\Users\anusha.raparthi\Desktop\RPSR23Q4.csv")
print(df)