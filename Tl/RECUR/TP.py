import timeit
import sys

sys.setrecursionlimit(1000001)

#########

def puissance_iterative(x,n):
    r=1
    i=1
    while i<=n:
        r=r*x
        i+=1
    return r



def puissance(x,n):
    if n==0:
        return 1
    else:
        return x*puissance(x,n-1)



def puissance_v2(x,n):
    if n==0:
        return 1
    elif n==1:
        return x
    else:

        if n%2==0:
            return puissance_v2(x,n//2)**2
        else:
            return x*(puissance_v2(x,n//2)**2)


######## TEST ######## n=1000000, x=2 puis x=3: Probleme au niveau de la memoire caché pour les fonction recur => Au final l'utilisation de ces fonctions est trés situationnel. 

'''n=int(input('n'))
x=int(input('x'))

start = timeit.default_timer()

puissance_iterative(x,n)

stop = timeit.default_timer()

a=stop - start



start = timeit.default_timer()

puissance(x,n)

stop = timeit.default_timer()

b = stop - start



start = timeit.default_timer()

puissance_v2(x,n)

stop = timeit.default_timer()

c = stop - start



print('Pour x =',x,'et n =',n, '\n le premier programme a pris ', a,' secondes', '\n le deuxième programme a pris ', b,' secondes', '\n le dernier programme a pris ', c,' secondes')'''

######## EX2 ########

def FactRecur(n):
    if n==0:
        return 1
    else:
        return n*FactRecur(n-1)

######## EX3 ########

def f(n,a,b):
    if n==0:
        return a
    elif n==1:
        return b
    else:
        return 3*f(n-1,a,b)+2*f(n-2, a, b)+5

########
'''
a_value=1
b_value=2
n_value=3

result = f(n_value, a_value, b_value)
print(f'f({n_value}) avec a={a_value} et b={b_value} : {result}')
'''
######## EX4 ########

def boucle(i,k):
    if i<=k:
        print(i,end=' ')
        boucle(i+1,k)

########
'''       
boucle(0, 3)
'''
######## EX5 ########

def nombre_de_chiffres(n):
    if n<0:
        n=-n
    if n<10:
        return 1
    else:
        return 1+nombre_de_chiffres(n // 10)

########
'''
print(nombre_de_chiffres(34126))
'''
######## EX6 ########

def hanoi(n,A,C,B):
  if n==1:
      print("Déplacer un disque de",A, "vers",C)
  else:
      hanoi(n-1,A,B,C)
      hanoi(1,A,C,B)
      hanoi(n-1,B,C,A)

# Appels de la fonction hanoi

hanoi(3,'A','C','B')
hanoi(3,'A','C','B')

#END