print("\n")


class Tuture:
    _liste_couleur = ["rouge", "bleue", "blanche"]
    _compteur = 0
    
    def __init__(self, couleur="rouge"):
        self._couleur = couleur
        self.set_couleur(couleur)
        self._vitesse_max = 220
        self._vitesse_securite = 230
        self._vitesse = 0
        self.est_demarree = False
        print("Création d'une voiture")
        type(self)._compteur += 1

    def __str__(self):
        return f"Une voiture {self._couleur} avec une vitesse max de {self._vitesse_max} km/h"

    # @property
    # def vitesse(self):
    #     print("JE SUIS UNE FONCTION")
    #     return self._vitesse

    # @vitesse.setter
    # def vitesse(self, nouvelle_vitesse):
    #     if (nouvelle_vitesse < self._vitesse_securite):
    #         self._vitesse = nouvelle_vitesse
    #     else:
    #         print("RISQUE DE CASSE MOTEUR !")

    def get_vitesse(self):
        return self._vitesse

    def set_vitesse(self, nouvelle_vitesse):
        if nouvelle_vitesse < self._vitesse_securite:
            self._vitesse = nouvelle_vitesse
            
    def set_couleur(self, nouvelle_couleur):
        if (nouvelle_couleur in type(self)._liste_couleur):
            self._couleur = nouvelle_couleur
        else:
            print("COULEUR NON AUTORISEE !")
            
    def autor_nouvelle_couleur(self, nouvelle_couleur):
        if (not nouvelle_couleur in type(self)._liste_couleur):
            type(self)._liste_couleur.append(nouvelle_couleur)
            
    def get_couleur_autor(self):
        return type(self)._liste_couleur
            
    def get_compteur(self):
        return type(self)._compteur
            
    def demarrer(self):
        if not self.est_demarree:
            self.est_demarree = True

    def avancer(self, vitesse_cible, pas=1):
        if self.est_demarree:
            vitesse_cible = min(vitesse_cible, self._vitesse_max + 1)
            for vit in range(self._vitesse, vitesse_cible, pas):
                self._vitesse = vit
                print(self._vitesse)


ma_voiture = Tuture()
print(ma_voiture)
ma_voiture.demarrer()
ma_voiture.avancer(20)

ma_voiture.set_couleur("bleue")
ma_voiture.autor_nouvelle_couleur("verte")
print(ma_voiture.get_couleur_autor())

# print(ma_voiture.vitesse)
# ma_voiture.vitesse = 500
ta_voiture = Tuture("rouge")
print(ta_voiture.get_couleur_autor())

sa_voiture = Tuture()

print(ma_voiture.get_compteur())