class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
        return
    
class Hoitola:
    def __init__(self, koiralista):
        # syntyy assosiaatio
        self.koirat = []

# Pääohjelma

koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")

koiralista = [koira1, koira2]
hoitola = Hoitola(koiralista)
print(hoitola.koirat)
print(hoitola.koirat[0].nimi)
