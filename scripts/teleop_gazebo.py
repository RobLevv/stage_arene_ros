#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import sys, termios, tty
import click
from geometry_msgs.msg import Twist

# Arrow keys codes
keys = {'\x1b[A':'up', '\x1b[B':'down', '\x1b[C':'right', '\x1b[D':'left','z':'up', 's':'down', 'd':'right', 'q':'left', 'p':'stop', 'w':'quit'}

if __name__ == '__main__':
    while not rospy.is_shutdown():
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
                msg.linear.x = 0.2
            if key == 's': # backward
                msg.linear.x = -0.2
            if key == 'd': # turn right
                msg.angular.z = -0.5
            if key == 'q': # turn left
                msg.angular.z = 0.5
            if key == 'p': # stop
                msg.linear.x = 0
                msg.angular.z = 0
            pub.publish(msg)


        except rospy.ROSInterruptException:
            pass