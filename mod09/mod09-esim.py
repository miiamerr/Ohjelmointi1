
k1 ='Sileäkarvainen collie'
k1_nimi ='Aino'
k1_syntymävuosi = 2014

k2 = 'Mopsi'
k2_nimi = 'Luna'
k2_syntymävuosi = 2004

k3 = 'Chihuahua'
k3_nimi = 'Lörtsy'
k3_syntymävuosi = 2026

class Koira:
    pass

# Luokka on kuin suunnitelma. Olio on sen perusteella rakennettu yksilö.

koira = Koira()
koira2 = Koira()

koira.nimi = 'Aino'
koira.rotu = 'Sileäkarvainen collie'

koira2.nimi = 'Luna'
koira2.rotu = 'Mopsi'

print('Ensimmäisen koiran nimi:', koira.nimi)
print('Ensimmäisen koiran rotu:', koira.rotu)

print('Ensimmäisen koiran nimi:', koira2.nimi)
print('Ensimmäisen koiran rotu:', koira2.rotu)

# teimme juuri luokan Koira ilman ominaisuuksia
# tämän jälkeen määrittelimme ominaisuudet yksi kerrallaan == työlästä!!!

# Näin tehdään oikeasti:
# Oliossa määritellään ns. tieto ja toiminta

#Koira:

# Koiran ominaisuudet
# - nimi
# - rotu
# - syntymävuosi

# Koiran toiminnot
# - Hauku
# - Heiluta häntää
# - Syö
# - Nuku

class Koira:

    # Luokkamuuttuja
    tehty = 0

    def __init__(self, nimi, rotu, syntymävuosi, haukahdus=('Vuuf-vuh')):
        self.nimi = nimi
        self.rotu = rotu
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        self.luokitus = 'nisäkäs'
        Koira.tehty += 1

    def hauku(self, kerrat):
        print(f"{self.nimi} tervehtii sinua")
        for i in range(kerrat):
             print(self.haukahdus)


koira = Koira("Lörtsy", "Chihuahua", 2026, "Woof")
koira2 = Koira("Aino", "Sileäkarvainen collie", 2014, "Hau Hau")
koira3 = Koira("Luna", "Mopsi", 2004)

Koira.tehty
print(f"Koiria on nyt {koira.tehty}.")

koira.hauku(10)
print()
koira2.hauku(2)
koira3.hauku(1)

print(f'1. Koiran nimi on {koira.nimi}, rotu on {koira.rotu} ja syntymävuosi {koira.syntymävuosi}')
print(f'2. Koiran nimi on {koira2.nimi} rotu on {koira2.rotu} ja syntymävuosi {koira2.syntymävuosi}')

# print(koira) - viittaus olioon, ei muuttuja

class Player:

    def __init__(self, name, skill_level, inventory):
        self.name = name
        self.skill_level = skill_level
        self.inventory = inventory


    def show_info(self):
        print(f"Player's name:", self.name)
        print(f"Player's skill level", self.skill_level)
        print(f"Player's inventory:", self.inventory)
        for item in self.inventory:
            print('>', item)
        print('-------')

    def add_item(self, item):
        self.inventory.add(item)
        

player = Player("Pyry", "10", "knife")
player2 = Player("Darrow", 1000, "axe")

player.show_info()
player2.show_info()

player.add_item("key")
player.show_info()


print(f"1. Player's name is {player.name}, skill level is {player.skill_level} and inventory: {player.inventory}.")
print(f"2. Player's name is {player2.name}, skill level is {player2.skill_level} and inventory: {player2.inventory}.")

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

for player in players:
    
    print(f"Pelaajan {player['name']} taitotaso on {player['skill_level']}, hallussa:")
    for item in player["inventory"]:
        print(f"- {item}")