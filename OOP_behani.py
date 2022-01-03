#Naprogramujte aplikaci, která obsluhuje člověka. Člověk má jméno a únavu, která je zpočátku 0. Může uběhnout určitou
# vzdálenost a také spát určitou dobu. Běháním se jeho únava zvyšuje (1 jednotka únavy na 1 km), spaním se snižuje (10 jednotek únavy na 1 hodinu).
# Navrhněte třídu tak, aby se únava nikdy nemohla dostat z rozmezí 0-20 jednotek.

class Person:
    def __init__(self, unava=0):
        self.__unava = unava

    def behani(self, vzdalenost):
        if self.__unava + vzdalenost > 20:
            print("Tuto vzdalenost už neuběhnu")
        else:
            self.__unava += vzdalenost

    def spanek(self, hodiny):
        if self.__unava - (hodiny * 10) < 0:
            print("Takto dlouho není možné spát")
        else:
            self.__unava -= (hodiny * 10)

    def zobraz(self):
        return self.__unava

josef = Person()
josef.behani(4)
print(josef.zobraz())
josef.behani(4)
print(josef.zobraz())
josef.behani(4)
print(josef.zobraz())
josef.behani(4)
print(josef.zobraz())
josef.behani(4)
print(josef.zobraz())
josef.behani(4)
print(josef.zobraz())
josef.spanek(2)
print(josef.zobraz())
josef.behani(20)
josef.spanek(2)
print(josef.zobraz())



