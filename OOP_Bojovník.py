from OOP_Arena import Dice

class Fighter():
    def __init__(self, name, maxhp=80, attack=12, defense=5,dice=Dice(10), luck=10, loose=1, potion=0):
        self._name = name
        self._maxhp = maxhp
        self._currentHP = maxhp
        self._attack = attack
        self._defense = defense
        self._dice = dice
        self._text = None
        self._luck = luck
        self._loose = loose
        self._throw = None
        self._strike = None
        self._potion = potion

    def __str__(self):
        return self._name

    def __repr__(self):
        return str(f"Fighter({self._name}, {self._maxhp}, {self._currentHP}, {self._attack}, {self._defense}, {self._dice})")

    @property
    def alive(self):
        return self._currentHP > 0

    def stats_info(self, actual, max):
        cross = int(actual / 10) * "#"
        space = int(((max - actual)) / 10) * " "
        if len(cross) < 1:
            cross = "#!"
        return f"[{cross}{space} {actual}]"

    def hp_graphic(self):
        return self.stats_info(self._currentHP, self._maxhp)

    def attack(self, target):
        self._throw = self._dice.throw()
        print(f"Hod na útok: {self._throw}")
        self._strike = self._attack + self._throw
        self._set_text(f"{self._name} útočí za {self._strike}")
        self.critical(target)
        target.block(self._strike)

    def critical(self, target):
        if self._throw == self._luck:    #critical hit
            self._strike = self._strike * 2
            if self.__class__ == Mage and self._mana == self._max_mana:
                self._set_text(f"Magic CRITICAL: {self._name} útočí za {self._strike}")
            else:
                self._set_text(f"CRITICAL: {self._name} útočí za {self._strike}")
            target.get_potion(target)

    def block(self, strike):
        throw = self._dice.throw()
        print(f"Hod na obranu: {throw}")
        block = self._defense + throw
        if throw == self._luck:
            print("CTIRICAL DEFENSE")
            block = block * 2
        elif throw == self._loose:
            print("CTIRICAL DEFENSE FAILURE")
            block = block / 2
        injury = strike - block
        if injury <= 0:
            self._set_text(f"{self._name} blokuje za {block} a vykril všechna zranění")
        else:
            if injury > 0:
                self._currentHP -= injury
                if self._currentHP <= 0:
                    text = f"{self._name} blokuje za {block} a obdržel {injury} a zemřel"
                else:
                    text = f"{self._name} blokuje za {block} a obdržel {injury} zranění"
            self._set_text(text)
        self.use_potion()

    def get_potion(self, target):
        target._potion += 1
        print(f"{target} získává léčivý lektvar")

    def use_potion(self):
        if self._currentHP < (self._maxhp / 4) and self._potion > 0 and self._currentHP > 0:
            self._potion -= 1
            heal = self._maxhp / 3
            self._currentHP += heal
            print(f"Výlečili jste se o {heal}")

    def _set_text(self, text):
        self._text = text

    def return_last_text(self):
        return self._text

class Mage(Fighter):
    def __init__(self, name, maxhp, attack, defense, dice, luck, loose, potion, mana, max_mana, magic_attack):
        super().__init__(name, maxhp, attack, defense, dice, luck, loose, potion)
        self._mana = mana
        self._max_mana = max_mana
        self.__magic_attack = magic_attack

    def mana_graphic(self):
        return self.stats_info(self._mana, self._max_mana)

    def attack(self, target):
        if self._mana != self._max_mana:
            self._mana += 10
            super().attack(target)
        else:
            self._throw = self._dice.throw()
            print(f"Hod na útok: {self._throw}")
            self._strike = self.__magic_attack + self._throw
            self._set_text(f"MAGIC ATTACK: {self._name} útočí za {self._strike}")
            super().critical(target)
            target.block(self._strike)
            self._mana = 0

class Arena:
    def __init__(self, fighter1, fighter2, dice):
        self.__fighter1 = fighter1
        self.__fighter2 = fighter2
        self.__dice = dice

    def show_fighter(self, fighter):
        print(fighter)
        print(f"Zdraví: {fighter.hp_graphic()}")
        if isinstance(fighter, Mage):
            print(f"Mana: {fighter.mana_graphic()}")
        print(f"Počet lektvarů: {fighter._potion}")

    def print_message(self, message):
        print(message)

    def print_separator(self):
        print(40*"*")

    def fight(self):
        import time
        import random as _random
        def sleeper():
            time.sleep(2)
        print("Vítejte v Aréně")
        print(f"""Dnes se utkají {self.__fighter1} VS {self.__fighter2}\n\n{40*"*"}""")
        sleeper()
        while (self.__fighter1.alive and self.__fighter2.alive):
            if _random.randint(0, 1):
                (self.__fighter1, self.__fighter2) = (self.__fighter2, self.__fighter1)
            self.__fighter1.attack(self.__fighter2)
            self.print_separator()
            self.show_fighter(self.__fighter1)
            self.show_fighter(self.__fighter2)
            self.print_message(self.__fighter1.return_last_text())
            self.print_message(self.__fighter2.return_last_text())
            self.print_separator()
            sleeper()
            if self.__fighter2._currentHP > 0:
                self.__fighter2.attack(self.__fighter1)
                self.print_separator()
                self.show_fighter(self.__fighter1)
                self.show_fighter(self.__fighter2)
                self.print_message(self.__fighter2.return_last_text())
                self.print_message(self.__fighter1.return_last_text())
                self.print_separator()
                sleeper()
            if self.__fighter1._currentHP <= 0 or self.__fighter2._currentHP <= 0:
                print("Je to konec, jeden zdechl")
                break
            else:
                continue

#kostka
dice = Dice(4)
dice1 = Dice(12)
#bojovníci
who = Fighter("Who Veliký", 80, 10, 8, dice, 4, 1, 1)
krysak = Fighter("Krysák Zlořádný")
marta = Mage("Marťa", 50, 15, 5, dice1,12, 1, 0, 10, 30, 50)
#arena
arena = Arena(who, marta, dice)
#souboj
arena.fight()

#Můje návrh Arény (skrytá)

#SKRYTÁ MOJE ARENA
# class Arena:
#     def __init__(self, rounds=5):
#         self.__rounds = rounds
#
#     def fight(self, fighter1, fighter2):
#         for round in range(self.__rounds):
#             print(f"{fighter1} Naživu: {fighter1.alive} {fighter1.hp_graphic()}")
#             print(f"{fighter2} Naživu: {fighter2.alive} {fighter2.hp_graphic()}")
#             fighter1.attact(fighter2)
#             print(fighter1.return_last_text())
#             print(fighter2.return_last_text())
#             fighter2.attact(fighter1)
#             print(f"{fighter1} Naživu: {fighter1.alive} {fighter1.hp_graphic()}")
#             print(f"{fighter2} Naživu: {fighter2.alive} {fighter2.hp_graphic()}")
#             print(fighter2.return_last_text())
#             print(fighter1.return_last_text())
#         if fighter1.alive or fighter2.alive != True:
#             print("Někdo umřel")
#             exit()

#kostka



