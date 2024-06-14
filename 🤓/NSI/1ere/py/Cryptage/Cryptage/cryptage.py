from random import randint

alphabet=[]
for k in range(33,127):
    alphabet.append(chr(k))
for k in range(161,173):
    alphabet.append(chr(k))
for k in range(174,256):
    alphabet.append(chr(k)) # Création d'un alphabet utilisable pour le cryptage

clef = "Einsteinnevergothisdriverlicense"

file = open("a_crypter.txt", "r", encoding = 'utf_8')
a_crypter = file.read()

message_crypte = ""

for i in range(len(a_crypter)):
    if a_crypter[i] == ' ':
        message_crypte += ' '
    elif a_crypter[i] == '\n':
        message_crypte += '\n'
    else:
        for j in range(len(clef)):
            Index = int(alphabet.index(a_crypter[i]))+int(alphabet.index(clef[j]))        

        if Index >= len(alphabet):
            New_index = Index-len(alphabet)
            Index = New_index
        message_crypte += alphabet[Index] # Création du str qui sera ensuite utiliser dans l'écriture
    
file.close()
file = open("crypte.txt", "w", encoding = 'utf_8')
file.write(message_crypte) # Écriture du crypte
file.close()
