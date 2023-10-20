print("\n")


class Animal:
    _label = "Animal"
    
    def __init__(self, nom):
        self._nom = nom
        print(f"Création de l'{type(self)._label} {self._nom}")

    def nourrir(self):
        print(f"Verifier que l'{type(self)._label} est vivant")
        print("Calcul du stock")
        print(f"Début de l'alimentation de {self._nom}")


class Chat(Animal):
    _label = "Chat"
    
    def nourrir(self):
        super().nourrir()
        print("Petit câlin")


class Requin(Animal):
    _label = "Requin"
    
    def nourrir(self):
        super().nourrir()
        print("On reste à distance")

class Licorne(Animal):
    _label = "Licorne"
    pass


minou = Chat("Miaous")
croc = Requin("Bill Gates")
php_bien_code = Licorne("Symfony")

animaux = [minou, croc, php_bien_code]

minou.nourrir()

animal: Animal
for animal in animaux:
    animal.nourrir()