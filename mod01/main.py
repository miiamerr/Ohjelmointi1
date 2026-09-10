import math
import random

numbers = []

while True:
    input_number = input("Anna kokonaisluku: ")
    if input_number == "":
        break
    num = int(input_number)
    numbers.append(int(input_number))
numbers.sort(revers=True)
for num in range(2):
    print(numbers[num])

