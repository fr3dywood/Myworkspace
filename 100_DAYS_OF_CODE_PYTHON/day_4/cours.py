import random  # Importe le module random pour générer des nombres aléatoires

# # Génère un entier aléatoire entre 1 et 10
# random_integer = random.randint(1, 10)
# print(random_integer)

# # Importe un module personnalisé (commenté car non utilisé)
# # import my_module

# # Affiche un nombre favori défini dans le module personnalisé (commenté car non utilisé)
# # print(my_module.my_favourite_number)

# # Génère un nombre flottant aléatoire entre 0 et 10
# # random_number_0_to_1 = random.random() * 10
# # print(random_number_0_to_1)

# # Génère un nombre flottant aléatoire entre 1 et 10
# # random_float = random.uniform(1, 10)
# # print(random_float)

# Génère un entier aléatoire entre 0 et 1 pour simuler un lancer de pièce
random_integer = random.randint(0, 1)
# Demande à l'utilisateur de choisir entre "Pile" ou "Face"
pile_face = input("Pile ou Face ? ").capitalize()

# Vérifie le résultat du lancer de pièce et compare avec le choix de l'utilisateur
if random_integer == 0:
    print("Pile")
    if pile_face == "Pile":
        print("Vous avez gagné !")
    else:
        print("Vous avez perdu")
else:
    print("Face")
    if pile_face == "Face":
        print("Vous avez gagné !")
    else:
        print("Vous avez perdu")

# # Liste des états américains 
# etats_americains = [
#     "Alabama", "Alaska", "Arizona", "Arkansas", "Californie", "Caroline du Nord", "Caroline du Sud", "Colorado", 
#     "Connecticut", "Dakota du Nord", "Dakota du Sud", "Delaware", "Floride", "Géorgie", "Hawaï", "Idaho", "Illinois", 
#     "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiane", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", 
#     "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New York", "Nouveau-Mexique", 
#     "Ohio", "Oklahoma", "Oregon", "Pennsylvanie", "Rhode Island", "Tennessee", "Texas", "Utah", "Vermont", "Virginie", 
#     "Virginie-Occidentale", "Washington", "Wisconsin", "Wyoming"
# ]

# # Ajoute un élément à la liste des états américains
# etats_americains.append("Fred")

# # Ajoute plusieurs éléments à la liste des états américains
# etats_americains.extend(["Fred", "Pablo"])

# # Modifie un élément de la liste des états américains
# etats_americains[1] = "Abraska"

# # Affiche la liste des états américains
# print(etats_americains)

# # Liste des amis 
# liste_amis = ["Fred", "Sengvanna", "Jessyme", "Gael", "Mika", "Louis"]

# # Sélectionne un ami aléatoirement dans la liste
# print(random.choice(liste_amis))

# # Sélectionne un ami aléatoirement dans la liste et l'affiche
# choix_ami = random.choice(liste_amis)
# print(choix_ami)

# # Génère un entier aléatoire pour sélectionner un ami dans la liste
# ami_aleatoire = random.randint(0, 5)
# # Affiche l'ami sélectionné aléatoirement
# print(liste_amis[ami_aleatoire])