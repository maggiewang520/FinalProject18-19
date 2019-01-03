import time

##intro

print ( "welcome, bienvenido, benvenuto, bem vinda, 欢迎, ようこそ, to Maggie's final project")
time.sleep(1)
print('you will embark on the ultimate adventure around LA')
time.sleep(2)
print( 'you will be exploring important landmarks - and by that I mean the houses of hot celebrities and youtubers')
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

## final battle setup