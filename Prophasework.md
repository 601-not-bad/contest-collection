1.环境配置  
https://github.com/chipsalliance/rocket-chip  
clone 出错，修改全局配置文件，全局配置文件在home 目录下，vim  .gitconfig  查看配置文件
git --config –global –list
问题和解决方法：
https://blog.csdn.net/qq_32791023/article/details/83622283?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
git clone 太慢了，这个问题实在不好解决，找国外师姐帮忙下载。 

2 开发日记  

3-6  
开会讨论下具体的工作分配，老师希望我们三个并行的去做工作，但是我们讨论后总觉得没有一个总体的框架，想一起生成一个Ip核，了解一下外部端口（引脚），对要做的工作有一个具体的概念后再进一步分工。师姐用Google drive传输，宣佚下载后传到网盘搞定 。 

3-7
虚拟机强烈推荐100G，否则容量不够，虚拟机扩容方法如下:  
https://blog.csdn.net/daemon_2017/article/details/80660372?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task  
https://blog.csdn.net/hzlarm/article/details/99622053?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task  

3-8  
花了一晚上时间编译，大概弄清了rocketchip每个部分的作用。

3-20  
综合时报错，sram显示内存太大 需要调小  
仿真[XSIM 43-3238] Failed to link the design

3-20_26  
按照老师要求看了单独rocket chip 取rom 数据，发现取数据时reset为0 ，然后我们freedom取bootrom数据是reset是1，我们觉得reset信号有问题，然后追踪reset信号，后来觉得reset没问题，追踪过程看信号受到了一些启发，觉得是仿真时间不够，然后我们就一直让它仿真，然后在bootrom代码里面下了断点，out<=rom[adddress]，仿真到16ms取出数据了。  
从ROM读出数据后继续追踪，追到Icache, 但是core的指令一直是xxxx，说明指令传到icache后似乎并没有传到core里面进行执行，但是理论上肯定是要传到core执行，一开始觉得是执行时间不够，然后继续执行，执行了270ms后还是显示xxxx,就没有继续仿真下去了，让老师看下信号执行，是不是我们有些地方没注意到  
期间看了scala级代码，目前知道了系统是如何传递参数了，也看了模块连接的一些代码，还有系统如何实例化以及测试的。