class Uzivatel:
    __minimalni_delka_hesla = 6 #třídní proměnná nastavená na 6
    __dalsi_id = 0

    def __init__(self, jmeno, heslo):
        self.jmeno = jmeno
        self.heslo = heslo
        self.prihlaseny = False
        self.__id = Uzivatel.__dalsi_id
        Uzivatel.__dalsi_id += 1

    @staticmethod #statická metoda
    def zvaliduj_heslo(heslo):
        if len(heslo) >= Uzivatel.minimalni_delka_hesla:
            return True
        else:
            return False

    @staticmethod
    def vrat_id():
        return Uzivatel.__dalsi_id

    @staticmethod
    def vrat_minimalni_delku_hesla():
        return Uzivatel.__minimalni_delka_hesla

    @classmethod #třídní metoda - dostává jako parametr třídu - Třídní metody se hodí v tom případě, že budeme třídu dědit a chceme mít v potomkovi jinou hodnotu třídní proměnné.
    def zvaliduj_heslo(cls, heslo): #standardně se první proměnná pojmenovává cls (funguje podobně jako self)
        if len(heslo) >= cls.__minimalni_delka_hesla:
            return True
        else:
            return False

    def prihlas_se(self, zadane_heslo):
        if self.heslo == zadane_heslo:
            self.prihlaseny = True
            return True
        else:
            self.prihlaseny
            return False

#test programu
u = Uzivatel("Tomáš Marný", "heslojeveslo")
print("ID prvního uživatele je:", u.vrat_id())
v = Uzivatel("Olí Znusinudle", "csfd1fg")
print("ID druhého uživatele je:", v.vrat_id())
print("Minimální délka hesla uživatele je:",
      Uzivatel.vrat_minimalni_delku_hesla())
print('Validnost hesla "heslo" je:',
      Uzivatel.zvaliduj_heslo("heslo"))
input()



# jmeno = input("Vložte jméno: ")
# heslo = input("Vložte heslo: ")
# user = Uzivatel(jmeno, heslo)
# print(user.zvaliduj_heslo(heslo))
# print(user.prihlas_se(heslo))
# print(user.vrat_id())

# print(f"Pepova minimální délka hesla je: {Uzivatel.minimalni_delka_hesla}")
# pepa = Uzivatel("pepiczek", "zrzounstvi17")
# pepa.minimalni_delka_hesla = 3 #pro danou instanci třídy mohu změnit třídní proměnnou
# print(f"Pepovo ID je: {pepa.heslo}")
# print(f"Pepovo heslo je platné: {Uzivatel.zvaliduj_heslo(pepa.heslo)}")

