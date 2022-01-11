class Prevodnik():
    @staticmethod
    def radian_na_uhel(radian):
        return (radian * 180) / 3.14

    @staticmethod
    def uhel_na_radian(uhel):
        return (uhel * 3.14) / 180

print(Prevodnik.radian_na_uhel(3.14))
print(Prevodnik.uhel_na_radian(180))
