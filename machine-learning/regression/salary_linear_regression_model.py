# Data Pre-processing

# Import essential libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the data set
dataset = pd.read_csv('Salary_Data.csv')
# independent var vector
x = dataset.iloc[:, :-1].values  # All the : means all the line, :-1 means except last one
# Create dependent var vector
y = dataset.iloc[:, 1].values

# Splitting the data set
from sklearn.cross_validation import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1 / 3, random_state=0)  # RS = 42
# print(len(x_train))

# Feature scaling Stadardisation, Normalisation

# Fitting Linear regression to the training set
from sklearn.linear_model import LinearRegression

linear_regressor = LinearRegression()  # Just creating a simple linear regression model
linear_regressor.fit(x_train, y_train, sample_weight=None)  # include IV and DV
# ^The model has Learned co-relation between salary and experience

# Predict the Test set results
y_predict = linear_regressor.predict(x_test)  # vector of predictions
print("Real salary:")
print(y_test)
print("Model Predicted Salary: ")
print(y_predict)

# visualizing the training set results
plt.scatter(x_train, y_train, color='red')  # Scatter plot on real salary
plt.plot(x_train, linear_regressor.predict(x_train), color='blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# visualizing the new data set results (test set)
plt.scatter(x_test, y_test, color='red')  # Scatter plot on real salary
plt.plot(x_train, linear_regressor.predict(x_train), color='blue')  # using learned model
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
