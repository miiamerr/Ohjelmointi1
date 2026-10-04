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
        pass


