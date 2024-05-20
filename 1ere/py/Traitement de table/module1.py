"""
explication
crée une liste pays

# −∗− coding : utf −8 −∗−
import csv
import codecs

pays = [ ]

csvfile=codecs.open('pays_monde.csv', encoding ='utf −8')
spamreader = csv.reader(csvfile,delimiter=' , ')
for row in spamreader:
    pays.append(row)

"""

import csv
import codecs

pays = []

mon_fichier=codecs.open('pays_monde.csv', encoding='pays_monde.csv')
mes_donnees=csv.reader(mon_fichier, delimiter = ',')

for i in mes_donnees:
    pays.append(i)

liste_population=[]
for p in pays:
    if p['POPULATION']>3000000:
        liste_population.append(p['PAYS'])
print(liste-popoualtion)
