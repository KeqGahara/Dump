from ArbreBinaire import *

# Parcours dit "Gauche-Racine-Droite"
def PP_INF(T):
    if T != None:
        PP_INF(T.gauche)
        print(T.cle,end="/")
        PP_INF(T.droite)

# Parcours dit "Racine-Gauche-Droite"
def PP_PREF(T):
    if T != None:
        print(T.cle,end="/")
        PP_PREF(T.gauche)
        PP_PREF(T.droite)
        
# Parcours dit "Gauche-Droite-Racine"
def PP_SUF(T):
    if T != None:
        PP_SUF(T.gauche)
        PP_SUF(T.droite)
        print(T.cle,end="/")

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

# Tests =
print("Parcours en profondeur INFIXE de T = ")
PP_INF(T)
print('\n')
print("Parcours en profondeur PREFIXE de T = ")
PP_PREF(T)
print('\n')
print("Parcours en profondeur SUFFIXE de T = ")
PP_SUF(T)