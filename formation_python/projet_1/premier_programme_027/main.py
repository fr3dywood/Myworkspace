def afficher_informations_personne(nom, age, taille=0):
    print()
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")

    print("L'an prochain vous aurez " + str(age + 1) + " ans")

    if age == 17:
        print("Vous êtres presque majeur")
    elif age < 18:
        print("Vous êtes adolescent")
    elif age == 1 or age == 2:
        print("Vous êtes un bébé")
    elif age == 18:
        print("Tout juste majeur : Félicitation")
    elif age > 60:
        print("Vous êtes sénior")
    elif age < 10:
        print("Vous êtes enfant")
    elif age >= 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")

    # afficher la taille
    if taille != 0:
        print("Votre taille : " + str(taille) + " m")

afficher_informations_personne("Jean", 1, 1.75)