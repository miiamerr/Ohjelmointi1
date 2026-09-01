
suorita = True
import random

while suorita:
    print("Tämä printtautuu vain kerran")
    suorita = False

print("Suoritus loppui")

# while == toista niin kauan kun ehto on tosi

luku = 1                # 1. alkuarvo / kierrosmuuttuja

while luku <= 5:        # 2. ehto
    print(luku)
    # luku = luku + 1 # 3. muuttujan arvon muuttaminen
    luku += 1

print("Jatketaan ohjelmaa")

# Lasketaan luku 10 alaspäin.

luku = 10

while luku >= 1:
    print(luku)
    luku -= 1

luku = int(input("Anna luku josta laskemme alaspäin:"))

while luku >= 1:
    print(luku)
    luku -=1

# käyttäjä lopettaa toiston

salasana = input("Anna salainen salasana jotta pääset sisään (python):")#.strip().lower()

# != eri suuri kuin

while salasana != "python":
    print("Väärä salasana")
    salasana = input("Anna salasana uudestaan:")

print("Tervetuloa sisään, koodi oli oikein")

# while / else rakenne
# suoritus siirtyy else haaraan kun toistoehto on epätosi
# sitä ei suoriteta jos poistutaan break-lauseella
# else rakenne on harvemmin käytetty

komento = input("Anna komento (lopeta, MAYDAY):").strip().lower()

while komento != "lopeta":
    if komento == "mayday":
        break
    print("Annoit komennon: ", komento)
    komento = input("Anna komento (lopeta):")
else:
    print("Annoit käskyn lopeta, joten näin tehdään!!!")

print("Ohjelma jatkuu")

noppa1 = noppa2 = heitot = 0

noppa1 = noppa2 = heitot = 0
while (noppa1 != 6 or noppa2 != 6):

    noppa1 = random.randint(1,6)
    noppa2 = random.randint(1,6)
    heitot = heitot + 1

print(f"Tarvittiin {heitot:d} heittoa.")


eka = 1
while eka <= 5:
    toka = 1
    while toka <= 5:
        print(f"{eka} kertaa {toka} on {eka*toka:d}")
        toka = toka + 1
    eka = eka + 1

pelikerta = 0
heitot = 0
while pelikerta < 1000:

    noppa1 = noppa2 = 0
    while (noppa1 != 6 or noppa2 != 6):
        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        # print(noppa1, noppa2)
        heitot = heitot + 1
    pelikerta += 1

print("Pelikertoja meillä oli:", pelikerta)
print(f"Tarvittiin {heitot:d} heittoa.")
print(f"Jokaisella kierroksella oli keskimäärin {heitot/pelikerta} heittoa")
