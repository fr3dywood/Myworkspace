print("Bienvenue dans le calculateur de pourboire !")

# Demande à l'utilisateur le montant total de la facture
total = (input("Quel était le montant total de la facture ? $"))

# Demande à l'utilisateur le pourcentage de pourboire qu'il souhaite donner
pourboire = (input("Combien de pourboire souhaitez-vous donner ? 10, 12 ou 15 ? "))

# Demande à l'utilisateur combien de personnes vont partager la facture
personnes = (input("Combien de personnes pour partager la facture ? "))

# Convertit les entrées utilisateur en types de données appropriés
total = float(total)
pourboire = int(pourboire)
personnes = int(personnes)

# Calcule le montant du pourboire
pourboire = pourboire / 100
pourboire = total * pourboire

# Ajoute le pourboire au total de la facture
total = total + pourboire

# Divise le total par le nombre de personnes pour obtenir le montant par personne
total = total / personnes

# Arrondit le montant à deux décimales
total = round(total, 2)

# Affiche le montant que chaque personne doit payer
print(f"Chaque personne doit payer : ${total}")
