class NONP:
  def __init__(self):
      self.dic = dict()

  def ajout_sommet(self, s):
      assert s not in self.dic, "Le sommet existe déjà."
      self.dic[s] = []

  def ajout_arete(self, a, b):  # arete entre a et b
      if a not in self.dic.keys():
          self.ajout_sommet(a)
      if b not in self.dic.keys():
          self.ajout_sommet(b)
      assert not self.est_voisin(a, b), "a et b sont déjà reliés."
      self.dic[a].append(b)
      self.dic[b].append(a)

  def ordre(self):
      return len(self.dic)

  def degre(self,a):
      return len(self.dic[a])

  def sommets(self):
      return list(self.dic.keys())

  def voisins(self, a):
      return self.dic[a]

  '''def matrice(self):
    M=[]
    sommets = self.dic.keys()
    for i in sommets:
        ligne = [int(j in self.dic[i])for j in sommets]
        M.append(ligne)
    txt=str(M).replace('],',']\n')
    return txt'''

  def matrice(self):
      M=[]
      sommets = self.dic.keys()
      for i in sommets:
          ligne = [int(j in self.dic[i]) for j in sommets]
          M.append(ligne)
      return M

  def parcours_largeur(self, sommet):
      visited = []
      queue = []
      visited.append(sommet)
      queue.append(sommet)
      while queue:
          s = queue.pop(0)
          for voisin in self.sommets[s]:
              if voisin not in visited:
                  visited.append(voisin)
                  queue.append(voisin)
      return visited

  def parcours_profondeur(self, sommet, visited=None):
      if visited is None:
          visited = []
      visited.append(sommet)
      for voisin in self.sommets[sommet]:
          if voisin not in visited:
              self.parcours_profondeur(voisin, visited)
      return visited

  def chemin(self, a, b): #vérifie si il existe un chemin
      visited = []
      d = list(self.dic[a])
      while d:
          v = d.pop()
          if v == b:
              return True , [a,b]
          if v not in visited:
              visited.append(v)
              d.extend(set(self.voisins(v)) - set(visited))
      return False ,visited

  def cycle(self):
      for sommet in self.sommets():
          if self.chemin(sommet, sommet):
              return True
      return False

  '''def dijkstra(self, a, b):
      distances = {sommet: float('infini') for sommet in self.sommets()}
      distances[a] = 0
      visite = set()
      while visite != set(self.sommets()):
          non_visite = {sommet: distances[sommet] for sommet in distances if sommet not in visite}
          sommet_actuel = min(non_visite, key=non_visite.get)
          visite.add(sommet_actuel)
          for voisin in self.successeurs(sommet_actuel):
              poids_total = distances[sommet_actuel] + self.dic[sommet_actuel][voisin]
              if poids_total < distances[voisin]:
                  distances[voisin] = poids_total
      return distances[b]'''

  def __repr__(self):
    return str(self.dic)

  def est_voisin(self, a, b):
    return b in self.dic[a]  


class OP:
  def __init__(self):
      self.dic = dict()

  def ajout_sommet(self,s):
      assert s not in self.dic
      self.dic[s] = dict()

  def ajout_arc_poid(self,a,b,poids:int):  
      if a not in self.dic.keys():
          self.ajout_sommet(a)
      if b not in self.dic.keys():
          self.ajout_sommet(b)

      assert not self.est_voisin(a,b)
      self.dic[a][b] = poids

  def ordre(self):
      return len(self.dic)

  def degre(self,a):
      return len(self.dic[a])

  def sommets(self):
      return list(self.dic.keys())

  def successeurs(self, a):
      return list(self.dic[a].keys())

  def predecesseurs(self, a): #s doit etre un sommet existant et faut que a soit son succeseur
      return [s for s in self.sommets() if a in self.successeurs(s)]

  def poids_arc(self, a, b):
      return self.dic[a][b]

  '''def matrice(self):
  sommets = self.sommets()
  n = len(sommets)
  mat = [[0]*n for _ in range(n)]
  for i, a in enumerate(sommets):
  for b in self.successeurs(a):
    j = sommets.index(b)
    mat[i][j] = self.dic[a][b]
  return mat'''

  def matrice(self):
      M=[]
      sommets = self.dic.keys()
      for i in sommets:
          ligne = [int(j in self.dic[i]) for j in sommets]
          M.append(ligne)
      return M

  def parcours_largeur(self, sommet):
      visited = []
      queue = []
      visited.append(sommet)
      queue.append(sommet)
      while queue:
          s = queue.pop(0)
          for voisin in self.sommets[s]:
              if voisin not in visited:
                  visited.append(voisin)
                  queue.append(voisin)
      return visited

  def parcours_profondeur(self, sommet, visited, chemin):
      if sommet in chemin:
          return True
      chemin.append(sommet)
      for voisin in self.voisins(sommet):
          if voisin not in visited:
              if self.parcours_profondeur(voisin, visited + [sommet], chemin):
                  return True
      chemin.pop()
      return False


  def cycle(self):
      for sommet in self.sommets():
          if self.chemin(sommet, sommet):
              return True
      return False

  '''def dijkstra(self, a, b):
  distances = {sommet: float('infini') for sommet in self.sommets()}
  distances[a] = 0
  visite = set()
  while visite != set(self.sommets()):
  non_visite = {sommet: distances[sommet] for sommet in distances if sommet not in visite}
  sommet_actuel = min(non_visite, key=non_visite.get)
  visite.add(sommet_actuel)
  for voisin in self.successeurs(sommet_actuel):
  poids_total = distances[sommet_actuel] + self.dic[sommet_actuel][voisin]
  if poids_total < distances[voisin]:
      distances[voisin] = poids_total
  return distances[b]'''


  def __repr__(self):
      return str(self.dic)

  def est_voisin(self, a, b): #ou arc c'est la meme chose
      return b in self.dic[a]


class NOP:
def __init__(self):
    self.dic = dict()

def ajout_sommet(self, s):
    assert s not in self.dic
    self.dic[s] = dict()

def ajout_arete_poids(self, a, b, poids : int):  # arete ponderee entre a et b
    if a not in self.dic.keys():
        self.ajout_sommet(a)
    if b not in self.dic.keys():
        self.ajout_sommet(b)

    assert not self.est_voisin(a, b)
    self.dic[a][b] = poids
    self.dic[b][a] = poids

def ordre(self):
    return len(self.dic)

def degre(self,a):
    return len(self.dic[a].keys())

def sommets(self):
    return list(self.dic.keys())

def voisins(self, a):
    return list(self.dic[a].keys())

def poids_arete(self, a, b):
    return self.dic[a][b]

'''def matrice(self):
    sommets = self.sommets()
    n = len(sommets)
    mat = [[0]*n for _ in range(n)]
    for i, a in enumerate(sommets):
        for b in self.voisins(a):
            j = sommets.index(b)
            mat[i][j] = self.dic[a][b]
    return mat'''

def matrice(self):
  M=[]
  sommets = self.dic.keys()
  for i in sommets:
      ligne = [int(j in self.dic[i]) for j in sommets]
      M.append(ligne)
  return M

def parcours_largeur(self, sommet):
  visited = []
  queue = []
  visited.append(sommet)
  queue.append(sommet)
  while queue:
      s = queue.pop(0)
      for voisin in self.sommets[s]:
          if voisin not in visited:
              visited.append(voisin)
              queue.append(voisin)
  return visited

def parcours_profondeur(self, sommet, visited=None):
  if visited is None:
      visited = []
  visited.append(sommet)
  for voisin in self.sommets[sommet]:
      if voisin not in visited:
          self.parcours_profondeur(voisin, visited)
  return visited

def chemin(self, a, b):
  visited = []
  liste = [a]
  while liste:
      v = liste.pop()
      if v == b:
          return True
      if v not in visited:
          visited.append(v)
          liste.extend(set(self.voisins(v)) - set(visited))
  return False

def cycle(self):
  for sommet in self.sommets():
      if self.chemin(sommet, sommet):
          return True
  return False

'''def dijkstra(self, a, b):
  distances = {sommet: float('infini') for sommet in self.sommets()}
  distances[a] = 0
  visite = set()
  while visite != set(self.sommets()):
      non_visite = {sommet: distances[sommet] for sommet in distances if sommet not in visite}
      sommet_actuel = min(non_visite, key=non_visite.get)
      visite.add(sommet_actuel)
      for voisin in self.voisins(sommet_actuel):
          poids_total = distances[sommet_actuel] + self.dic[sommet_actuel][voisin]
          if poids_total < distances[voisin]:
              distances[voisin] = poids_total
  return distances[b]'''


def __repr__(self):
    return str(self.dic)

def est_voisin (self, a, b):
    return b in self.dic[a]


class ONP:
def __init__(self):
    self.dic = dict()

def ajout_sommet(self, s):
    assert s not in self.dic
    self.dic[s] = []

def ajout_arc(self, a, b):  #sommet a:origine et sommet b: destination
    if a not in self.dic.keys():
        self.ajout_sommet(a)
    if b not in self.dic.keys():
        self.ajout_sommet(b)
    assert not self.est_voisin(a, b)
    self.dic[a].append(b)

def ordre(self):
    return len(self.dic)

def degre(self,a):
    return len(self.dic[a].keys())

def sommets(self):
    return list(self.dic.keys())

def voisins(self, a):
    return self.dic[a]

def successeurs(self, a):
    return list(self.dic[a])

def predecesseurs(self, a): #s doit etre un sommet existant et faut que a soit son succeseur
    return [s for s in self.sommets() if a in self.successeurs(s)]

def est_voisin(self, a, b):
    return b in self.dic[a]  

'''def matrice(self):
    sommets = self.sommets()
    n = len(sommets)
    mat = [[0]*n for _ in range(n)]
    for i, a in enumerate(sommets):
        for b in self.successeurs(a):
            j = sommets.index(b)
            mat[i][j] = self.dic[a][b]
    return mat'''

  def matrice(self):
      M=[]
      sommets = self.dic.keys()
      for i in sommets:
          ligne = [int(j in self.dic[i]) for j in sommets]
          M.append(ligne)
      return M

  def parcours_largeur(self, depart, arrivee):
      visited = set()
      queue = [(depart, [depart])]
      while queue:
          sommet, path = queue.pop(0)
          if sommet == arrivee:
              return path
          if sommet not in visited:
              visited.add(sommet)
              for voisin in self.voisins(sommet):
                  queue.append((voisin, path + [voisin]))
      return None


def parcours_profondeur(self, sommet, visited, chemin):
      if sommet in chemin:
          return True
      chemin.append(sommet)
      for voisin in self.voisins(sommet):
          if voisin not in visited:
              if self.parcours_profondeur(voisin, visited + [sommet], chemin):
                  return True
      chemin.pop()
      return False

def chemin(self, a, b):
  visited = self.parcours_profondeur(a)
  if b == self.voisin(a):
      return True, [a,b]
  elif b == visited:
      return True, visited
  else :
      return False, []

def cycle(self):
  return any(self.chemin(sommet, sommet) for sommet in self.sommets())

'''def dijkstra(self, a, b):
  distances = {sommet: float('infini') for sommet in self.sommets()}
  distances[a] = 0
  visite = set()
  while visite != set(self.sommets()):
      non_visite = {sommet: distances[sommet] for sommet in distances if sommet not in visite}
      sommet_actuel = min(non_visite, key=lambda x: non_visite[x])
      visite.add(sommet_actuel)
      for successeur in self.successeurs(sommet_actuel):
          poids_total = distances[sommet_actuel] + 1 
          if poids_total < distances[successeur]:
              distances[successeur] = poids_total
  return distances[b]'''

def __repr__(self):
    return str(self.dic)


#Test

'''
a=input('Type ?')
assert type(['NONP','OP','NOP','ONP'].index(a))==int
'''

G=ONP()
G.ajout_sommet('a')
G.ajout_sommet('b')
G.ajout_sommet('c')
G.ajout_sommet('d')
G.ajout_arc('a','b')
G.ajout_arc('a','c')
G.ajout_arc('b','d')
G.ajout_arc('c','d')
G.cycle()
                                                                                                                          

