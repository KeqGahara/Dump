#Classe File en s'inspirant de la classe liste chaînée

from ClassListeC import *

class File():
    def __init__(self,tete=None):
       #Son attribut tete est de type Maillon, ou bien vaut None si la liste est vide.
        assert type(tete)==Maillon or tete==None
        self.tete = tete
    
    def est_vide(self):
        return self.tete is None
    
    def Tete(self):
        assert not self.est_vide(),"File vide !"
        return self.tete.valeur
    
    def Queue(self):
        assert not self.est_vide(), "File vide !"
        Q=File(self.tete.suiv)
        return Q
    
    def enfiler(self, v):
        M=Maillon(v)
        m = self.tete
        if m is None:
            self.tete=M
        else:
            while m.suiv is not None:
                m = m.suiv
            m.suiv = M
        
    def defiler(self):
        assert not self.est_vide(), "File vide !!"
        t = self.tete
        self.tete = t.suiv
        return t.valeur
    
#################### Méthodes pour les affichages ########################

    def longueur(self): 
   
        m = self.tete
        l = 0 
        while m is not None:
            l += 1
            m = m.suiv
        return l
    
    def get_maillon_indice(self, i):
        assert i<self.longueur()
        
        j = 0
        m = self.tete 
        while j < i:
            j += 1
            m = m.suiv
        return m
    
    def afficher(self):
        l=[]
        for k in range(self.longueur()):
            l.append(self[k])
        print(l)
        
    def __getitem__(self, i):
        '''
        Permet d'utiliser les fonctions de python et d'accéder
        aux éléments d'une liste directement par Liste[i]
        '''
        return self.get_maillon_indice(i).val
    
    
'''
f=File()
f.enfiler(3)
assert f.Tete()==3
f.enfiler(8)
assert f.Tete()==3
f.Queue().Tete()==8
assert f.defiler()==3
assert f.Tete()==8
'''