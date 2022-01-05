class Person:
    def __init__(self, jmeno=None, matka="Neznámá", otec="Neznámý"):
        self.jmeno = jmeno
        self.matka = matka
        self.otec = otec

    def __str__(self):
        return str(f"{self.jmeno}")

    def informace(self):
        print(f"""{self.jmeno} \nOtec: {self.otec} \nMatka: {self.matka}\n{30 * "*"}""")

    def rodokmen(self):
        if self.matka == "Neznámá" and self.otec != "Neznámý":
            self.informace()
            self.otec.rodokmen()
        elif self.otec == "Neznámý" and self.matka != "Neznámá":
            self.informace()
            self.matka.rodokmen()
        elif self.otec == "Neznámý" and self.matka == "Neznámá":
            self.informace()
        else:
            self.informace()
            self.otec.rodokmen()
            self.matka.rodokmen()

pepa = Person("Pepa Šnábl")
bouvier = Person("Jackie Bouvier")
jackie = Person("Mr. Bouvier")
abraham = Person("Abraham Simpson", "Neznámá",pepa)
penelope = Person("Penelope Olsen")
marge = Person("Marge Simpson", jackie, bouvier)
homer = Person("Homer Simpson", penelope, abraham)
bart = Person("Bart Simposon", marge, homer)

bart.rodokmen()
homer.rodokmen()




