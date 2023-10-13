print("\n")
# Boucle While

choix = "o"
note = 0
moyenne = 0
liste_notes = []

# while (choix == "o"):
#     note = float(input("Veuillez saisir une note : "))
#     liste_notes.append(note)
#     moyenne = moyenne + note
    
#     choix = input("Voulez vous saisir une nouvelle note ? (o/n)")
# print(f"La moyenne de la classe est : {round(moyenne / len(liste_notes), 2)}")

# Boucle for

animaux = ["Lion", "Rat", "Requin", "Vautour"]

i = 0
while (i < len(animaux)):
    print(animaux[i])
    i += 1
    
for animal in animaux:
    print(animal)
    
nb_e = 0
    
for car in "Coucou mamie !":
    print(car)
    
for nb in range(0, 101, 2):
    print(nb ** 2)
    
for i in range(0, len(animaux), 1):
    animaux[i] = f"Animal n°{i}: {animaux[i]}"

for elem in enumerate(animaux):
    print(elem)
    
animaux = ["Lion", "Rat", "Requin", "Vautour"] # list
animaux2 = ("Lion", "Rat", "Requin", "Vautour") # tuple

# animaux[0] = "Chien"
print(animaux)
# animaux2[0] = "Chien"
animaux2.append("LOL")