# Demande un nombre à l'utilisateur
nombre_str = input("Entrée un nombre : ")

# Vérifie si l'entrée est bien un nombre entier
if nombre_str.isdigit():
    nombre = int(nombre_str)  # Convertit l'entrée en entier

    # Vérifie si le nombre est pair ou impair
    if nombre % 2 == 0:
        print(f"Le nombre {nombre} est pair.")
    else:
        print(f"Le nombre {nombre} est impair.")
else:
    print("Oops ! Merci d'entrer un nombre entier valide.")  # Message d'erreur si l'entrée n'est pas un nombre
