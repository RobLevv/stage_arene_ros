#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import rospy
import numpy as np
import time
from random import randint
from gazebo_msgs.msg import LinkStates, LinkState
from std_msgs.msg import String

class Barrier:
    def __init__(self, id):
        self.id = id
        self.link_name = "barrier" + str(id) + "::barrier"
        self.traffic_light = TrafficLight(id)
        self.state = True # True = open, False = closed

    def change_state(self):
        current_state = rospy.wait_for_message('/gazebo/link_states', LinkStates)
        ind = current_state.name.index(self.link_name)
        msg = LinkState()
        msg.link_name = self.link_name
        msg.pose = current_state.pose[ind]
        msg.twist.angular.x = 6 * (-1)**self.state
        msg.twist.angular.y = 6 * (-1)**(self.state+1)
        self.state = not self.state
        self.traffic_light.change_state()
        pubState.publish(msg) 

class TrafficLight:
    def __init__(self, id):
        self.id = id
        self.link_name_g = "traffic_light" + str(id) + "::light_green"
        self.link_name_r = "traffic_light" + str(id) + "::light_red"
        self.links_name = [self.link_name_r, self.link_name_g]
        self.state = True # True = green, False = red

    def change_state(self):
        current_state = rospy.wait_for_message('/gazebo/link_states', LinkStates)
        for i in range(2):
            ind = current_state.name.index(self.links_name[i])
            msg = LinkState()
            
            msg.link_name = self.links_name[i]      # Set link name
            msg.pose = current_state.pose[ind]  # Set the same pose as the current state
            msg.pose.position.z = current_state.pose[ind].position.z + (0.002 * (-1)**(i + self.state))
            pubState.publish(msg)
            time.sleep(0.1)
        self.state = not self.state

def callback(msg):
    print("callbacking")
    tmp = msg.data.split(",")
    object_name = tmp[0]
    object_number = int(tmp[1])
    command = tmp[2]
    if object_name == "barrier":
        current_object = Objects[object_number-1]
        if command == current_object.state:
            print("Barrier already" + command)
        elif command != current_object.state:
            current_object.change_state()
        else:
            print("Error: command not recognized")

if __name__ == '__main__':
    try:
        # Node name
        rospy.init_node('objects_animation', anonymous=False)

        # Create objects
        Objects = [Barrier(1),Barrier(2)]

        # Create publisher
        pubState = rospy.Publisher('/gazebo/set_link_state', LinkState, queue_size=1) 
        pubCMDarene = rospy.Publisher('/arene/cmd', String , queue_size=1)
        subCMDarene = rospy.Subscriber('/arene/cmd', String, callback)
        print("World control node initialized")

    except rospy.ROSInterruptException:
        pass
    rospy.spin()