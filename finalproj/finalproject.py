import time

##intro

print ( "welcome, bienvenido, benvenuto, bem vinda, 欢迎, ようこそ, to Maggie's final project")
time.sleep(1)
print('you will embark on the ultimate adventure around LA')
time.sleep(1)
print( 'and you will collect allies, items, and more along the way')
time.sleep(3)
print( 'this is all in preparation for an epic battle at the end')
time.sleep(2)
print( "and here is a little bit of good luck from me cuz you'll need it")
time.sleep(2)

start = input( 'are you ready to begin the adventure?! ')

if start == 'yes':
    print("of course you are. I expected no less of you. let's go")
else:
    print("welp. too bad. we are starting anyway")

time.sleep(1)
for x in range (0,5):
    b = "Loading" + "." * x
    print (b, end="\r")
    time.sleep(1)

playerName = input('ok, first, what is your name? ')

## final battle setup

class Fighter:

    def __init__(self, name, species, health, atkCoeff, defCoeff):
        self.name = name
        self.species = species
        self.health = health
        self.atkCoeff = atkCoeff
        self.defCoeff = defCoeff

    def eat(self):
        print(f"{self.name} ate the food and increased their health")
        self.health += 20
        print(f"{self.name}'s health is now {self.health}")

    def __str__(self):
        return self.name

    __repr__ = __str__

class Youtuber(Fighter):

    def __init__(self, name, species, health, atkCoeff, defCoeff, subscribers):
        Fighter.__init__(self, name, species, health, atkCoeff, defCoeff)
        self.subscribers = subscribers

    def stats(self):
        print(f"these are the stats of {self.name}")
        time.sleep(1)
        print(f" - species: {self.species}")
        time.sleep(1)
        print(f" - health: {self.health}")
        time.sleep(1)
        print(f" - attack power: {self.atkCoeff}")
        time.sleep(1)
        print(f" - defense power: {self.defCoeff}")
        time.sleep(1)
        print(f" - subscribers: {self.subscribers}")
        time.sleep(1)

    def gainSubs(self):
        print(f"{self.name} posted a diss track and gained subscribers!")
        self.subscribers += 100000
        print(f"{self.name}'s subscriber count is now {self.subscribers}")
        print(f"this also makes {self.name} more powerful")
        self.atkCoeff += 1
        print(f"{self.name}'s attack power is now {self.atkCoeff}")

    def loseSubs(self):
        print(f"{self.name} was racist and sexist and lost subscribers")
        self.subscribers -= 1000000
        print(f"{self.name}'s subscriber count is now {self.subscribers}")
        print(f"this also makes {self.name} weaker")
        self.atkCoeff -= 1
        print(f"{self.name}'s attack power is now {self.atkCoeff}")

class Celeb(Fighter):

    def __init__(self, name, species, health, atkCoeff, defCoeff, networth):
        Fighter.__init__(self, name, species, health, atkCoeff, defCoeff)
        self.networth = networth

    def stats(self):
        print(f"these are the stats of {self.name}")
        time.sleep(1)
        print(f" - species: {self.species}")
        time.sleep(1)
        print(f" - health: {self.health}")
        time.sleep(1)
        print(f" - attack power: {self.atkCoeff}")
        time.sleep(1)
        print(f" - defense power: {self.defCoeff}")
        time.sleep(1)
        print(f" - net worth: {self.networth}")
        time.sleep(1)

    def makeMoney(self):
        print(f"{self.name} put out a new movie or song and acquired the dough!")
        self.networth += 1000000
        print(f"{self.name}'s net worth is now {self.networth}")
        print(f"this also makes {self.name} more powerful")
        self.atkCoeff += 1
        print(f"{self.name}'s attack power is now {self.atkCoeff}")

    def loseMoney(self):
        print(f"{self.name} screwed up and lost the dough")
        self.networth -= 1000000
        print(f"{self.name}'s net worth is now {self.networth}")
        print(f"this also makes {self.name} weaker")
        self.atkCoeff -= 1
        print(f"{self.name}'s attack power is now {self.atkCoeff}")


ksi = Youtuber( 'KSI', 'the devil himself', 50, 2, 1, 19921956)
lpaul = Youtuber( 'Logan Paul', 'chungus', 60, 1, 2, 18773617)

jpaul = Youtuber( 'Jake Paul', 'chungus jr.', 40, 1.5, 1, 17709933)
shane = Youtuber( 'Shane Dawson', 'illuminati himself', 70, 2, 2.5, 19733606)

pew = Youtuber( 'PewdiePie', 'swedish lasagna', 90, 3, 3, 80278892)
tseries = Youtuber( 'T-Series', 't-gay', 70, 2, 2, 79593540)

jstar = Youtuber( 'Jeffree Star', 'definitely not human', 70, 2, 1.5, 12110610)
jcharles = Youtuber( 'James Charles', 'sister', 80, 1.5, 2, 13114500)

kimk = Celeb( 'Kim Kardashian', 'birth giver', 60, 1.5, 2, 350000000)
kylie = Celeb( 'Kylie Jenner', 'birth giver 3000', 80, 2, 2, 900000000)

allies = []
enemies = []

set1 = {
    'attacks': {
        'attack1': 5,
        'attack2': 3,
        'attack3': 4
    },
    'defenses': {
        'defense1': 5,
        'defense2': 4,
        'defense3': 3
    }
}

set2 = {
    'attacks': {
        'attack1': 5,
        'attack2': 3,
        'attack3': 4
    },
    'defenses': {
        'defense1': 5,
        'defense2': 4,
        'defense3': 3
    }
}

set3 = {
    'attacks': {
        'attack1': 5,
        'attack2': 3,
        'attack3': 4
    },
    'defenses': {
        'defense1': 5,
        'defense2': 4,
        'defense3': 3
    }
}

## adventure begins

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
    print("these are all the destinations that are available")
    print(*available_dests, sep = ", ")

def whereToYeet( alldests ):
    global available_dests
    displaydests()
    dest = input(f"where would you like to go? choose one of the valid destinations " )
    while dest not in alldests:
        dest = input(f"please choose one of the valid destinations: {available_dests} " )
    time.sleep(1)
    print(f"okay, we are yeeting to {dest} now.")
    available_dests.remove(dest)
    time.sleep(1)
    for x in range (0,5):
        b = "Transporting" + "." * x
        print (b, end="\r")
        time.sleep(1)
    print(f"we have arrived in {dest}!")
    return dest

def displayTeams():
    print("these are your allies")
    time.sleep(1)
    print(*allies, sep = ", ")
    time.sleep(1)
    print("and these are your enemies")
    time.sleep(1)
    print(*enemies, sep = ", ")

def chooseAlly( place ):
    time.sleep(1)
    print(f"at {place}, you come accross {dests[place][0]} and {dests[place][1]} hanging out together")
    time.sleep(1)
    print(f"you can only pick one to be your ally, and the other one will automatically be placed in the enemy team" )
    time.sleep(1)
    print(f"you will now see the stats of {dests[place][0]} and {dests[place][1]} to decide")
    time.sleep(1)
    dests[place][0].stats()
    time.sleep(1)
    dests[place][1].stats()
    time.sleep(2)
    yourally = input(f"Choose an ally from {place}: {dests[place][0]} or {dests[place][1]} ")
    yourenemy = ""
    if yourally == dests[place][0].name :
        allies.append(dests[place][0])
        yourenemy = dests[place][1]
        enemies.append(dests[place][1])
    elif yourally == dests[place][1].name :
        allies.append(dests[place][1])
        yourenemy = dests[place][0]
        enemies.append(dests[place][0])
    print(f"{yourally} is now your new friend and {yourenemy} is so offended you chose {yourally} over them that they hate you")
    time.sleep(1)
    displayTeams()

time.sleep(1)
print(f"it's already time to go to our first destination.")
time.sleep(1)
chooseAlly(whereToYeet(available_dests))

while len(available_dests) >= 1:
    time.sleep(1)
    print(f"okay, next destination")
    time.sleep(1)
    chooseAlly(whereToYeet(available_dests))
    time.sleep(1)