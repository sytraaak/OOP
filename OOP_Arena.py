import random

class Dice:
    def __init__(self, sides=6): #kontruktor s parametrem v základu nastaveném na 6
        self.__sides = sides #atribut počtu stěn - atributy se vytvářejí -> self.název_atributu - pokud dám před název __ bude privátní (zapouzdřený)

    def __str__(self): #textová reprezentace objektu - pokud není definována, tak pouze vypíše cestu k instanci - vrací vždy str
        return str(f"Kostka s {self.__sides} stěnami")

    def __repr__(self): #Vrací v řetězci kód konstruktoru pro funkci eval(). V tomto případě vrací konstruktor kostky
        return str(f"Dice({self.__sides})")

    def show_sides(self): #zobrazí počet stran
        return self.__sides

    def throw(self):
        return random.randint(1,self.__sides)


#vytvoření instance
kostka = Dice() #bude mít 6 stěn parametr v kontruktoru je nastaven na sides=6
desetistenna = Dice(10) #bude 10ti stenná, protože parametr zadaný do kontruktoru je 10
nova_kostka = eval(repr(desetistenna)) #vytvoří kopii kostky desetistenne


print(kostka.show_sides()) #zobrazí počet stěn instance
print(desetistenna.show_sides()) #zobrazí počet stěn instance desetistenna
print(nova_kostka.show_sides()) #zobrazí počet stěn kopie kostky
print(kostka.throw()) #hod 6ti stěnnou kostkou

#hod šestistěnnou
print(f"\n{kostka}")  #zobrazí textovou reprezentaci objektu ze __str__
for _ in range(10):
    print(kostka.throw(), end=" ")

#hod desetistěnnou
print(f"\n{desetistenna}")
for _ in range(10):
    print(desetistenna.throw(), end=" ")