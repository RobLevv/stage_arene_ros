#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import time

from std_msgs.msg import String

TIMESLEEP = 5

if __name__ == "__main__":

    # Initialize the publisher 
    pubCMDarene = rospy.Publisher('/arene/cmd',String,queue_size=1)

    # Initialize the node
    rospy.init_node("etudiant_test", anonymous=True)

    # Main loop
    while not rospy.is_shutdown():
        # This is an example of how to publish a message
        try:
            # Message : "[object],[id],[action]"
            pubCMDarene.publish("barrier,1,close") # Publish to close the barrier 1
            time.sleep(TIMESLEEP)
            pubCMDarene.publish("barrier,1,open") # Publish to open the barrier 1
            time.sleep(TIMESLEEP)
            pubCMDarene.publish("barrier,2,close") # Publish to close the barrier 2
            time.sleep(TIMESLEEP)
            pubCMDarene.publish("barrier,2,open") # Publish to open the barrier 2
            time.sleep(TIMESLEEP)

            # wrong syntax command that generates an error
            pubCMDarene.publish("barrier,3,close")
            time.sleep(0.1)
            pubCMDarene.publish("bar,3,close")
            time.sleep(0.1)
            pubCMDarene.publish("barrier,2,close it")
            time.sleep(0.1)

        except rospy.ROSInterruptException:
            pass
    rospy.spin()