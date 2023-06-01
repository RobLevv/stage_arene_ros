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
            msg.linear.x = 0
            msg.angular.z = 0
            # Get character from console
            mykey = click.getchar()
            if mykey in keys.keys():
                char=keys[mykey]

            if char == 'up':    # UP key
                msg.linear.x = 0.2
                
            if char == 'down':  # DOWN key
                msg.linear.x = -0.2
                
            if char == 'left':  # LEFT
                msg.angular.z = 1
                
            if char == 'right': # RIGHT
                msg.angular.z = -1
            pub.publish(msg)
            if char == "quit":  # QUIT
                msg.linear.x = 0
            
            
        except rospy.ROSInterruptException:
            pass