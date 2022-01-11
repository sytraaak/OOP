#Naprogramujte aplikaci, která obsluhuje člověka. Člověk má jméno a únavu, která je zpočátku 0. Může uběhnout určitou
# vzdálenost a také spát určitou dobu. Běháním se jeho únava zvyšuje (1 jednotka únavy na 1 km), spaním se snižuje (10 jednotek únavy na 1 hodinu).
# Navrhněte třídu tak, aby se únava nikdy nemohla dostat z rozmezí 0-20 jednotek.

class Person:
    def __init__(self, unava=0):
        self._unava = unava

    def behani(self, vzdalenost):
        if self._unava + vzdalenost > 20:
            print("Tuto vzdalenost už neuběhnu")
        else:
            self._unava += vzdalenost

    def spanek(self, hodiny):
        if self._unava - (hodiny * 10) < 0:
            print("Takto dlouho není možné spát")
        else:
            self._unava -= (hodiny * 10)

    def zobraz(self):
        return f"Únava: {self._unava}"

class Pythonista(Person):
    def __init__(self, unava, ide):
        super().__init__(unava)
        self.__ide = ide
        self.radky = 0

    def programuj(self, radky):
        if self._unava + ((self.radky + radky) / 10) > 20:
            print(f"Tohle už nezvládnu\nNaprogramuji už pouze {10*(round(20 - self._unava - (self.radky / 10),1))} řádku")
        else:
            self.radky += radky
            if self.radky + radky >= 10:
                self._unava += (self.radky - (self.radky % 10)) / 10
                self.radky = self.radky % 10

    def __str__(self):
        return f"Řádky: {self.radky} Únava: {self._unava}"

poskok = Pythonista(0, "PyCharm")
print(poskok)
poskok.behani(19)
poskok.programuj(1)
print(poskok)
poskok.programuj(8)
poskok.programuj(8)
print(poskok.radky)




