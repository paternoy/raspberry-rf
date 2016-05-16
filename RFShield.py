import RPi.GPIO as GPIO
import pi_switch
import time
import logging

class RFShield(object):
	
	def __init__(self):
		self.transmitter = pi_switch.RCSwitchSender()
		self.transmitter.enableTransmit(0)
		self.butPin=22
		self.redPin=24
		self.bluePin=23
		self.greenPin=25
		self.active=False
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.butPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(self.redPin,GPIO.OUT)
		GPIO.setup(self.bluePin,GPIO.OUT)
		GPIO.setup(self.greenPin,GPIO.OUT)
		GPIO.add_event_detect(self.butPin, GPIO.RISING, callback=self.buttonCallback, bouncetime=1000)
		GPIO.output(self.redPin,False)
		GPIO.output(self.greenPin,False)
		GPIO.output(self.bluePin,False)

	def transmitCode(self,code):
		self.transmitter.sendDecimal(code, 24)

	def buttonCallback(self,channel):
		print("Button Pressed")
		self.toggle()

	def refresh(self):
		GPIO.output(self.redPin,not self.active)
		GPIO.output(self.greenPin,self.active)
	
	def toggle(self):
		self.active= not self.active
		self.refresh()
	def cleanup(self):
		GPIO.cleanup()

