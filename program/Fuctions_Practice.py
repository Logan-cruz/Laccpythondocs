#Logan Cruz
#Functions Practice

#IDLE will turn fuctions purple
#Fuctions will always have paraenthesis at the end
#You will never see parenthesus without a fuction or equation
print("This is a function")

#You can "call" Functions their name and passing their required arguments
print("I am calling the print fuction. This sentence is a argument.")
#You can define your own fuctions with the def keyword
def printHello():
    print("This print in the printHello() function")
    print("Hello")

#You can define arguments that the function requires
def add(a,b):
    print("This functions add two arguments.")
    print(a + b)
#You can pass 'arguments' to a function when calling
add( 5,7)

#Functions can have return values
def subtract(a,b):
    print("This function subracts two arguments the returns the answer")
    c =a-b
    return c
#This won't print anything
subtract(7,5)
#You must print the return value
print(subtract(7,5))







#EOF
