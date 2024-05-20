#Classe Pile en s'inspirant de la classe Liste (tête et queue)

class Pile():
    def __init__(self, *args):
        if len(args) == 0:
            self.val = []
        else:
            self.val = [args[0]]

    def estvide(self):
        return self.val == []

    def sommet(self):
        assert not self.estvide(), "Pile vide"
        return self.val[0]

    def empiler(self, v):
        self.val = [v] + self.val  # Ajoute l'élément au sommet de la pile

    def depiler(self):
        assert not self.estvide(), "Pile vide"
        a = self.sommet()
        self.val = self.val[1:]
        return a

    def __repr__(self):
        return str(self.val)


#Tests
'''
P=Pile()
assert P.estvide()==True
P.empiler(5)
P.empiler(7)
assert P.estvide()==False
assert P.sommet()==7
P.empiler(2)
assert(P.depiler())==2
P.depiler()
P.depiler()
assert P.estvide()==True
'''