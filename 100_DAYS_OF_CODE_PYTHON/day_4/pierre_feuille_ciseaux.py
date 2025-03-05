# Pierre Feuille Ciseaux
import random  # Importe le module random pour générer des nombres aléatoires

# Définition des représentations graphiques pour Pierre, Feuille et Ciseaux
pierre = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

feuille = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

ciseaux = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# Demande à l'utilisateur de choisir entre Pierre, Feuille ou Ciseaux
choix_utilisateur = int(input("Pierre, Feuille, Ciseaux ! Que choisissez-vous ? 0 pour Pierre, 1 pour Feuille, 2 pour Ciseaux : "))
# Génère un choix aléatoire pour l'ordinateur
choix_ordinateur = random.randint(0, 2)

# Affiche le choix de l'utilisateur
if choix_utilisateur == 0:
    print("Vous avez choisi : Pierre")
    print(pierre)
elif choix_utilisateur == 1:
    print("Vous avez choisi : Feuille")
    print(feuille)
elif choix_utilisateur == 2:
    print("Vous avez choisi : Ciseaux")
    print(ciseaux)

# Affiche le choix de l'ordinateur
if choix_ordinateur == 0:
    print("L'ordinateur a choisi : Pierre")
    print(pierre)
elif choix_ordinateur == 1:
    print("L'ordinateur a choisi : Feuille")
    print(feuille)
elif choix_ordinateur == 2:
    print("L'ordinateur a choisi : Ciseaux")
    print(ciseaux)

# Détermine le résultat du jeu
if choix_utilisateur == choix_ordinateur:
    print("Égalité")
elif (choix_utilisateur == 0 and choix_ordinateur == 2) or (choix_utilisateur == 1 and choix_ordinateur == 0) or (choix_utilisateur == 2 and choix_ordinateur == 1):
    print("Vous avez gagné")
else:
    print("Vous avez perdu")