import random

magicNumber = random.randint(1,20)
guessesMade = 0
numberGuessed = False
#this will loop while true
while numberGuessed == False:
    guessesMade = guessesMade + 1
    guess = input("Guess what number i'm thinking of: ")
    guess = int(guess)
    if guess > magicNumber:
        print("Your number is too high!")
    elif guess < magicNumber:
        print("Your number is too low.")
    else:
        break
        print(guessesMade)
    
