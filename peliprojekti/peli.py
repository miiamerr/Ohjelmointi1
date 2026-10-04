
from esine.esine import Esine
from koira.koira import Koira
from maailma.maailma import Maailma
from pelaaja.pelaaja import Pelaaja
from maailma.maailma import Koti, Piha, Puutarha

try: 
    with open("intro.txt", "r") as tiedosto:
        intro = tiedosto.read()

    with open("ohjeet.txt", "r") as tiedosto:
        ohjeet = tiedosto.read()

    print(intro)
    print() # tekee tyhjän rivin tekstien väliin
    print(ohjeet)
except FileNotFoundError:
    print("Tiedostoa ei löydy.")
except IOError:
    print("Tiedoston käsittelyssä tapahtui virhe.")


# Peli alkaa, että käyttäjältä kysytään heidän nimeä ja ikää
# Jos pelaajan ikä on alle 13 vuotta, peli sammuu automaattisesti.
nimi = input ('Mikä sinun nimesi on? ') 
print('Hauska tavata', nimi + '!')
ikäraja = 13
ikä = float(input("Anna ikäsi: "))
if ikä >= 13:
    print("\n---TERVETULOA REKKU RESCUEEN---", nimi + "!!!!")
    print() # tulostaa tyhjän rivin tekstien väliin
    print("\nRakas koirasi Rekku on kadonnut ja täytyy löytää välittömästi!")
elif ikä < ikäraja:
    print("Pelaaja on alaikäinen")
    print("\nRekku Rescue sammutetaan")
    

# Maailma luokan alaluokkien: Koti, Piha ja Puutarha pääohjelma.
makuuhuone = Koti("Makuuhuone", None, "Koiranpeti")
keittiö = Koti("Keittiö", None, "Koiranluu")
olohuone = Koti("Olohuone", "Sohva", "Lämmin viltti")
piha = Piha ("Piha", "Kuisti", "Koiran pallo")
puutarha = Puutarha ("Puutarha", "Niitty", "Kukka")

# Esine luokan pääohjelma esine1.
esine1 = Esine("Pallo")

# Varustevalikossa ilmaantuvat esineet esiintyvät listamuodossa
# varusteet ovat Esine-luokkan olioita.
varusteet = [
    Esine("Rekun hihna"),
    Esine("Rekun lelu"),
    Esine("Koirannamit")
]

# Pelaaja luoka pääohjelma, joka kysyy käyttäjältä
# pelaajan ikää.
pelaajan_ikä = input("Anna pelaajallesi ikä: ")
pelaaja1 = Pelaaja("Pelaaja1", pelaajan_ikä, makuuhuone)

# Koira-luokan pääohjelma, johon on kirjattu olion tiedot.
koira = Koira("Rekku", 3, "Chihuahua", "vaalea")

# Peli avautuu päävalikkoon, jossa on neljä vaihtoehtoa. 
# Peli toistuu while-funktion ansiosta ja if-valintarakenne mahdollistaa
# että ohjelma suorittaa koodirivit vain silloin, kun määritelty ehto on tosi.
while True:
    print("\n---REKKU RESCUE---")
    print()
    print("Valitse minne mennään ensimmäisenä: Uusi peli (1), Varustevalikko (2), \nTietoa Rekusta (3), Lopeta peli (L).")
    print() # tulostaa tyhjän rivin tekstien väliin/helpottaa lukemista
    valinta = input("Mistä aloitetaan: ")

    if valinta == "1":
        for i in range(3, 0, -1):
            print(i)
        print("\n---PELI ALKAA---")
        print() # tulostaa tyhjän rivin tekstien väliin
        break

    elif valinta == "2":
        def varustevalikko(varusteet):
            print("\n---VARUSTEET---")
            print("Valitse haluamasi varusteet: ")

            for varuste in varusteet:
                print(varuste.nimi)

            valinta = input("Kirjoita varusteen nimi: ")
            valitut = []

            for varuste in varusteet:
                if varuste.nimi  == valinta:
                    valitut.append(varuste)

            return valitut

        omat_varusteet = varustevalikko(varusteet)
        print("Valitsemasi varusteet: ")
        for varuste in omat_varusteet:
            print(varuste.nimi)

        valitut = input("Valitse tarvittavat tavarat: ")

        print("Valitsit seuraavat tavarat: ")
        print(valitut)
            
    elif valinta == "3":
        def tietolista(koira):
            print("\n---REKUN TIEDOT---")
            print("Nimi: ", koira.nimi)
            print("Ikä: ", koira.ikä)
            print("Rotu: ", koira.rotu)
            print("Väri: ", koira.väri)

        tietolista(koira)
        
    elif valinta == "L":
        print("Kiitos pelaamisesta!")
        print("Peli päättyy.")
        break

    else: 
        print("Virheellinen valinta.")

peli_käynnissä = True
sijainti = makuuhuone

while peli_käynnissä:
    print("Olet paikassa: ", sijainti.nimi)
    print("Minne haluat mennä?")

    if sijainti == makuuhuone:
        print("1. Keittiö")
        print("2. Olohuone")

        valinta = input("Minne haluat mennä? ")

        if valinta == "1":
            sijainti = keittiö

        elif valinta == "2":
            sijainti = olohuone

    elif sijainti == keittiö:
        print("1. Puutarha")
        print("2. Olohuone")
        print("3. Etsi vihjeitä")

        valinta = input("Valitse minne haluat mennä? ")

        if valinta == "1":
            sijainti = puutarha

        elif valinta == "2":
            sijainti = olohuone

        elif valinta == "3":
            print("Rekun namipiilosta löytyi tyhjä herkkupussi")
            print("Onko Rekku käynyt namivarkailla?")
            print("Jatketaan etsintää!")
            

    elif sijainti == olohuone:
        print("1. = Makuuhuone")
        print("2. = Piha")

        valinta = input("Minne haluat mennä? ")

        if valinta == "1":
            sijainti = makuuhuone

        elif valinta == "2":
            sijainti = piha

    elif sijainti == piha:
        print("1. = Mene puutarhaan")
        print("2. = Etsi vihjeitä")

        valinta = input("Mitä aiot tehdä? ")

        if valinta == "1":
            sijainti = puutarha

        elif valinta == "2":
            print("Hyvä, löysit Rekun tassunjälkiä pihalta!")
            print("Mihin tassujäljet vievät? ")

    elif sijainti == puutarha:
        print("Olet puutarhassa, jossa on paljon kauniita kukkia.")
        print("1. = Etsi Rekku")
        print("2. = Palaa takaisin pihalle")

        valinta = input ("Mitä aiot tehdä?")

        if valinta == "1":
            print(koira.haukahdus)
            print("Etsi Rekkua kukkien seasta...") 
            print("Mahtavaa, löysit Rekun!!")
            break
