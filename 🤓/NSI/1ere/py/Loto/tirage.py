import csv
import codecs

mon_fichier=codecs.open('tirage_loto.csv', encoding='utf-8')
mes_donnes=list(csv.DictReader(mon_fichier, delimiter = ';'))

def probabilitées (numero):
    n=0
    for i in range (len(tirage)):
        if int(tirage[i]['boule_1'])==numero:
            n=n+1
        elif int(tirage[i]['boule_2'])==numero:
            n=n+1
        elif int(tirage[i]['boule_3'])==numero:
            n=n+1
        elif int(tirage[i]['boule_4'])==numero:
            n=n+1
        elif int(tirage[i]['boule_5'])==numero:
            n=n+1
    print(n)
    return(n)

"""

loto = []

for i in mes_donnes :
    loto.append(i)

for i in 
    loto.pop[(i)(0)]
    
"""    

