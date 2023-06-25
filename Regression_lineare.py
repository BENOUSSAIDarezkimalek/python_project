import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt



data = pd.read_csv('Salary_Data.csv')
# print(data)
X = data.iloc[:,0]
Y = data.iloc[:,1]

Y = Y.values.reshape(Y.shape[0],1)
X = X.values.reshape(X.shape[0],1)
# print(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
model = LinearRegression()
model.fit(X_train, Y_train)
Y_pred = model.predict((X_test))
print(Y_pred)
plt.scatter(X, Y, c='g')
plt.plot(X_test, Y_pred, c="blue")
plt.show()