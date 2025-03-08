"""Premier programme
Formation Python
apprendre la programmation"""

def demander_age():
    age_int = 0  # Initialisation de la variable age_int à 0
    # Boucle jusqu'à ce que l'utilisateur entre un âge valide (un nombre entier)
    while age_int == 0:
        age_chaine = input("Quel est votre age ? ")  # Demande à l'utilisateur d'entrer son âge
        try:
            age_int = int(age_chaine)  # Tente de convertir l'entrée en entier
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")  # Affiche un message d'erreur si la conversion échoue
    return age_int  # Retourne l'âge valide
    
#----------------------------------------
#             
# demander le nom
nom = ""  # Initialisation de la variable nom à une chaîne vide
# Boucle jusqu'à ce que l'utilisateur entre un nom non vide
while nom == "":
    nom = input("Quel est votre nom ? ")  # Demande à l'utilisateur d'entrer son nom

# demander l'age
age = demander_age()  # Appelle la fonction pour demander l'âge

# Afficher les résultats
print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")  # Affiche un message avec le nom et l'âge
print("L'an prochain vous aurez " + str(age+1) + " ans")  # Affiche l'âge de l'utilisateur l'année prochaine


