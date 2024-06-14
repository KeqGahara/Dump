"""class Maillon:

    def __init__(self,val,suiv=None):
        self.valeur = val
        assert type(suiv) == Maillon or suiv is None
        self.suiv = suiv

    def get_valeur(self):
        return self.val

    def get_suivant(self):
        return self.suiv

    def set_valeur(self,v):
        self.val=v

    def set_suivant(self,s):
        assert type(s)==Maillon or type(s) is None
        self.suiv=s


class ListeC:

    def __init__(self,tete=None):
        assert type(tete)==Maillon or tete is None
        self.tete=tete

    def __getitem__(self, i):
        m=self.tete
        for _ in range(i):
            if m is None:
                raise IndexError("Index out of range")
            m=m.suiv
        if m is None:
            raise IndexError("Index out of range")
        return m.valeur

    def estVide(self):
        return self.tete is None

    def ajouter_debut(self,M):
        M.suiv=self.tete
        self.tete=M

    def ajouter_fin(self,M):
        m=self.tete
        while m is not None and m.suiv is not None:
            m=m.suiv
        if m is None:
            self.tete=M
        else:
            m.suiv=M

    def ajouter_apres(self, M, N):
            m = self.tete
            while m != N:
                m = m.suiv
            M.suiv = N.suiv
            N.suiv = M

    def supprimer_debut(self):
        assert not self.estVide()
        t = self.tete
        self.tete = self.tete.suiv
        return t

    def supprimer_apres(self,M):
        assert not self.estVide()
        m=self.tete
        while m!=M:
            m=m.suiv
        n=m.suiv
        m.suiv=m.suiv.suiv
        return n.val

    def get_maillon_indice(self, i):
        m = self.tete
        for _ in range(i):
            if m is None:
                return None
            m = m.suiv
        if m is None:
            return None
        return m

    def longueur(self):
        m=self.tete
        l1=0
        while m is not None:
            l1+=1
            m=m.suiv
        return l1

    def longueur_recursive(self):
        l1=ListeC(self.tete)
        if self.tete is None:
            return 0
        else:
            l1=ListeC(self.tete.suiv)
            return 1+l1.longueur_recursive()

    def afficher(self):
         l1=[]
         for k in range(self.longueur()):
             l1.append(self[k])
         print(l1)

'''
#troll Verz: (the_not_serious_one)

    def __init__(self,tete=None):
        assert type(tete) == Maillon or tete == None
        self.tete=[]

    def ajouter_debut(self,M):
        self.tete.insert(0,M.valeur)

    def ajouter_fin(self,M):
        self.tete.append(M.valeur)

    def ajouter_apres(self,M,N):
        self.tete.insert(N.suiv,M.valeur)

    def supprimer_debut(self):
        self.tete.remove(0)

    def supprimer_fin(self):
        self.tete.pop()

    def supprimer_apres(self,M):
        self.tete.remove(M.suiv)

    def longueur(self):
        if self.estVide():
            return 0
        else:
            for i in self.tete:
                return i

    def __str__(self):
        char=[]
        for i in self.tete:
            char.append(str(i))
        return str(char)

    def __repr__(self):
        char1=[]
        for j in self.tete:
            char1.append(str(j))
        return str(char1)    
'''


#Test:
L=ListeC()
M1=Maillon(1)
M2=Maillon(2,M1)
M3=Maillon(3,M2)
L.ajouter_debut(M1)
L.ajouter_debut(M2)
L.ajouter_debut(M3)
L.afficher()
print(L.estVide())
print(L.longueur())
print(L.get_maillon_indice(2))"""

# On peut implémenter un maillon de liste chaînée en Python à l’aide d’une classe Maillon :


class Maillon:

    def __init__(self,val,suiv=None):
        self.val = val
        assert type(suiv)==Maillon or suiv==None
        self.suiv = suiv #Son attribut suiv est de type Maillon, ou bien vaut None si le maillon est le dernier de la liste chainée

    def get_valeur(self):
        return self.val

    def get_suivant(self):
        return self.suiv

    def set_valeur(self,v):
        self.val=v

    def set_suivant(self,s):
        assert type(s)==Maillon or type(s)==None
        self.suiv=s

    def __repr__(self):
        return str(self.val)

# On peut implémenter une liste chaînée à l'aide d'une classe ListeC définie par un maillon qui représente sa tête :

class ListeC:

    def __init__(self,tete=None):
       #Son attribut tete est de type Maillon, ou bien vaut None si la liste est vide.
        assert type(tete)==Maillon or tete==None
        self.tete = tete

    def est_vide(self):
        return self.tete is None

    def longueur(self): 

        m = self.tete
        l = 0 
        while m is not None:
            l += 1
            m = m.suiv
        return l

# Version récursive de la longueur
    def longueur_recursive(self):
        l=ListeC(self.tete)
        if self.tete==None:
            return 0
        else:
            l=ListeC(self.tete.suiv)
            return 1+l.longueur_recursive()

# Renvoie Maillon d'indice i dans la liste L

    def get_maillon_indice(self, i):
        assert i < self.longueur()

        j = 0
        m = self.tete 
        while j < i:
            j += 1
            m = m.suiv
        return m

    def __getitem__(self, i):
        '''
        Permet d'utiliser les fonctions de python et d'accéder
        aux éléments d'une liste directement par Liste[i]
        '''
        return self.get_maillon_indice(i).val

# Ajouter le Maillon M au début de la liste  
    def ajouter_debut(self,M):
        M.suiv=self.tete
        self.tete=M

# Ajouter le maillon M en queue de la liste : équivalent de append
    def ajouter_fin(self, M):
        M.suiv=None
        m = self.tete
        if m is None:
            self.tete=M
        else:
            while m.suiv is not None:
                m = m.suiv
            m.suiv = M

# Ajouter le maillon N après le maillon N dans la liste
    def ajouter_apres(self, M, N):
        N.suiv = M.suiv
        M.suiv = N

#Insérer une valeur après l'élement d'indice i
    def inserer(self,i,v):
        assert i > 0
        M=Maillon(v)
        self.ajouter_apres(self.get_maillon_indice(i-1),M)

#Supprimer le 1er maillon de la liste  et le renvoie : équivalent de pop(0)
    def supprimer_debut(self):
        t = self.tete
        self.tete = t.suiv
        return t

#Supprimer le dernier maillon de la liste  et le renvoie : équivalent de pop()
    def supprimer_fin(self):
        m = self.tete
        while m.suiv is not None:
            n=m
            m = m.suiv
        n.suiv = None
        return m

#Supprimer le maillon de la liste situé après le maillon M et le renvoie
    def supprimer_apres(self, M):
        assert M.suiv != None #vérifier que M n'est pas le dernier maillon
        s = M.suiv
        M.suiv = M.suiv.suiv
        return s

#Supprimer un élément d'indice i et le renvoie
    def supprimer(self,i):
        assert i<self.longueur()
        if i==0:
            return self.supprimer_debut()
        else:
            M=self.get_maillon_indice(i-1)
            return self.supprimer_apres(M)


#Afficher la liste chainée sous forme de tableau
    def afficher(self):
        l=[]
        for k in range(self.longueur()):
            l.append(self[k])
        print(l)

#Concaténer l1 et l2 (l1 sera identique à la concaténation à cause des pointeurs)
def concatener(l1, l2):
    """concatène les listes l1 et l2,
       sous la forme d'une nouvelle liste"""
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    else:
        l=ListeC(l1.tete)
        n=l1.longueur()
        M=l1.get_maillon_indice(n-1)
        M.suiv=l2.tete
    return l 


#Test:
L=ListeC()
M1,M2=Maillon(12),Maillon(25)
M1.set_suivant(M2)
L.tete=M1
print(L.est_vide())
print(L.longueur())
L.inserer(1,17)
print(L.longueur())
print(L.get_maillon_indice(1))
L.afficher()