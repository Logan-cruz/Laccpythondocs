#Logan cruz
# Conditional statements (if(elif/else)
# 8/31/2021
# "listen well sayia-...Goku. Even though you are a mortal, you have
#the power of the gods."
#Have three animals and aknoledge it/ if any other pet, say it. if no pet, no pet.

#A statement is one line of code.
myPet=input("What is your pet?")
petColor=input("What color is it?")

#A conditional statemnt is a block of code that only runs if they condition is true
if myPet == "bird":
    print("You have " +petColor+ " Bird." )
elif myPet== "frog":
    print("You have " +petColor+ " frog")
elif myPet =="dog":
    print("you have a "+ petColor + " dog.")
elif myPet:
    print("You have " + petColor + myPet)
else:
    print("You don't have a pet")

#EOF 
