import RPi.GPIO as GPIO
import time

bluePin=23
redPin=24
greenPin=25
butPin=22

def buttonCallback(channel):
		print("Button Pressed")
		global active
		active=not active

GPIO.setmode(GPIO.BCM)
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.output(redPin,False)
GPIO.output(greenPin,False)
GPIO.output(bluePin,False)
GPIO.add_event_detect(butPin, GPIO.RISING, callback=buttonCallback, bouncetime=300)
active=False
i=0
while True:
	if active:
		GPIO.output(redPin,True)
		GPIO.output(bluePin,i%6==1)
		GPIO.output(greenPin,i%3==2)
	else:
		GPIO.output(redPin,False)
		GPIO.output(bluePin,False)
		GPIO.output(greenPin,False)
	
	time.sleep(0.1)
	i=i+1

