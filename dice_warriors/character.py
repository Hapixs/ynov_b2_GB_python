print("\n")

from dice import Dice

class Character:
    
    def __init__(self, name, max_hp, attack, defense):
        self._name = name
        self._max_hp = max_hp
        self._current_hp = max_hp
        self._attack_value = attack
        self._defense_value = defense

    def __str__(self):
        return f"{self._name} the Character enter the arena with attack: {self._attack_value} and defense: {self._defense_value}"
    
    def is_alive(self):
        return self._current_hp > 0       
        # return bool(self._current_hp)
        
    # show_healthbar
        # Elle affiche : [oooooooo            ] 8/20hp
            # +++ En une ligne
    def show_healthbar(self):
        missing_hp = self._max_hp - self._current_hp
        healthbar = f"[{"♥" * self._current_hp}{"♡" * missing_hp}] {self._current_hp}/{self._max_hp}hp"
        print(healthbar)

    def decrease_health(self, amount):
        self._current_hp -= amount
        self.show_healthbar()

if __name__ == "__main__":
    
    character1 = Character("Salim", 20, 8, 3)
    print(character1)
    print(character1.is_alive())
    character1.decrease_health(17)