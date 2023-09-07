#Importing libraries 
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

#Importing dataset
dataset = pd.read_csv('iris.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

#Encoding the dependent variable
le = LabelEncoder()
y = le.fit_transform(y)

#Splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

#Training the svm model on the training set
from sklearn.svm import SVC
classifier = SVC()
classifier.fit(X_train, y_train)

#Saving model to current working directory
pickle.dump(classifier, open('model.pkl','wb'))





