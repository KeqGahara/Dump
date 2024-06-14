import random
import time
import matplotlib.pyplot as plt 
# Exercice 1 :
def minimal(A):
    """
    in : une liste A  de nombres
    out : un tuple qui renvoye le minimum A et son indice
    """
    for i in range (len(A)-1):
        r=A[0+i]
        l=A[1+i]
        if r >= l:
            minimum = l
        else :
            minimum = r
    return (minimum, A.index(minimum))

# Exercice 2 et 3 :
def tri_selection(A):
    for i in range(len(A)-1):
        m = i
        for j in range(i+1, len(A)):
            if A[j] < A[m]:
                m = j
        A[i], A[m] = A[m], A[i]
    return A
# Exercice 4 :
def tri_par_selection(A): #incomplet; r == false
    """
    in : une liste A de nombres
    out : une liste triée de nombres
    """
    i = list(range(len(A)))
    r = minimal(A[i:])
    for i in range (len(A)):
        min_value, min_index = r
        A[i], A[i+min_index] = A[i+min_index], A[i]
    return A

# Exercice 5 :
def alea(i):
    """
    In : i un entier, la taille du tableau
    Out : une liste de i entiers de 0 à 100
    """
    L = [str(random.randrange(1,100)) for j in range(i)]
    return L

def TempsAlgo(i):
    """
    In : i un entier, la taille du tableau
    Out : le temps mis par l'algorithme de tri par séléction
    """
    A = alea(i)
    a = time.time()
    tri_selection(A)
    d = time.time()-a
    return d
for i in range (1000,10000,1000):
    Temps = [str(TempsAlgo(i))]
    Taille = [str(i)]

plt.title("Complexite tri par selection")
plt.plot(Taille,Temps)#On trace la figure les tailles en abscisse,

#les temps en ordonnées

plt.xlabel("Taille liste")
plt.ylabel("Temps")
plt.show() #On montre le graphe.
