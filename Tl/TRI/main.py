# Tri par sélection :

def mini(A):
    min = A[0]
    indice  = 0
    for i in range(len(A)-1):
        if min > A[i+1]:
            min = A[i+1]
            indice = i + 1
    return (min,indice)

def Tri_Par_Selection(A):
    for i in range(len(A)):
        minimum,indice = mini(A[i:])
        if minimum < A[i]:
            A[i],A[indice+i] = A[indice+i],A[i]
    return A

# Tri par sélection :

def insertion(t,i):
    '''
    IN : liste de int, float ou str. i = int
    OUT : liste de int, float, str.
    Insertion de t[i] dans t[0...i[.
    '''
    m = t[i]
    while i > 0 and m < t[i-1]:
        t[i] = t[i-1]
        i -= 1
    t[i] = m
    return t


def Tri_Par_Insertion(t):
    '''
    IN : liste de int, float, str.
    OUT : liste de int, float, str.
    Tri croissant de t par insertion.
    '''
    for i in range(1,len(t)):
        insertion(t,i)
    return t

# Tri fusion, "diviser pour régner" :

def fusion(T1,T2):
    '''
    IN : Deux listes de int, float, str.
    ATTENTION ces Deux listes doivent avoir des éléments de même type
    OUT : liste de int, float, str.
    Fusion de deux listes T1 et T2.
    Ordre brute, c'est à dire qu'on initialise au premier élément le plus petit pour ensuite effectuer un tri croissant du reste de T1 et T2.
    '''
    assert type(T1) == list
    assert type(T2) == list

    if T1==[]: 
        return T2
    if T2==[]:
        return T1
        # Ces deux conditions if vérifient si l'une des listes est vide
        # Elles servent aussi de cas initial pour l'appel recursive 
    if len(T1)<len(T2):
        for i in range(len(T1)):
            assert type(T1[i])==type(T2[i])
        for j in range(len(T2)-len(T1)-1):
            assert type(T1[j])==type(T1[0])
    elif len(T1)==len(T2):
        for i in range(len(T1)):
            assert type(T1[i])==type(T2[i])
    else :
        for i in range(len(T2)):
            assert type(T1[i])==type(T2[i])
        for j in range(len(T1)-len(T2)-1):
            assert type(T2[j])==type(T2[0])
        # Ces asserts vérifient si les éléments des deux listes a fusionner sont de même type (car la fonction ne marche pas si les elements des deux listes n'ont pas le même type)

    if T1[0]<T2[0]:
        # Determination de l'ordre d'operations, c'est à dire le sens du découpage 
        return [T1[0]]+fusion(T1[1:],T2)
            # Premier cas (appel recursive)
    else:
        return[T2[0]]+fusion(T1,T2[1:])
            # Deuxième cas (appel recursive)

def trifusion(T) :
    '''
    IN : liste de int, float, str.
    OUT : liste de int, float, str.
    Tri croissant de T par fusion.
    '''
    assert type(T) == list
    if len(T)<=1 :
        return T
            # Le cas de base pour la recursion 
    T1=[T[x] for x in range(len(T)//2)]
    T2=[T[x] for x in range(len(T)//2,len(T))]
        # L'action de découpage
    return fusion(trifusion(T1),trifusion(T2))
        # L'action de fusion (l'appel recursive)


if __name__ == "__main__":
    L1 = [2,1,3]
    print('L1 =',L1)
    L2 = [6,5,4]
    print('L2 =', L2 ,'\n','Le trifusion de L2 est : ',trifusion(L2))
    L3 = fusion(L1,L2)
    print('L3 fusion de L1 et L2 :',L3,'\n','Le trifusion de L3 est : ',trifusion(L3))
