#!/usr/bin/env python
# This is an example of service client node

import sys
import rospy
from learn_ros_figures_command.srv import *

def draw_figure_client(figure_command):

    rospy.wait_for_service('draw_config')

    try:

        draw_config_client = rospy.ServiceProxy('draw_config',DrawConfig)

        resp = draw_config_client.call(DrawConfigRequest(figure_command))

        print resp.configuration

    except rospy.ServiceException, e:
        print "Service call failed:%s"%e

if __name__=="__main__":
    
    figure_command = raw_input("please input a figure command:")
    draw_figure_client(figure_command)
