#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import time

from std_msgs.msg import String

TIMESLEEP = 5

if __name__ == "__main__":
    pubCMDarene = rospy.Publisher('/arene/cmd',String,queue_size=1)
    rospy.init_node("etudiant_test", anonymous=True)

    while not rospy.is_shutdown():
        try:
            # print("try start")
            # pubCMDarene.publish("traffic_light,1,green")
            # time.sleep(5)
            # pubCMDarene.publish("traffic_light,1,yellow")
            # time.sleep(0.5)
            # pubCMDarene.publish("barrier,1,close")
            # time.sleep(5)
            # pubCMDarene.publish("traffic_light,1,red")
            # time.sleep(5)
            # pubCMDarene.publish("barrier,1,open")
            # time.sleep(5)
            # print("try end")
            pubCMDarene.publish("barrier,1,close")
            time.sleep(TIMESLEEP)
            pubCMDarene.publish("barrier,1,open")
            time.sleep(TIMESLEEP)
            pubCMDarene.publish("barrier,2,close")
            time.sleep(TIMESLEEP)
            pubCMDarene.publish("barrier,2,open")
            time.sleep(TIMESLEEP)

        except rospy.ROSInterruptException:
            pass
    rospy.spin()