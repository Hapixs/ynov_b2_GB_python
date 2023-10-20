print("\n")
# classe
# objet


class Voiture:
    def __init__(self, couleur="rouge"):
        self.couleur = couleur
        self.vitesse_max = 220
        self.vitesse = 0
        self.est_demarree = False
        print("Création d'une voiture")

    def __str__(self):
        return f"Une voiture {self.couleur} avec une vitesse max de {self.vitesse_max} km/h"


    def demarrer(self):
        if (not self.est_demarree): 
            self.est_demarree = True
            
    def avancer(self, vitesse_cible, pas = 1):
        if (self.est_demarree):
            vitesse_cible = min(vitesse_cible, self.vitesse_max + 1)
            for vit in range(self.vitesse, vitesse_cible, pas):
                self.vitesse = vit
                print(self.vitesse)

ma_voiture = Voiture()
print(ma_voiture)
ma_voiture.demarrer()
ma_voiture.avancer(20)
ma_voiture.avancer(100)
ma_voiture.avancer(500)
# print(ma_voiture.couleur)

ta_voiture = Voiture("bleue")
print(ta_voiture)
# print(ta_voiture.couleur)

# sa_voiture = Voiture()
# print(sa_voiture.couleur)
