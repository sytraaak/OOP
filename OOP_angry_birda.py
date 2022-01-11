class Ptak:
    hlad = 100
    vaha = 50

    def snez(self, potrava):
        self.vaha += potrava
        self.hlad -= potrava
        if self.hlad < 0:
            self.hlad = 0

    def __str__(self):
        info = f"Hlad {self.hlad} \nVaha: {self.vaha}"
        if isinstance(self, AngryPtak):
            info = info + f"\nNastvanost: {self.vztek}"
        return info

class AngryPtak(Ptak):
    vztek = 50

    def provokuj(self, provokace):
        if self.hlad < 10:
            self.vztek += provokace
        else:
            self.vztek += provokace * 2

ptak = Ptak()
nastvanej = AngryPtak()
print(ptak)
ptak.snez(20)
print(ptak)
print(nastvanej)

