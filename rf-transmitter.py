import pi_switch
import time
sender = pi_switch.RCSwitchSender()
sender.enableTransmit(2) # use WiringPi pin 0
while True:
	sender.sendDecimal(20, 24) # switch on
	time.sleep(1)
	sender.sendDecimal(21, 24) # switch off
	time.sleep(1)

