#!/usr/bin/env python

# 实际上每个node就是一个可执行文件，这里我们使用了rospy客户端库，即ROS的Python客户端，因此
# 我们需要编写Python程序作为ROS的node

# 首先加载rospy客户端库，用以创建节点
# 然后从learn_ros_figures_command/msg文件夹中加载Figures类型的消息文件，注意导入方式
import rospy
from learn_ros_figures_command.msg import Figures

# 定义节点函数
def commander():
    pub = rospy.Publisher('draw_figure',Figures,queue_size=10)  # 定义节点为一个消息发送者publisher，
    rospy.init_node('figures_commander',anonymous=True)         # 发送Figures类型的消息到draw_figure这个话题上，频率为
    rate = rospy.Rate(10)                                       # 节点名称默认为figures_commander,支持系统自动分配名字
    
    # 在上面代码中需要注意的是话题draw_figure的定义，是没有额外
    # 代码的，只是一个输入字符串而已

    while not rospy.is_shutdown():
        figure = raw_input('Input figure command: ')            # 输入指令
        pub.publish(figure)                                     # 将消息对象figure发送出去(发送到之前定义的topic上去)
        rate.sleep()

if __name__ == '__main__':
    try:
        commander()
    except rospy.ROSInterruptException:
        pass
