# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encode categorical variables
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

label_encoder_x = LabelEncoder()
x[:, 3] = label_encoder_x.fit_transform(x[:, 3])

one_hot_encoder = OneHotEncoder(categorical_features=[3])
x = one_hot_encoder.fit_transform(x).toarray()

print(x)

# Avoiding dummy variable trap
x = x[:, 1:]  # have to remove one dummy variable away, you don't need all three states

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Fit multiple Linear Regression to the training set
from sklearn.linear_model import LinearRegression

regression = LinearRegression()
regression.fit(X_train, y_train)

# Predicting the Test set result
y_predict = regression.predict(X_test)

print("Real profits: ")
print(y_test)
print()
print("Predicted Profits by the model")
print(y_predict)
