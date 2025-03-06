import random
import string

def generer_mot_de_passe(longueur):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longueur))

mot_de_passe_correct = "1390"

while True:
    mots_de_passe_a_tester = [generer_mot_de_passe(4) for _ in range(4)]
    for mot_de_passe in mots_de_passe_a_tester:
        if mot_de_passe == mot_de_passe_correct:
            print("Mot de passe correct, vous avez accès au compte")
            break
        else:
            print(f"Mot de passe {mot_de_passe} incorrect")
    else:
        continue
    break
