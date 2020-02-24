import RPi.GPIO as GPIO
import time

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

#Setup default controll 

# Connect 3.3V, and RDX(15)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.OUT)

while True: 
   if GPIO.input(15) == GPIO.HIGH:            
            GPIO.output(21, True)
   else:
       GPIO.output(21, False)