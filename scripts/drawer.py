#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 本节点注册到draw_figure话题，从其接收消息，并执行相应指令
# 注意需要用到matplotlib和numpy支持包，python版本为2.7

import matplotlib.pyplot as plt
import numpy as np
import rospy
from learn_ros_figures_command.msg import Figures

# 定义画圆函数，输入参量为圆半径
def draw_circle(radius):
    x = np.arange(0,2*np.pi,0.01)
    plt.plot(radius*np.cos(x),radius*np.sin(x))
    plt.show()

# 定义画图函数，输入参量为接收到的消息，可根据不同的指令画出不同的图形
# 目前仅支持画圆，作为演示所用
def draw(figure):
    if(figure.figures=='circle'):       # 注意，传入参量为figure，是一个Figures类型的消息对象，可以调用其中的
        draw_circle(5)                  # 属性数据figures，以查看输入的具体数据

    else:
        print 'Please input "circle"'

def drawer():
    rospy.init_node('figures_drawer',anonymous=True)
    rospy.Subscriber('draw_figure',Figures,draw)        # 此处与定义publisher时的情形类似，话题仍是以字符串的
    rospy.spin()                                        # 的形式传入函数，上面的消息类型为Figures

# 上面的代码与定义publisher时的情形类似，话题仍是以字符串的形式传入函数
# 话题上承载的消息类型为Figures，在接收到Figures类型的消息之后，将消息
# 作为参数传入到回调函数draw(figure)中去，画出相应图形

if __name__=='__main__':
    drawer()
#draw('circle')
