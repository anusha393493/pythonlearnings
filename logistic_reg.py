import numpy as np
from sklearn import linear_model
x=np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
y=np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
#print(x)
logr=linear_model.LogisticRegression()
logr.fit(x,y)
predicted=logr.predict(np.array([7.46]).reshape(-1,1))
print(predicted)
log_odds=