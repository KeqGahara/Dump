def naive(motif,texte):
    ''' In : motif une chaine de caractère à chercher dans texte (le texte)
    Out : le nombre d'occurrences du mot cherché (0 si aucun)'''
    m=len(motif)
    n=len(texte)
    compteur=0
    assert m <= n
    for s in range(n-m+1) :
        if motif == texte[s:s+m]:
            compteur += 1
            print("Le motif est trouvé avec le décalage",s,
            ", nombre d'occurrences =", compteur)
    return compteur

'''
texte = 'QSFDSFQSDFSFQDFSFQSDFQSDFQSQFSDDFQDSFQSFQFDFQSDFDFFDFSFSFQDSFQDFSFQSFDSFQ'
motif = 'QFSD'
a=naive(motif,texte)
'''

def uneligne(motif,texte):
    ''' In : motif une chaine de caractère à chercher dans texte (le texte)
    Out : bool qui indique si le motif est dans le texte (n'indique ni le nombre d'occurance ni le décalage)'''
    return motif in texte

def native(motif,texte):
    ''' In : motif une chaine de caractère à chercher dans texte (le texte)
    Out : le nombre d'occurrences du mot cherché (0 si aucun)'''
    assert len(texte)>= len(motif)
    print("Le motif est trouvé avec le décalage",texte.find(motif),
            ", nombre d'occurrences =", texte.count(motif))
    return texte.count(motif)


texte = 'QSFDSFQSDFSFQDFSFQSDFQSDFQSQFSDDFQDSFQSFQFDFQSDFDFFDFSFSFQDSFQDFSFQSFDSFQ'
motif = 'QFSD'
texte.find(motif)
a = native(motif,texte)

def bmh(texte, motif):
    '''In : texte et motif des chaines de caractères
    Out : une liste de la position des occurrences du motif dans le texte'''
    assert len(texte)>= len(motif)
    size = len(texte) # On récupère la taille de chaque chaine,
    taille = len(motif) 
    positions = [] # Création d'une liste pour récupérer les positions des motifs trouvés
    if(taille<=size): # Si la taille du motif est inférieur ou égale à celle du texte
        decalage = table_sauts(motif) #Remplissage de la liste: création de la table des sauts
        i=0
        compteur=0
        trouve=False # variable booleenne qui vaut True si on a trouvé un mot
        while(i<=size-taille): # tant que l'indice i est inférieur à la taille du texte moins celle du motif
            for j in range (taille-1,-1,-1): # On teste en partant de la droite la correspondance des caractères du motif avec ceux du texte
                compteur=compteur+1
                trouve=True
                if(texte[i+j]!=motif[j]):
                    if(texte[i+j] in decalage and decalage[texte[i+j]]<=j):
                        i+=decalage[texte[i+j]]
                    else:
                        i+=j+1 # Décalage du reste du motif
                    trouve=False
                    break
                if(trouve): # Si tous les caractères correspondent
                    positions.append(i) # On ajoute la position de la portion du texte
                    i=i+1 # On décale de 1
                    trouve=False # on reinitialise la variable
        print(size," ", compteur) #On affiche toutes les positions trouvées
    return positions

def horspool(texte, motif):
    '''In : texte et le motif à chercher
    Out : nombre d'occurrences, position et nombres de tests effectués'''
    size = len(texte) # On récupère la taille de chaque chaîne
    taille = len(motif)
    occurences = [] # Création d'une liste pour récupérer les positions des motifs trouvés dans le texte
        if(taille<=size): # Si la taille du motif est inférieur ou égale à celle du texte
        tab = [] # Création d'une liste de dictionnaire
        #*******Tables Sauts*******
        # tab va contenir toutes les tables de sauts sous forme de dictionnaires
            for j in range(taille):
                decalage = {}
                for i in range(taille-1-j):
                    decalage[motif[i]]=taille-1-j-i
                decalage[0]=taille-j
                tab.append(decalage) # Remplissage de la liste: création de la table des sauts
            #***************************
            for t in range(len(tab)):
                print(tab[t]) # On affiche la table des sauts
            i=0
            compteur=0
            trouve=False
            while(i<=size-taille): # Tant que l'indice i est inférieur à la taille du texte moins celle du motif avec ceux du texte
                for j in range(taille-1,-1,-1): # On teste en partant de la droit la correspondance des caractères du motif
                    compteur=compteur+1 # On compte le nb de tests
                    trouve=True
                    if(texte[i+j]!=motif[j]): # Si les caractères ne correspondent pas
                        if(texte[i+j] in tab[taille-j-1]): #Si le caractère testé dans le texte est dans le reste du motif
                            i=i+tab[taille-j-1][texte[i+j]]
                        else:
                            i=i+tab[taille-j-1][0]
                        trouve=False
                        break
                if(trouve): # Si tous les caractères correspondent
                    occurences.append(i) # On ajoute la position de la portion du texte
                    i=i+1 # On décale de 1
                    trouve=False
    return len(occurences),occurences,compteur #On affiche toutes les positions trouvées

def table_sauts(motif):
    '''In : motif une chaine de caractère
    Out : un dictionnaire avec les positions des caractères du motif dans le motif'''
    tab = {} # Création d'un dictionnaire
    for i in range(len(motif)-1): # On parcourt le motif
        tab[motif[i]]=len(motif)-i-1 # On remplit le dictionnaire avec les positions des caractères du motif dans le motif
    return tab