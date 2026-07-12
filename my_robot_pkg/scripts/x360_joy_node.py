#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

def joy_callback(data):
    twist = Twist()
    if data.axes[7] == 1.0 :
        twist.linear.x = 0.5
    elif data.axes[7] == -1.0 :
        twist.linear.x = -0.5
    elif data.axes[6] == 1.0 :
        twist.angular.z = 0.5
    elif data.axes[6] == -1.0 :
        twist.angular.z = -0.5
    else :
       twist.linear.x = data.axes[1] * 1.5
       twist.angular.z = data.axes[0] * 0.5
    pub.publish(twist)

rospy.init_node('joystick_controller')
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
rospy.Subscriber('joy', Joy, joy_callback)
rospy.spin()
