#Vytvořte aplikaci, evidující dva lidi. Každý člověk má jméno, věk a přítele. Každý člověk se také umí představit a to
# tak, že vypíše své jméno, věk a jméno svého kamaráda. Vytvořte v aplikaci 2 lidi, kteří se navzájem kamarádí, a nechte je se představit.

class Clovek:
    def pozdrav(self):
        print(f"Ahoj, já jsem {self.jmeno}, je mi {self.vek} let a můj kamarád je {self.kamarad}")

pepa = Clovek()
pepa.jmeno = "Pepa Novák"
pepa.kamarad = "Jarda Kornelie"
pepa.vek = 33

jarda = Clovek()
jarda.jmeno = "Jarda Kornelie"
jarda.kamarad = "Pepa Novák"
jarda.vek = 67

pepa.pozdrav()
jarda.pozdrav()

#nová poznámka aa
