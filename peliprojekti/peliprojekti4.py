
class Koira:
    def __init__(self, nimi, ikä, rotu, väri, haukahdus="Hau hau"):
        self.nimi = nimi
        self.rotu = rotu
        self.ikä = ikä
        self.väri = väri
        self.haukahdus = haukahdus
        print(f"{self.haukahdus}")
        pass


koira1 = Koira("Rekku", "Chihuahua", 3, "vaalea", "Hau hau")

class Huone:
    def __init__(self, nimi, esine):
        self.nimi = nimi
        self.esine = esine
        pass

huone1 = Huone("Makuuhuone", "koiranpeti")
huone2 = Huone("Keittiö", "koiranruokapussi")
huone3 = Huone("Olohuone", "lämmin viltti")



