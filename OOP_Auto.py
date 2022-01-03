class Auto:
    def naloz(self, tuny):
        self.naklad += tuny
        if self.naklad > 3:
            print("Překročen váhový limit, tento náklad není možné naložit")
            self.naklad -= tuny
        else:
            print(f"Naloženo {tuny}")

    def vyloz(self, tuny):
        self.naklad -= tuny
        if self.naklad < 0:
            print("Chcete vyložit více nákladu než je naloženo. Náklad nebyl vyložen")
            self.naklad += tuny
        else:
            print(f"Vyloženo {tuny}")

    def jed(self, vzdalenost, rychlost):
        self.rychlost += rychlost
        self.vzdalenost += vzdalenost
        cas = self.vzdalenost / self.rychlost
        cesta = f"Auto jelo rychlostí {self.rychlost}, uejlo {self.vzdalenost} km, za {cas} hodin"
        self.rychlost = 0
        self.pozice += vzdalenost
        return print(cesta)

class Ridic:
    def nastup(self):
        if auto.ridic == 1:
            print("Už jste v autě")
        else:
            print("Nastoupili jste do auta")
            auto.ridic = 1

    def vystup(self):
        if auto.ridic == 0:
            print("Už jste venku")
        else:
            print("Vystoupili jste")
            auto.ridic = 0

class Menu():
    def zobrazeni(self):
        menu.volba = int(input("""Co chcete provést?
                1. Nakládat
                2. Vykládat
                3. Jed na místo
                4. Vystoupit
                5. Nastoupit
                6. EXIT\nZadejte číselnou volbu: """))
    def volba1(self):
        tuny = float(input(f"Zadejte kolik tun nánkladu chcete naložit. Aktuální náklad je {auto.naklad} tun\nPočet tun na naložení: "))
        auto.naloz(tuny)
    def volba2(self):
        tuny = float(input(f"Zadejte kolik tun nánkladu chcete vyložit. Aktuální náklad je {auto.naklad} tun\nPočet tun na naložení: "))
        auto.vyloz(tuny)
    def volba3(self):
        if auto.ridic == 1:
            menu.zjisteni_cesty()
        else:
            print("Popíjeli jste venku lahváče, podívali jste se na hodinky a zjistili, že musíte jet. Nastoupili jste")
            auto.ridic = 1
            menu.zjisteni_cesty()
    def volba4(self):
        ridic.vystup()
    def volba5(self):
        ridic.nastup()
    def volba6(self):
        print("Konec hry")
        menu.zapnuto = 0
    def zjisteni_cesty(self):
        vzdalenost = int(input("Vložte kolik KM chcete ujet: "))
        rychlost = int(input("Vložte jakou rychlostí chcete jet: "))
        auto.jed(vzdalenost, rychlost)

menu = Menu()
menu.zapnuto = 1
menu.volba = 0

#class ridic class benzinka
#penize
#cena benzinu
#unava

ridic = Ridic()
ridic.jmeno = "Automaticky pilot"

auto = Auto()
auto.naklad = 0
auto.vzdalenost = 0
auto.rychlost = 0
auto.ridic = 0
auto.nadrz = 150
auto.pozice = 0

while menu.zapnuto == 1:
    try:
        menu.zobrazeni()
        if menu.volba == 1:
            menu.volba1()
        if menu.volba == 2:
            menu.volba2()
        if menu.volba == 3:
            menu.volba3()
        if menu.volba == 4:
            menu.volba4()
        if menu.volba == 5:
            menu.volba5()
        if menu.volba == 6:
            menu.volba6()
    except:
        print("Zadali jste neplatnou volbu")






