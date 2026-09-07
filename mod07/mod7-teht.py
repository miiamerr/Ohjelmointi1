import random

# tehtävä 1

def heitä_noppaa():
    return random.randint(1,6)

while True:
    silmäluku = heitä_noppaa()
    print(silmäluku)

    if silmäluku == 6:
        break

# tehtävä 2

def heitä_noppaa(tahkot):
    return random.randint(1, tahkot)

maksimi = int(input("Anna nopan tahkojen lukumäärä: "))
while True:
    silmäluku = heitä_noppaa(maksimi)
    print(silmäluku)

    if silmäluku == maksimi:
        break


# tehtävä 3

def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

while True:
    gallonat = float(input("Anna gallonamäärä: "))

    if gallonat < 0:
        break
    litrat = gallonat_litroiksi(gallonat)
    print(f"{ litrat: 3f} litraa")
    break

# tehtävä 4

random_luku = [random.randint(-100, 100) for _ in range (0,10)]
summa = sum(random_luku)
print(random_luku)
print("Lukujen summa: ", summa)

# tehtävä 5

def summa(luvut):
    return sum(luvut)

luvut = [1, 2, 3, 4, 5]
tulos = summa(luvut)
print(tulos)


    