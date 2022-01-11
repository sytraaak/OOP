import math

class Tvar:
    def __init__(self, barva):
        self._barva = barva

class Trojuhelnik(Tvar):
    def __init__(self, barva, a, b, c):
        super().__init__(barva)
        self.__a = a
        self.__b = b
        self.__c = c

    def obsah(self):
        s = (self.__a + self.__b + self.__c) / 2
        S = math.sqrt(s*(s - self.__a)*(s - self.__b)*(s - self.__c))
        return S

class Obdelnik(Tvar):
    def __init__(self, barva, sirka, vyska):
        super().__init__(barva)
        self.__sirka = sirka
        self.__vyska = vyska

    def obsah(self):
        s = self.__sirka * self.__vyska
        return s

trojuhelnik = Trojuhelnik("cerveny", 25, 15, 15)
obdelnik = Obdelnik("černý", 3, 26)
obsah = 4 * trojuhelnik.obsah() + obdelnik.obsah()
print(obsah)
print(trojuhelnik._barva)
print(obdelnik._barva)