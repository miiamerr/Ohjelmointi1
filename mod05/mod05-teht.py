import random
import math

# tehtävä 1

luku = 1
while luku <= 1000:
    # onko luku kolmella jaollinen, jos on niin printtaa
    if luku % 3 == 0:
        print(luku)
    luku += 1

# tehtävä 2

tuuma = 2.54
tuuma = float(input("Anna tuumien määrä niin muutan sen senttimetreiksi (cm):"))

senttimetri = tuuma * 2.54

if tuuma >= 0:
    print(f"{tuuma} tuumaa on {senttimetri} senttimetriä (cm)")

elif tuuma < 0:
    print ("Ohjelma loppui, annoit negatiivisen lukuarvon.")

# tehtävä 3


# tehtävä 4

oikea_numero = 3
arvaus = int(input("Arvaa numero 1 ja 10 väliltä:"))

while arvaus < oikea_numero:
    print("Liian pieni arvaus")
    arvaus = int(input("Arvaa uudestaan:"))

if arvaus > oikea_numero:
    print("Liian suuri arvaus")
    arvaus = int(input("Arvaa vielä kerran:"))

if arvaus == oikea_numero:
    print("Oikein!!")


# tehtävä 4 modattuna
# TODO: tee tehtävä loppuun
oikea_numero = 7
arvaus = int(input("Arvaa numero 1 ja 10 välillä:"))

while arvaus != oikea_numero:
    print("Väärin")
    arvaus = int(input("Arvaa uudestaan:"))

print(f"Jes, sait kaiken oikein!!! Numero tosiaan oli {oikea_numero}")

# usein while rekennetta käytetään ja varsinkin teidän projekteissa!!
# niin sanottu pääsilmukka ELI main loop

peli_käynnissä = True
# main loop
print("Tervetuloa peliini!!!")

while peli_käynnissä:
    print("Valitse minne mennään (j tai l) eli jatka tai lopeta")
# j jatkaa peliä ja l lopettaa
    valinta = input("Anna komento:")
    if valinta == "j":
        print("Jatkoit peliä")
    elif valinta == "l":
        print("Lopetit pelin")
        peli_käynnissä = False
        # break 

    else: 
        print("Et osannut antaa käskyjä!")


# tehtävä 5

käyttäjätunnus = input("Anna käyttäjätunnus (python):")
salasana = input("Anna salasana jotta pääset sisään (rules):")

while käyttäjätunnus != "python":
    print("Väärä käyttäjätunnus")
    käyttäjätunnus = input("Anna käyttäjätunnus uudestaan:")

if käyttäjätunnus != "python":
    print("Väärä käyttäjätunnus")
    käyttäjätunnus = input("Anna oikea käyttäjätunnus:")

if käyttäjätunnus != "python":
    print("Väärä käyttäjätunnus")
    käyttäjätunnus = input("Anna käyttäjätunnus vielä kerran:")

while salasana != "rules":
    print("Väärä salasana")
    salasana = input("Anna salasana uudestaan:")

if salasana != "rules":
    print("Väärä salasana")
    salasana = input("Anna salasana vielä kerran:")

print("Tervetuloa!!!")

if käyttäjätunnus or salasana != True:
    print("Pääsy evätty")


# tehtävä 6

# n=4n/N, jossa n on ympyrän sisään osuvat pisteet ja N kaikki arvotut pisteet
# Piste on ympyrän sisällä, jos x^2+y^2<1

N = 100 #kaikkien pisteiden lukumäärä
n = 0 # lasketaan ympyrään osuneiden pisteiden lukumäärä
counter = 0

while counter < N:
    counter += 1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    print(f"{counter} Arvotun pisteen koordinaatit, x: {x}, y: {y}")
    if x ** 2 + y ** 2 < 1:
        n = n +1
        print("Piste on ympyrän sisällä.")

print(f"Pisteitä arvottu yhteensä {N}, joista ympyrän sisälle osui {n} kpl.")

#TODO: Laskee pii annetulla kaavalla ja tulostaa . Kokeile myös eri N arvoilla.