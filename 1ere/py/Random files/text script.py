"""

explication :
liste un nom comme une vraiable mais contiens ensemble de valuer modifiable chaque valeur a l'interieur tiens un rang de 0 a N
tuble un nom comme une vraiable mais contiens ensemble de valuer non modifiable chaque valeur a l'interieur tiens un rang de 0 a N
append ajouter au dernier rang (liste)
insert ajouter au rang selectionner (liste)
pop retirer le rnag choisis (liste)
index apres insertion d'une valeur , donner le rang de la valeur dans dite liste / tuple

# Exercice 1 :

a=(4,5,6)
b=a[2]
print(a)
print(b)

"""

# Exercice 3.1 :

def multiple1(n):
    l=[]
    for i in range (1,11):
        l.append(i*n)
    return l

# Exercice 3.2 :

def multiple2(n):
    l=[]
    i=1
    while i*n < 1000:
        l.append(i*n)
        i = i+1
    return l

# Exercice 3.3 :

def diviseur(n):
    l=[]
    for i in range(1,1+n):
        if n%i==0:
            l.append(i)
    return l

# Exercice 4 :

def produit(l,n): # l est une liste et n un entier
    l2=[]
    for i in range(len(l)):
        l2.append(l[i]*n)
    return l2 # l2 est une liste

"""
ma_liste=[2,5,19,-3,42]
n=3
produit(ma_liste,n)
print(produit(ma_liste,n))
"""

# Exercice 5 :

def mystere(liste1,liste2):
    liste=[]
    i,j=0,0
    while i<len(liste1) and j<len(liste2):
        if liste1[i]<liste2[j]:
            liste.append(liste1[i])
            i=i+1
        else:
            liste.append(liste2[j])
            j=j+1
    return liste

# Exercice 6 :

def maxi(a,b,c):
    tup=tuple(sorted((a,b,c)))
    d=tup[-1]
    return d

# Exercice 7 :

def ville(a,b):
    for c in positions.keys():
        if abs(c[0]-a)<0.001 and abs(c[1]-b)<0.001:
            print(positions[c])

ville(36.8185 , 10.1651)
Tunis










