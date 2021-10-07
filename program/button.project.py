import RPi.GPIO as GPIO #Impport rasberry Pi GPIO libary
GPIO.setwarnings(False) #Ignore warning for now
GPIO.setmode(GPIO.BOARD)#Use physical pin numbering
GPIO.setup(10,GPIO.IN, pull_up_down = GPIO.PUD_UP)
#Set up pin 10 to be an input pin and set inital value to be pulled low(off)
LEDlit =False
while True:
    if GPIO.input(06) == GPIO.HIGH:
        print("First button was pressed!")
        if LEDlit is True:
            LEDlit=False
            GPIO.input = GPIO.LOW
        else:
            LEDlit = True
            GPIO.input(06)= GPIO.HIGH
    if GPIO.input(13) == GPIO.HIGH:
        print("Second button was pushed!")
    if GPIO.input(19) == GPIO.HIGH:
        print("third button was pushed!")
    if GPIO.input(25) == GPIo.HIGH:
        print("Fourth button was pushed!")
            