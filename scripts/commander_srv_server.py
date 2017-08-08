#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Filename: commander_srv_server.py
# 由于注释使用了中文，因此在第二行中声明使用utf8编码方式

# 导入必要模块
from learn_ros_figures_command.srv import *
import rospy
import matplotlib as plt
import numpy as np
from drawer import draw

# 定义service的处理函数，相当于msg中的回调函数，用于处理接收到的信息
def handle_function(figure_command):

    # 注意此处调用request中的信息的方式，与之前各node之间通过topic传输消息的调用方式是一样的
    # 都是将其看作是对象中的一个属性。调用时直接按照object.attribute的方式调用
    print "You want to draw a %s"%figure_command.figures

    # 将request数据传入draw函数，画图。注意，draw函数本身是为topic&message的通信方式
    # 设计的，也就是说draw函数的输入量是一个Figures类型的message，但是此处输入量却是一个
    # DrawConfig类型的service，令人意外地，函数能够正常工作。这也从另外一个方面说明了，
    # message和service本质上是一样的，都是一个对象，只要这个里面包含了draw函数所需要的属性即可。
    draw(figure_command)

    # 为了能将反馈信息传送到response中去，这里需要返回一个DrawConfigResponse类。注意，
    # 这个类是ROS机制在使用service时自动生成的。
    return DrawConfigResponse("This is a configuration from service server. OK!")

def draw_config_server():
    rospy.init_node('draw_config_server')
    s = rospy.Service('draw_config',DrawConfig,handle_function)
    rospy.spin()


if __name__=="__main__":
    draw_config_server()
