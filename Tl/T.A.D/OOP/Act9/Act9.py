from Pile_tete_queue import Pile

# Exercice 1

def inverser_pile(P):
    pile_aux = Pile()   

    while not P.estvide():
        pile_aux.empiler(P.depiler())  

    return pile_aux

# Test sur la pile 2, 8, 13, 1, 5

P = Pile()
P.empiler(2)
P.empiler(8)
P.empiler(13)
P.empiler(1)
P.empiler(5)
print("Pile initiale:",P)

P_inverse = inverser_pile(P)
print("Pile inversée:", P_inverse)


# Exercice 2

def deplacer_paires_impairs(P1):
    P2 = Pile()  
    pile_paires = Pile()  

    while not P1.estvide():
        element = P1.depiler()
        if element % 2 == 0:
            pile_paires.empiler(element)  
        else:
            P2.empiler(element)  

    while not pile_paires.estvide():
        P2.empiler(pile_paires.depiler())  

    return P2

P1 = Pile()
P1.empiler(2)
P1.empiler(9)
P1.empiler(13)
P1.empiler(12)
P1.empiler(5)
P1.empiler(8)
P1.empiler(3)
P1.empiler(6)
print("Pile P1:", P1)

P2 = deplacer_paires_impairs(P1)
print("Pile P2:", P2)
