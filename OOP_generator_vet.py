import random

# class Generator:
#     def __init__(self):
#         self.jaky = "velký automatizovaný hubený modrý nejlepší hubený vysoký umělohmotný sluníčkářský".split(" ")
#         self.kdo = "programátor manažer hroch pes jednorožeč kůň žabák T-rex velbloud komunista".split(" ")
#         self.jak = "s oblibou,rychle,pomalu,obscénně".split(",")
#         self.co = "derivoval spal uklízel vařil šukal hledal kombinoval".split(" ")
#         self.kde = "u kamarádky,v parku,na baru,v uličce".split(",")
#
#     def generuj_vetu(self, opakovani:int=1):
#         for _ in range(opakovani):
#             print(f"{random.choice(self.jaky)} {random.choice(self.kdo)} {random.choice(self.jak)} {random.choice(self.co)} {random.choice(self.kde)}")

class Generator:
    def __init__(self):
        self.seznam = ["velký automatizovaný hubený modrý nejlepší hubený vysoký umělohmotný sluníčkářský".split(" "),"programátor manažer hroch pes jednorožeč kůň žabák T-rex velbloud komunista".split(" "),"s oblibou,rychle,pomalu,obscénně".split(","),"derivoval spal uklízel vařil šukal hledal kombinoval".split(" "),"u kamarádky,v parku,na baru,v uličce".split(",")]

    def generuj_vetu(self, opakovani:int=1):

            for _ in range(opakovani):
                veta = ""
                for n in enumerate(self.seznam):
                    veta += f"{random.choice(self.seznam[n[0]])} "
                print(veta)

while True:
    try:
        opakovani = int(input(f"""{40*"*"}\nVložte, kolik chcete vygenerovat vět: """))
        generator = Generator()
        generator.generuj_vetu(opakovani)
    except:
        print("Neplatné zadaní")






