# Utilise la fonction input pour demander à l'utilisateur son nom et stocke la réponse dans la variable 'nom'
nom = input("Quel est votre nom ? ")

# Utilise la fonction input pour demander à l'utilisateur son âge et stocke la réponse dans la variable 'age'
age = input("Quel est votre âge ? ")

# La fonction print affiche du texte à l'écran. Ici, elle utilise une f-string pour afficher "Vous vous appelez {nom}, vous avez {age} ans"
# Les variables 'nom' et 'age' sont insérées dans la chaîne de caractères pour former la phrase complète.
print(f"Vous vous appelez {nom}, vous avez {age} ans")