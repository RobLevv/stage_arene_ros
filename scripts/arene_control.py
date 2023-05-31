#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import click
from std_msgs.msg import Float64



class AreneControl:
    def __init__(self):
        self.pub_barrier1 = rospy.Publisher('/barrier_1/gear_to_barrier_1_position_controller/command', Float64, queue_size=10)
        self.pub_barrier2 = rospy.Publisher('/barrier_2/gear_to_barrier_2_position_controller/command', Float64, queue_size=10)
        self.pub_light_green1 = rospy.Publisher('/traffic_lights_1/base_to_light_1_position_controller_1/command', Float64, queue_size=10)
        self.pub_light_yellow1 = rospy.Publisher('/traffic_lights_1/base_to_light_2_position_controller_1/command', Float64, queue_size=10)
        self.pub_light_red1 = rospy.Publisher('/traffic_lights_1/base_to_light_3_position_controller_1/command', Float64, queue_size=10)
        self.pub_light_green2 = rospy.Publisher('/traffic_lights_2/base_to_light_1_position_controller_2/command', Float64, queue_size=10)
        self.pub_light_yellow2 = rospy.Publisher('/traffic_lights_2/base_to_light_2_position_controller_2/command', Float64, queue_size=10)
        self.pub_light_red2 = rospy.Publisher('/traffic_lights_2/base_to_light_3_position_controller_2/command', Float64, queue_size=10)

    def to_green1(self):
        self.pub_light_green1.publish(1)
        self.pub_light_yellow1.publish(-1)
        self.pub_light_red1.publish(-1)

    def to_red1(self):
        self.pub_light_green1.publish(-1)
        self.pub_light_yellow1.publish(-1)
        self.pub_light_red1.publish(1)

    def yellow_blink1(self,n):
        for i in range(n):
            self.pub_light_green1.publish(-1)
            self.pub_light_yellow1.publish(1)
            self.pub_light_red1.publish(-1)
            rospy.sleep(0.5)
            self.pub_light_green1.publish(-1)
            self.pub_light_yellow1.publish(-1)
            self.pub_light_red1.publish(-1)
            rospy.sleep(0.5)

    def to_green2(self):
        self.pub_light_green2.publish(1)
        self.pub_light_yellow2.publish(-1)
        self.pub_light_red2.publish(-1)
    
    def to_red2(self):
        self.pub_light_green2.publish(-1)
        self.pub_light_yellow2.publish(-1)
        self.pub_light_red2.publish(1)

    def yellow_blink2(self,n):
        for i in range(n):
            self.pub_light_green2.publish(-1)
            self.pub_light_yellow2.publish(1)
            self.pub_light_red2.publish(-1)
            rospy.sleep(0.5)
            self.pub_light_green2.publish(-1)
            self.pub_light_yellow2.publish(-1)
            self.pub_light_red2.publish(-1)
            rospy.sleep(0.5)

if __name__=="__main__":
    while not rospy.is_shutdown():
        rospy.init_node("arene_control",anonymous=True)
        AC = AreneControl()
        try:
            char = click.getchar()
            if char == 'a':
                AC.pub_barrier1.publish(0.2)
            if char == 'q':
                AC.pub_barrier1.publish(-0.2)
            if char == 'z':
                AC.pub_barrier2.publish(0.2)
            if char == 's':
                AC.pub_barrier2.publish(-0.2)
            if char == 'e':
                AC.to_green1()
            if char == 'r':
                AC.to_red1()
            if char == 't':
                AC.yellow_blink1(3)
            if char == 'd':
                AC.to_green2()
            if char == 'f':
                AC.to_red2()
            if char == 'g':
                AC.yellow_blink2(3)

        except rospy.ROSInterruptException:
                pass