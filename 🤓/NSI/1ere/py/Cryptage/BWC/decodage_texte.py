from codage_texte import cle
from creation_liste_alphabet_utf8 import alphabet

file = open("albatros_chiffre1.txt", "r", encoding = 'utf_8')
a_decrypter = file.read()

message_clair = ""

for i in range(len(a_decrypter)):
    if a_decrypter[i] == ' ':
        message_clair += ' '
    elif a_decrypter[i] == '\n':
        message_clair += '\n'
    else:
        for j in range(len(cle)):
            Index = int(alphabet.index(a_decrypter[i]))-int(cle[j])
        message_clair += alphabet[Index]   

file = open("albatros_dechiffre1.txt", "w", encoding = 'utf_8')
file.write(message_clair)
file.close()
