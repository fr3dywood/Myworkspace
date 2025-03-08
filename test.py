def demander_nom():
    nom_str = ""
    while nom_str == "":
        nom_str = input("Quel est votre nom ? ")
    return nom_str
def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre âge ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print(nom_personne + " Entrez un âge valide !")
    return age_int

nom1 = demander_nom()
nom2 = demander_nom()
age1 = demander_age(nom1)
age2 = demander_age(nom2)

print(f"Bonjour {nom1} vous avez {age1} ans, l'année prochaine vous aurez {age1 + 1}")
print(f"Bonjour {nom2} vous avez {age2} ans, l'année prochaine vous aurez {age2 + 1}")