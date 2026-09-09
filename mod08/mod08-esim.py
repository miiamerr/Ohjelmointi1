# mod 8 esimerkkejä

viikonpäivät =("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
print(viikonpäivät)
print("ensimmäinen viikonpäivä", viikonpäivät[0])

# monikko monikon sisällä (kaksi- tai moniulotteinen monikko)
print("\narkipäivät ja viikonlopun päivät ovat omissa monikoissaan samassa monikossa:")
viikonpäivät_v2 =(("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai"), ("lauantai", "sunnuntai"))
print(viikonpäivät_v2)
print("arkipäivät ovat", viikonpäivät_v2[0])
print("viikonlopun päivät ovat", viikonpäivät_v2[1])
print("ensimmäinen arkipäivä", viikonpäivät_v2[0][0])

# yksittäisten arvojen purku erillisiin muuttujiin

(eka, toka, kolmas, neljäs, viides, kuudes, seitsemäs) = viikonpäivät
print(eka, kolmas, viides, seitsemäs)


## monikko ja funktio (muokattu esimerkki materiaalista)
import random

print("\nTuplanoppa")

def heitä():
    # luodaan kaksialkioinen monikko ja palautetaan se suoraan
    return (random.randint(1, 6), random.randint(1, 6))

nopat = heitä()
print(nopat)
noppa1, noppa2 = heitä()
print(f"Nopista tuli {nopat[0]} ja {nopat[1]}.")

###################
## Joukko (set)
print("\nJoukkoja")
viikonpäivät ={"maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai"}
print(viikonpäivät)

# Sama arvo voi esiintyä joukossa vain kerran (arvot on uniikkeja)
viikonpäivät.add("extrapäivä")
viikonpäivät.add("extrapäivä")
for päivä in viikonpäivät:
    print(päivä)
viikonpäivät.remove("keskiviikko")
# kaatuu jos viitataan arvoon, mitä ei ole
#viikonpäivät.remove("jotain_mitä_ei_löydy")
print(viikonpäivät)

########################
# Sanakirja (dictionary)
print("\nSanakirjaesimerkkejä")
numerot = {"Viivi": "050-1234567",
           "Ahmed": "040-1112223",
           "Pekka": "050-7654321"}

numerot["Olga"] = "050-1011012"
numerot["Mary"] = "0401-2132139"

# sanakirjan arvoihin viitataan avaimella, joka on uniikki
numerot["Pekka"] = "poistettu"
# sama arvo voi toistus
numerot["Ahmed"] = "050-1234567"

print(numerot)
print("Olgan numero on", numerot["Olga"])

#nimi =input("Anna nimi: ")
nimi = "Pekka"
# if-lauseessa voi testata, esiintyykö avain sanakirjassa
if nimi in numerot:
    print(f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}.")

###
# Sisäkkäiset tietorakenteet
print("\nEsimerkki pelaajien mahdollisesta tietorakenteesta jossain monipelissä")
players = [
    {
    "name": "Player 1",
    "skill_level": 10,
    "inventory": {"map", "knife"}
    },
    {
    "name": "Player 2",
    "skill_level": 20,
    "inventory": {"tent", "axe"}
    }
]

# Tulostetaan pelaajien tiedot
#print(players)
for player in players:
    #print(player)
    print(f"Pelaajan {player['name']} taitotaso on {player['skill_level']}, hallussa:")
    for item in player["inventory"]:
        print(f"- {item}")