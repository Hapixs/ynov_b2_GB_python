print("\n")
# classe
# objet


class Voiture:
    def __init__(self, couleur = "rouge"):
        self.couleur = couleur
        self.vitesse_max = 220
        print("Création d'une voiture")

    def __str__(self):
        return f"Une voiture {self.couleur} avec une vitesse max de {self.vitesse_max} km/h"

ma_voiture = Voiture()
print(ma_voiture)
# print(ma_voiture.couleur)

ta_voiture = Voiture("bleue")
print(ta_voiture)
# print(ta_voiture.couleur)

# sa_voiture = Voiture()
# print(sa_voiture.couleur)
