# Demande à l'utilisateur de saisir son nom et le stocke dans la variable 'nom'
nom = input("Quel est votre nom ? ")

# Initialise la variable 'age' à 0
age = 0

# Boucle tant que 'age' est égal à 0
while age == 0:
    # Demande à l'utilisateur de saisir son âge et le stocke dans la variable 'age_str'
    age_str = input("Quel est votre age ? ")
    try:
        # Essaie de convertir 'age_str' en entier et de le stocker dans 'age'
        age = int(age_str)
    except ValueError:
        # Si une exception ValueError est levée (c'est-à-dire si la conversion échoue), affiche un message d'erreur
        print("ERREUR: Vous devez rentrer un nombre pour l'age")

# Affiche le nom et l'âge de l'utilisateur
print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")

# Affiche l'âge que l'utilisateur aura l'année prochaine
print("L'an prochain vous aurez " + str(age+1) + " ans")