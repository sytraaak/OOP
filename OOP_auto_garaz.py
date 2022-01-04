class Car:
    def __init__(self, spz, color):
        self.spz = spz
        self.color = color
        self.currentPlace = None
        self.currentPlaceName = None

    def __str__(self):
        return str(f"{self.spz} {self.color}")

    def park(self, where):
        if self.currentPlace == where:
            print("Tady již parkujete")
        elif where.occupied == "Yes":
            print(f"Aktuálně je již zaparkované auto, napřed potřebujete vyjet s {where.currentCar}")
        elif self.currentPlace != None:
            self.depart()
            self.park(where)
            print(f"Již parkujete v garáž {self.currentPlaceName}\nNapřed jste tedy vyjeli a zaparkovali v garáži: {where.name}")
        else:
            where.occupied = "Yes"
            where.currentCar = self
            self.currentPlace = where
            self.currentPlaceName = where.name

    def depart(self):
        self.currentPlace.occupied = "No"
        self.currentPlace.currentCar = None
        self.currentPlace = None
        self.currentPlaceName = None

class Garage:
    def __init__(self, name):
        self.name = name
        self.occupied = "No"
        self.currentCar = None

garage = Garage("garage")
garage1 = Garage("garage1")
car = Car("OLO 13-22", "red")
car1 = Car("BRQ 10-22", "blue")

car.park(garage)
car1.park(garage1)
print(garage.currentCar)
print(garage1.currentCar)
car1.park(garage)
car.park(garage1)
print(garage.currentCar)
print(garage1.currentCar)






