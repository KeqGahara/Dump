import csv
import matplotlib.pyplot as plt

fichier=open("nouveauFichier.csv")
iris=list(csv.DictReader(fichier,delimiter=","))


X_iris_0=[float(ligne['longueur_petale']) for ligne in iris
            if ligne['espece']=='setosa']
Y_iris_0=[float(ligne['largeur_petale']) for ligne in iris
            if ligne['espece']=='setosa']
X_iris_1=[float(ligne['longueur_petale']) for ligne in iris
            if ligne['espece']=='versicolor']
Y_iris_1=[float(ligne['largeur_petale']) for ligne in iris
            if ligne['espece']=='versicolor']
X_iris_2=[float(ligne['longueur_petale']) for ligne in iris
            if ligne['espece']=='virginica']
Y_iris_2=[float(ligne['largeur_petale']) for ligne in iris
            if ligne['espece']=='virginica']
fichier.close()

plt.figure()
plt.scatter(X_iris_0, Y_iris_0, color='g', label='setosa',s=20 ,marker='*')
plt.scatter(X_iris_1, Y_iris_1, color='r', label='versicolor',s=20 ,marker='.')
plt.scatter(X_iris_2, Y_iris_2, color='b', label='virginica',s=20 ,marker='+')
plt.scatter(2, 0.5, color='orange',s=20 ,marker = '^')
plt.scatter(2.5, 0.75, color='purple', s=20 ,marker = 'v')
plt.legend()
plt.xlabel('Longueur des pétales')
plt.ylabel('Largeur des pétales')
plt.show()
plt.savefig('plot.png')

def knn(liste_dico, k, longueur, largeur):
    '''In : liste de dictionnaires (ici iris), le paramètre k
        et la longueur et largeur de l'iris à tester
    Out : une liste des k plus proches voisins
    '''
    L = []
    xb = longueur
    yb = largeur
    for dico in liste_dico:
        # Calcule de la distance entre le point (longueur, largeur)
        # et le point dans le dictionnaire
        xa = dico['longueur_petale']
        ya = dico['largeur_petale']
        distance = ((float(xa) - float(xb)) ** 2 + (float(ya) - float(yb)) ** 2) ** 0.5

        # Ajouter le tuple (distance, dico) à la liste L
        L.append((distance, dico))

    # Trier la liste L par rapport à la distance
    L = sorted(L, key=lambda x: x[0])

    # Récupérer les k plus proches voisins
    voisins = [t[1] for t in L[:k]]

    return voisins

def decision(liste_dico,k,longueur,largeur):
    '''In : liste de dictionnaires (ici iris), le paramètre k
        et la longueur et largeur de l'iris à tester
    Out : l'espèce attribuée'''
    '''L = knn(liste_dico,k,longueur,largeur)'''




