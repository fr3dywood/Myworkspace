# print("Bienvenue dans la tour de la terreur")
# taille = int(input("quelle est votre taille ? "))

# if taille >= 120 :
#     print("Vous pouvez monter")
#     age = int(input("Quel est votre age ? "))
#     if age <= 12 :
#         print("Vous devez payer 5 euros")
#     elif age <= 18 :
#         print("Vous devez payer 7 euros")
#     else:
#         print("Vous devez payer 12 euros")    
# else:    
#     print("Vous ne pouvez pas monter")
#     print("Merci d'avoir visité la tour de la terreur") 

# # nombre = int(input("Entrez un nombre : "))
# # if nombre % 2 == 0:
# #     print("Le nombre est pair")
# # else:
# #     print("Le nombre est impair")
# # print("Merci d'avoir utilisé mon programme")

weight = int(input("Entrez votre poids en kg : "))
height = float(input("Entrez votre taille en m : "))

bmi = weight / (height ** 2)


if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")