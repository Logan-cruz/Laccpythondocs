#Logan Cruz
#Object/Classes Practice
#It creates a class
class Fighter():
#Defines INIT,InIT is a construter. it needs "self" as the argument
    def __init__(self):
        #it gives fighter class the HP property of 20
        self.hp=20
        #it gives the name property of the class fighter "Fighter"
        self.name="Fighter"
    def  punch(self, target):
        #This entire function allows bob and frank to punch and kill each other
        #The print tells the user that the figher punch it's target
        print(self.name + " punches " + target.name)
        target.hp=target.hp-3
        print(target.hp)
bob= Fighter()
#now bob is a fighter
bob.name="bob"
#Bob has change it's name property to "Bob"
#With Frank as a fighter. Now Frank is a fighter Object
frank=Fighter()
#Both Bob and Frank can punch each other due to the function punch.
bob.punch(frank)
frank.punch(bob)

