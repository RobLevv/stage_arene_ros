#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import click
from std_msgs.msg import Float64

class Barrier:
    def __init__(self, id):
        self.id = id
        self.pub = rospy.Publisher('/barrier_' + str(id) + '/gear_to_barrier_' + str(id) + '_position_controller/command', Float64, queue_size=10)
    
    def open(self):
        self.pub.publish(0.2)
    
    def close(self):
        self.pub.publish(-0.2)

class TrafficLight:
    def __init__(self, id):
        self.id = id
        self.pub_green = rospy.Publisher('/traffic_lights_' + str(id) + '/base_to_light_1_position_controller_' + str(id) + '/command', Float64, queue_size=10)
        self.pub_yellow = rospy.Publisher('/traffic_lights_' + str(id) + '/base_to_light_2_position_controller_' + str(id) + '/command', Float64, queue_size=10)
        self.pub_red = rospy.Publisher('/traffic_lights_' + str(id) + '/base_to_light_3_position_controller_' + str(id) + '/command', Float64, queue_size=10)

    def to_green(self):
        self.pub_green.publish(1)
        self.pub_yellow.publish(-1)
        self.pub_red.publish(-1)
    
    def to_red(self):
        self.pub_green.publish(-1)
        self.pub_yellow.publish(-1)
        self.pub_red.publish(1)

    def yellow_blink(self,n):
        for i in range(n):
            self.pub_green.publish(-1)
            self.pub_yellow.publish(1)
            self.pub_red.publish(-1)
            rospy.sleep(0.2)
            self.pub_green.publish(-1)
            self.pub_yellow.publish(-1)
            self.pub_red.publish(-1)
            rospy.sleep(0.2)

if __name__=="__main__":
    pass