print("\n")

from dice import Dice

class Character:
    
    def __init__(self, name, attack, defense, max_hp):
        self._name = name
        self._attack_value = attack
        self._defense_value = defense
        self._max_hp = max_hp

    def __str__(self):
        return f"{self._name} the Character enter the arena with attack: {self._attack_value} and defense: {self._defense_value}"
    
    # is_alive
        # retourne vrai ou faux
            # ++ En une ligne
        
    # show_healthbar
        # Elle affiche : [oooooooo            ] 8/20hp
            # +++ En une ligne

if __name__ == "__main__":
    
    character1 = Character("Salim", 20, 8, 3)
    print(character1)