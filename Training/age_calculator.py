# Demande l'année de naissance à l'utilisateur
age = input("En quelle année es-tu né(e) ? ")

# Vérifie que l'entrée est bien un nombre
if age.isdigit():  # Vérifie si age est composé uniquement de chiffres
    total = 2024 - int(age)  # Calcule l'âge
    print(f"Tu as environ {total} ans.")  # Affiche le résultat
else:
    print("Oops ! Entre une année valide (ex: 2000).")  # Message d'erreur si l'entrée n'est pas valide
