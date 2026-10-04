from maailma.maailma import keittiö, olohuone, piha, puutarha

class Pelaaja:
    def __init__(self, nimi, ikä, sijainti):
        self.nimi = nimi
        self.ikä = ikä
        self.esineet = []
        self.sijainti = sijainti

    def liiku(self, uusi_sijainti):
        self.sijainti = uusi_sijainti
        print(f"Siirryit huoneeseen: {self.sijainti}.")


    def etsi(self):
        if self.sijainti == keittiö:
            print("Tutkit keittiötä...")
            print("Löysit tyhjän namipussin!")
            print("Onko Rekku käynyt namivarkaissa?")

        elif self.sijainti == olohuone:
            print("Tutkit olohuonetta...")
            print("Ei jälkiä rekusta olohuoneessa...")
            print("Jatketaan etsimistä.")

        elif self.sijainti == piha:
            print("Tutkit pihaa...")
            print("Löysit Rekun tassunjälkiä!")
            print("Katsotaan mihin ne johtavat")

        elif self.sijainti == puutarha:
            print("Huh, löysit Rekun.")
            print("Mahtavaa työtä!")

        else:
            print("Et löytänyt mitään kiinnostavaa.")


