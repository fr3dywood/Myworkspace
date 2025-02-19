# Boucle infinie pour demander le prénom de l'utilisateur
while True:
    # Demande à l'utilisateur d'entrer son prénom et enlève les espaces inutiles
    name = input("Entrez votre prénom : ").strip()
    # Si le prénom n'est pas vide, sortir de la boucle
    if name: 
        break
    # Si le prénom est vide, afficher un message d'erreur
    print("Erreur : Veuillez entrer un prénom valide.")

# Demande à l'utilisateur d'entrer un nombre
nombre_str = input("Entrez un nombre : ")
try:
    # Essaie de convertir l'entrée en un entier
    nombre = int(nombre_str)
    # Boucle pour afficher le message autant de fois que le nombre entré
    for i in range(nombre):
        print(f"Bonjour, je m'appelle {name}, et j'apprends Python")
except ValueError:
    # Si la conversion échoue, afficher un message d'erreur
    print("Entrez un nombre valide !")