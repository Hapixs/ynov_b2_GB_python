print("\n")
# classe
# objet


class Voiture:
    def __init__(self, couleur="rouge"):
        self.couleur = couleur
        self._vitesse_max = 220
        self._vitesse_securite = 230
        self._vitesse = 0
        self.est_demarree = False
        print("Création d'une voiture")

    def __str__(self):
        return f"Une voiture {self.couleur} avec une vitesse max de {self._vitesse_max} km/h"

    @property
    def vitesse(self):
        print("JE SUIS UNE FONCTION")
        return self._vitesse

    @vitesse.setter
    def vitesse(self, nouvelle_vitesse):
        if (nouvelle_vitesse < self._vitesse_securite):
            self._vitesse = nouvelle_vitesse
        else:
            print("RISQUE DE CASSE MOTEUR !")

    def get_vitesse(self):
        return self._vitesse
    
    def set_vitesse(self, nouvelle_vitesse):
        if (nouvelle_vitesse < self._vitesse_securite):
            self._vitesse = nouvelle_vitesse

    def demarrer(self):
        if not self.est_demarree:
            self.est_demarree = True

    def avancer(self, vitesse_cible, pas=1):
        if self.est_demarree:
            vitesse_cible = min(vitesse_cible, self._vitesse_max + 1)
            for vit in range(self._vitesse, vitesse_cible, pas):
                self._vitesse = vit
                print(self._vitesse)


ma_voiture = Voiture()
print(ma_voiture)
ma_voiture.demarrer()
ma_voiture.avancer(20)

print(ma_voiture.vitesse)
ma_voiture.vitesse = 500