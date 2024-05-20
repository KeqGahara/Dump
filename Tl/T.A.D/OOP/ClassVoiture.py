class Voiture:
    
    def __init__(self):
        self.modele='Mercedes'
        self.couleur='Noir'
        
    def getAttributs(self):
        return (self.modele,self.couleur)
    
    def immatriculation(self):
        return 'OK'
    
    def paindre(self):
        self.couleur=input('Saisir la couleur de la Voiture')

ma_voiture = Voiture()


