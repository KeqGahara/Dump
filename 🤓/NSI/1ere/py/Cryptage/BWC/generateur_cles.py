from random import randint

""""prise de note en classe
mon_fichier=open("codes.txt", "w", encoding = 'utf_8') # w désigne write 
mon_fichier.write("ceci est un test")
mon_fichier.close() # close le fichier est essentiel pour le fonctionnement du code
"""
"""
N = []
N = [i for i in range(1,101)]
    #liste qui sera utiliser pour la numérotation 

L = []
L = [[str(randint(1,11)) for i in range(randint(5,7))] for j in range(1,101)]
    #liste contenant les clés  

mon_fichier=open("cles.txt", "w")
    #Création du fichier 

for i in range(100):
    files.write(N[i]+" " + str(L[i]).replace("[",' ').replace("'",'').replace(",",' ').replace("]",'')+"\n")
            #Replace ici sert a remplacer les str dans la list L qui sont en trop afin de passer d'une forme x["x","x",..."x"] a x x x...x 
            #donc en remplaçant le crochet l'apostrophe et la virgule par des espaces ou bien rien tous simplement. 
    mon_fichier.write('\n')
            #Écriture dans le fichier

mon_fichier.close()
    #fin
        #Messy verz 
"""

mon_fichier = open("cles.txt", "w", encoding = 'utf_8')
for i in range(100):
    mon_fichier.write(str(i+1))
    for j in [randint(1,11) for a in range(randint(5,7))]:
        mon_fichier.write(" "+str(j))
    mon_fichier.write("\n")
mon_fichier.close()
    #code plus propre, le même que celui qui le precede mais en plus compact, sans l'utilisation des list   
