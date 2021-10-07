#Logan Cruz
#Places a randomly colored wool block
'''
set up program for Mc and two buttons
create a 'counter' variable that starts at 0.
create a list of blockdata numbers for different wool colors
define a function called PlacedNext
    it takes an argument called direction
    it changes the counter by adding the direction argument
    place wool block of the color from the list where the index matches the variable counter
    if the counter is out of bounds of the index, reset it.
in a forever loop:
    if the first button was pressed, placeNext(1)
    if the second button was pressed, placeNext(-1)
    '''
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
counter = 0
woolColors= [2,7,9,10,13,14,15]
def placeNext(direction):
    tilePos=mc.player.getTilePos()
    global counter
    counter= counter+direction
    if  counter < 0:
         counter=6
    elif  counter > 6:
         counter=0
    else:
        pass
    mc.setBlock(tilePos.x+1,tilePos.y,tilePos.z, 35,woolColors[counter])
while True:
    if GPIO.input(6) == GPIO.LOW:
        placeNext(1)
    elif GPIO.input(13) == GPIO.LOW:
        placeNext(-1)
    
    
    
