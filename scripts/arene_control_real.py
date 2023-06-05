#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import time

from std_msgs.msg import String

if __name__ == "__main__":
    pubCMDarene = rospy.Publisher('/arene/cmd',String,queue_size=1)
    rospy.init_node("etudiant_test", anonymous=True)
    rospy.spin()
    while not rospy.is_shutdown():
        try:
            print("try start")
            pubCMDarene.publish("barrier,1,open")
            print("try end")
            time.sleep(2)
        except rospy.ROSInterruptException:
            pass