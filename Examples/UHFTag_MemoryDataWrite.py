'''
- This code demostrate how to write data into Memory of UHF Tags,
- Only EPC and USER memory are writeable
- EPC memory allow to change default EPC value of Tag
- USER memory to store required data 
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
'''
Memory Bank 
1 - EPC  --> Read/Write
3 - USER --> Read/Write
'''

Memory_bank = '3'	# Make sure to select correct bank for Read/Write operation

#Select the Tag for write operation
response = uhf.Set_select_pera('80464500e280101010121100') # change with the EPC of the tag, which you want to write
print(response)

'''Make sure to maintain correct data length cannot exceed 32 words (64 bytes) for write operation, as shown below
e.g.
91418800000000000000000000000000  => Any Data, 32 word length 
10c9340080464500e280101010121100  => with EPC value, again 32 word length

- Build write data for USER : simply contains byte value of your choice

- Build EPC write data : this include,
Checksum (of Previous EPC) + PC(of Previous EPC) + EPC (change with NEW) =>
10c9 + 3400 + 80464500e280101010121100

To get checksum and PC of Tag run below script first,
https://github.com/sbcshop/UHF_Lite_HAT_Software/blob/main/Examples/multiple_read.py
'''

#Change Data which you want to Write, in case of EPC write build correct data format as shown above
response = uhf.Write_tag_data('91418800000000000000000000000000',Memory_bank) # maximum length is 32 words 
print(response)

