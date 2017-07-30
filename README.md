# learn_ros_figures_command

## 功能描述

这个包是为了讲述如何写一个最简单的package，以及node之间的沟通机制，其实现的主要功能为：

commander和drawer两个节点注册到draw_figure话题上，通过commander向话题发送消息，消息的

类型为Figure的消息，drawer从话题接受消息，在接收到相应的消息后，可以画出相应的图形。

## 原理讲解

首先要明白，ROS各个node之间是通过话题（topic）进行通信的，话题的作用就相当于一个中转站。

有node往上面发送消息，这样的node称为publisher；也有node从上面接收消息，这样的node称为

subscriber。

下面首先列出包中各文件所包含的代码

**消息**

文件位置：msg/Figure.msg

每个topic上的消息都只有一种类型，虽然如此，但是要注意，这里的类型范围很广，消息本身相当于

一个对象，里面可以包含各种基本类型的属性，例如本例中定义Figure类型的消息：

		string figures

里面就包含了一个string类型的属性figures，在调用时也遵循类中属性的调用规则，例如本例中drawer.py

文件中，消息对象在draw(figure)函数中调用，调用属性时方法为figure.figures

**话题**

文件位置：scripts/commander.py  drawer.py

topic本质上来说就是一个字符串，通过ROS机制将这个字符串保存到master中，作为相应节点之间通信的

渠道，topic本身不需要另写程序定义，只需要在定义节点时指定topic名称即可。在commander.py和drawer.py

相应的代码分别如下：

		pub = rospy.Publisher('draw_figure',Figures,queue_size=10)

		rospy.Subscriber('draw_figure',Figures,draw)

**catkin文件编译系统**

上面只是一个最简单的节点-话题-节点通信机制的演示，下面讲解catkin_make文件编译有关的文件。

文档中package.xml和CMakeList.txt两个文件，在使用自己创建的msg文件时需要更改的地方，首先是

package.xml文件，其中主要是三大部分：作者信息，许可类型以及相关依赖项。作者信息填写自己的

邮箱、姓名以及个人网站等等，许可类型一般为BSD，也有其他许可类型，具体可参见文件相应的注释。

package.xml文件中的依赖项需要注意，
