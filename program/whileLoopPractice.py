#Logan Cruz
#While Loop Practice
import random
magicNumber = random.randint(1,10)
guesses=5
#Loop for as long as they have guesses remaining mortal.
while guesses > 0:
    print("you have " + str(guesses) +" left")
    #Get the users guess and convert it to a integer
    userGuess = input("Guess my number: ")
    userGuess = int(userGuess)
    #See if the user's guess was higher, lower, or equal to magic number
    if userGuess > magicNumber:
        print("You guessed, too high. Mortal.")
    elif userGuess < magicNumber:
        print("You guessed, too low monkey.")
    else:
        print("How could you know?!! You have the power of the gods, i will strip it away from you.")
        #break out of loop, if they are correct
        break
    #remove one guess
    guesses-=1
