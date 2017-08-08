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

package.xml文件中的依赖项需要注意，依赖项分为四部分，分别为：buildtool_depend,build_depend

run_depend, test_depend,但常用的一般是前三个部分。

第一部分，buildtool_depend,这个部分是固定的，统一为catkin

第二部分，build_depend, 这部分主要填写编译时需要用到的包，在本例中，我们只需要最基本的，

即rospy和message_generation

第三部分，run_depend, 这部分主要时运行时需要用到的包，在本例中，也是只需要rospy和message_runtime

下面讲解CMakeList的填写：

本例中只使用了自己写的msg文件，并未写srv文件，也没有用到std_msgs消息，因此只需处理与message

有关的函数：

		find_package(catkin REQUIRED rospy message_generation)

		add_message_files(FILES Figures.msg)

		catkin_package(CATKIN_DEPENDS message_runtime)

上面第一行和第三行代码与package.xml文件中相对应，中间add_message_files()函数，添加自定义的msg

文件夹下的msg文件。

上面工作完成后，切换到catkin_ws工作空间，执行编译命令

		cd ~/catkin_ws
		catkin_make

编译完成之后，即可运行节点,注意每个命令都在一个新的终端执行：

		roscore
		rosrun learn_ros_figures_command commander.py
		rosrun learn_ros_figures_command drawer.py

运行之后，在commander终端中输入对应的消息，如circle，即可显示圆形图像。

**launch文件的编写**

launch文件就是一系列node的集合，可以方便的在一个文件中同时运行多个node，不用像上面一样一个个

node运行，那样太麻烦。launch文件代码较为简单,参见包中launch/commander_drawer.launch文件即可。

需要注意：

launch文件运行时，不需要单独运行roscore，在ros机制中，运行launch文件时，roscore是自动默认运

行的。

## Service的编写

从本质上来说，service与message差不多，都是用来实现ROS中node之间的通信。不同的是，service可以

实现反馈，当一个node(client)接收到另一个node发送过来的service请求时，可以做出相应的反应，并且

给出一个反馈信息。例如在本例中，如果画图的node接收到画图命令时，执行画图程序，并且给其客户端

一个反馈，确认自己收到了这条命令并且正确执行了。

service所实现的双向通信，其实仍然可以认为是单向的，只能由一个node发起请求，另一个node给出反馈，

反馈方在没有收到请求时，是不能给client端发送消息的。

要实现通过service的通信机制，首先要建立srv文件，可以认为是msg文件的扩展版。首先在包目录下建立

srv文件夹，然后新建DrawConfig.srv文件，如下：

		cd ~/catkin_ws/srv/learn_ros_figures_command
		mkdir srv
		cd srv
		touch DrawConfig.srv

在DrawConfig文件中输入如下代码：

		string figures
		---
		string configuration

注意，srv文件里的内容分为request和response两部分，以---分割，前面为request的类型，后面为response

的类型，这里我们每部分都只有一个属性数据。如果有需要，你也可以分别对其加入更多的数据类型。我们

看到，srv文件与msg文件极其类似，srv文件可以看成是双向的msg。


