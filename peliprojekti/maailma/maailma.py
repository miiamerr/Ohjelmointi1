class Maailma:
    def __init__(self, nimi, paikka, esine):
        self.nimi = nimi
        self.paikka = paikka
        self.esine = esine


class Koti(Maailma):
    pass

class Piha(Maailma):
    pass

class Puutarha(Maailma):
    pass

# Maailma luokan alaluokkien: Koti, Piha ja Puutarha pääohjelma.
# makuuhuoneen ja keittiö paikan kohdalla on "None", koska niillä ei
# ole pelille oleellista roolia/paikkaa. "None" komento ohittaa paikka 
# parametrin.
makuuhuone = Koti("Makuuhuone", None, "Koiranpeti")
keittiö = Koti("Keittiö", None, "Koiranluu")
olohuone = Koti("Olohuone", "Sohva", "Lämmin viltti")
piha = Piha ("Piha", "Kuisti", "Koiran pallo")
puutarha = Puutarha ("Puutarha", "Niitty", "Kukka")