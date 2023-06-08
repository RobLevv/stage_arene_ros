#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import click
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    # Initialize the node, the pubCMDlisher and the message
    rospy.init_node("robot_teleop",anonymous=True)
    msg = Twist()
    pubCMD = rospy.Publisher("/cmd_vel",Twist,queue_size=10)

    try:    

        # Get character from console
        key = click.getchar()

        # Initialize the message
        msg.linear.x = 0
        msg.angular.z = 0

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

        # Publish the message
        pubCMD.publish(msg)


    except rospy.ROSInterruptException:
        pass