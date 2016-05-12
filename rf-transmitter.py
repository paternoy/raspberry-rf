import pi_switch
import time


def printCode(code):
	print("{0:b}".format(code).zfill(24)+":{}".format(code))

sender = pi_switch.RCSwitchSender()
sender.enableTransmit(2) # use WiringPi pin 0
code=20
bit=0
printCode(code)
sender.sendDecimal(code, 24) # switch on
time.sleep(1)
while bit<24:
	code2=code|2**bit
	if code2==code:
		code2=code&~2**bit
	printCode(code2)
	sender.sendDecimal(code2, 24) # switch on
	time.sleep(0.5)
	bit=bit+1

