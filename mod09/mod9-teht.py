# tehtävä 1, 2 ja 3.
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        # self.nopeus = self.nopeus + muutos
        self.nopeus += muutos
        # Auton nopeus ei saa kasvaa huippunopeutta
        # suuremmaksi eikä alentua nollaa pienemmäksi
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        self.kuljettu_matka += auto.nopeus * aika   

        
auto = Auto("ABC-123", 142)
autolista = [
    #autot...
    #autot...
]

# pääohjelma
# while-loop

print("Auton rekisteritunnus", auto.rekisteritunnus)
print("Auton huippunopeus on", auto.huippunopeus)
print("Auton nopeus on", auto.nopeus)
print("Auton kuljettu matka on", auto.kuljettu_matka)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print("Auton nopeus kiihdytyksen jälkeen:", auto.nopeus)
auto.kulje(1.5)
print("Kuljettu matka 1.5h jälkeen on", auto.kuljettu_matka)

auto.kiihdytä(-200)
print("Auton nopeus jarrutuksen jälkeen:", auto.nopeus)