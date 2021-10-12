#Logan Cruz+
#Chicken cooking calculator
def coalNeeded(chickens):
    chickens/8
    return chickens
def chickenNeeded(coal):
    coal*8
    return coal
answer = input("do you want to calculate chickens or coal today mortal? ")
if answer == "Coal" or "coal":
    chickens= input("How many chickens do you have? ")
    chickens= int(chickens)
    print(coalNeeded(chickens))
elif answer == "Chickens" or "chickens":
    coal=input("How many coal do you have? ")
    coal=int(coal)
    print(chickenNeeded(coal))
else:
    print("That was void and null.")
