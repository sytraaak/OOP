from OOP_Arena import Dice

class Fighter():
    def __init__(self, name, maxhp, attack, defense,dice, luck=10, loose=1):
        self.__name = name
        self.__maxhp = maxhp
        self.currentHP = maxhp
        self.__attack = attack
        self.__defense = defense
        self.__dice = dice
        self.__text = ""
        self.__luck = luck
        self.__loose = loose

    def __str__(self):
        return self.__name

    def __repr__(self):
        return str(f"Fighter({self.__name}, {self.__maxhp}, {self.currentHP}, {self.__attack}, {self.__defense}, {self.__dice})")

    @property
    def alive(self):
        return self.currentHP > 0

    def hp_graphic(self):
        cross = int(self.currentHP / 10) * "#"
        space = int(((self.__maxhp - self.currentHP)) / 10) * " "
        if len(cross) < 1:
            cross = "#!"
        return f"[{cross}{space} {self.currentHP}HP]"

    def attack(self, target):
        throw = self.__dice.throw()
        print(f"Hod na útok: {throw}")
        strike = self.__attack + throw
        text = f"{self.__name} útočí za {strike}"
        if throw == self.__luck:    #critical hit
            strike = strike * 2
            text = f"CRITICAL: {self.__name} útočí za {strike}"
        target.block(strike)
        self.__set_text(text)

    def block(self, strike):
        throw = self.__dice.throw()
        print(f"Hod na obranu: {throw}")
        block = self.__defense + throw
        if throw == self.__luck:
            print("CTIRICAL DEFENSE")
            block = block * 2
        elif throw == self.__loose:
            print("CTIRICAL DEFENSE FAILURE")
            block = block / 2
        injury = strike - block
        if injury <= 0:
            text = f"{self.__name} blokuje za {block} a vykril všechna zranění"
        else:
            if injury > 0:
                self.currentHP -= injury
                if self.currentHP <= 0:
                    text = f"{self.__name} blokuje za {block} a obdržel {injury} a zemřel"
                else:
                    text = f"{self.__name} blokuje za {block} a obdržel {injury} zranění"
        self.__set_text(text)


    def __set_text(self, text):
        self.__text = text

    def return_last_text(self):
        return self.__text

class Arena:
    def __init__(self, fighter1, fighter2, dice):
        self.__fighter1 = fighter1
        self.__fighter2 = fighter2
        self.__dice = dice

    def fight(self):
        import time
        import random as _random
        print("Vítejte v Aréně")
        print(f"""Dnes se utkají {self.__fighter1} VS {self.__fighter2}\n\n{40*"*"}""")
        time.sleep(1)
        while (self.__fighter1.alive and self.__fighter2.alive):
            if _random.randint(0, 1):
                (self.__fighter1, self.__fighter2) = (self.__fighter2, self.__fighter1)
            self.__fighter1.attack(self.__fighter2)
            print(self.__fighter1.return_last_text())
            print(self.__fighter2.return_last_text())
            print(f"{self.__fighter1} {self.__fighter1.hp_graphic()}")
            print(f"{self.__fighter2} {self.__fighter2.hp_graphic()}")
            print(40*"*")
            time.sleep(2)
            if self.__fighter2.currentHP > 0:
                self.__fighter2.attack(self.__fighter1)
                print(self.__fighter2.return_last_text())
                print(self.__fighter1.return_last_text())
                print(f"{self.__fighter1} {self.__fighter1.hp_graphic()}")
                print(f"{self.__fighter2} {self.__fighter2.hp_graphic()}")
                print(40 * "*")
                time.sleep(2)
            if self.__fighter1.currentHP <= 0 or self.__fighter2.currentHP <= 0:
                print("Je to konec, jeden zdechl")
                break
            else:
                continue

dice = Dice(10)
#bojovnice
who = Fighter("Who Veliký", 80, 15, 3, dice)
krysak = Fighter("Krysák Zlořádný", 50, 4, 8, dice)
#arena
arena = Arena(who, krysak, dice)
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



