import math

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









    
    