def tervehdi():
    print("Moi!")
    return

print("Päivä alkaa tervehdyksellä.")
tervehdi()
print("Sitten siirrytään muihin asioihin.")



def tervehdi(kerrat):
    for i in range(kerrat):
        print("Hyvää päivää " + str(i+1) + ". kerran")
    return

print("Päivä alkaa tervehdyksillä.")
tervehdi(5)
print("Tervehditään lisää.")
tervehdi(2)


def vaihda():
    kaupunki = "Espoo"
    print("Funktiossa lopuksi: " + kaupunki)
    return

kaupunki = "Helsinki"
print("Pääohjelmassa aluksi: " + kaupunki)
vaihda()
print("Pääohjelmassa lopuksi: " + kaupunki)



#print("print() on Pythonin sisäänrakennettu funktio")

#def do_nothing():
 #   pass
 #   return
#do_nothing()

#def print_list_of_numbers():
 #   print(1)
 #  print(2)
 #   print(3)

#print_list_of_numbers()
# Funktion parametrit (argumentit) ovat muuttajia, joiden arvot ovat käytössä
# funktion sisällä, ja joille syötetään arvot. funktiota kutsuessa.
def print_list_of_numbers(start, end):
    print(f"Tulostettava väli: {start}, {end}")
    for i in range(start, end+1, 1):
        print(i)
    return
    #print(start)
    #print(end)

print_list_of_numbers(1, 5)
# funktio ilman return-sanaa tai pelkkä return-sana ilman määriteltyä 
# paluuarvoa: None
# mitä palauttaa funktio ilman return-sanaa
test_return_value = print_list_of_numbers(7, 11)
print("test return value", test_return_value)

# Funktio ja paluuarvo (return)
print()
number = "01"
# int()-funktio palauttaa annetun parametrin arvon kokonaislukutyyppisenä
print(int(number)) # "01" => 1

# Funktio joka ei tulosta numeroita suoraan vaan palauttaa ne listamuodossa.
def create_list_of_numbers(start, end):
    print(f"Tehdään lista, jossa arvot: {start}-{end}")
    number_list = []
    for i in range(start, end+1, 1):
        number_list.append(i)
    return number_list

print(create_list_of_numbers(3, 7))

list_of_numbers = create_list_of_numbers(11, 16)
#print(list_of_numbers)

def inventaario(tavarat):
    print("Sinulla on seuraavat tavarat:")
    for t in tavarat:
        print("- " + t)
    # Tavarat katoavat inventaariosta
    tavarat.clear()
    return

reppu = ["Vesipullo", "Kartta", "Kompassi"]
inventaario(reppu)
reppu.append("Linkkuveitsi")
inventaario(reppu)

# primitiiviarvoilla alkuperäinen (pääohjelman b) arvo ei muutu
def tulosta_luku(a):
    print(a)
    a = 0

b = 3
tulosta_luku(b)
tulosta_luku(b)

### vaihtuva määrä parametrejä , käsitellään monikkona (kuin lista)

def summa(*luvut):
    print("Syötetyt arvot:", luvut)
    s = 0
    for l in luvut:
        s += l
    return s

print("Summa on", summa(1, 1, 1, 1, 1, 1))

import random

# T1 + T1 + EXTRAA
def heitä_noppaa(tahkojen_lkm):
    return random.randint(1, tahkojen_lkm)

def noppapeli():
    print("\n=== Noppapeli ===")
    nopan_koko = int(input("Anna nopan koko (maksimisilmäluku): "))
    silmäluku = 0
    heittolaskuri = 0
    while silmäluku != nopan_koko:
        heittolaskuri += 1
        silmäluku = heitä_noppaa(nopan_koko)
        print(silmäluku)
    print(f"Heitettäessä {nopan_koko}-tahkoista noppaa, meni {heittolaskuri} heittoa, jotta saatiin {nopan_koko}.")

noppapeli()

# sovelluksen päävalikko ns main loop, josta voidaan käynnistää eri aliohjelmia
while True:
    komento = input("Anna komento>> ")
    if komento == "lopeta":
        print("Heippa!")
    if komento == "noppa":
        noppapeli()
    else:
        print("En ymmärtänyt")
