import random
import math

# tehtävä 1

print("\n=== Noppapeli ===")
def heitä_noppaa():
    return random.randint(1,6)

silmäluku = 0
while silmäluku != 6:
    silmäluku = heitä_noppaa()
    print(silmäluku)


# tehtävä 2

print("\n=== Noppapeli ===")
def heitä_noppaa(tahkot):
    return random.randint(1, tahkot)

tahkojen_lukumäärä = int(input("Anna nopan koko (tahkojen lukumäärä): "))
silmäluku = 0
while silmäluku != tahkojen_lukumäärä:
     silmäluku = heitä_noppaa(tahkojen_lukumäärä)
     print(silmäluku)


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


# tehtävä 6

def calculate_unit_price(diameter_in_cm, price):
    # pinta-ala: pi * r*r
    r = diameter_in_cm/100/2
    area = math.pi * r**2
    # palauttaa yksikköhinnan eur/m2
    return price / area

unit_prices = []
for pizza_number in range(2):
    diameter = float(input(f"Anna {pizza_number+1}. pizzan halkaisija (cm): "))
    price = float(input(f"Anna {pizza_number+1}. pizzan hinta (eur): "))
    unit_price = calculate_unit_price(diameter, price)
    unit_prices.append(unit_price)
    unit_prices.append(calculate_unit_price(diameter, price))
    print(f"{pizza_number+1}. Pizzan yksikköhinta (eur/m2): {unit_price:0.2f}")

if unit_prices[0] < unit_prices[1]:
    print("Ensimmäinen pizza on halvempi.")
elif unit_prices[0] > unit_prices [1]:
    print("Toinen pizza on halvempi.")
else:
    print("Yhtä halpoja.")

# TODO EXTRA: miten kehittää ohjelmaa niin, että se toimii N-määrällä pizzoja?
#
# toinen for-looppi hintojen vertailuun 