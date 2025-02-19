# Demande à l'utilisateur d'entrer un nombre
nombre_str = input("Entrez un nombre : ")

try:
    nombre = int(nombre_str)  # Essaye de convertir l'entrée en entier
    for i in range(nombre, 0, -1):  # Compte à rebours
        print(i)
    print("C'est parti !")
except ValueError:  # Si l'entrée n'est pas un nombre
    print("Oops ! Ce n'est pas un nombre.")  # Affiche un message d'erreur
