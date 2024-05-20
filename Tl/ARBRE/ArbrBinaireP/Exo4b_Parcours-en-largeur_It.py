from ArbreBinaire import *
from File import *

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

def ParcoursLargeur(T):
    if T == None:
        return
    f = File()
    f.enfiler(T)
    while not f.estVide():
        x = f.defiler()
        assert x is not None 
        print(x.get_cle(),end = "/")
        if x.get_gauche() is not None:
            f.enfiler(x.get_gauche())
        if x.get_droite() is not None:
            f.enfiler(x.get_droite())



# Test de cette version itérative =
print("Parcours en largeur de T = ")
ParcoursLargeur(T)