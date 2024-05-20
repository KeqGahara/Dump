def indice_max_tableau(t):
    #Cette fonction renvoie l'indice de la valuer maximale de la liste affecter.
    """ ceci est une fonction qui donne l'indice du maximum d'une liste, elle prends en entrée une liste, et donne un entier """
    assert len(t) > 0, 'la liste est vide, elle admet donc pas de maximum !!!'
    m = 0
    if len(t) != 0:
        for i in range (len(t)):
            if t[i] > t[m]:
                m = i
        return m

