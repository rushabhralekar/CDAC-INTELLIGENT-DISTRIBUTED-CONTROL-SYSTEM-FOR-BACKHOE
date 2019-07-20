import Adafruit_BBIO.GPIO as GPIO
import time
outPin = "P9_12"

GPIO.setup(outPin, GPIO.OUT)

from time import sleep
for i in range (0,50):
    GPIO.output(outPin, GPIO.HIGH)
    sleep(3)
    print i

   # GPIO.output(outPin, GPIO.LOW)
 #   print i
  #  sleep(3)

GPIO.cleanup()


