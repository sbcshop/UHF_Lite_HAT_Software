# library og UHF HAT
import serial
import binascii
import time
import array
####################################################
STARTBYTE     ='BB00'
ENDBYTE       ='7E'
HARD_VERSION  ='0300010004'
MULTIPLE_READ ='27000322271083'
SINGLE_READ   ='22000022'
STOP_READ     ='28000028'
###################################################
class UHF():
    def __init__(self,port,baudrate):
        self.serial = serial.Serial(port='/dev/ttyS0',baudrate = 115200,
                      parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,
                      bytesize=serial.EIGHTBITS,timeout=1)
        self.serial.flush()
        
    def read_mul(self):
        rec_data = self.serial.read(24)
        if rec_data[0] != 0xbb or rec_data[23] != 0x7e or rec_data[1] != 0x02:
            return None        
        return [format(x, '02x') for x in rec_data]
        

    def send_command(self,data):
        Data = ''.join(data)
        bin_data = binascii.unhexlify(Data)
        response = self.serial.write(bin_data)

    def hardware_version(self):
        self.send_command([STARTBYTE,HARD_VERSION,ENDBYTE])
        d = self.serial.read(23)
        s = []
        def split_bytes_data(data, packet_size):
            # Split the bytes object into packets of the specified size
            packets = [data[i:i+packet_size] for i in range(0, len(data), packet_size)]
            return packets
        ds = split_bytes_data(d,6)        
        for i in range(1,len(ds)):
               s.append(str(ds[i],'latin-1'))
        return "".join(s)
    
    def multiple_read(self):
        data = self.send_command([STARTBYTE,MULTIPLE_READ,ENDBYTE])


    def stop_read(self):
        data = self.send_command([STARTBYTE,STOP_READ,ENDBYTE])

    def single_read(self):
        data = self.send_command([STARTBYTE,SINGLE_READ,ENDBYTE])
        rec_data = self.serial.read(24)
        rec_hex = bytes.hex(rec_data)
        rec_data_split = [rec_hex[i:i+2] for i in range(0, len(rec_hex), 2)]

        if len(rec_data_split) == 24 and rec_data_split[-1] == '7e' and rec_data_split[-24] == 'bb':
            if rec_data_split[-23] != '01':
                return rec_data_split
        else:
            return None   

        
        
