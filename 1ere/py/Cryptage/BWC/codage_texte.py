from random import randint
from creation_liste_alphabet_utf8 import alphabet


file = open("cles.txt", "r", encoding = 'utf_8')
for i in range(randint(1,101)):
    cles = file.readline().replace("'",'').replace("\n",'').replace(" ",' ')
cle = list(cles.split(" "))
    #cette ligne convertie le str cles en cle list
cle.pop(0)
file.close()


file = open("albatros.txt", "r", encoding = 'utf_8')

a_crypter = file.read()
message_crypte = ""

for i in range(len(a_crypter)):
    if a_crypter[i] == ' ':
        message_crypte += ' '
    elif a_crypter[i] == '\n':
        message_crypte += '\n'
    else:
        for j in range(len(cle)):
            Index = int(alphabet.index(a_crypter[i]))+int(cle[j])        
               
        if Index >= len(alphabet):
            New_index = Index-len(alphabet)
            Index = New_index
        message_crypte += alphabet[Index]
    
file.close()

file = open("albatros_chiffre1.txt", "w", encoding = 'utf_8')
file.write(message_crypte)
file.close()


