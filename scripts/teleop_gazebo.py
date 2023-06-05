#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import sys, termios, tty
import click
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
from arene_control import Barrier, TrafficLight

# Arrow keys codes
keys = {'\x1b[A':'up', '\x1b[B':'down', '\x1b[C':'right', '\x1b[D':'left','z':'up', 's':'down', 'd':'right', 'q':'left', 'p':'stop', 'w':'quit'}

if __name__ == '__main__':
    while not rospy.is_shutdown():
        B1 = Barrier(1)
        B2 = Barrier(2)
        TL1 = TrafficLight(1)
        TL2 = TrafficLight(2)
        rospy.init_node("robot_teleop",anonymous=True)
        msg = Twist()
        pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10)
        try:    
            # Initialize the message
            msg.linear.x = 0
            msg.angular.z = 0
            # Get character from console
            key = click.getchar()
            # Move the robot with the keyboard
            if key == 'z': # forward
                msg.linear.x = 0.5
            if key == 's': # backward
                msg.linear.x = -0.5
            if key == 'd': # turn right
                msg.angular.z = -0.5
            if key == 'q': # turn left
                msg.angular.z = 0.5
            if key == 'p': # stop
                msg.linear.x = 0
                msg.angular.z = 0
            pub.publish(msg)

            # Move the arena objects with the keyboard
            if key == 'y': # open barrier 1
                B1.open()
            if key == 'h': # close barrier 1
                B1.close()
            if key == 'u': # open barrier 2
                B2.open()
            if key == 'j': # close barrier 2
                B2.close()
            if key == 'i': # turn traffic light 1 to green
                TL1.to_green()
            if key == 'o': # turn traffic light 1 to red
                TL1.to_red()
            if key == 'b': # blink 3 times traffic light 1 in yellow
                TL1.yellow_blink(3)
            if key == 'k': # turn traffic light 2 to green
                TL2.to_green()
            if key == 'l': # turn traffic light 2 to red
                TL2.to_red()
            if key == 'n': # blink 3 times traffic light 2 in yellow
                TL2.yellow_blink(3)

        except rospy.ROSInterruptException:
            pass