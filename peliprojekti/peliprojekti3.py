pelaaja = input ('Mikä sinun nimesi on? ') 
print('Hauska tavata', pelaaja + '!')

ikäraja = 13
ikä = float(input("Anna ikäsi: "))
if ikä >= 13:
    print("\n---Tervetuloa Rekku Rescue-peliin", pelaaja + "!!!!---")
elif ikä < ikäraja:
    print("Pelaaja on alaikäinen")
    print("\n---Rekku Rescue sammutetaan---")

peli_käynnissä = True

while peli_käynnissä:
    print("Valitse minne mennään: Uusi peli (U), Varustevalikko (V) tai Lopeta peli (L): ")
    valinta = input("Anna komento: ")
    if valinta == "U":
        print("\n-----Uusi peli!-----")
        print("3, 2, 1, Peli alkaa: ")
        arvaus1 = input("Missä huoneessa Rekku voisi olla?\n 1. Makuuhuone, 2. Keittiö, 3. Piha: ")
        while arvaus1 == "1.":
           print("Huh, löysit Rekun. Hyvää työtä!")
           break
        if arvaus1 != "1.":
            print("Rekkua ei löytynyt.")
            print("Jatketaan etsimistä!")
        
    elif valinta == "L":
        print("Lopetetaan peli")
        print("Peli sammutetaan")
    elif valinta == "V":
        tavarat = ["koiran namit", "Rekun kuva", "Rekun hihna", "Taskulamppu", "Puhelin"]
        valitut = []
        print(tavarat)
    while True:
        valinta = input("Valitse mukaasi tarvittavat tavarat,\n Lopeta painamalla Enter: ")
        if valinta == "":
         break
        valitut.append(valinta)
    print("Valitut tavarat: ", valitut)
        
        
        
    
         

