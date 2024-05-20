class Maillon:
    
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
    
    def supprimer_fin(self):
        assert not self.estVide()
        m = self.tete
        while m.suiv != None and m.suiv.suiv != None:
            m = m.suiv
        f = m.suiv.valeur
        m.suiv = None
        return f
    
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
'''
L=ListeC()
M1=Maillon(1)
M2=Maillon(2,M1)
M3=Maillon(3,M2)
L.ajouter_debut(M1)
L.ajouter_debut(M2)
L.ajouter_debut(M3)
L.supprimer_fin()
L.afficher()
print(L.estVide())
print(L.longueur())
print(L.get_maillon_indice(0))
'''

