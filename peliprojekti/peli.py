from esine.esine import Esine
from koira.koira import Koira
from maailma.maailma import Maailma
from pelaaja.pelaaja import Pelaaja
from maailma.maailma import Koti, Piha, Puutarha

def tallenna_peli(pelaaja, sijainti):
    with open("tiedot.txt", "w") as tiedosto:
        tiedosto.write(pelaaja + "\n")
        tiedosto.write(sijainti + "\n")

def lataa_peli():
    try:
        with open("tiedot.txt", "r") as tiedosto:
            pelaaja = tiedosto.readline().strip()
            sijainti = tiedosto.readline().strip()
        return pelaaja, sijainti
    
    except FileNotFoundError:
        return None

tiedot = lataa_peli() # kysytään, löytyykö vanhaa tallennusta

if tiedot:
    print("Tallennettu peli löydetty!")
    pelaaja, sijainti = tiedot

    print("Pelaaja", pelaaja)
    print("Jäit viimeksi paikkaan: ", sijainti)
    
    jatka = input("Haluatko jatkaa peliä: Kyllä (K) vai Ei (E)? ")

    if jatka != "K":
        pelaaja = input("Anna pelaajallesi nimi: ")
        sijainti = "makuuhuone"

else:
    pelaaja = input("Anna pelaajallesi nimi: ")
    ikä = input("Anna pelaajallesi ikä: ")
    sijainti = "makuuhuone"


with open("peliprojekti/alkutekstit/intro.txt", "r", encoding="utf-8") as tiedosto:
    intro = tiedosto.read()

print(intro)

with open("peliprojekti/alkutekstit/ohjeet.txt", "r", encoding="utf-8") as tiedosto:
    ohjeet = tiedosto.read()

print(ohjeet)    

# Peli alkaa, että käyttäjältä kysytään heidän nimeä ja ikää
# Jos pelaajan ikä on alle 13 vuotta, peli sammuu automaattisesti.
nimi = input ('Mikä sinun nimesi on? ') 
print('Hauska tavata', nimi + '!')
ikäraja = 13
ikä = float(input("Anna ikäsi: "))
if ikä >= 13:
    print("\nTERVETULOA REKKU RESCUEEN", nimi + "!!!!")
    print() # tulostaa tyhjän rivin tekstien väliin
    print("\nRakas koirasi Rekku on kadonnut ja täytyy löytää välittömästi!")
elif ikä < ikäraja:
    print("Pelaaja on alaikäinen")
    print("\nRekku Rescue sammutetaan")
    
# Maailma luokan alaluokkien: Koti, Piha ja Puutarha pääohjelma.
# makuuhuoneen ja keittiö paikan kohdalla on "None", koska niillä ei
# ole pelille oleellista roolia/paikkaa. "None" komento ohittaa paikka 
# parametrin.
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
# pelaajan nimeä sekä ikää.
pelaajan_nimi = input("Anna pelaajallesi nimi: ")
pelaajan_ikä = input("Anna pelaajallesi ikä: ")
pelaaja1 = Pelaaja(pelaajan_nimi, pelaajan_ikä, makuuhuone)

# Koira-luokan pääohjelma, johon on kirjattu olion tiedot.
koira = Koira("Rekku", 3, "Chihuahua", "vaalea")

# Funktio lopettaa ja tallentaa pelin tiedot heti kun käyttäjä
# lopettaa itse pelin kirjoittamalla kenttään "L".
def kysy_valinta(kysymys):
    valinta = input(kysymys)
                        
    if valinta == "L":
        tallenna_peli(pelaaja, sijainti)
        print("Peli tallennettu. Nähdään myöhemmin!")
        exit()

    return valinta


# Pelin lopetus kun Rekku on löytynyt, funktio ja ehtorakenne
def pelin_lopetus():
    print("\nRekku on löytänyt erittäin uhanalaisen lintulajin, hömötiaisen!")
    valinta = input("Mitä tehdään: 1. Jätät linnun rauhaan ja lähdette Rekun kanssa kotiin.\n 2. Mene katsomaan lintua lähempää. ")

    if valinta == "1":
        print("\nHyvää työtä! Luonto kiittää")

    elif valinta == "2":
        print("Lintu säikähtää ja lentää pois.")
        print("\nLuontoa täytyy kunnioittaa, joten jätetään lintu rauhaan ensi kerralla.")

    else:
        print("\nVirheellinen valinta")

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

            valinta = kysy_valinta("Kirjoita varusteen nimi: ")
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
    print("Olet paikassa: ", pelaaja1.sijainti.nimi)
    print("Minne haluat mennä?")

    if pelaaja1.sijainti == makuuhuone:
        print("1. Keittiö")
        print("2. Olohuone")

        valinta = kysy_valinta("Minne haluat mennä? ")
        print() # tyhjä rivi

        if valinta == "1":
            pelaaja1.liiku(keittiö)

        elif valinta == "2":
            pelaaja1.liiku(olohuone)

    elif pelaaja1.sijainti == keittiö:
        print("1. Puutarha")
        print("2. Olohuone")
        print("3. Etsi vihjeitä")
        print() # tyhjä rivi

        valinta = kysy_valinta("Valitse minne haluat mennä? ")

        if valinta == "1":
            pelaaja1.liiku(puutarha)

        elif valinta == "2":
            pelaaja1.liiku(olohuone)

        elif valinta == "3":
            pelaaja1.etsi()
            print() # tyhjä rivi
            

    elif pelaaja1.sijainti == olohuone:
        print("1. = Makuuhuone")
        print("2. = Piha")
        print() # tyhjä rivi

        valinta = kysy_valinta("Minne haluat mennä? ")

        if valinta == "1":
            pelaaja1.liiku(makuuhuone)

        elif valinta == "2":
            pelaaja1.liiku(piha)

    elif pelaaja1.sijainti == piha:
        print("1. = Mene puutarhaan")
        print("2. = Etsi vihjeitä")
        print() # tyhjä rivi

        valinta = kysy_valinta("Mitä aiot tehdä? ")
        print() # tyhjä rivi

        if valinta == "1":
            pelaaja1.liiku(puutarha)

        elif valinta == "2":
            pelaaja1.etsi()
            print() # tyhjä rivi
            print("Hyvä, löysit Rekun tassunjälkiä pihalta!")
            print("Mihin tassujäljet vievät? ")

    elif pelaaja1.sijainti == puutarha:
        print("Olet puutarhassa, jossa on paljon kauniita kukkia.")
        print() # tyhjärivi
        print("1. = Etsi Rekku")
        print("2. = Palaa takaisin pihalle")

        valinta = kysy_valinta("Mitä aiot tehdä? ")
        print() # tyhjä rivi

        if valinta == "1":
            koira.haukahdus()
            print() # tyhjä rivi
            print("Kuulitko tuon? Se oli Rekun haukahdus!!")
            print() # tyhjä rivi
            koira.haukahdus()
            print() # tyhjä rivi
            print("Etsi Rekkua kukkien seasta...") 
            koira.haukahdus()
            print() # tyhjä rivi
            print("Löysit Rekun!!")
            print("Hetkonen...")

            pelin_lopetus()
            break 
            
            
       


