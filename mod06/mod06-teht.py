import random

# tehtävä 1

arpakuutioiden_lukumäärä = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0
for i in range(arpakuutioiden_lukumäärä):
    luku = random.randint(1, 6)
    print(luku)
    summa += luku
print("Arpakuutioiden silmälukujen summa:", summa)


# tehtävä 2
numbers = []

while True:
    input_number = input("Anna luku: ")
    if input_number == "":
        # lopeta kysely
        break
        #running = False kumpi tahansa käy
    # lisätään syötetty luku listalle
    num =int(input_number)
    numbers.append(int(input_number))
numbers.sort(reverse=True)

# quick'n'dirty
#print(numbers[0:5])

# for-lauseella viisi ensimmäistä alkiota
for num in range(5):
    print(numbers[num])


# tehtävä 3

kokonaisluku = int(input("Anna kokonaisluku, ilmoitan onko se alkuluku: "))
alkuluku = True

if luku < 2:
    alkuluku = False
else:
    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            alkuluku = False
            break
if alkuluku:
    print("Luku on alkuluku")
else: 
    print("Luku ei ole alkuluku")
