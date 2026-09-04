
pelaaja = input ('Mikä sinun nimesi on? ') 
print('Hauska tavata', pelaaja + '!')

ikäraja = 13
ikä = float(input("Anna ikäsi: "))
if ikä >= 13:
    print("Tervetuloa seikkailu-peliin", pelaaja + "!!!!")
elif ikä < ikäraja:
    print("Pelaaja on alaikäinen")
    print("Seikkailu-peli sammutetaan")
    


peli_käynnissä = True

while peli_käynnissä:
    print("Valitse minne mennään: Uusi peli (U), Kustomoi hahmoa (K) tai Lopeta peli (L): ")
    valinta = input("Anna komento: ")
    if valinta == "U":
        print("Uusi peli! ")
        print("3, 2, 1, Peli alkaa: ")
        peli1_arvaus = input("Valitse oikea ovi: Ovi 1, Ovi 2 vai Ovi 3: ")
        while peli1_arvaus == "Ovi 3":
            print("Hienoa valitsit oikean oven")
            print("Jatketaan eteenpäin")
            break
        if peli1_arvaus != "Ovi 3":
            print("Hävisit pelin")
            print("Valitsit väärän oven")

    elif valinta == "L":
        print("Lopetetaan Seikkailu-peli")
        print("Peli sammutetaan")
    elif valinta == "K":
        print("Ehostetaan tyyliäsi! ")
        väri = input ("Valitse hahmosi väri?: ")
        print("Tyylikästä,", väri, "sopii sinulle hyvin!")
    
         

