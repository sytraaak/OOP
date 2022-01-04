import random

class Dice:
    def __init__(self, sides=6): #kontruktor s parametrem v základu nastaveném na 6
        self.__sides = sides #atribut počtu stěn - atributy se vytvářejí -> self.název_atributu - pokud dám před název __ bude privátní (zapouzdřený)

    def __str__(self): #textová reprezentace objektu - pokud není definována, tak pouze vypíše cestu k instanci
        return str(f"Kostka s {self.__sides} stěnami")

    def show_sides(self): #zobrazí počet stran
        return self.__sides

    def throw(self):
        return random.randint(1,self.__sides)

kostka = Dice() #bude mít 6 stěn parametr v kontruktoru je nastaven na sides=6
desetistenna = Dice(10) #bude 10ti stenná, protože parametr zadaný do kontruktoru je 10

print(kostka.show_sides()) #zobrazí počet stěn instance
print(desetistenna.show_sides())
print(kostka.throw()) #hod 6ti stěnnou kostkou
print() #zobrazí textovou reprezentaci objektu ze __str__

#hod šestistěnnou
print(f"\n{kostka}")
for _ in range(10):
    print(kostka.throw(), end=" ")

#hod desetistěnnou
print(f"\n{desetistenna}")
for _ in range(10):
    print(desetistenna.throw(), end=" ")