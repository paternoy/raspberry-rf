
# -*- coding: utf-8 -*-
"""
@author     Alexander Rüedlinger <a.rueedlinger@gmail.com>
@date       30.07.2015
"""

from pi_switch import RCSwitchReceiver
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,False)
receiver = RCSwitchReceiver()
receiver.enableReceive(1)

num = 0

while True:
    if receiver.available():
        received_value = receiver.getReceivedValue()

        if received_value:
            num += 1
#            print("Received[%s]:" % num)
            print("{0:b}".format(received_value).zfill(24)+":{}".format(received_value))
#            print(received_value)
#            print("%s / %s bit" % (received_value, receiver.getReceivedBitlength()))
#            print("Protocol: %s" % receiver.getReceivedProtocol())
#            print("")

        receiver.resetAvailable()
