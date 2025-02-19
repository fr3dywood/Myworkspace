
caractere = input("Entrez un caractère : ")
nombre_str = input("Entrez un nombre : ")

try:
    nombre = int(nombre_str)
    for i in range(nombre):
        print("*")  # Affiche une étoile à chaque tour
    for i in range(nombre): # Affiche le caractère à chaque tour
        print(caractere)

except ValueError:
    print("Entrez un nombre valide !")
