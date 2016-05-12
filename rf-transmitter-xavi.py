import pi_switch
import time
sender = pi_switch.RCSwitchSender()
sender.enableTransmit(2) # use WiringPi pin 0
codes=[20,16404,4116]
bit=3

for i in range(0,3):
	code=codes[i]
	codeOn=code|2**bit
	codeOff=code&~2**bit
	print("Plug {}".format(i))
	print("on")
	print("{0:b}".format(codeOn).zfill(24)+":{}".format(codeOn))
	sender.sendDecimal(codeOn, 24) # switch on
	time.sleep(1)
	print("off")
	print("{0:b}".format(codeOff).zfill(24)+":{}".format(codeOff))
	sender.sendDecimal(codeOff, 24) # switch on
	time.sleep(1)
