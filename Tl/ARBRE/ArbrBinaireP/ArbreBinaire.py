class ArbreBinaire:
    
    def __init__(self, cle):
        self.cle=cle
        self.gauche=None
        self.droite=None
        
    def insert_gauche(self, cle):
        if self.gauche == None:
            self.gauche = ArbreBinaire(cle)
        else:
            nouveau_noeud = ArbreBinaire(cle)
            nouveau_noeud.gauche = self.gauche
            self.gauche = nouveau_noeud
    
    def insert_droite(self, cle):
        if self.droite == None:
            self.droite = ArbreBinaire(cle)
        else:
            nouveau_noeud = ArbreBinaire(cle)
            nouveau_noeud.droite = self.droite
            self.droite = nouveau_noeud
    
    def get_cle(self):
        return self.cle
    
    def get_gauche(self):
        return self.gauche
    
    def get_droite(self):
        return self.droite
    
    
#Affichage de l'arbre sous forme de tuple
    
def affiche(T):
        if T != None:
            return (T.get_cle(),affiche(T.get_gauche()),affiche(T.get_droite()))