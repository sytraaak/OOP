class Clovek:
    def __init__(self, jmeno=None, vek=None, kamarad=None):
        self.__jmeno = jmeno
        self.__vek = vek
        self.__kamarad = kamarad

    def __str__(self):
        return f"{self.__jmeno}, {self.__vek} let"

    def pozdrav(self):
        print(f"Ahoj, já jsem {self.__jmeno}, je mi {self.__vek} let a můj kamarád je {self.__kamarad}")

pepa = Clovek("Pepa Novák", 35, "Jarda Kornelie") #není možné zadat do třetího parametru pouze jarda, protože jarda ještě nevznikl
jarda = Clovek("Jarda Kornelie", 27, pepa) #zde, protože již existuje instance pro pepa, tak si systém informace dotáhne

pepa.pozdrav()
jarda.pozdrav()


