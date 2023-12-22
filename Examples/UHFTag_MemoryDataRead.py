'''
Code to perform read operation from Memory of UHF Tags,
Reserved, EPC, TID and User are different memory options available

'''
#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import serial
import sys
sys.path.append("..")
from Library import uhf 

from uhf import UHF
from os import path
import time as sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(7,GPIO.OUT)

GPIO.output(7,GPIO.LOW) # LOW to enable the UHF, HIGH to disable UHF


baudrate ='115200' # default baudrate
port     ='/dev/ttyS0'


uhf = uhf.UHF(port,baudrate)

'''
Memory Bank 
1 - EPC  --> Read/Write
2 - TID  --> Only readable
3 - USER --> Read/Write
'''

Memory_bank = '3' # Change to read corresponding Memory 

#Select the tag EPC id for read data
response = uhf.Set_select_pera('80464500e280101010121100') # provide the EPC of the tag, which you want to read
print(response)

#Tag data read
response = uhf.Read_tag_data(Memory_bank)
print(response)

