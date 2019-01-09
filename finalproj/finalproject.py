import time

##intro

print ( "welcome, bienvenido, benvenuto, bem vinda, 欢迎, ようこそ, to Maggie's final project")
time.sleep(1)
print('you will embark on the ultimate adventure around LA')
time.sleep(2)
print( 'you will be exploring important landmarks throughout LA - such as Youtubers houses')
time.sleep(1)
print( 'and collecting allies, items, and more along the way')
time.sleep(3)
print( 'this is all in preparation for an ePiC battle at the end')
time.sleep(2)
print( "and here is a little bit of good luck from me cuz you'll need it")
time.sleep(2)

start = input( 'are you ready to begin the adventure?! ')

if start == 'yes':
    print("of course you are. I expected no less of you. let's gooo")
else:
    print("welp. too bad. we are starting anyway")

time.sleep(1)
for x in range (0,5):
    b = "Loading" + "." * x
    print (b, end="\r")
    time.sleep(1)

playerName = input('ok, first, what is your name?')

## final battle setup

class Fighter:

    def __init__(self, name, species, health, atkCoeff, defCoeff, excl):
        self.name = name
        self.species = species
        self.health = health
        self.atkCoeff = atkCoeff
        self.defCoeff = defCoeff
        self.excl = excl

    def eat(self):
        print(f"{self.name} ate the food and increased their health")
        self.health += 20
        print(f"{self.name}'s health is now {self.health}")

class Youtuber(Fighter):

    def __init__(self, name, species, health, atkCoeff, defCoeff, excl, subscribers):
        Fighter.__init__(self, name, species, health, atkCoeff, defCoeff, excl)
        self.subscribers = subscribers

    def stats(self):
        print(f"these are the stats of {self.name}")
        print(f"species: {self.species}")
        print(f"health: {self.health}")
        print(f"attack power: {self.atkCoeff}")
        print(f"defense power: {self.defCoeff}")
        print(f"subscribers: {self.subscribers}")

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

    def __init__(self, name, species, health, atkCoeff, defCoeff, excl, networth):
        Fighter.__init__(self, name, species, health, atkCoeff, defCoeff, excl)
        self.networth = networth

    def stats(self):
        print(f"these are the stats of {self.name}")
        print(f"species: {self.species}")
        print(f"health: {self.health}")
        print(f"attack power: {self.atkCoeff}")
        print(f"defense power: {self.defCoeff}")
        print(f"net worth: {self.networth}")

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

attacks = { }
defenses = { }

ksi.stats()
kimk.stats()
