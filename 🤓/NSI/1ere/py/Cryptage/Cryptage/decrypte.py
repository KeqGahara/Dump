from cryptage import clef

alphabet=[]
for k in range(33,127):
    alphabet.append(chr(k))
for k in range(161,173):
    alphabet.append(chr(k))
for k in range(174,256):
    alphabet.append(chr(k)) # Recréation d'une liste d'alphabet utilisable pour le (de)cryptage

file = open("crypte.txt", "r", encoding = 'utf_8')
a_decrypter = file.read()

message_clair = ""

for i in range(len(a_decrypter)):
    if a_decrypter[i] == ' ':
        message_clair += ' '
    elif a_decrypter[i] == '\n':
        message_clair += '\n'
    else:
        for j in range(len(clef)):
            Index = int(alphabet.index(a_decrypter[i]))-int(alphabet.index(clef[j]))
        message_clair += alphabet[Index] # Processus de décryptage et donc creation du str qui sera ensuite utiliser dans l’écriture

file = open("decrypter.txt", "w", encoding = 'utf_8')
file.write(message_clair) # Écriture du décryptage
file.close()