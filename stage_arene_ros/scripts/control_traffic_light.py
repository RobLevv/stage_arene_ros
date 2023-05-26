#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from gazebo_msgs.srv import ApplyJointEffort, ApplyJointEffortRequest
from random import randint

def control_traffic_light(color, effort, duration):
    rospy.wait_for_service('/gazebo/apply_joint_effort')
    TL_request.joint_name = "base_to_light_{}".format(color)
    TL_request.effort = effort
    TL_request.start_time.secs = 0
    TL_request.duration.secs = duration
    TL_handle(TL_request)

def to_red():
    control_traffic_light('red', 1, 1)
    control_traffic_light('green', -1, 1)
    
def to_green():
    control_traffic_light('red', -1, 1)
    control_traffic_light('green', 1, 1)
    
def orange_blink(n):
    for i in range(n):
        rospy.sleep(1)
        control_traffic_light('orange', 1, 1)
        rospy.sleep(1)
        control_traffic_light('orange', -1, 1)
        
    


if __name__ == '__main__':
    rospy.init_node('barrier', anonymous=True) # anonymous=True allows multiple nodes with the same name to be launched
    rate = rospy.Rate(0.2) # 0.2hz
    TL_request = ApplyJointEffortRequest()
    TL_handle = rospy.ServiceProxy('/gazebo/apply_joint_effort',ApplyJointEffort)
    cmpt = 0
    while not rospy.is_shutdown():
        cmpt+=1
        try:
            to_green()
            rospy.sleep(5)
            orange_blink(3)
            to_red()
            rospy.sleep(5)
            orange_blink(1)
            to_green()
            
        except rospy.ROSInterruptException:
            pass
    rospy.spin()
    
