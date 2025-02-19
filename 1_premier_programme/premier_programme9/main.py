# Demande à l'utilisateur de saisir son nom
nom = input("Quel est votre nom ? ")

# Demande à l'utilisateur de saisir son âge
age = input("Quel est votre age ? ")

try:
    # Essaie de convertir l'âge en entier
    age_int = int(age)  
except ValueError:
    # Si une erreur de conversion se produit (par exemple, si l'utilisateur saisit une valeur non numérique),
    # affiche un message d'erreur
    print("ERREUR: Vous devez rentrer un nombre pour l'age")
else:
    # Si aucune erreur ne se produit, affiche le nom et l'âge actuel de l'utilisateur
    print("Vous vous appelez " + nom + ", vous avez " + str(age_int) + " ans")
    # Affiche l'âge que l'utilisateur aura l'année prochaine
    print("L'an prochain vous aurez " + str(age_int + 1) + " ans")