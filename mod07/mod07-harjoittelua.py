def tervehdi():
    print("Moi!")
    return

print("Päivä alkaa tervehdyksellä.")
tervehdi()
print("Sitten siirrytään muihin asioihin.")



def tervehdi(kerrat):
    for i in range(kerrat):
        print("Hyvää päivää " + str(i+1) + ". kerran")
    return

print("Päivä alkaa tervehdyksillä.")
tervehdi(5)
print("Tervehditään lisää.")
tervehdi(2)


def vaihda():
    kaupunki = "Espoo"
    print("Funktiossa lopuksi: " + kaupunki)
    return

kaupunki = "Helsinki"
print("Pääohjelmassa aluksi: " + kaupunki)
vaihda()
print("Pääohjelmassa lopuksi: " + kaupunki)