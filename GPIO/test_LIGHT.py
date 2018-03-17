import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.IN)

while True:
	value = GPIO.input(40)
	print(value)
	time.sleep(1)
