# Demande un nombre à l'utilisateur
nombre_str = input("Entrez un nombre : ")

try:
    nombre = int(nombre_str)  # Convertit l'entrée en entier

    # Boucle pour afficher les nombres pairs de 1 à nombre
    for i in range(2, nombre + 1, 2):  # Commence à 2, saute de 2 en 2
        print(i)

except ValueError:
    print("Entrez un nombre valide !")
