import serial
import re
try:
    arduino=serial.Serial("COM3",timeout=1)
except:
    print("please check port")
while True:
    a=str(arduino.readline())
    x=re.findall('[0-9]+',a)
    if(len(x)==0):
        print('0')
    else:
        print(x)
