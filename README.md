# contest-collection
用来记录比赛中的一些问题、过程和总结等


## 2020-4-16 接下来的任务分析

接下来，考虑进一步的计划。

（1）显示字母

将RISC-VSoC的至少8路数字I/O或2路模拟I/O连接到硬件逻辑分析仪或示波器通道上（推荐采用Analog Discovery Studio）, 在硬件逻辑分析仪或示波器上显示出“RISC-V”字样（任意字体）(类似下面逻辑分析仪中的”春节快乐!”)

（2）硬件连接以太网

基础功能部分同时需要实现简单的以太网图像数据获取功能：图像获取部分功能实现如上图，在FPGA中实现以太网通信接口及缓存，作为RISC-V片上系统的一个外设，编写软件程序，能够通过以太网接口与外部的FTP/tFTP服务器通信，并从服务器上获取已经准备好的图片数据，通过软件程序控制能够将获取到的图片数据依次显示在外设液晶屏幕上。

- 任务1：通过GPIO输出“RISCV”（1周，暂不实现）
- 任务2：硬件连接以太网，通过AXI的IP （1周）
- 任务3：实现RAM或者DRAM，保证获得的数据有地方存放（1周， 李宣佚）
- 任务4：硬件连接显示屏（1周，李宣佚）
- 任务5：软件运行freertos（2周，张亮）
- 任务6：软件移植lwip（2周，张亮）
- 任务7：编写ftp shell软件，与服务器沟通（1周，暂不实现）
- 任务8：完成基本要求，获得、存储并显示（暂不确定，暂不实现）
- 任务9：算法调研及C语言实现（暂不确定，刘东宸）

任务之间的关系如下：
```
任务1->任务2->任务3->任务4
         |            |
         v            v
任务5->任务6-----------
                |
                v
       任务7 ->任务8
任务9
```
