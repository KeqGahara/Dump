def test(L):
  '''
  In : Liste de int
  out : Bool
  Cette fonction vérifie si une liste de n valeurs est canonique
  '''
  for i in range(len(L)):
      if sum(L[:i]) < L[i]: # Etape de vérification
          return True
  return False

# Exemple d'utilisation
"""
liste1 = [0,1,2,3,4]
liste2 = [1,2,3,4,5]

print(test(liste1))  # True
print(test(liste2))  # False
"""

def glouton(somme, pieces):
  '''
  In : Liste de int et un int 
  out : liste de int 
  algo glouton pour le problème de rendue de pièce
  '''
  pieces.sort(reverse=True)  # Trie les pièces en ordre décroissant
  rendu = []
  for piece in pieces:
      while somme >= piece:
          rendu.append(piece)
          somme -= piece
  return rendu

#Cas canonique
"""
rendu = 83
print("Canonique :\nrendu =", rendu)
pieces_disponibles = [1,2,5,10]  # Valeurs des pièces disponibles
print("pieces_disponibles =", pieces_disponibles)
print("Rendu de monnaie:", glouton(rendu, pieces_disponibles))
print("La fonction est vérifier, car somme de rendu de monnaie =", sum(glouton(rendu, pieces_disponibles)),"\n est égale au rendu =", rendu)
"""
#Cas non canonique
"""
rendu = 83
print("Non Canonique :\nrendu =", rendu)
pieces_disponibles = [2,5,6,8,10]
print("pieces_disponibles =", pieces_disponibles)
print("Rendu de monnaie:", glouton(rendu, pieces_disponibles))
print("La fonction n'est pas vérifier, car la somme de rendu de monnaie :", sum(glouton(rendu, pieces_disponibles)),"\n est differente du rendu =", rendu)
"""

def nbopt(somme, pièces):
  '''
  In : Liste de int et un int 
  out : int 
  algo d'optimisation
  '''
  L = glouton(somme,pièces)
  if len(glouton(somme,pièces))<=2:
      return len(L) # optimiser, pas de changement
  for i in range(len(glouton(somme,pièces))):
      pièces.sort(reverse=True)
      pièces.pop(i)
      a = glouton(sum(L[:i]),pièces) #predifinition de la liste a otpimsier
      if len(a)<len(L[:i]):
          return len(a+L[i:]) #optimisation de la liste
      return len(L)


