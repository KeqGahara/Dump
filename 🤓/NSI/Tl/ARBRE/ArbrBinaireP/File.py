class File:
    
    def __init__(self):
        self.valeurs=[]
        
    def enfiler(self,valeur):
        self.valeurs.append(valeur)
        
    def defiler(self):
        if self.valeurs:
            return self.valeurs.pop()
    
    def estVide(self):
        return self.valeurs==[]
    
    def __str__(self):
        y = "\nEtat de la file:\n"
        for x in self.valeurs:
            y +=  str(x) + " "
        return y
