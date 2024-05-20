fic=open('fichier.txt','w')


for i in range(11):
    a=3*i
    fic.write("3x"+str(i)+"="+str(a)+"\n")

fic.close()

