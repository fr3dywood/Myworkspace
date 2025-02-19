# Demande un nombre à l'utilisateur
nombre_str = input("Entrez un nombre : ")

try:
    nombre = int(nombre_str)  # Convertit l'entrée en entier

    # Initialisation de la somme
    somme = 0

    # Boucle pour additionner les nombres de 1 à nombre
    for i in range(1, nombre + 1):
        somme += i  # Ajoute i à la somme

    # Affichage du résultat
    print(f"La somme des nombres de 1 à {nombre} est : {somme}")

except ValueError:
    print("Veuillez entrer un nombre entier valide.")
