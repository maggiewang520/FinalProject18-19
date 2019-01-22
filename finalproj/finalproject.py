import time
import random

## introduction to game

print ( "welcome! to Maggie's final project! ")
print()
time.sleep(2)
print('in a short moment, you will be thrusted into the hell that is LA')
time.sleep(2)
print("in order to escape, you will have to collect allies and win the fight at the end")
time.sleep(2)
print()
print( "good luck, you're gonna need it")
time.sleep(2)

print()
start = input( 'are you ready to begin the adventure?! ')

if start == 'yes':
    print("of course you are. I expected no less of you. let's go")
else:
    print("too bad. we are starting anyway")

time.sleep(1)
print()
for x in range (0,5):
    b = "Loading" + "." * x
    print (b, end="\r")
    time.sleep(1)

playerName = input('ok, first, what is your name? ')

## character setup and collection

class Fighter:

    ### class for all characters in the game that have characteristics needed for the final battle ###

    def __init__(self, name, species, health, atkCoeff, defCoeff):
        self.name = name
        self.species = species
        self.health = health
        self.atkCoeff = atkCoeff
        self.defCoeff = defCoeff

    def attack(self, opponent):
        ### simple attack function with use of attack power and defense power ###
        print()
        print(f"{self.name} has attacked {opponent.name}!")
        time.sleep(2)
        if opponent.health >= 20:
          print(f"{opponent.name} still had ample health left so they were able to use their defense power")
          dmg = self.atkCoeff - opponent.defCoeff
          opponent.health -= dmg
        else:
          print(f"{opponent.name} has not enough health so they were not able to use their defense power.")
          opponent.health -= self.atkCoeff
        print()
        time.sleep(2)
        print(f"the resulting health of {opponent.name} is {opponent.health}")
        print()
        time.sleep(1)

    def __str__(self):
        return self.name

    __repr__ = __str__

class Youtuber(Fighter):

    ### sub class of fighter for youtubers specifically (subscribers trait is unique) ###

    def __init__(self, name, species, health, atkCoeff, defCoeff, subscribers):
        Fighter.__init__(self, name, species, health, atkCoeff, defCoeff,)
        self.subscribers = subscribers

    def stats(self):
        ### displaying the statistics of the character ###
        print()
        print(f"these are the stats of {self.name}")
        time.sleep(1)
        print(f" - species: {self.species}")
        print(f" - health: {self.health}")
        print(f" - attack power: {self.atkCoeff}")
        print(f" - defense power: {self.defCoeff}")
        print(f" - subscribers: {self.subscribers}")
        print()

class Celeb(Fighter):

    ### sub class of fighter for traditional celebrities only (net worth) ###

    def __init__(self, name, species, health, atkCoeff, defCoeff, networth):
        Fighter.__init__(self, name, species, health, atkCoeff, defCoeff )
        self.networth = networth

    def stats(self):
        ### displaying the statistics of the character ###
        print()
        print(f"these are the stats of {self.name}")
        time.sleep(1)
        print(f" - species: {self.species}")
        print(f" - health: {self.health}")
        print(f" - attack power: {self.atkCoeff}")
        print(f" - defense power: {self.defCoeff}")
        print(f" - net worth: {self.networth}")
        print()

ksi = Youtuber( 'KSI', 'the devil himself', 50, 10, 1, 20000000)
lpaul = Youtuber( 'Logan Paul', 'chungus', 60, 9, 2, 19000000)

jpaul = Youtuber( 'Jake Paul', 'chungus jr.', 70, 8, 1, 18000000)
shane = Youtuber( 'Shane Dawson', 'illuminati himself', 60, 9, 2, 20000000)

pew = Youtuber( 'Pewdiepie', 'swedish lasagna', 90, 11, 2, 80000000)
tseries = Youtuber( 'T-Series', 't-gay', 80, 10, 3, 79000000)

jstar = Youtuber( 'Jeffree Star', 'inhuman', 50, 9, 2, 12000000)
jcharles = Youtuber( 'James Charles', 'sister', 60, 8, 2, 13000000)

kimk = Celeb( 'Kim Kardashian', 'birth giver', 60, 9, 2, 350000000)
kylie = Celeb( 'Kylie Jenner', 'birth giver 3000', 70, 8, 1, 900000000)

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
    ### this function displays the remaining available destinations that the player can head to" ###
    global available_dests
    time.sleep(1)
    print()
    print("available destinations: ")
    for x in range(len(available_dests)):
        print(f" - {available_dests[x]}")
        time.sleep(0.5)
    print()

def whereToYeet( alldests ):
    ### this function allows the player to choose where to head to from a given list of locations ###
    global available_dests
    print()
    print(f"{playerName}, where would you like to go?")
    displaydests()
    dest = input(f"choose a valid destinations listed above: " )
    while dest not in alldests:
        displaydests()
        dest = input(f"please choose a valid destination: " )
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
    ### this function displays the current status of the two teams (allies and enemies), determined by how many locations the player has already visited ###
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
    ### this function allows the player to meet the two characters present at each given location and allows the player to select which they would like as an ally and which as an enemy ###
    time.sleep(1)
    print()
    print(f"at {place}, you come accross {dests[place][0]} and {dests[place][1]} having a huge argument with one another")
    time.sleep(2)
    print(f"they appear to hate each other. now is your chance to snatch an ally!")
    time.sleep(2)
    print()
    print(f"you will now see the stats of {dests[place][0]} and {dests[place][1]} to help you make a decision")
    time.sleep(2)
    dests[place][0].stats()
    time.sleep(2)
    dests[place][1].stats()
    time.sleep(2)
    yourally = input(f"Choose an ally from {place}: {dests[place][0]} or {dests[place][1]} ? ")
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
    time.sleep(2)
    displayTeams()

print()
time.sleep(1)
print(f"it's already time to go to our first destination.")
time.sleep(1)
print(f"at these destinations, you will meet pairs of characters and have a choice of an ally")
time.sleep(2)
print(f"you can only pick one to be your ally, and the other one will become your enemy" )
time.sleep(2)
print(f"in the final battle, these 5 pairs will fight one another, so choose carefully")
print()
time.sleep(2)

chooseAlly(whereToYeet(available_dests))

while len(available_dests) >= 1:
    time.sleep(1)
    print(f"okay, time to head to the next destination")
    time.sleep(1)
    chooseAlly(whereToYeet(available_dests))
    time.sleep(1)

## special items

class Item():

    ### this class defines the special attacks and defenses that can be used during the final battle ###

    def __init__(self, name, itemtype, power, use):
        self.name = name
        self.itemtype = itemtype
        self.power = power
        self.use = use

    def showstats(self):
        ### displaying the statistics of the attack or defense ###
        print()
        print(f"these are the stats of '{self.name}' : ")
        print(f" - type : {self.itemtype}")
        print(f" - {self.itemtype} power : {self.power}")
        print(f" - number of uses : {self.use}")
        print()

    def __str__(self):
        return self.name

    __repr__ = __str__

ds = Item('diss track', 'attack', 10, 2)
exp = Item('expose for racism', 'attack', 18, 1)
call = Item('call out for scamming fans', 'attack', 10, 1)
twit = Item('taking it to twitter', 'attack', 6, 2)

fake = Item('fake apology', 'defense', 4, 2)
disapp = Item('disappear off the internet', 'defense', 6, 1)
exc = Item('making bad excuses', 'defense', 6, 2)
proof = Item('disproving rumors with proof', 'defense', 10, 1)

avail_attacks = [ ds, exp, call, twit ]
avail_defenses = [ fake, disapp, exc, proof ]

your_attacks = [ ]
your_defenses = [ ]

def display_items():
    ### this function displays the attacks and defenses that are available to the player based on what they have already selected ###
    print("these are the attacks available to you")
    time.sleep(1)
    print(*your_attacks, sep = ", ")
    time.sleep(2)
    print()
    print("and these are the defenses available to you")
    time.sleep(1)
    print(*your_defenses, sep = ", ")
    print()

def which_one( choice1, choice2, atk_or_def ):
    ### this function allows the player to choose between pairs of attacks and defenses based on statistics of the items ###
    print(f"your two choices are {choice1.name} and {choice2.name}")
    time.sleep(3)
    choice1.showstats()
    time.sleep(2)
    choice2.showstats()
    item_choices = [ choice1.name, choice2.name ]
    time.sleep(2)
    item_choice = input(f"which one would you like to pick? ")
    while item_choice not in item_choices:
        item_choice = input(f"please pick a valid choice: {choice1} or {choice2}? ")
    if atk_or_def == 'attack':
        if item_choice == choice1.name:
            your_attacks.append(choice1)
            avail_attacks.remove(choice1)
        elif item_choice == choice2.name:
            your_attacks.append(choice2)
            avail_attacks.remove(choice2)
    elif atk_or_def == 'defense':
        if item_choice == choice1.name:
            your_defenses.append(choice1)
            avail_defenses.remove(choice1)
        elif item_choice == choice2.name:
            your_defenses.append(choice2)
            avail_defenses.remove(choice2)
    time.sleep(2)
    display_items()

print()
print(f"well done, you have chosen well.")
time.sleep(2)
print(f"the last thing there is to do is to go to walmart and select your special items")
time.sleep(2)
print(f"these are special attacks and defenses that can greatly increase your chances of winning")
print()
time.sleep(3)
print(f"yeeting to walmart now...")
time.sleep(2)
print()
print(f"you walk into walmart and head to the attacks section first.")
time.sleep(2)
print(f"you will be given two pairs of options, choose 1 from each pair.")
time.sleep(2)
print(f"the one you do not select will be your enemies' items")
print()
time.sleep(3)
which_one( ds, exp, 'attack')
time.sleep(3)
print(f"next pair of attack items")
time.sleep(1)
which_one( call, twit, 'attack')
time.sleep(3)
print(f"now we are moving on to the defense items")
time.sleep(2)
which_one( fake, disapp, 'defense')
time.sleep(3)
print(f"next pair of defense items")
time.sleep(1)
which_one( exc, proof, 'defense')
print()
time.sleep(5)

## final battle

print()
print(f"ok. now that you have collected all your allies and formed two teams, and selected your items")
time.sleep(2.5)
print(f"it is time...")
time.sleep(1)
print()
print(f"before we begin, these are all of your current stats")
time.sleep(2)
print()
displayTeams()
print()
time.sleep(2)
display_items()
print()
time.sleep(4)
print(f"best 3 out of 5 battles. good luck!")
print()
print()
time.sleep(3)
print(f"okay, {playerName}, we are gonna get started now")
ready = input(f"are you ready to begin the battle?")
if ready == 'yes':
    print("of course you are. let us begin")
else:
    print("too bad, you have no choice. i can't watch you rot here in LA")

num_won = 0
num_lost = 0
game_num = 0

def enemy_use_item( attacker, opponent ):
    ### this function randomly decides if the enemy will use a special item or not, and uses it if yes ###
  coin = [ 'heads', 'tails', 'tails', 'tails' ]
  use_or_not = random.choice(coin)
  time.sleep(2)
  if use_or_not == 'heads':
    print(f"oof, {attacker.name} has decided to use a special item")
    all_items_to_avail = [ your_attacks[0], your_attacks[1], your_defenses[0], your_defenses[1] ]
    enemy_item_used = random.choice(all_items_to_avail)
    time.sleep(2)
    print()
    print(f"{opponent.name} decided to use {enemy_item_used.name} which is a {enemy_item_used.itemtype}")
    if enemy_item_used.itemtype  == 'attack':
      print()
      time.sleep(3)
      damage = attacker.atkCoeff + enemy_item_used.power
      print(f"{attacker.name} has attacked {opponent.name} with an increased attack power of {damage} using {enemy_item_used.name}")
      opponent.health -= damage
      print()
      print(f"the resulting health of {opponent.name} is {opponent.health}")
      time.sleep(2)
      print()
      enemy_item_used.use -= 1
      if enemy_item_used.use == 0:
        print(f"{attacker.name} may no longer use this anymore" )
        all_items_to_avail.remove(enemy_item_used)
      else:
        print(f"the remaining number of uses left for {enemy_item_used.name} is {enemy_item_used.use}")
    elif enemy_item_used.itemtype == 'defense':
      print(f"since the item is a defense, {attacker.name} will now restore their health unconditionally with a level of {enemy_item_used.power}"  )
      print()
      time.sleep(3)
      attacker.health += enemy_item_used.power
      print(f"the resulting health of {attacker.name} is {attacker.health}")
      print()
      enemy_item_used.use -= 1
      if enemy_item_used.use == 0:
        print(f"{attacker.name} may no longer use this item anymore" )
        all_items_to_avail.remove(enemy_item_used)
      else:
        print(f"the remaining number of uses left for {enemy_item_used.name} is {enemy_item_used.use}")

  else:
    print(f"{opponent} decided they are not going to use a special item. you are in luck")
    print()
    time.sleep(2)

def ally_attack( attacker, opponent ):
    ### this function allows the player to choose whether or not to regularly attack the enemy and attacks them ###
  print()
  attack_or_not = input(f"would you like for {attacker.name} to attack {opponent.name}?")
  time.sleep(2)
  print()
  if attack_or_not == 'yes':
    print(f"{attacker.name} has attacked {opponent.name} with a power of {attacker.atkCoeff}!")
    time.sleep(3)
    if opponent.health >= 20:
      print(f"{opponent.name} still had ample health left so they were able to use their defense power of {opponent.defCoeff}")
      dmg = attacker.atkCoeff - opponent.defCoeff
      opponent.health -= dmg
      print()
      time.sleep(3)
      print(f"the amount of damage done to {opponent} was {dmg} health points")
    else:
      print(f"{opponent.name} has not enough health so they were not able to use their defense power.")
      opponent.health -= attacker.atkCoeff
      print()
      time.sleep(2)
      print(f"the amount of damage done to {opponent} was {dmg} health points")
    time.sleep(2)
    print(f"the resulting health of {opponent.name} is {opponent.health}")
    print()
    time.sleep(3)
  else:
    print(f"ok... idk why you would choose this but anyways...")
    time.sleep(2)
  time.sleep(3)
  print()
  use_item_or_not( attacker, opponent )
  print()
  print()

def enemy_attack( attacker, opponent ):
    ### this function always has the enemy attacing the ally ###
  print()
  print(f"{attacker.name} has ⓐⓣⓣⓐⓒⓚed {opponent.name} with a power of {attacker.atkCoeff}!")
  time.sleep(2)
  if opponent.health >= 20:
    print(f"{opponent.name} still had ample health left so they were able to use their defense power of {opponent.defCoeff}")
    dmg = attacker.atkCoeff - opponent.defCoeff
    opponent.health -= dmg
    print()
    time.sleep(3)
    print(f"the amount of damage done to {opponent} was {dmg} health points")
  else:
    print(f"{opponent.name} has not enough health so they were not able to use their defense power.")
    opponent.health -= attacker.atkCoeff
    print()
    time.sleep(3)
    print(f"the amount of damage done to {opponent} was {dmg} health points")
  time.sleep(2)
  print(f"the resulting health of {opponent.name} is {opponent.health}")
  print()
  time.sleep(3)
  print()
  enemy_use_item( attacker, opponent )

def use_item( attacker, opponent, item_used ):
    ### this function uses an item if the player decides to do so ###
  print(f"okay. so you want to use {item_used.name}")
  print()
  time.sleep(2)
  item_used.showstats()
  print()
  time.sleep(2)
  if item_used.itemtype  == 'attack':
    print(f"since the item you chose to use is an attack, {attacker} will now ⓐⓣⓣⓐⓒⓚ {opponent} with an additional attack power of {item_used.power}"  )
    print()
    time.sleep(3)
    damage = attacker.atkCoeff + item_used.power
    print(f"{attacker.name} has attacked {opponent.name} with an increased attack power of {damage} using {item_used.name}")
    opponent.health -= damage
    print()
    time.sleep(3)
    print(f"the resulting health of {opponent.name} is {opponent.health}")
    time.sleep(2)
    print()
    item_used.use -= 1
    if item_used.use == 0:
      print(f"now that you used the item once, you may no longer use this item anymore" )
      your_attacks.remove(item_used)
    else:
      print(f"the remaining number of uses left for {item_used.name} is {item_used.use}")
  elif item_used.itemtype == 'defense':
    print(f"since the item you chose to use is an defense, {attacker} will now restore their health unconditionally with a level of {item_used.power}"  )
    print()
    time.sleep(2)
    attacker.health += item_used.power
    print(f"the resulting health of {attacker.name} is {attacker.health}")
    print()
    time.sleep(2)
    item_used.use -= 1
    if item_used.use == 0:
      print(f"now that you used the item once, you may no longer use this item anymore" )
      your_defenses.remove(item_used)
    else:
      print(f"the remaining number of uses left for {item_used.name} is {item_used.use}")

def use_item_or_not( attacker, opponent ):
    ### this function allows the player to choose whether or not to use a special item and which one they would like to use ###
  use_item_question = input(f"now... would you like to use a special item in your inventory? keep in mind that your special items have limited uses   ")
  print()
  if use_item_question == 'yes':
    time.sleep(2)
    print(f"okay.")
    display_items()
    time.sleep(2)
    which_item_use = input(f"which item in available in your inventory would you like to use? ")
    time.sleep(2)
    all_items_to_use = [ your_attacks[0].name, your_attacks[1].name, your_defenses[0].name, your_defenses[1].name ]
    while which_item_use not in all_items_to_use :
      which_item_use = input(f"please pick a valid item ")
    if which_item_use == your_attacks[0].name:
      print(f"using {your_attacks[0]}...")
      time.sleep(1)
      print()
      use_item( attacker, opponent, your_attacks[0] )
    elif which_item_use == your_attacks[1].name:
      print(f"using {your_attacks[1]}...")
      time.sleep(1)
      print()
      use_item( attacker, opponent, your_attacks[1] )
    elif which_item_use == your_defenses[0].name:
      print(f"using {your_defenses[0]}...")
      time.sleep(1)
      print()
      use_item( attacker, opponent, your_defenses[0] )
    elif which_item_use == your_defenses[1].name:
      print(f"using {your_defenses[0]}...")
      time.sleep(1)
      print()
      use_item( attacker, opponent, your_defenses[1] )
  else:
    print()
    time.sleep(1)
    print(f"okay, the battle will continue then.")

def battle( ally, enemy ):
    ### this function is the structure of an entire battle - which there are 5 of. it regulates the turns etc. ###
    global num_won
    global game_num
    global num_lost

    print(f"welcome to battle {game_num + 1}!")
    print()
    time.sleep(2)
    print(f"{ally}, who is on your team, will be fighting {enemy}!")
    print()
    for x in range (0,5):
      b = "Loading" + "." * x
      print (b, end="\r")
      time.sleep(1)
    print()
    ally.stats()
    time.sleep(2)
    enemy.stats()
    print()
    time.sleep(1)
    print(f"--------------------------------------")
    print(f"you will be going first.")
    time.sleep(2)
    while ally.health > 0 and enemy.health > 0:
      print(f"it is your turn")
      ally_attack( ally, enemy )
      print(f"--------------------------------------"
      )
      print(f"it is now {enemy.name}'s turn")
      time.sleep(2)
      enemy_attack( enemy, ally )
      print(f"--------------------------------------"
      )
    if ally.health <= 0:
      num_lost += 1
      print(f"sorry, you lost. you've lost {num_lost} game(s) so far")
    if enemy.health <= 0:
      num_won += 1
      print(f"congrats! you won battle {game_num + 1}! you have won {num_won} battles so far")
    game_num += 1

    time.sleep(1)
    print()
    for x in range (0,5):
      b = "Loading next game" + "." * x
      print (b, end="\r")
      time.sleep(1)
    print()
    print()
    print()
    print()

def exit_game():
    ### this function is used when the player has won 3 games or the computer has won 3 games, because the final winnter has been determined at this point ###
    if num_won == 3:
        print()
        print(f"congradulations! you won!")
    else:
        print(f"unfortunately, you lost. better luck next time...")
    print()
    time.sleep(1)
    print(f"thank you very much for playing")
    time.sleep(1)
    print(f"i hope you enjoyed your time. bye!")

while True:
  battle( allies[game_num], enemies[game_num])
  if num_won == 3 or num_lost == 2 :
    exit_game()
    exit()