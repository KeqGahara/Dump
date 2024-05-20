import math

"""
##1
nom = input("Saisir votre nom ?")
print("Bienvenue", nom)

age = int(input("Saisir votre age?"))
print("Votre année de naissance est", 2023-age)

##2
somme = 0
for i in range(1,101):
    somme += i
print(somme)

somme = 0
for i in range(2,101,2):
    somme += i
print(somme)

##3
cel = int(input("Saisir la temperature en degré celsius"))
print("la convertion en ferhenheit est de ", cel*1.8+32)

##4
n = int(input("veuillez saisir un nombre"))
if n/2 == True :
    print ("le nombre est pair")
else:
    print ("le nombre est impair")

##5
for i in range(1,11):
    print(i)

##6
Fruits = ["banane","pomme","poire","orange"]
for i in Fruits:
    print(i)

##7
L = [54,2,65,1,3]
somme = 0
for i in L:
    somme += i
print("la somme des termes de la list est egale a", somme)
print("la medianne de la list est", L[2])
print("la moyenne est égale a", i/2)
"""
##8
def surface(r):
    """input: un rayon d'un cerlce
    output: la surface de ce cercle"""
    s = r**2*math.pi
    return(s)
##9
def listTri(L):
    """input: une liste de nombre
    output: cette liste triée par ordre croissant"""
    L.sort()
    return(L)

"""
##10

x = input("sassir un nombre")
if x!=int:
    print("Ceci n'est pas un NOMBRE!!")

##11
dico = {"Pierre":10,"Marco":35,"Polo":50}
for i in dico.items():
    print(i)
    
##12
notes = (17,10,12,14,20,8,9)
notes.list().sum()#INCOMPLET
"""
    