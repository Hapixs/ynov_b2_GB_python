import random

random.seed(1)

print("\n")


class Dice:
    def __init__(self, faces=6):
        self._faces = faces

    def __str__(self):
        return f"I'm a {self._faces} faces dice"

    def roll(self):
        return random.randint(1, self._faces)


class RiggedDice:
    pass

    # Elle doit hériter de Dice
        # Elle doit polymorpher roll() qui accepte désormais un booléen "rigged"
        # Si rigged est vrai
            # Le dé est truqué
        # Sinon
            # Le dé n'est pas truqué


a_dice = Dice()
print(a_dice)

for _ in range(100):
    print(a_dice.roll())