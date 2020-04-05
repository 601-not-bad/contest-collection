# -*- coding:utf-8 -*-
# @Time : 2020/4/5 0005 下午 20:17
# @Author: xuanyi
# @File : matchVerilogModule.py


if __name__ == '__main__':
    core = dict()
    soc = dict()
    name_equal = list()
    data_equal = list()
    data_not_equal = list()
    # 获取core的所有module
    with open("freechips.rocketchip.system.DefaultConfig.v") as f_core:
        for line in f_core.readlines():
            if line.startswith("module"):
                module = line.split()[1].split("(")[0]
                core[module] = list()
            elif line.startswith("endmodule"):
                pass
            else:
                core[module].append(line.split("//")[0])

    # 获取soc的所有module
    with open("sifive.freedom.everywhere.e300artydevkit.E300ArtyDevKitConfig.v") as f_soc:
        for line in f_soc.readlines():
            if line.startswith("module"):
                module = line.split()[1].split("(")[0]
                soc[module] = list()
            elif line.startswith("endmodule"):
                pass
            else:
                soc[module].append(line.split("//")[0])

    for module in core:
        if module in soc:
            name_equal.append(module)
            if core[module] == soc[module]:
                data_equal.append(module)
            else:
                data_not_equal.append(module)

    print("The length of core:", core.__len__())
    print("The length of soc:", soc.__len__())
    print("The length of module name matching between core and soc:", name_equal.__len__())
    print("The length of module data matching between core and soc:", data_equal.__len__())
    print("The length of module data not matching between core and soc:", data_not_equal.__len__())

    print("分割线".center(100, "-"))

    for module in data_equal:
        print(module)
