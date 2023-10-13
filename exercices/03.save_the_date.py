print("\n")
date = "26/07/2985"

jour = date[:2]
mois = date[3:5]
annee = date[-4:]

print(jour + "." + mois + "." + annee)
print(jour, mois, annee, sep=".", end=" | ")
print(".".join([jour, mois, annee]))