"""
Exercice : Calculateur d'IMC (Indice de Masse Corporelle)
Objectif : Écrire un programme qui demande à l'utilisateur son poids et sa taille, puis calcule et affiche son IMC.

Instructions :
1) Demander à l'utilisateur son nom.
2) Demander son poids en kilogrammes (float).
3) Demander sa taille en mètres (float).
4) Vérifier que l'utilisateur entre bien des nombres pour le poids et la taille.
5) Calculer l'IMC avec la formule :
    IMC = Poids / (Taille * Taille)
6) Afficher l'IMC avec une interprétation du résultat :
    - IMC < 18.5 : Sous-poids
    - 18.5 ≤ IMC < 24.9 : Poids normal
    - 25 ≤ IMC < 29.9 : Surpoids
    - IMC ≥ 30 : Obésité
"""

# Demande du nom
name = input("Quel est votre nom ? ")

# Demander le poids (float) avec vérification
while True:
    weight_str = input("Quel est votre poids en kg ? ")
    try:
        weight = float(weight_str)
        if weight > 0:
            break
        else:
            print("ERREUR: Le poids doit être un nombre positif.")
    except ValueError:
        print("ERREUR: Vous devez entrer un nombre valide.")

# Demander la taille (float) avec vérification        
while True:
    height_str = input("Quelle est votre taille en mètres (ex: 1.75) ? ")
    try:
        height = float(height_str)
        if height > 0:
            break
        else:
            print("ERREUR: La taille doit être un nombre positif, par exemple : 1.70")
    except ValueError:
        print("ERREUR: Vous devez entrer un nombre valide.")

# Calcul de l'IMC
imc = weight / (height ** 2)
imc = round(imc, 2)  # Arrondi à 2 décimales

# Interprétation de l'IMC
if imc < 18.5:
    interpretation = "Vous êtes en sous-poids."
elif 18.5 <= imc < 24.9:
    interpretation = "Votre poids est normal."
elif 25 <= imc < 29.9:
    interpretation = "Vous êtes en surpoids."
else:
    interpretation = "Vous êtes en obésité."

# Affichage du résultat
print(f"{name}, votre IMC est de {imc}. {interpretation}")
