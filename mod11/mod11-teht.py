# tehtävä 1

class Julkaisu:
    def __init__(self, kirja, lehti):
        self.kirja = kirja
        self.lehti = lehti
        

    def tulostaa_tiedot(self):
        print(f"Julkaisu on {self.kirja}/{self.lehti}")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumäärä):
        self.nimi = nimi
        self.kirjailija = kirjailija
        self.sivumäärä = sivumäärä
    

    def tulosta_tiedot(self):
        print(f"Teoksen nimi on {self.nimi}, sen on kirjoittanut {self.kirjailija} ja siinä on {self.sivumäärä} sivua.")


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.nimi = nimi
        self.päätoimittaja = päätoimittaja
    

    def tulosta_tiedot(self):
        print(f"Teoksen nimi on {self.nimi} ja sen päätoimittaja on {self.päätoimittaja}.")
    

kirja1 = Julkaisu
lehti1 = Julkaisu
kirja1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
lehti1 = Lehti("Aku Ankka", "Aki Hyyppä", )
kirja1.tulosta_tiedot()
lehti1.tulosta_tiedot()


# tehtävä 2

