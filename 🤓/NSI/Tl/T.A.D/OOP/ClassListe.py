class Liste:
    
    def __init__(self,*args):
        if len(args)==0:
            self.valeurs=[]
        else:
            self.valeurs=[args[0],args[1]]
            
    def __getItem__(self,i):
        if i<2:
            return self.valeurs[i]

    def estvide(self):
        return self.valeurs==[]

    def tete(self):
        assert not self.estvide() #liste vide
        return self.valeurs[0]

    def queue(self):
        assert not self.estvide() #liste vide
        return self.valeurs[1]

    def ajouterEnTete(self, x):
        self.valeurs[0]=(x,self.tete)
        return self.valeurs
    

    def supprTete(self):
        assert not self.estvide() #liste vide
        a = self.valeurs[0]
        self.valeurs = self.valeurs[1]
        return a
    
    def longueur(self):
        if self.estvide():
            return 0
        else:
            return 1+self.queue().longueur()
        
    def concatener(self, L2):
        if self.estvide():
            return L2
        else:
            x = self.tete()
            L = Liste()
            L.ajouterEnTete(x)
            L.queue().concatener(L2)
            return L


# Retourne une chaîne de caractères représentative de l'état de l'instance.
    
    def __str__(self):
        return str(self.valeurs)
    def __repr__(self):
        return str(self.valeurs)


#Test
'''
L=Liste()
L=Liste(5,L)
L=Liste(8,L)

L=Liste()
assert L.estvide()==True
L=Liste(5,L)
assert L.estvide()==False
L=Liste(8,L)
L=Liste(3,L)
L=Liste(6,L)
assert L.tete()==6
assert L.queue().tete()==3
t=L.supprTete()
assert t==6
assert L.tete()==3
assert L.longueur()==3
'''
