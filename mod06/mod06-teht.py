
# tehtävä 1

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