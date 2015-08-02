from time import sleep
import pyupm_hmc5883l as hmc5883l
import serial
import mraa
import ctypes

class IMU:
    
    def __init__(self):
        self.hmc = hmc5883l.Hmc5883l(0)
        self.hmc.set_declination(0.2749)
        self.x= mraa.Uart(0)
        self.ser = serial.Serial('/dev/ttyMFD1', 115200)        
    
    def getHeading(self):
        self.hmc.update()
        return self.hmc.heading() 

    def getAcc(self):
        temp = self.ser.readline()
        temp = temp.split(',')
        acc_array = list()
        for i in temp[0:3]:
            acc_array.append((float)(ctypes.c_int16(int(i,16)).value)/-2048)
        return acc_array

    def getGyro(self):
        temp = self.ser.readline()
        temp = temp.replace('\r\n','').split(',')
        gyro_array = list()
        for i in temp[3:6]:
            gyro_array.append((float)(ctypes.c_int16(int(i,16)).value)/-2048)
        return gyro_array

"""test = IMU()
while 1:
    print test.getHeading()
    print test.getAcc()
    print test.getGyro()
"""
