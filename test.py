def demander_nom():
    nom = ""
    while nom == "" or not nom.isalpha():
        nom = input("Entrez votre nom :")
    return nom

def demander_age():
    age_int = 0
    while age_int == 0:
        age_str = input("Entrez votre age : ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("Entrez un âge valide ! ")
    return age_int

nom = demander_nom()
age = demander_age()

print(f"Bonjour {nom} vous avez {age} ans")
print(f"L'année prochaine vous aurez {age + 1} ans")