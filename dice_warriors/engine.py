from dice import Dice
from character import Character

if __name__ == "__main__":
    
    #
    #
    #
    
    
    #
    #
    #
    
    character1 = Character("Salim", 20, 8, 3, Dice(6))
    character2 = Character("Lisa", 20, 8, 3, Dice(6))
    
    #
    #
    #
    
    #
    #
    #
    
    while (character1.is_alive() and character2.is_alive()):
        damages = character1.attack()        
        character2.defense(damages)
        
        damages = character1.attack()        
        character2.defense(damages)