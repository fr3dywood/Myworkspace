print("Bienvenue dans le calculateur de pourboires !")  # Affiche un message de bienvenue
montant_total = (input("Quel était le montant total de la facture ?"))  # Demande le montant total de la facture
pourboire = (input("Combien de pourboire souhaitez-vous donner ? 10, 12 ou 15 ? "))  # Demande le pourcentage de pourboire
personnes = (input("Combien de personnes pour partager la facture ? "))  # Demande le nombre de personnes pour partager la facture

montant_total = float(montant_total)  # Convertit le montant total en nombre décimal
pourboire = int(pourboire)  # Convertit le pourcentage de pourboire en entier
personnes = int(personnes)  # Convertit le nombre de personnes en entier

pourboire = pourboire / 100  # Convertit le pourcentage de pourboire en décimal
pourboire = montant_total * pourboire  # Calcule le montant du pourboire
montant_total = montant_total + pourboire  # Ajoute le pourboire au montant total
montant_total = montant_total / personnes  # Divise le montant total par le nombre de personnes
montant_total = round(montant_total, 2)  # Arrondit le montant à deux décimales

print(f"Chaque personne doit payer : {montant_total}")  # Affiche le montant que chaque personne doit payer
