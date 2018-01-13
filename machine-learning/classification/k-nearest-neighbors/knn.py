# Data Pre-processing

# Import essential libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the data set
dataset = pd.read_csv('PartOne_Data_Preprocessing/Data.csv')
# independent var vector
x = dataset.iloc[:, :-1].values  # All the : means all the line, :-1 means except last one
# Create dependent var vector
y = dataset.iloc[:, 3].values
print()

"""
How to handle missing data
    Replace the missing data with the mean or median or most frequent value of the column
"""
# Taking care of missing data
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(x[:, 1:3])  # imputer object is fitted to data set
x[:, 1:3] = imputer.transform(x[:, 1:3])
# print(x)

# Encode categorical variables
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

label_encoder_x = LabelEncoder()
x[:, 0] = label_encoder_x.fit_transform(x[:, 0])

one_hot_encoder = OneHotEncoder(categorical_features=[0])
x = one_hot_encoder.fit_transform(x).toarray()

# For dependent variable we need to use Label encoder
label_encoder_y = LabelEncoder()
y = label_encoder_y.fit_transform(y)

# print(x)
# print(y)

# Splitting the data set
from sklearn.cross_validation import train_test_split

x_train, x_test, y_train_, y_test = train_test_split(x, y, test_size=0.2, random_state=0)  # RS = 42
# print(len(x_train))

# Feature scaling Stadardisation, Normalisation
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
# do we need to transform the dummy variables? Depend on the context
# what about y_train and y_test ? we don't

print(x_train)
print(x_test)
