# Mod 11 - Perintä - esimerkki

class Eläin:
    def __init__(self, nimi, paino, syntymäaika):
        self.nimi = nimi
        self.paino = paino
        self.syntymävuosi = syntymäaika
        Eläin.eläinten_lkm += 1

    def liiku(self):
        print(f"{self.nimi} liikkuu jotenkin johonkin.")

    def kaikki_tiedot(self):
        print(f"Nimi: {self.nimi}, paino: {self.paino/100} kg, syntymäaika: {self.syntymävuosi}.")


class Ilves(Eläin):
    def kilju(self):
        print(f"Ilves nimeltä {self.nimi} kiljuu.")

    def kaikki_tiedot(self):
        print("\nIlves")
        super().kaikki_tiedot()

class Karhu(Eläin):
    def __init__(self, nimi, paino, syntymäaika, on_horroksessa):
        self.on_horroksessa = on_horroksessa
        # koska konstruktori eli alustaja "ylikirjoitetaan", tarvitsee yliluokan konstruktoria kutsua
        # erikseen, jos sitä halutaan hyödyttää
        super().__init__(nimi, paino, syntymäaika)

    def karju(self):
        print(f"Karhu nimeltä {self.nimi} karjuu")

    def liiku(self):
        print(f"Karhu {self.nimi} myörii eteenpäin.")

    def kaikki_tiedot(self):
        print(f"\nKarhu on talviunilla: {self.on_horroksessa}")
        super().kaikki_tiedot()


uusi_eläin = Eläin("Joku elukka", 1500, 10122022)
uusi_eläin.liiku()

ilves1 = Ilves("Ilmari", 6700, 6102026)
ilves1.liiku()
ilves1.kilju()

karhu1 = Karhu("Nalle", 13500, 19072026, False)
karhu1.liiku()
karhu1.karju()
#print(karhu1.on_horroksessa)

kaikki_eläimet = [uusi_eläin, ilves1, karhu1]
kaikki_eläimet.append(Karhu("Isonalle", 25000, 22092026))

kaikki_eläimet = [uusi_eläin, ilves1, karhu1]
for eläin in kaikki_eläimet:
    eläin.kaikki_tiedot()