#!/usr/bin/env python
# This is an example of service server

from learn_ros_figures_command.srv import *
import rospy
import matplotlib as plt
import numpy as np
from drawer import draw
def handle_function(figure_command):

    print "You want to draw a %s"%figure_command.figures
    draw(figure_command)
    return DrawConfigResponse("This is a configuration from service server. OK!")

def draw_config_server():
    rospy.init_node('draw_config_server')
    s = rospy.Service('draw_config',DrawConfig,handle_function)
    rospy.spin()


if __name__=="__main__":
    draw_config_server()
