#!/usr/bin/env python3
import serial
import random
import time
import rospy
from std_msgs.msg import String

def callback(msg):
    print("Command received: " + msg.data + "\n")
    tmp = msg.data.split(",")
    object_name = tmp[0]
    object_number = int(tmp[1])
    command = tmp[2]
    send_to_arduino(object_name, object_number, command)

def send_to_arduino(object_name, object_number, command):
    
    if object_name == "barrier":
        barrier_number = object_number
        if command == "open":
            ser.write(str(barrier_number).encode('utf-8'))
        elif command == "close":
            ser.write(str(barrier_number+2).encode('utf-8'))
        else:
            print("Unknown command.")
    else:
        print("Unknown object.")

if __name__ == '__main__':
    pubCMDarene = rospy.Publisher('/arene/cmd',String,queue_size=1)
    subCMDarene = rospy.Subscriber('/arene/cmd', String, callback)
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    rospy.init_node('arduino_com_node', anonymous=True)
    rospy.spin()

