import math
import random

# tehtävä 1
nimi = input ("Anna nimesi:")
print(f'Terve, {nimi}!')

#tehtävä 2
# ympyrän pinta-ala: pi * r^2
r = float(input('Anna säde niin lasken ympyrän pinta-alan:'))
# r = float(r)
# ympyrän pinta-ala: a = pi * r^2
A = math.pi * r**2
pyöristys = round (A, 2)
print(f'Ympyrän pinta-ala on {pyöristys}')

# tehtävä 3
a = float(input('Anna suorakulmion kanta:'))
b = float(input('Anna suorakulmion korkeus:'))

p = 2 * (a + b)
# p2 = 2 * a + 2 * b
A = a * b

print(f'Suorakulmion piiri on: {p:.2f} ja pinta-ala {a*b}')

# tehtävä 4
l = float(input('Anna kokonaisluku : '))
l2= float(input('Anna toinen kokonaisluku:'))
l3= float(input('Anna kolmas kokonaisluku:'))
summa = l + l2 + l3
tulo = l * l2 * l3
keskiarvo = summa / 3
print(f'Summa on {summa}, tulo on {tulo} ja keskiarvo on {keskiarvo}')

# tehtävä 5
leiviskat_lkm = float(input('Anna leiviskien määrä:'))
naulat_lkm = float(input('Anna naulojen määrä:'))
luodit_lkm = float(input ('Anna luotien määrä:'))

# lasketaan leiviskät mukaan nauloihin
naulat_lkm = leiviskat_lkm * 20 + naulat_lkm
# lasketaan naulat mukaan luoteihin
luodit_lkm = naulat_lkm * 32 + luodit_lkm

print('Koko massa luoteina:', + luodit_lkm)




# tehtävä 6
luku = random.randint(0, 9)
luku2 = random.randint(0, 9)
luku3 = random.randint(0, 9)
print(f'{luku}, {luku2}, {luku3}')
