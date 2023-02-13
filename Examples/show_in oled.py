#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import serial
import sys
sys.path.insert(0,'/home/pi/Desktop/UHF_LITE_HAT/Library')# Make sure use your library path here
from oled_091 import SSD1306
from uhf import UHF
from os import path
import time as sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(7,GPIO.OUT)

GPIO.output(7,GPIO.LOW)
DIR_PATH = path.abspath(path.dirname(__file__))
FontSize = path.join(DIR_PATH, "Fonts/GothamLight.ttf")

baudrate ='115200' # default baudrate
port     ='/dev/ttyS0'

uhf = UHF(port,baudrate)

display = SSD1306()

display.DrawRect()
display.ShowImage()
time.sleep(1)
try:
    h = uhf.hardware_version()
    print(h)
    display.PrintText(str(h), cords=(5, 10), Font=FontSize)
    display.DrawRect()
    display.ShowImage()
                
        
except KeyboardInterrupt:
    GPIO.cleanup()
