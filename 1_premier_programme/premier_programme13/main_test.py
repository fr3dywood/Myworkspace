age = 0
while age == 0:
    try:
        age = int(input("Donnez votre âge :"))
    except ValueError:
        print("Donnez un âge valide !")
    else:
        print(f"Vous avez {age}, l'année prochaine vous aurez {age+1}")

mdp = ""
while mdp != "Fred":
    mdp = input("Saisissez le mdp :")
    if mdp == "Fred":
        print("Bienvenue Fred !")
        break
    else:
        print("Mot de passe incorrect, essayez encore.")