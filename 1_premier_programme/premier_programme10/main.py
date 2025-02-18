# Initialiser la variable mot_de_passe avec une chaîne vide
mot_de_passe = "" 

# Boucle tant que le mot de passe n'est pas "TOTO"
while not mot_de_passe == "TOTO":
    # Demander à l'utilisateur de saisir le mot de passe
    mot_de_passe = input("Quel est le mot de passe ? ")

# Afficher un message lorsque le mot de passe correct est saisi
print("Mot de passe correct, vous avez accès au compte")