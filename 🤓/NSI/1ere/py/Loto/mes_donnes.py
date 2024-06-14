import csv
import codecs

mon_fichier=codecs.open('tirage_loto.csv', encoding='utf-8')
tirage=list(csv.dictreader(mon_fichier, delimiter = ';'))

tirage = []

for i in mes_donnees:
    Loto.append(i)
    


