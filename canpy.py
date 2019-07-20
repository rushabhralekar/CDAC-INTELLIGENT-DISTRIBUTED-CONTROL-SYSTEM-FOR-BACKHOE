#adafruit libraries used for communication with bb pins
import Adafruit_BBIO.ADC as ADC
#importng can libraries
import can
#can.rc class provides can support for python
can.rc['interface'] = 'socketcan_ctypes'
import threading
#provides thread based parallelism and 
#sleep for dealay
from threading import Thread,Lock
from time import sleep
#importing can libraries for interfacing
from can.interfaces.interface import Bus
from can import Message

ADC.setup()
#variable defination
adc_val=0
#setting the adc pin no 33
def Adc_33():
    #selecting the ANI pin of bb 
    #from port 9 pin 33
    analog_33="P9_33"
    global adc_val
    adc_pre=0
    while(1):
        #locking- used to avoid synchronization
        lock.acquire()
        adc_val_digital=ADC.read(analog_33)
        adc_val=(adc_val_digital*100)//1
        #converting the adc values
        adc_val=int(adc_val)
       # if adc_val>(adc_pre+3) or adc_val<(adc_val-3):
          #  can(0x11)
          # providing id to the can
        adc_pre=adc_val
        print"the p9_33 value is ",adc_val
        lock.release()
        sleep(3)
#defining can 
def Can(id):
    global adc_val
    can_interface = 'can0'
    bus = Bus(can_interface)

    print "send message..."
    Message.extended_id = False
    Message.extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 1
    Message.is_error_frame=False
    if id==0x22:
        Message.arbitration_id=id
        Message.dlc=3
        adc_val1=adc_val/ 10
        adc_val2=adc_val %10
        #message data frame 
        Message.data=[0x00,adc_val1,adc_val2]
#exception for error handling 
    try:
        bus.send(Message);
        print"data=",Message.data
        print "id=",id

    except:
        print "OOPS somthing went wrong"
        sleep(3)

#main defination
def main():
    data=0
    while(1):

             
        can_interface = 'can0'
        bus = Bus(can_interface)


        print "send message....."
        sleep(3)
        Message.extended_id =False
        Message.is_remote_frame = False
        Message.id_type = 1
        Message.is_error_frame=False
        Message.arbitration_id = 0x33
        Message.dlc = 1

        Message.data=[data]
        try:

            bus.send(Message);
            print Messgae.data

        except:

            print "invalid operation!!!!!!"
        sleep(0.1)


if __name__=="__main__":

    lock=Lock()
    th1=Thread(target=Adc_33,args=())
    
    th1.start()
    th1.join()

