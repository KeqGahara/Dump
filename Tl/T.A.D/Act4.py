# TAD Liste[T]
#
# Opérations
#       Vide : → Liste[T]
#       Cons : TxListe[T] → Liste[T]
#       estVide : Liste[T] → Booléen
#       supprEnTete : Liste[T] → T  
#       longueur : Liste[T] → Entier
#       tete : Liste[T] → T
#       queue : Liste[T] → Liste[T]
#       dernier : Liste[T] → T
#       concatener : Liste[T]xListe[T] → Liste[T]


def vide():
    """
    input: vide
    output: vide (Liste[T])
    """
    return None

def cons(x,L):
    """
    input: Un élément x et une Liste[T]
    output: Une Liste[T] avec l'élément x implémenter dans cette Liste[T] 
    """
    return[x,L]

def estVide(L):
    """
    input: Une liste[T]
    output: Un bool indiquant si la liste est vide ou pas 
    """
    return L is None
    
#Renvoyer la tête de la Liste L non vide
def tete(L):
    """
    input: Une liste[T]
    output: Son premier élément qui est une cons
    """
    assert not estVide(L)
    return L[0]  
    
#Renvoyer la Liste queue d'une liste L non vide
def queue(L):
    """
    input: Une liste[T]
    output: Le queue de cette Liste[T]
    """
    assert not estVide(L)
    return L[1]
    
#Supprimer la tête de la Liste et la renvoyer
def supprEnTete(L):
    """
    input: Une Liste[T]
    output: La tête de cette Liste[T]
    """
    assert not estVide(L)
    t=tete(L)
    q=queue(L)
    L.pop()
    L.pop()
    for a in q:
        L.append(a)
    return t
    
#Renvoyer la longueur de la Liste
def longueur(L):
    """
    input: Une liste[T]
    output: Un entier qui represente la longueur de celle-çi
    """
    if estVide(L):
        return 0
    else:
        return 1+longueur(queue(L))
#alternative du prof:
#n=0
#while not estVide(L):
#   n=+1
#   L=queue(L)
#return n
   
#Renvoyer le dernier élément d'une Liste non vide
def dernier(L):
    """
    input: Une liste[T]
    output: Le dernier élément de celle-çi
    """
    while not queue(L)==None:
        L=queue(L)
    return L[0]
        
#Renvoyer une liste Python contenant les éléments de L dans l'ordre inverse
def inverser(L):
    """
    input: Une Liste[T] 
    output: Une Liste[T] qui est l'inverse de la liste insérer
    """
    I=[]
    while not estVide(L):
        I.insert(0,L[0])
        L=queue(L)
    return I

#Concaténer deux Listes et renvoyer une nouvelle liste
#On pourra utiliser la fonction inverser

def concatener(L1,L2):
    """
    input: Deux Listes[T]
    output: Une liste[T], qui est la concaténation des deux Listes
    """
    assert type(L1) and type(L2)==list , "Les éléments L1 et L2 ne sont pas deux listes"
    return L1+L2

#Tests :
    
L = vide()
assert estVide(L)==True

L = cons(5, cons(4, cons(3, cons(2, cons(1, cons(0,L))))))
assert L==[5, [4, [3, [2, [1, [0, None]]]]]]
assert estVide(L)==False
assert tete(L)==5
assert queue(L)==[4, [3, [2, [1, [0, None]]]]]
assert longueur(L)==6
assert inverser(L)==[0,1,2,3,4,5]

x=supprEnTete(L)
assert x==5
assert L==[4, [3, [2, [1, [0, None]]]]]
"""
M=vide()
M=cons(8, cons(12, cons(7, cons(10,M))))
assert concatener(L,M)==[5, [4, [3, [2, [1, [0, [8, [12, [7, [10, None]]]]]]]]]]
"""