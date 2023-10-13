# if

age = int(input("Quel est votre âge ? "))

if (age < 18):
    print("Statut mineur : remise de 15%")
elif (age >= 18) and (age < 70):
    print("Statut voyageur : pas de remise")
elif (age >= 70) and (age < 150):
    print("Statut sénior : 10% de remise")
else:
    print("Erreur système dans l'âge")
    print("")
    
bool
True
False

age = 14
mineur = age > 18