#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import rospy
import numpy as np
import time
from random import randint
from gazebo_msgs.msg import LinkStates, LinkState
from std_msgs.msg import String

class Barrier:
    """Class to control the barrier"""
    def __init__(self, id):

        self.id = id
        self.link_name = "barrier" + str(id) + "::barrier"
        self.traffic_light = TrafficLight(id)
        self.state = True # True = open, False = closed

    def change_state(self):
        """Change the state of the barrier (open or closed)"""

        # Get the current state of the barrier
        current_state = rospy.wait_for_message('/gazebo/link_states', LinkStates)

        # Get the index of the barrier in the list of links
        ind = current_state.name.index(self.link_name)

        # Create the message
        msg = LinkState()
        msg.link_name = self.link_name
        msg.pose = current_state.pose[ind]

        # Change the position of the barrier
        msg.twist.angular.x = 6 * (-1)**self.state
        msg.twist.angular.y = 6 * (-1)**(self.state+1)

        # Update the state of the barrier
        self.state = not self.state

        # Update the state of the traffic light
        self.traffic_light.change_state()

        # Publish the message
        pubState.publish(msg) 

class TrafficLight:
    """Class to control the traffic light"""

    def __init__(self, id):
        
        self.id = id
        self.link_name_g = "traffic_light" + str(id) + "::light_green"
        self.link_name_r = "traffic_light" + str(id) + "::light_red"
        self.links_name = [self.link_name_r, self.link_name_g]
        self.state = True # True = green, False = red

    def change_state(self):
        """Change the state of the traffic light (green or red)"""

        # Get the current state of the traffic light
        current_state = rospy.wait_for_message('/gazebo/link_states', LinkStates)

        # We change the state of both lights
        for i in range(2):
            # Get the index of the light in the list of links
            ind = current_state.name.index(self.links_name[i])

            # Create the message
            msg = LinkState()
            msg.link_name = self.links_name[i]  # Set link name
            msg.pose = current_state.pose[ind]  # Set the same pose as the current state
            
            # Change the position of the light
            msg.pose.position.z = current_state.pose[ind].position.z + (0.002 * (-1)**(i + self.state)) # If the light is up, we put it down and vice versa depending on the state (+0.002 or -0.002)

            # Publish the message
            pubState.publish(msg)
            time.sleep(0.1) # Wait a little bit to avoid errors and let the message be published

        self.state = not self.state

def callback(msg):

    # Message : "[object],[id],[action]" 
    msg_received = msg.data.split(",")
    object_name = msg_received[0]
    object_number = int(msg_received[1])
    command = msg_received[2]

    # Check if the object exists
    if object_name == "barrier":

        # Check if the object number exists
        try:

            # Command the object to change state
            current_object = Objects[object_number-1]
            if command == current_object.state:
                rospy.loginfo("Barrier already " + command)
            elif command != current_object.state and command in ["open", "close"]:
                current_object.change_state()
            else:
                rospy.logerr("Error: command not recognized : ' " + command + " '")

        except IndexError:
            rospy.logerr("Error: object number not recognized : ' " + str(object_number) + " '")

    else:
        rospy.logerr("Error: object not recognized : ' " + object_name + " '")

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
        rospy.loginfo("World control node initialized")

    except rospy.ROSInterruptException:
        pass
    rospy.spin()