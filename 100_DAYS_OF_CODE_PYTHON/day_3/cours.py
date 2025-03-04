# TICKET PROJET

print("Bienvenue dans la tour de la terreur")
taille = int(input("quelle est votre taille ? "))
prix = 0

if taille >= 120 :
    print("Vous pouvez monter")
    age = int(input("Quel est votre age ? "))
    if age <= 12 :
        prix = 5
        print("Le ticket enfant est de 5 euros")
    elif age <= 18 :
        prix = 7
        print("Le ticket ado est de 7 euros")
    elif 45 <= age <= 60 :
        prix = 0
        print("Le ticket senior est gratuit")
    else:
        prix = 12
        print("Le ticket adulte est de 12 euros")
    photo = input("Voulez-vous une photo souvenir ? (O/N) ") 
    if photo == "O":
        prix += 3
        print(f"Le prix avec la photo souvenir est de, {prix} euros")
    else:
        print(f"Le prix sans la photo souvenir est de, {prix} euros")
       
else:    
    print("Vous ne pouvez pas monter")
    print("Merci d'avoir visité la tour de la terreur") 
    
# #----------------------------------------------------------------------------

# #IMC PROJET

# # # nombre = int(input("Entrez un nombre : "))
# # # if nombre % 2 == 0:
# # #     print("Le nombre est pair")
# # # else:
# # #     print("Le nombre est impair")
# # # print("Merci d'avoir utilisé mon programme")

# # weight = int(input("Entrez votre poids en kg : "))
# # height = float(input("Entrez votre taille en m : "))

# # bmi = weight / (height ** 2)


# # if bmi >= 25:
# #     print("overweight")
# # elif bmi >= 18.5:
# #     print("normal weight")
# # else:
# #     print("underweight")

#-------------------------------------------------------------------------------

# PIZZA PROJET

# print("Bienvenue chez Fredo Pizza")

# # Boucle pour s'assurer que l'utilisateur entre une taille valide
# while True:
#     size = input("Quelle taille voulez-vous ? S, M, ou L: ")
#     if size in ["S", "M", "L"]:
#         break
#     else:
#         print("Vous avez entré un mauvais caractère. Veuillez réessayer.")

# # Boucle pour s'assurer que l'utilisateur entre une réponse valide pour les pepperoni
# while True:
#     pepperoni = input("Voulez-vous des pepperoni dans votre pizza ? O ou N: ")
#     if pepperoni in ["O", "N"]:
#         break
#     else:
#         print("Vous avez entré un mauvais caractère. Veuillez réessayer.")

# # Boucle pour s'assurer que l'utilisateur entre une réponse valide pour le supplément de fromage
# while True:
#     extra_cheese = input("Voulez-vous un supplément de fromage sur votre pizza ? O ou N: ")
#     if extra_cheese in ["O", "N"]:
#         break
#     else:
#         print("Vous avez entré un mauvais caractère. Veuillez réessayer.")

# prix = 0

# if size == "S":
#     prix += 15
# elif size == "M":
#     prix += 20
# elif size == "L":
#     prix += 25

# if pepperoni == "O":
#     if size == "S":
#         prix += 2
#     else:
#         prix += 3

# if extra_cheese == "O":
#     prix += 1

# print(f"Le prix de votre pizza est de {prix} euros")
# print("Merci d'avoir commandé chez Fredo Pizza")