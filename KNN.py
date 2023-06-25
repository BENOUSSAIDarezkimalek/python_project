import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split



# Importer notre data set
dataframe= pd.read_csv("Iris.csv")

X = dataframe.iloc[:, 1:5]
Y = dataframe.iloc[:, 5]

X_train, X_test, y_train, y_test = train_test_split(X,Y,train_size=0.7,random_state=5)
monmodel = KNeighborsClassifier(n_neighbors=3)
monmodel.fit(X_train, y_train)
y_pred = monmodel.predict(X_test)
accuracy=metrics.accuracy_score(y_test, y_pred)


#variable pour la moyenne accuracy
print("la moyenne des resultats justes",accuracy )

#test sur un nouveau jeu de donées
sample = [[5, 5, 3, 2], [2, 4, 3, 5]]
#
print("\n les Prédictions pour le nouveau jeu de donnees:\n", "     ",monmodel.predict(sample))


# Affichage des resultats
plt.figure(figsize=(8 , 6))
plt.scatter(X[Y == 'Iris-setosa'].iloc[:, 0], X[Y == 'Iris-setosa'].iloc[:, 2],  label='Iris-setosa',color='g',s=35,marker='2',alpha=0.8 )
plt.scatter(X[Y == 'Iris-versicolor'].iloc[:, 0], X[Y == 'Iris-versicolor'].iloc[:,2],label='Iris-versicolor', color='b',s=25,marker='x',alpha=0.8)
plt.scatter(X[Y == 'Iris-virginica'].iloc[:, 0], X[Y == 'Iris-virginica'].iloc[:, 2],label='Iris-virginica', color='orange',s=25, marker='^',alpha=0.8)
plt.legend(["Iris-setosa", "Iris-versicolor","Iris-virginica"],loc ="lower right", shadow='bool')
plt.grid(alpha=0.2)
plt.xlabel('la longueur des sépales')
plt.ylabel('la longueur des pétales')
plt.title('nuage de points representant la longueur \n des petales et des sépales de chaque  espèces d iris')
plt.show()
