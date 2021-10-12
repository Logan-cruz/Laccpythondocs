#Lump
#Random Dice Generator
#For Dungeons & Dragons and other nerd stuff

#it loads a package that allows you to run random()
import random

#you only need the program running in order for it to work,He needs it so the rest of the code can fuction right.:
programRunning = True
results= 0
dicesides = 6
#It will force a loop to begin.:
while programRunning ==True:
    diceamount = input("How many dice are you rolling? ")
    if diceamount=="0":
        break
    dicesides= input("How many sides does your dice have? ")
    #If they type '0' for diceAmount, the loop should quit immediately,
    modifier = input("What should I add to the total result? ")
    loops = int(diceamount)
    #this makes it so you can keep rolling the dice.
    while int(loops) > 0:
        loops -= 1
        results += random.randint(1, int(dicesides))
        results += int(modifier)
        print(results)
        results=0
        
