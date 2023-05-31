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
            # Control of the barriers with the keyboard with lights
            if char == 'a': # open barrier 1
                AC.yellow_blink1(1)
                AC.pub_barrier1.publish(0.2)
                AC.to_green1()
            if char == 'q': # close barrier 1
                AC.yellow_blink1(3)
                AC.pub_barrier1.publish(-0.2)
                AC.to_red1()
            if char == 'z': # open barrier 2
                AC.yellow_blink2(1)
                AC.pub_barrier2.publish(0.2)
                AC.to_green2()
            if char == 's': # close barrier 2
                AC.yellow_blink2(3)
                AC.pub_barrier2.publish(-0.2)
                AC.to_red2()

            # If we want to control the traffic lights manually
            if char == 'e': # green light 1
                AC.to_green1()
            if char == 'r': # red light 1
                AC.to_red1()
            if char == 't': # yellow light 1
                AC.yellow_blink1(3)
            if char == 'd': # green light 2
                AC.to_green2()
            if char == 'f': # red light 2
                AC.to_red2()
            if char == 'g': # yellow light 2
                AC.yellow_blink2(3)

        except rospy.ROSInterruptException:
                pass