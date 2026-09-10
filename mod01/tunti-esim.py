
## Moduuli 3
# tehtävä 1

import math
print("\nYmpyrän ja neliön pinta-alat")
r = float(input("Anna ympyrän säteen pituus: "))
p = float(input("Anna neliön sivun pituus: "))
pinta_ala = math.pi * r**2
A = p * p
print(f"Ympyrän pinta-ala on {pinta_ala:.2f} ja neliön pinta-ala on {A:.2f}.")

# tehtävä 2

print("\nHedelmien kilohinta")
banaani = float(input("Anna banaanien määrä (kg): "))
omena = float(input("Anna omenien määrä (kg): "))
appelsiini = float(input("Anna appelsiinien määrä (kg): "))

banaanit = banaani * 2.85
omenat = omena * 3.15
appelsiinit = appelsiini * 4.15
summa = banaanit + omenat + appelsiinit

print("Ostokset yhteensä:" )
print(f"Banaanit: {banaanit:.2f} € ")
print(f"Omenat: {omenat:.2f} € ")
print(f"Appelsiinit: {appelsiinit:.2f} € ")
print(f"Yhteensä: {summa} € ")

# Moduuli 4
# tehtävä 3 

import random
print("\nNoppasimulaattori")
noppa1 = random.randint(1,6)
noppa2 = random.randint(1,20)

print(noppa1)
print(noppa2)

summa = noppa1 + noppa2
print(f"Noppien silmälukujen summa: {summa}")

# tehtävä 4

print("\nÄänestysoikeus")
ikä = float(input("Kuinka vanha olet: "))
äänestysoikeus = 18 - ikä

if ikä >= 18:
    print("Olet tarpeaksi vanha äänestämään Suomen eduskuntavaaleissa.")
elif ikä < 18:
    print(f"Et voi äänestää Suomen eduskuntavaaleissa, sillä olet {äänestysoikeus} vuotta liian nuori.")

# tehtävä 5 

print("\nSähkönkulutus")
sähkön_kulutus = float(input("Anna sähkön kulutus kilowattitunteina (kWh): "))
hinta = 0

if sähkön_kulutus <= 50:
    hinta = sähkön_kulutus * 10
    print(f"Kun sähköä kuluu {sähkön_kulutus} kWh, sähkö maksaa {hinta} senttiä.")

elif sähkön_kulutus <= 200:
    hinta = 50 * 10
    hinta = hinta (sähkön_kulutus - 50) * 8
    print(f"Sähkön kulutus: {hinta} senttiä.")

else:
    hinta = 50 * 10 + 150 * 8 + (sähkön_kulutus - 200) * 6
    print(f"Sähkön kulutus: {hinta} senttiä.")

# tehtävä 6
fysiikka = int(input("Anna koulumenestyksesi fysiikasta (0-100): "))
kemia = int(input("Anna koulumenestyksesi kemiasta (0-100): "))
matematiikka = int(input("Anna koulumenestyksesi matematiikasta (0-100): "))


if fysiikka and matematiikka > 90:
    print("Stipendi myönnetään.")
elif kemia > 95:
    print("Stipendi myönnetään.")
elif fysiikka or kemia or matematiikka < 50:
    print(f"Stipendia ei myönnetty koska tulos oli alle 50.")
else:
    print("Stipendiä ei myönnetty.")



## Moduuli 5
# tehtävä 7

kokonaisluku = int(input("Anna kokonaisluku: "))
i = 0

while i <= kokonaisluku:
    print(i)
    i += 2
if i >= 0:
    print("Ohjelma päättyy")


# tehtävä 8

summa = 0

while summa <= 1000:
    luku = int(input("Anna kokonaisluku: "))
    summa += luku

print("Summa ylitti 1000. Lopullinen summa oli", summa)

# tehtävä 9

t = float(input("Anna esineen alkukorkeus (m): "))
g = 9.81
s = 0.5 * g * t**2

print(f"Esine putosi: {s:.2f} metriä. ")

t = float(input("Anna putoamisaika sekunteina: "))
while t > 0:
    g = 9.81
    s = 0.5 * g * t**2
    print(f"Putoamismatka: {s} metriä")
    t = float(input("Anna putoamisaika sekunteina: "))

## Moduuli 6
# tehtävä 10
