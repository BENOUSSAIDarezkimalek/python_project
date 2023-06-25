import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix


# importer la data
data=pd.read_csv('Produit_acheter.csv')
print(data.head())

# la colonne User ID ne vas pas nous servir dans ce cas car elle n'a aucune influence
data.drop(['User ID'],axis='columns',inplace=True)

# Transformer la variable Gender avec des valeurs numerique
data.Gender = data.Gender.map({'Male': 1, 'Female': 2})

#  affichage d'une projection 3d avec Gender
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.scatter(data.Gender,data.Age,data.EstimatedSalary, c=data.Purchased)
# plt.show()




# Influence du genre sur  l'achat
table= pd.crosstab(data.Gender,data.Purchased)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Genre / Achat')
plt.xlabel('Genre')
plt.ylabel('Pourcentage de client')
plt.show()

# Supprimer la colonne Gender
data.drop(['Gender'],axis='columns',inplace=True)

# Influence de l'age sur l'achat
table= pd.crosstab(data.Age,data.Purchased)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Age / Achat')
plt.xlabel('Age')
plt.ylabel('Pourcentage de client')
plt.savefig('Age-Achat')
plt.show()

# Influence du salaire estimé sur le salaire
table= pd.crosstab(data.EstimatedSalary,data.Purchased)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Salaire / Achat')
plt.xlabel('Salaire')
plt.ylabel('Pourcentage de client')
plt.show()

# visualiser le data set
print(data)

# Définir notre variable dépendante y et nos varaibles indépendantes X
X = data.iloc[:, [0, 1]].values
y = data.iloc[:, -1].values


# Visualisation des points
plt.scatter(X[:,0],X[:,1], c=y)
plt.show()

# Diviser le dataset entre le Training set et le Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


# Normalisation des données
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# Construction du modèle
classifier = LogisticRegression(random_state = 0, solver='liblinear')
classifier.fit(X_train, y_train)

# Faire de nouvelles prédictions
y_pred = classifier.predict(X_test)
print(y_pred)

# Verifie le taux de fiabilité des predictions
classifier.score(X_test,y_test)
print("Moyenne =",classifier.score(X_test,y_test))

# Matrice de confusion
cm = confusion_matrix(y_test, y_pred)
print(cm)


