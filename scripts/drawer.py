#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import rospy
from learn_ros_figures_command.msg import Figures

def draw_circle(radius):
    x = np.arange(0,2*np.pi,0.01)
    plt.plot(radius*np.cos(x),radius*np.sin(x))
    plt.show()

def draw(figure):
    if(figure.figures=='circle'):
        draw_circle(5)

    else:
        print 'Please input "circle"'

def drawer():
    rospy.init_node('figures_drawer',anonymous=True)
    rospy.Subscriber('draw_figure',Figures,draw)
    rospy.spin()

if __name__=='__main__':
    drawer()
#draw('circle')
