# Demande à l'utilisateur d'entrer un nombre
nombre_str = input("Entrez un nombre : ")

# Vérifie que l'entrée est bien un nombre entier positif
if nombre_str.isdigit():
    # Convertit l'entrée en un entier
    nombre = int(nombre_str)

    # Boucle pour générer et afficher la table de multiplication de 1 à 100
    for multiplicateur in range(1, 101):
        # Affiche le résultat de la multiplication
        print(f"{nombre} x {multiplicateur} = {nombre * multiplicateur}")
else:
    # Affiche un message d'erreur si l'entrée n'est pas un nombre entier valide
    print("Merci de rentrer un nombre entier valide ")