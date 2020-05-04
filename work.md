## 进展记录  
- 5-1  
  尝试增加AXI4接口的RAM。
  (1) 对verilog代码进行修改看能否添加成功，通过脚本将包含所有module的大文件切割成若干个module.v文件，方便进行代码的查找和修改。在实际操作过程中，先尝试把E310自带的的tilelink接口的maskrom转成axi4接口的RAM，找到rocket chip中tilelink转axi4模块的verilog代码， 想移植到E310中，移植中发现找到的tl2axi4模块代码并不是规整的，即该模块的axi4接口不包含完整的AXI4接口信号，这导致从Verilog角度实现该功能难度很大。  
  (2) 尝试阅读，修改chisel代码来实现功能，来发现耦合性极高，需要对chisel级别的代码有透彻的了解才能够修改chisel代码。
  (3) 总结：今日无具体进展，但对硬件实现的难度有了一定了解
