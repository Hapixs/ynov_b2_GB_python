choix = "o"
note = 0
moyenne = 0
liste_notes = []

while (choix == "o"):
    note = float(input("Veuillez saisir une note : "))
    liste_notes.append(note)
    moyenne = moyenne + note
    
    choix = input("Voulez vous saisir une nouvelle note ? (o/n)")
print(f"La moyenne de la classe est : {round(moyenne / len(liste_notes), 2)}")