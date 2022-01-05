class Location:
    text, east, west, north, south = None, None, None, None, None

    def __init__(self, name, text):
        self.name = name
        self.text = text

    def __str__(self):
        smery = ""
        if self.east == 1:
            smery += "východ "
        if self.west == 1:
            smery += "západ "
        if self.north == 1:
            smery += "sever "
        if self.south == 1:
            smery += "jih "

        return f"""{self.name}\n*******\n{self.text}\nMůžeš již na {smery}"""

hrad = Location("Hrad", "Nacházíš se na hradě?")
hrad.east = 1

les = Location("Les", "Trčíte v lese, nikde nic, jenom tady řvou ptáci")
les.east, les.west = 1, 1

les1 = Location("Les", "Trčíte v lese, nikde nic, jenom tady řvou ptáci, ale směrem na východ jde vidět rybník")
les1.east, les1.west = 1, 1

les2 = Location("Les u domu", "Nacházíš se v lese, na východ od tebe skrz strom jde vidět dům")
les2.north, les2.east = 1, 1

rozcesti = Location("Rozcesti", "Jste na rozcestí, nic moc zajímavýho tady není")
rozcesti.east, rozcesti.west, rozcesti.south = 1, 1, 1

rybnik = Location("Rybník", "Jste u rybníka, je tady stánek s pivek a klobásou")
rybnik.west = 1

dum = Location("Dům", "Stojíte před vážně divným domem")

class Player:
    def __init__(self, jmeno):
        self.jmeno = jmeno

class Game:
    lokace = hrad
    way = 0
    on = 1

    def switch(self):
        while self.on == 1:
            print(hra.lokace)
            self.way = input("Kam chceš jít?: ")
            hra.move()

    def move(self):
        if self.way == "konec":
            print("Ukončuji program")
            self.on = 0
        elif self.lokace == hrad:
            if self.way == "východ":
                self.lokace = les
        elif self.lokace == les:
            if self.way == "západ":
                self.lokace = hrad
            if self.way == "východ":
                self.lokace = rozcesti
        elif self.lokace == rozcesti:
            if self.way == "západ":
                self.lokace = les
            if self.way == "východ":
                self.lokace = les1
            if self.way == "jih":
                self.lokace = les2
        elif self.lokace == les1:
            if self.way == "západ":
                self.lokace = rozcesti
            if self.way == "východ":
                self.lokace = rybnik
        elif self.lokace == rybnik:
            if self.way == "západ":
                self.lokace = les1
        elif self.lokace == les2:
            if self.way == "východ":
                self.lokace = dum
            if self.way == "sever":
                self.lokace = rozcesti
        elif self.lokace == dum:
            if self.way == "západ":
                self.lokace = les1


hrac = Player("Honzík")
hra = Game()
hra.switch()








