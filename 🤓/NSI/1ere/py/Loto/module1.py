import csv
import codecs

Loto = []

mon_fichier=codecs.open('tirage_loto.csv', encoding='utf-8')
mes_donnees=csv.reader(mon_fichier, delimiter = ',')
