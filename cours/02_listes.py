print("\n")

eleves = ["Tom", "Arnaud", "Marie", "Lise", "Jules"]
#           |       |          |       |       |
#           0       1          2       3       4
#                              -3      -2     -1
notes = [10.0, 5.5, 18.0, 19.5, 12.5]
dates = []
dates = list()

print(eleves)
print(eleves[0])
print(eleves[len(eleves) -1])

print(eleves[-1])
print(eleves[len(eleves) * -1])

# Slicing

jours = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"]
print(jours[0:5])
print(jours[:5])
print(jours[3+1:6])
nouveau_tab = jours

eleves = ["Tom", "Arnaud", "Marie", "Lise", "Jules"]
notes = [10.0, 5.5, 18.0, 19.5, 12.5]

eleves.append("Salim")
notes.append(16.5)

eleves.pop(0)
# eleves.remove("Bernard")

# Les chaines de carac sont des listes

phrase = ".... est en retard !"
print(phrase)
print(phrase[-8:])

phrase = phrase[:-1] + "?"

print(phrase)