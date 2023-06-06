#!/usr/bin/env python3
import serial
import random
import time
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        led_number = random.randint(1,4)
        print("Sending number " + str(led_number) + " to Arduino.")
        ser.write(str(led_number).encode('utf-8'))
        time.sleep(2)