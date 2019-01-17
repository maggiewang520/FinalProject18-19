import time

##intro

print ( "welcome, bienvenido, benvenuto, bem vinda, 欢迎, ようこそ, to Maggie's final project")
print()
time.sleep(1)
print('you will be thrusted into the hell that is LA')
time.sleep(1)
print("in order to escape, you will have to collect allies and win the fight at the end")
time.sleep(1)
print()
print( "good luck, you're gonna need it")
time.sleep(2)

print()
start = input( 'are you ready to begin the adventure?! ')

if start == 'yes':
    print("of course you are. I expected no less of you. let's go")
else:
    print("welp. too bad. we are starting anyway")

time.sleep(1)
print()
for x in range (0,5):
    b = "Loading" + "." * x
    print (b, end="\r")
    time.sleep(1)

playerName = input('ok, first, what is your name? ')

## battle setup + etc

class Fighter:

    def __init__(self, name, species, health, atkCoeff, defCoeff, atks, defs):
        self.name = name
        self.species = species
        self.health = health
        self.atkCoeff = atkCoeff
        self.defCoeff = defCoeff
        self.atks = atks
        self.defs = defs

    def attack(self, opponent):
        print()
        print(f"{self.name} has attacked {opponent.name}!")
        if opponent.health >= 20:
            if opponent in enemies:
                print(f"unfortunately, {opponent.name} still has ample health left so they were able to use their defense power.")
                dmg = self.atkCoeff - opponent.defCoeff
                opponent.health -= dmg
            else:
                print(f"fortunately, {opponent.name} has a health less than 20 so they were not able to use their defense power.")
                opponent.health -= self.atkCoeff
        print()
        print(f"the resulting health of {opponent.name} is {opponent.health}")
        print()

    def use_atk(self, opponent):
        print(f"{self.name} has attacked {opponent.name} with {self.atks[1]}")

    def __str__(self):
        return self.name

    __repr__ = __str__

class Youtuber(Fighter):

    def __init__(self, name, species, health, atkCoeff, defCoeff, atks, defs, subscribers):
        Fighter.__init__(self, name, species, health, atkCoeff, defCoeff, atks, defs)
        self.subscribers = subscribers

    def stats(self):
        print()
        print(f"these are the stats of {self.name}")
        time.sleep(1)
        print(f" - species: {self.species}")
        print(f" - health: {self.health}")
        print(f" - attack power: {self.atkCoeff}")
        print(f" - defense power: {self.defCoeff}")
        print(f" - attacks: {self.atks}")
        print(f" - defenses: {self.defs}")
        print(f" - subscribers: {self.subscribers}")
        print()

class Celeb(Fighter):

    def __init__(self, name, species, health, atkCoeff, defCoeff, atks, defs, networth):
        Fighter.__init__(self, name, species, health, atkCoeff, defCoeff, atks, defs)
        self.networth = networth

    def stats(self):
        print()
        print(f"these are the stats of {self.name}")
        time.sleep(1)
        print(f" - species: {self.species}")
        print(f" - health: {self.health}")
        print(f" - attack power: {self.atkCoeff}")
        print(f" - defense power: {self.defCoeff}")
        print(f" - attacks: {self.atks}")
        print(f" - defenses: {self.defs}")
        print(f" - net worth: {self.networth}")
        print()

ksi = Youtuber( 'KSI', 'the devil himself', 50, 10, 1, {'attack1': 2, 'attack2': 3}, {'defense1': 1, 'defense': 1}, 20000000)
lpaul = Youtuber( 'Logan Paul', 'chungus', 60, 9, 2, {'attack1': 2, 'attack2': 3}, {'defense1': 1, 'defense': 1}, 19000000)

jpaul = Youtuber( 'Jake Paul', 'chungus jr.', 70, 8, 1, {'attack1': 2, 'attack2': 3}, {'defense1': 1, 'defense': 1}, 18000000)
shane = Youtuber( 'Shane Dawson', 'illuminati himself', 60, 9, 2, {'attack1': 2, 'attack2': 3}, {'defense1': 1, 'defense': 1}, 20000000)

pew = Youtuber( 'Pewdiepie', 'swedish lasagna', 90, 11, 2, {'attack1': 2, 'attack2': 3}, {'defense1': 1, 'defense': 1}, 80000000)
tseries = Youtuber( 'T-Series', 't-gay', 80, 10, 3, {'attack1': 2, 'attack2': 3}, {'defense1': 1, 'defense': 1}, 79000000)

jstar = Youtuber( 'Jeffree Star', 'inhuman', 50, 9, 2, {'attack1': 2, 'attack2': 3}, {'defense1': 1, 'defense': 1}, 12000000)
jcharles = Youtuber( 'James Charles', 'sister', 60, 8, 2, {'attack1': 2, 'attack2': 3}, {'defense1': 1, 'defense': 1}, 13000000)

kimk = Celeb( 'Kim Kardashian', 'birth giver', 60, 9, 2, {'attack1': 2, 'attack2': 3}, {'defense1': 1, 'defense': 1}, 350000000)
kylie = Celeb( 'Kylie Jenner', 'birth giver 3000', 70, 8, 1, {'attack1': 2, 'attack2': 3}, {'defense1': 1, 'defense': 1}, 900000000)

allies = []
enemies = []

## adventure : team formation

print()
print(f"welcome, {playerName}. you have just arrived in LAX...")
time.sleep(1)

dests = {
    'team 10 house': [jpaul, shane],
    'supreme store': [ksi, lpaul],
    'sephora': [jstar, jcharles],
    'jenner house': [kimk, kylie],
    'hotel': [pew, tseries]
     }

available_dests = list(dests.keys())

def displaydests( ):
    global available_dests
    time.sleep(1)
    print()
    print("these are all the destinations that are available")
    for x in range(len(available_dests)):
        print(f" - {available_dests[x]}")
        time.sleep(0.5)
    print()

def whereToYeet( alldests ):
    global available_dests
    print()
    print(f"so, {playerName}, where would you like to go?")
    displaydests()
    dest = input(f"choose one of the valid destinations listed above " )
    while dest not in alldests:
        displaydests()
        dest = input(f"please choose a valid destination " )
    time.sleep(1)
    print()
    print(f"okay, we are yeeting to {dest} now.")
    available_dests.remove(dest)
    time.sleep(1)
    for x in range (0,3):
        b = "Transporting" + "." * x
        print (b, end="\r")
        time.sleep(1)
    print(f"we have arrived in {dest}!")
    print()
    return dest

def displayTeams():
    print("these are your allies")
    time.sleep(1)
    print(*allies, sep = ", ")
    time.sleep(1)
    print()
    print("and these are your enemies")
    time.sleep(1)
    print(*enemies, sep = ", ")
    print()

def chooseAlly( place ):
    time.sleep(1)
    print()
    print(f"at {place}, you come accross {dests[place][0]} and {dests[place][1]} having a huge argument with one another")
    time.sleep(1)
    print(f"they appear to hate each other. now is your chance to snatch an ally!")
    time.sleep(1)
    print()
    print(f"you will now see the stats of {dests[place][0]} and {dests[place][1]} to help you make a decision")
    time.sleep(1)
    dests[place][0].stats()
    time.sleep(1)
    dests[place][1].stats()
    time.sleep(2)
    yourally = input(f"Choose an ally from {place}: {dests[place][0]} or {dests[place][1]} ")
    yourenemy = ""
    possible_chars = [ dests[place][0].name, dests[place][1].name ]
    while yourally not in possible_chars:
        yourally = input(f"Please choose a valid from {place}: {dests[place][0]} or {dests[place][1]} ")
    if yourally == dests[place][0].name :
        allies.append(dests[place][0])
        yourenemy = dests[place][1]
        enemies.append(dests[place][1])
    elif yourally == dests[place][1].name :
        allies.append(dests[place][1])
        yourenemy = dests[place][0]
        enemies.append(dests[place][0])
    print()
    print(f"{yourally} is now on your side and will fight for you!")
    time.sleep(1)
    print(f"and {yourenemy} is now against you and aspires to destroy you in the final battle")
    print()
    time.sleep(1)
    displayTeams()

print()
time.sleep(1)
print(f"it's already time to go to our first destination.")
time.sleep(1)
print(f"at these destinations, you will meet pairs of characters and have a choice of an ally")
time.sleep(1.5)
print(f"you can only pick one to be your ally, and the other one will automatically be placed in the enemy team" )
time.sleep(2)
print(f"in the final battle, these 5 pairs will fight one another, and best 3 out of 5 battles wins. so choose carefully")
print()
time.sleep(2)

chooseAlly(whereToYeet(available_dests))

while len(available_dests) >= 1:
    time.sleep(1)
    print(f"okay, time to head to the next destination")
    time.sleep(1)
    chooseAlly(whereToYeet(available_dests))
    time.sleep(1)

print()
print(f"ok. now that you have collected all your allies and formed two teams,")
time.sleep(1)
print(f"it is time...")
time.sleep(1)

## final battle

allies[1].use_atk(enemies[1])




