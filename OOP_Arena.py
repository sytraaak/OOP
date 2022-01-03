import random

class Dice:
    """
    Nekonečně stěnná kostka
    """
    def __init__(self, sides=6): #kontruktor s klíčovým argumentem nastaveným v základu na 6
        """
        Konstruktor
        """
        self.__sides = sides #definice počtu stěn v kontruktoru - je potřeba, aby bylo zadáno např. self.

    def __str__(self): #textová reprezentace objektu - pokud není definována, tak pouze vypíše cestu k třídě
        return str(f"Kostka s {self.__sides} stěnami")

    def show_sides(self): #zobrazí počet stran
        return self.__sides

    def throw(self):
        return random.randint(1,self.__sides)

sestistenna = Dice() #bude mít 6 stěn protože v základu je nastaveno na 6
desetistenna = Dice(10) #bude 10ti stenná, protože je zadán parametr

print(sestistenna.show_sides())
print(desetistenna.show_sides())
print(sestistenna.throw()) #hod 6ti stěnnou kostkou
print(sestistenna) #zobrazí textovou reprezentaci objektu ze __str__

#hod šestistěnnou
print(f"\n{sestistenna}")
for _ in range(10):
    print(sestistenna.throw(), end=" ")

#hod desetistěnnou
print(f"\n{desetistenna}")
for _ in range(10):
    print(desetistenna.throw(), end=" ")