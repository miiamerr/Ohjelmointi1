# tehtävä 1
print("\nKuukaudet vuodenaikoina")
vuodenajat =("talvi", "kevät", "kesä", "syksy")
kuukausi = int(input("Anna kuukauden numero (1-12): "))
if 1 <= kuukausi <= 12:
    vuodenaika = (kuukausi % 12) // 3
    vuodenaika = vuodenajat[vuodenaika]
    print(f"{kuukausi}. kuukausi kuuluu vuodenaikaan {vuodenaika}")
else:
    print("Virhe: syötä numero 1-12.")


# tehtävä 2

print("\nNimi-simulaattori")

nimet = set()
while True:
   nimi = input("Anna nimi: ")
   print(nimi)
   if nimi == "":
    break
   if nimi in nimet:
        print("Aiemmin syötetty nimi")
   else:
    print("Anna uusi nimi: ")
    nimet.add(nimi)

print("\nSyötetyt nimet:")
for nimi in nimet:
   print(nimi)
  
        
# tehtävä 3
print("\nLentoasema hakukoke:")
lentoasemat = {
   "EFHK": "Helsinki-Vantaa",
   "ESSA": "Arlanda",
   "EGLL": "Heathrow",
   "VTBS": "Suvarnabhum",
   "VTSP": "Phuket"}

print(lentoasemat)
while True:
   haku = input("Valitse: syötä uusi lentoasema, hae jo syötetty lentoasema vai lopetta. (syötä, hae, lopeta): ")
   if haku == "syötä":
      koodi = input("Syötä: lentoaseman ICAO-koodi ja nimi: ")
      print("Lentoaseman ICAON-koodi ja nimi:", koodi)

   elif haku == "hae":
      koodi = input("Syötä ICAO-koodi: ")
      if koodi in lentoasemat:
         print(f"ICAO-koodi {koodi} on {lentoasemat[koodi]} lentoasema.")

   elif haku == "lopeta":
      print("Ohjelma päättyy")
      break

   
