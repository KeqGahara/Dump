from random import randint
#ex1
a=1
L=[]
for i in range(49):
    L.append(a+i*2)
    #print(sum(L)) #le dernier élément correspends a la reponse

a=1
L=[]
for i in range(100):
    L.append(a+i)
    #print(sum(L)) #le dernier élément correspends a la reponse

def somme(dernier_élément, premier_élément, r):
    L=[premier_élément]
    while L[-1]!=dernier_élément:
        for i in range(1,dernier_élément):
            L.append(premier_élément+i*r)
    return (sum(L))

#ex2
def pli_papier(h,épaisseur):
    n=0
    while épaisseur!=h:
        épaisseur=épaisseur*2
        n=n+1
    return n

#ex3




