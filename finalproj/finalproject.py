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

if start == 'yes' or 'y' or 'sure' or 'yeah' or 'ye' or 'yeet':
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

class Youtuber(Fighter):

    def __init__(self, name, species, health, atkCoeff, defCoeff, subscribers):
        Fighter.__init__(self, name, species, health, atkCoeff, defCoeff)
        self.subscribers = subscribers

    def gainSubs(self):
        print(f"{self.name} posted a diss track and gained subscribers!")
        self.subscribers += 100000
        print(f"{self.name}'s subscriber count is now {self.subscribers}")
        print(f"this also makes {self.name} more powerful")
        self.atkCoeff += 1
        print(f"{self.name}'s attack power is now {self.atkCoeff}")

class Celeb(Fighter):

    def __init__(self, species, health, atkCoeff, defCoeff, networth):
        Fighter.__init__(self, name, species, health, atkCoeff, defCoeff)
        self.networth = networth

    def makeMoney(self):
        print(f"{self.name} put out a new movie or song and acquired the dough!")
        self.networth += 1000000
        print(f"{self.name}'s net worth is now {self.networth}")
        print(f"this also makes {self.name} more powerful")
        self.atkCoeff += 1
        print(f"{self.name}'s attack power is now {self.atkCoeff}")

allies = []
enemies = []
