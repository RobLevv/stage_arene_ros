#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from gazebo_msgs.srv import ApplyJointEffort, ApplyJointEffortRequest
from random import randint

def control_barrier(joint, effort, duration):
    rospy.wait_for_service('/gazebo/apply_joint_effort')
    barrier_request.joint_name = joint
    barrier_request.effort = effort
    barrier_request.start_time.secs = 0
    barrier_request.duration.secs = duration
    barrier_handle(barrier_request)


if __name__ == '__main__':
    rospy.init_node('barrier', anonymous=True) # anonymous=True allows multiple nodes with the same name to be launched
    rate = rospy.Rate(0.2) # 0.2hz
    barrier_request = ApplyJointEffortRequest()
    barrier_handle = rospy.ServiceProxy('/gazebo/apply_joint_effort',ApplyJointEffort)
    val = -1
    while not rospy.is_shutdown():
        if val == -1:
            val = 1
        else:
            val = -1
        try:
            control_barrier('gear_to_barriere_1', val, 1)
            control_barrier('gear_to_barriere_2', -val, 1)
        
        except rospy.ROSInterruptException:
            pass
        rate.sleep()
    rospy.spin()
    
