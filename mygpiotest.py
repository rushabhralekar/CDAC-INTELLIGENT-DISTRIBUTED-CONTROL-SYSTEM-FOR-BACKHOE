import Adafruit_BBIO.GPIO as GPIO
outPin="P9_12"
GPIO.setup(outPin,GPIO.OUT) 
from time import sleep
for i in range(0,5):
    GPIO.output(outPin,GPIO.HIGH)
    sleep(3)
    GPIO.output(outPin,GPIO.LOW)
    sleep(3)
GPIO.cleanup()

