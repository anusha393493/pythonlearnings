import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn import svm,datasets
from sklearn.model_selection import GridSearchCV
iris=datasets.load_iris

parameters={'kernel':('linear', 'rbf'), 'C':[1, 10]}
svc=svm.SVC()
clf=GridSearchCV(svc,parameters)
clf.fit(iris.data,iris.target)
GridSearchCV(estimator=SVC(),
             param_grid={'C': [1, 10], 'kernel': ('linear', 'rbf')})
#print(sorted(clf.cv_results_.keys()))
