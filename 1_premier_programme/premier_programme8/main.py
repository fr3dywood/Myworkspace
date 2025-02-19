# Demande à l'utilisateur de saisir son nom
nom = input("Quel est votre nom ? ")

# Demande à l'utilisateur de saisir son âge
age = input("Quel est votre age ? ")

try:
    # Essaie de convertir l'âge en entier et ajoute 1 pour obtenir l'âge de l'année prochaine
    age_prochain = int(age) + 1
except:
    # Si une erreur se produit lors de la conversion, affiche un message d'erreur
    print("ERREUR: Vous devez rentrer un nombre pour l'âge")
else:
    # Si aucune erreur ne se produit, affiche le nom et l'âge actuel de l'utilisateur
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    # Affiche l'âge que l'utilisateur aura l'année prochaine
    print("L'an prochain vous aurez " + str(age_prochain) + " ans")