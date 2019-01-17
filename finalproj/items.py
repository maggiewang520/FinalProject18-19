## special items

class Item():

    def __init__(self, name, type, power, use):
        self.name = name
        self.type = type
        self.power = power
        self.use = use

    def showstats(self):
        print()
        print(f"these are the stats of '{self.name}' : ")
        print(f" - type : {self.type}")
        print(f" - {self.type} power : {self.power}")
        print(f" - number of uses : {self.use}")
        print()

    def __str__(self):
        return self.name

    __repr__ = __str__

ds = Item('diss track', 'attack', 10, 2)
exp = Item('expose for racism', 'attack', 18, 1)
call = Item('call out for scamming fans', 'attack' 10, 1)


fake = Item('fake apology', 'defense', 5, 2)
disapp = Item('disappear off the internet for like a month', 'defense', 8, 1)
exc = Item('make bull excuses for being an idiot', 'defense', 6, 2)



all_attacks = [ ds, exp, call,
all_defenses = [ fake, disapp, exc,

your_attacks = [ ]
your_defenses = [ ]

def which_one( choice1, choice2 ):
    ### function of choosing between pairs of attacks and defenses ###

print()
print(f"well done, you have chosen well.")
time.sleep(1)
print(f"the last thing there is to do is to go to walmart and select your special items")
time.sleep(1)
print(f"these are special attacks and defenses that can greatly increase your chances of winning")
print()
time.sleep(1)
print(f"yeeting to walmart now...")
time.sleep(2)
print()
print()
print(f"you walk into walmart and head to the attacks section first.")
time.sleep(1)
print(f"you will be given two pairs of options, choose 1 from each pair.")
time.sleep(1)
print()
