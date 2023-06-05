#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import rospy
import numpy as np
from random import randint
from gazebo_msgs.msg import LinkStates, LinkState

class Barrier:
    def __init__(self, id):
        self.id = id
        self.link_name = "barrier::barrier_" + str(id)
    
    def action(self, action):
        if action == 0:
            self.open()
        elif action == 1:
            self.close()
        else:
            raise ValueError("Action must be 0 or 1")
    
    def open(self):
        current_state = rospy.wait_for_message('/gazebo/link_states', LinkStates)
        ind = current_state.name.index(self.link_name)
        msg = LinkState()
        msg.link_name = self.link_name
        msg.pose = current_state.pose[ind]
        msg.twist.angular.x = -1
        msg.twist.angular.y = 1
        pub.publish(msg)

    def close(self):
        current_state = rospy.wait_for_message('/gazebo/link_states', LinkStates)
        ind = current_state.name.index(self.link_name)
        msg = LinkState()
        msg.link_name = self.link_name
        msg.pose = current_state.pose[ind]
        msg.twist.angular.x = 1
        msg.twist.angular.y = -1
        pub.publish(msg)

class TrafficLight:
    def __init__(self, id):
        self.id = id
        self.link_name = "barrier::light_green_" + str(id)
    
    def action(self, action):
        if action == 0:
            self.to_green()
        elif action == 1:
            self.to_red()
        else:
            raise ValueError("Action must be 0 or 1")
    
    def to_green(self):
        current_state = rospy.wait_for_message('/gazebo/link_states', LinkStates)
        ind = current_state.name.index(self.link_name)
        msg = LinkState()
        msg.link_name = self.link_name
        msg.pose = current_state.pose[ind]
        msg.twist.linear.z = 0.1
        pub.publish(msg)
    
    def to_red(self):
        current_state = rospy.wait_for_message('/gazebo/link_states', LinkStates)
        ind = current_state.name.index(self.link_name)
        msg = LinkState()
        msg.link_name = self.link_name
        msg.pose = current_state.pose[ind]
        msg.twist.linear.z = -0.1
        pub.publish(msg)


if __name__ == '__main__':
    try:
        # Node name
        rospy.init_node('objects_animation', anonymous=False)

        # Create objects
        Objects = [Barrier(1), Barrier(2), TrafficLight(1), TrafficLight(2)]

        # Lets define a publisher on the topic_name topic (Twist message)
        # When a connection is latched, a reference to the last message published is saved and sent to any future subscribers that connect. This is useful for slow-changing or static data like a map. 
        pub = rospy.Publisher('/gazebo/set_link_state', LinkState, queue_size=1, latch=True) 
        msg = LinkState()
        
        while not rospy.is_shutdown():
            rospy.loginfo("Objects animation")
            for o in Objects:
                rospy.loginfo("Object "+str(o.link_name) + str(o.id))
                o.action(0)
                rospy.sleep(1)
           

    except rospy.ROSInterruptException:
        pass