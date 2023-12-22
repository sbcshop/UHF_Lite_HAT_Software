#!/usr/bin/env python3
#This file show single read function
import time
import sys
sys.path.append("..")
from Library import uhf 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(7,GPIO.OUT)

GPIO.output(7,GPIO.LOW)# Enable the module

baudrate ='115200'
port     ='/dev/ttyS0'

uhf = uhf.UHF(port,baudrate)

'''
Uncomment corresponding section to increase reading range,
you will have to set the region as per requirment
'''
#uhf.setRegion_EU() 
#uhf.setRegion_US()

rev = uhf.single_read()
if rev is not None:
   print('EPC = ',rev[8:20])
   print('RSSI(dBm) = ',int(rev[5],base=16))
   print('CRC = ',rev[20],rev[21])

time.sleep(1)
uhf.stop_read()

   









