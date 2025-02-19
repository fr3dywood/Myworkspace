name = input("Entrez votre prénom :")
nombre_str = input("Entrez un nombre : ")

try:
    nombre = int(nombre_str)
    for i in range(nombre):
        print(f"Bonjour, je m'apelle {name}, et J'apprends Python")

except ValueError:
    print("Entrez un nombre valide !")
