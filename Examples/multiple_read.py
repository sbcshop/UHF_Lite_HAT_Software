import time
import sys
sys.path.insert(0,'/home/pi/Desktop/UHF_LITE_HAT/Library')# Make sure use your library path here
from uhf import UHF
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(7,GPIO.OUT)

GPIO.output(7,GPIO.LOW)# (LOW)Enable the module, and (HIGH) disable the module

baudrate ='115200' # default baudrate
port     ='/dev/ttyS0'

uhf = UHF(port,baudrate)
uhf.multiple_read()
try:
    while 1:
        rev = uhf.read_mul()
        if rev is not None:
            print(rev)
            print('RSSI(dBm) = ',int(rev[5],base=16))
            print('CRC = ',rev[20],rev[21])
        time.sleep(0.0009)
except KeyboardInterrupt:
    uhf.stop_read()
    time.sleep(1)
    print("stop")
   









