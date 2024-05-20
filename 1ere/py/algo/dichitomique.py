from random import randint
def DevinerNombre(N):
    """
    In: N, un entier int
    Out: nbCoup, un entier int
    """
    n=randint(1,N)
    nc=1
    np=int(input('Proposer un nompbre entre 1 et '+str(N)+' '))
    while n!=np:
        if np>n:
            np=int(input('votre nombre est trop grand veuillez donner un nombre moin important '))
            nc+=1
        elif np<n:
            np=int(input('votre nombre est trop petit veuillez donner un nombre moin important '))
            nc+=1
        else :
            print('vous avez GAGNEZ !!!')
    return nc,n

def DevinerNombreAutomatique(N):
    """
    In: N, un entier int
    Out: nbCoup, un entier int
    """
    n=randint(1,N)
    nc=1
    s=1
    e=N
    np=(s+e)//2
    print('Proposer un nompbre entre 1 et '+str(N)+': '+str(np))
    while n!=np:
        if np>n:
            e=np
            np=(s+e)//2
            print('votre nombre est trop grand veuillez donner un nombre moin important que'+': '+str(np))
            nc+=1
        elif np<n:
            s=np
            np=(s+e)//2
            print('votre nombre est trop petit veuillez donner un nombre moin important que'+': '+str(np))
            nc+=1
        else :
            print('vous avez GAGNEZ !!!')
    return nc,n

def RechercheNombreBrut(N):
  nc=0
  n=randint(N)
  for i in range(N):
    if i!=n:
      nc+=1
    else :
      print("le nombre aleatoire a etait trouve en " +str(nc) + " coups")
      
def aleatrier(x) :
  n = []
  for i in range(x):
    n.append(randint(200))
  n.sort()

  return n

def rechercheDichotomique(A, x):
    """
    In: A une liste de int, x un int
    Out: xinA booléen
    """
    debut = 0
    fin = len(A) - 1
    
    while debut <= fin:
        milieu = (debut + fin) // 2
        
        if A[milieu] == x:
            return True
        
        elif A[milieu] > x:
            fin = milieu - 1
            
        else:
            debut = milieu + 1
            
    return False
'''
Pour une recherche séquentielle dans une liste de taille n, il faudrait en moyenne n/2 comparaisons pour trouver l'élément recherché, car en moyenne l'élément se trouve à la moitié de la liste.

En utilisant la recherche dichotomique, on divise la liste en deux à chaque itération, réduisant ainsi de moitié le nombre d'éléments à parcourir à chaque fois. Ainsi, le nombre de comparaisons pour une liste de taille n sera approximativement égal à log2(n). Par exemple, pour une liste de taille 64, on peut s'attendre à environ 6 comparaisons en utilisant la recherche dichotomique.

Voici le tableau rempli pour différentes tailles de liste :

Taille de la liste	1	2	4	8	16	32	64	128	N
Recherche séquentielle	1	2	4	8	16	32	64	128	n
Recherche dichotomique	1	1	2	3	4	5	6	7	log2(n)
La première ligne représente la taille de la liste en puissance de 2, allant de 20 à 27 (correspondant à une liste de taille 1 à 128). On remarque que le nombre de comparaisons pour la recherche séquentielle augmente linéairement avec la taille de la liste, alors que pour la recherche dichotomique, le nombre de comparaisons augmente logarithmiquement avec la taille de la liste. On peut donc constater que la recherche dichotomique est beaucoup plus efficace que la recherche séquentielle pour des listes de grande taille.
'''