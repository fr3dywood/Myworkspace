# Demander à l'utilisateur son nom
nom = input("Quel est votre nom ? ")

# Demander à l'utilisateur son âge
age = input("Quel est votre age ? ")

# Convertir l'âge en entier et calculer l'âge l'année prochaine
age_prochain = int(age) + 1

# Afficher le nom et l'âge actuel
# La fonction str() convertit l'entier 'age' en chaîne de caractères pour pouvoir le concaténer avec d'autres chaînes
print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")

# Afficher l'âge l'année prochaine
# La fonction str() convertit l'entier 'age_prochain' en chaîne de caractères pour pouvoir le concaténer avec d'autres chaînes
print("L'an prochain vous aurez " + str(age_prochain) + " ans")

