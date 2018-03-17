import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)

p = GPIO.PWM(12,50)
p.start(0)

while(1):
	for dc in range(0,125,5):
		p.ChangeDutyCycle(dc / 10)
		time.sleep(0.1)
	for dc in range(125, 0, -5):
		p.ChangeDutyCycle(dc / 10)
		time.sleep(0.1)

p.stop()
GPIO.cleanup()
