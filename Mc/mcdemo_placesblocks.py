#logan cruz
#Build out a house with a button press
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
def buildHouse():
    tilePos=mc.player.getTilePos()
    mc.setBlocks(tilePos.x+6,tilePos.y+5,tilePos.z+15,tilePos.x+10,tilePos.y+2,tilePos.z+3,1)
    mc.setBlocks(tilePos.x+6,tilePos.y+5,tilePos.z+15,tilePos.x+10,tilePos.y+2,tilePos.z+2,1)
    mc.setBlocks(tilePos.x+7,tilePos.y+4,tilePos.z+14,tilePos.x+9,tilePos.y+3,tilePos.z+3,0)
    mc.setBlocks(tilePos.x+9,tilePos.y+3,tilePos.z+15,tilePos.x+9,tilePos.y+4,tilePos.z+15,0)
    mc.setBlocks(tilePos.x+7, tilePos.)






GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
   
    if GPIO.input(6) == GPIO.LOW:
        buildHouse()
        
     