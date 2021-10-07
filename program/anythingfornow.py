#Logan cruz
#4 buttons one led
#Setup for buttons and LED
#Use a module for requesting data online
import requests
from mcpi.minecraft import Minecraft
#Use a module to control time
import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

#Setup each pin number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#Start infinite loop
mc=Minecraft.create()
while True:
#wait for one second
    time.sleep(1)
#check first button
    if GPIO.input(6) == GPIO.LOW:
        print("button 6 was pressed.")
        mc.player.getPos()
        mc.postToChat(mc.player.getPos())
    elif GPIO.input(13) == GPIO.LOW:
        print("button 13 was pressed")
        mc.player.getTilePos() 
        mc.player.setTilePos(3.9,100,-2.9)
    elif GPIO.input(19) == GPIO.LOW:
        print("button 19 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=up")
    elif GPIO.input(26) == GPIO.LOW:
        print("button 26 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=down") 