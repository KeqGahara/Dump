class Pile:

    def __init__(self):
        self.valeurs=[]

    def empiler(self,valeur):
        self.valeurs.append(valeur)

    def depiler(self):
        if not self.estVide():
            return self.valeurs.pop()
        else:
            raise ValueError("La pile est vide #Mouaffak")

    def estVide(self):
        return self.valeurs==[]

    def __str__(self):
        y=''
        for x in self.valeurs:
            y="|\t"+str(x)+"\t|"+"\n"+y
        return y


#Test
'''
p = Pile()
p.empiler(9)
p.empiler(2)
p.empiler(5)

print(p)

p.depiler()
p.empiler(7)

print(p.estVide())

print(p)
'''
