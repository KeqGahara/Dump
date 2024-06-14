# -*- coding: utf-8 -*-

#création d'une liste de caractères ISO-Latin-1
alphabet=[]
for k in range(33,127):
    alphabet.append(chr(k))
for k in range(161,173):
    alphabet.append(chr(k))
for k in range(174,256):
    alphabet.append(chr(k))

print(alphabet)
