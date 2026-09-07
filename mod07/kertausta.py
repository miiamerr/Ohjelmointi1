# tehtävä 1
#name = input("Anna nimesi: ")
#print("Hei, hauska tavata", name + "!")

import math

# tehtävä 3.2
#r = float(input("Anna ympyrän säde: "))
#A = math.pi * r**2
#print(f"Ympyrän pinta-ala on: {A}")

# tehtävä 3.3
#kanta = float(input("Anna suorakulmion kannan pituus: "))
#korkeus = float(input("Anna suorakulmion korkeus: "))
#piiri = kanta * 2 + korkeus * 2
#A = kanta * korkeus
#print(f"Suorakulmion piiri on {piiri} ja pinta-ala on {A}")

#tehtävä 3.4
#luku1 = float(input("Anna kokonaisluku: "))
#luku2 = float(input("Anna toinen kokonaisluku: "))
#luku3 = float(input("Anna kolmas kokonaisluku: "))
#summa = luku1 + luku2 + luku3
#tulo = luku1 * luku2 * luku3
#keskiarvo = tulo / 3
#print(f"Kokonaislukujen summa: {summa}, tulo: {tulo} ja keskiarvo: {keskiarvo}.")

# tehtävä 3.5

import math

leiviskat_lkm = float(input('Anna leiviskien määrä:'))
naulat_lkm = float(input('Anna naulojen määrä:'))
luodit_lkm = float(input ('Anna luotien määrä:'))

# lasketaan leiviskät mukaan nauloihin
naulat_lkm = leiviskat_lkm * 20 + naulat_lkm
# lasketaan naulat mukaan luoteihin
luodit_lkm = naulat_lkm * 32 + luodit_lkm

# välitarkastus
#print('Koko massa luoteina: {luodit_lkm}')

massa_g = luodit_lkm * 13,3

print(f"Massa nykymittojen mukaan: {massa_g // 1000:.0f} kiloa ja {massa_g % 1000} grammaa.")