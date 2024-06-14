from ArbreBinaire import *

T = ArbreBinaire("A")
T.insert_gauche("B")
T.insert_droite("F")
n2 = T.get_gauche()
assert n2 is not None 
n2.insert_gauche("C")
n2.insert_droite("D")
n3 = T.get_droite()
assert n3 is not None 
n3.insert_gauche("G")
n3.insert_droite("H")
n4 = n2.get_gauche()
assert n4 is not None 
n4.insert_droite("E")
n6 = n3.get_gauche()
n7 = n3.get_droite()
assert n6 is not None 
n6.insert_gauche("I")
assert n7 is not None 
n7.insert_droite("J")
affiche(T)

def hauteur(T):
    if T != None:
        return 1 + max(hauteur(T.gauche),hauteur(T.droite))
    else:
        return 0

def ParcoursLargeur(T):
    h = hauteur(T)
    for n in range(1,h+1):
        AfficheNiveau(T,n)

def AfficheNiveau(T,niveau):
    if T == None:
        return
    elif niveau == 1:
        print(T.get_cle(),end="/")
    else:
        AfficheNiveau(T.get_gauche(),niveau-1)
        AfficheNiveau(T.get_droite(),niveau-1)

# Test de cette version récursive =
print("Parcours en largeur de T = ")
ParcoursLargeur(T)