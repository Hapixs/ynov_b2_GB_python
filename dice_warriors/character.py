print("\n")

from dice import Dice

class Character:
    
    def __init__(self, name: str, max_hp: int, attack: int, defense: int, dice: Dice):
        self._name = name
        self._max_hp = max_hp
        self._current_hp = max_hp
        self._attack_value = attack
        self._defense_value = defense
        self._dice = dice

    def __str__(self):
        return f"""{self._name} the Character enter the arena with :
    ■ attack: {self._attack_value} 
    ■ defense: {self._defense_value}"""
        
    
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
        
    def attack(self):
        roll = self._dice.roll()
        damages = self._attack_value + roll
        print(f"{self._name} attack with {damages} damages (attack: {self._attack_value} + roll: {roll})")
        return damages
    
    def defense(self, damages):
        roll = self._dice.roll()
        wounds = damages - self._defense_value - roll
        print(f"{self._name} take {wounds} wounds (damages: {damages} - defense: {self._defense_value} - roll: {roll})")
        self.decrease_health(wounds)

if __name__ == "__main__":
    character1 = Character("Salim", 20, 8, 3, Dice(6))
    # character2 = Character("Lisa", 18, 7, 3, Dice(10))
    print(character1)
    
    damages = character1.attack()
    character1.defense(damages)