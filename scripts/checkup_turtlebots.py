#!/usr/bin/env python3
# −*− coding: utf−8 −*−

import matplotlib.pyplot as plt
import numpy as np
import rospy
from sensor_msgs.msg import LaserScan
import cv_bridge 
import cv2 
from sensor_msgs.msg import Image,CompressedImage

def callbackScan(scan):
        """Function to receive and process the laser scan"""
        
        # Plot the scan
        sonar(scan.ranges)


def sonar(vector):
        """Function to plot the obstacles in the robot's reference frame"""
    
        # Processing of the scan
        x,y = [],[]                     # Empty lists for the polar plot
        for i,val in enumerate(vector):
            x.append(np.radians(i))     # Angle
            y.append(val)               # Distance
            
        # Plot the scan
        fig.polar(x,y,"ro") # Polar plot
        ax = plt.gca()
        ax.set_rmax(0.5)
        fig.draw()
        fig.title("Scan")
        fig.pause(0.01)     # Pause to let the plot update
        fig.clf()           # Clear the plot

def image_callback(image):
    cvImage_raw = bridge.imgmsg_to_cv2(image, desired_encoding='bgr8')
    cv2.imshow("Camera", cvImage_raw);cv2.waitKey(3)

def image_callback_compressed(msg):
    cvImage = bridge.compressed_imgmsg_to_cv2(msg, desired_encoding='bgr8') # Transform the image to openCV format , msg is the original image from ROS         
    cv2.imshow("Image_debut_compressed", cvImage);cv2.waitKey(1)

if __name__=="__main__":
    bridge = cv_bridge.CvBridge()
    subScan = rospy.Subscriber("/scan",LaserScan,callbackScan)
    subCam = rospy.Subscriber('/cam/image_raw', Image, image_callback)
    image_sub_compressed = rospy.Subscriber('/raspicam_node/image/compressed', CompressedImage, image_callback_compressed)

    fig = plt.figure()

    rospy.init_node( 'checkup', anonymous=True )
    rospy.spin()