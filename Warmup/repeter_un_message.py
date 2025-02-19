# Demande un message et un nombre à l'utilisateur
message = input("Entrez un message : ")
nombre_str = input("Entrez un nombre : ")

try:
    nombre = int(nombre_str)  # Convertit l'entrée en entier

    # Répète le message "nombre" fois
    for i in range(nombre):  
        print(message)  # Affiche le message

except ValueError:
    print("Entrez un nombre valide.")
