import random

class Dice:
    """
    Nekonečně stěnná kostka
    """
    def roll(self, sides):
        """
        :param sides: int
        :return: random integer between 1 and parameter
        """
        return random.randint(1,sides)

help(int)
dice = Dice()
print(dice.roll(6))

#nová poznámka
