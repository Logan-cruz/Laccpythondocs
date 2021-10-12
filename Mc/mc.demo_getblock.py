#Logan cruz
#get knowledge of block
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
pos=mc.player.getTilePos()

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(6) == GPIO.LOW:
        blockData= mc.getBlock(pos.x,pos.y-1,pos.z)
        if blockData==57:
            mc.player.setPos(pos.x,pos.y+20,pos.z)
        
