## Concept !!

class Noeud:
  def __init__(self, valeur):
        self.valeur = valeur #Integer pour arbre de recherche
        self.gauche = None
        self.droite = None
        
  def __repr__(self):
      return f"Noeud({self.valeur})"


class ArbreBinaire:
  def __init__(self,Noeud):
        self.racine = Noeud

  def est_vide(self):
      return self.racine is None

  def get_gauche(self):
      return self.racine.gauche

  def get_droite(self):
      return self.racine.droite

  def insert_gauche(self, Noeud):
      if self.est_vide() is True :
          self.racine = Noeud
      else:
          if isinstance(Noeud.valeur, str):
              if Noeud.valeur.isdigit() == True :
                  assert Noeud.valeur > self.racine.valeur
                  nouveau_noeud = ArbreBinaire(Noeud)
                  nouveau_noeud.gauche = Noeud.gauche # type: ignore
                  Noeud.gauche = nouveau_noeud
              else:
                  nouveau_noeud = ArbreBinaire(Noeud)
                  nouveau_noeud.droite = Noeud.droite # type: ignore
                  Noeud.droite = nouveau_noeud       
          if isinstance(Noeud.valeur, int):
              assert Noeud.valeur < self.racine.valeur
              nouveau_noeud = ArbreBinaire(Noeud)
              nouveau_noeud.gauche = Noeud.gauche # type: ignore
              Noeud.gauche = nouveau_noeud
          else:
              if Noeud.gauche == None:
                  Noeud.gauche = ArbreBinaire(Noeud)
              else:
                  nouveau_noeud = ArbreBinaire(Noeud)
                  nouveau_noeud.gauche = Noeud.gauche # type: ignore
                  Noeud.gauche = nouveau_noeud

  def insert_droite(self, Noeud):
      if self.est_vide() is True:
          self.racine = Noeud
      else:
          if isinstance(Noeud.valeur, str):
              if Noeud.valeur.isdigit() == True :
                  assert Noeud.valeur > self.racine.valeur
                  nouveau_noeud = ArbreBinaire(Noeud)
                  nouveau_noeud.droite = Noeud.droite # type: ignore
                  Noeud.droite = nouveau_noeud
              else:
                  nouveau_noeud = ArbreBinaire(Noeud)
                  nouveau_noeud.droite = Noeud.droite # type: ignore
                  Noeud.droite = nouveau_noeud                                    
          if isinstance(Noeud.valeur, int):
              assert Noeud.valeur > self.racine.valeur
              nouveau_noeud = ArbreBinaire(Noeud)
              nouveau_noeud.droite = Noeud.droite # type: ignore
              Noeud.droite = nouveau_noeud
          else:
              if Noeud.droite == None:
                  Noeud.droite = ArbreBinaire(Noeud)
              else:
                  nouveau_noeud = ArbreBinaire(Noeud)
                  nouveau_noeud.droite = Noeud.droite # type: ignore
                  Noeud.droite = nouveau_noeud

  def hauteur(self, Noeud):
      if Noeud is None:
          return 0
      else:
          taille_Gauche = self.hauteur(Noeud.gauche)
          taille_Droite = self.hauteur(Noeud.droite)

          if taille_Gauche > taille_Droite:
              return taille_Gauche + 1
          else:
              return taille_Droite + 1

  def taille(self, Noeud):
      if Noeud is None:
          return 0
      else:
          return (self.taille(Noeud.gauche) + 1 + self.taille(Noeud.droite))

  def affiche(self):
      if self.racine is not None:
          self.affiche()

  def _affiche(self, Noeud, n):
      if Noeud is not None:
          self._affiche(Noeud.droite, n + 1)
          print('\t' * n + str(Noeud.valeur))   
          self._affiche(Noeud.gauche, n + 1)


#Test:
N1 = Noeud(15)
N2 = Noeud(4)
N3 = Noeud(8)
N4 = Noeud(3)
N5 = Noeud(12)
N6 = Noeud(20)
N7 = Noeud(17)
T = ArbreBinaire(N1)
T.insert_gauche(N2)
T.insert_gauche(N3)
T.insert_gauche(N4)
T.insert_gauche(N5)
T.insert_droite(N6)
T.insert_droite(N7)
print(T.hauteur(N1))
print(T.taille(N1))
#T._affiche(N1,0) !!!!!



