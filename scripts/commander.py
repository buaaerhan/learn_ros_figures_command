#!/usr/bin/env python

import rospy
from learn_ros_figures_command.msg import Figures

def commander():
    pub = rospy.Publisher('draw_figure',Figures,queue_size=10)
    rospy.init_node('figures_commander',anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        figure = raw_input('Input figure command: ')
        pub.publish(figure)
        rate.sleep()

if __name__ == '__main__':
    try:
        commander()
    except rospy.ROSInterruptException:
        pass
