# Import scikit learn
from sklearn import datasets
import pandas as pd
# Load data
iris= datasets.load_iris()
# Print shape of data to confirm data is loaded
#print(iris)
df=pd.DataFrame(iris)