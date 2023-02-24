#!/usr/bin/env python3
#This file show general info of module
import time
import sys
sys.path.append("..")
from Library import uhf 

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(7,GPIO.OUT)

GPIO.output(7,GPIO.LOW)# Enable the module

baudrate ='115200' # default baudrate
port     ='/dev/ttyS0'

uhf = uhf.UHF(port,baudrate)
uhf.hardware_version()

   









