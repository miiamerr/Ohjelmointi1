# tehtävä 1
import math
import random

kala = float(input("Syötä kuhan pituus senttimetreinä:"))
kuha = 37

if kala < 37:
    pituus = kala - 37
    print(f"Laske kuha takaisin järveen. Kuha on {pituus} senttiä alimittainen.")


elif kala >= 37:
    print("Voit pyydystää kuhan.") 

# tehtävä 2

hyttiluokka = input("Anna laivan hyttiluokkasi (LUX, A, B, C):")

if hyttiluokka == "LUX":
    print( "LUX on parvekkeellinen hyhtti yläkannella.")

elif hyttiluokka == "A":
    print ("A on ikkunallinen hytti yläkannella.")

elif hyttiluokka == "B":
    print ("B on ikkunaton hytti autokannen alapuolella.")

elif hyttiluokka == "C":
    print ("C on ikkunaton hytti autokannen alapuolella.")

else:
    print ("Virheellinen hyttiluokka.")


# tehtävä 3

sukupuoli = input("Anna biologinen sukupuolesi (mies, nainen):")

hemoglobiiniarvo = int(input("Anna hemoglobiiniarvo g/l:"))

if sukupuoli == "nainen":
    if hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiiniarvo <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvio on korkea.")

if sukupuoli == "mies":
    if hemoglobiiniarvo <134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiiniarvo <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")


# tehtävä 4

vuosi = int(input("Anna vuosiluku:"))
if vuosi % 400 == "karkausvuosi":
    print("Vuosi on karkausvuosi.")
elif vuosi % 100 == 0:
    print("Vuosi ei ole karkausvuosi.")
elif vuosi % 4 == 0:
    print ("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")
