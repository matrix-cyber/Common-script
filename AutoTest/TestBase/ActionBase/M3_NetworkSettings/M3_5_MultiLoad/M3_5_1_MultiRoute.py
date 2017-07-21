import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
import time
import TestBase.ActionBase.Base_Action.SSH_Action as SSHA
import TestBase.TopoBase as Topo
import socket

class MultiRoute:
    #初始化：（1）将WEB句柄交给此模块  （2）导入该模块的CSS元素库及测试数据
    def __init__(self, web_handler, ssh_handler, TestData): #模块初始化
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu  # 目录元素库
        self.ElementCss = CSS.ElementBase.MultiRoute  # 模块元素库
        self.TestData = TestData  # 测试数据
        self.bool = True

    # 封装查找命令
    def find_element(self, para): #公用
        return self.web_handler.find_element_by_css_selector(para)

    def ADD(self): #添加
        self.find_element(self.ElementCss["全部选择"]).click()
        self.find_element(self.ElementCss["全部删除"]).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        time.sleep(2)
        self.web_handler.refresh_page()
        time.sleep(2)
        self.find_element(self.ElementCss["添加"]).click()
        time.sleep(3)
        self.find_element(self.ElementCss["负载模式"]).click()
        time.sleep(1)
        LinkType = self.TestData["连接类型"]
        self.find_element(self.ElementCss[LinkType]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["运营商"]).click()
        # time.sleep(1)
        self.find_element(self.ElementCss["全部"]).click()
        self.find_element(self.ElementCss["备注"]).send_keys(self.TestData["备注"])
        self.find_element(self.ElementCss["线路1"]).click()
        self.find_element(self.ElementCss["线路2"]).click()
        self.find_element(self.ElementCss["确定"]).click()
        time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        loadmode = self.find_element(self.ElementCss["获取负载模式"]).text
        if loadmode != self.TestData["备注"]:
            self.bool = False
        if not self.Check_ADD():
            return False
        else:
            return True

    def EDIT_LineWeight(self):
        self.find_element(self.ElementCss["编辑"]).click()
        Weight1 = "线路1的比例"+self.TestData["比例1"]
        Weight2 = "线路2的比例" + self.TestData["比例2"]
        # print(Weight1,Weight2)
        self.find_element(self.ElementCss["编辑线路1比例"]).click()
        time.sleep(3)
        self.find_element(self.ElementCss[Weight1]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["编辑线路2比例"]).click()
        time.sleep(3)
        self.find_element(self.ElementCss[Weight2]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["编辑确定"]).click()
        time.sleep(1)

    def ON_one(self): #单个启用
        user_stat = self.find_element(self.ElementCss["启停用状态"]).text
        if user_stat == "已启用":
            return True
        else:
            self.find_element(self.ElementCss["单独启用"]).click()
            time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        new_stat = self.find_element(self.ElementCss["启停用状态"]).text
        if new_stat == "已启用":
            return True
        else:
            return False

    def OFF_one(self): #单个停用
        user_stat = self.find_element(self.ElementCss["启停用状态"]).text
        if user_stat == "已停用":
            return True
        else:
            self.find_element(self.ElementCss["单独停用"]).click()
            time.sleep(2)
            self.web_handler.accept_confirm_msg()
            time.sleep(2)
        self.web_handler.refresh_page()
        time.sleep(3)
        new_stat = self.find_element(self.ElementCss["启停用状态"]).text
        if new_stat == "已停用":
            return True
        else:
            return False

    def DELETE_one(self): #单个删除
        self.find_element(self.ElementCss["单独删除"]).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        try:
            self.find_element(self.ElementCss["获取IP"])
            return False
        except:
            return True

    def ON_all(self): #全部启用
        self.find_element(self.ElementCss["全部选择"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["全部启用"]).click()
        self.web_handler.refresh_page()
        time.sleep(2)
        new_stat = self.find_element(self.ElementCss["启停用状态"]).text
        if new_stat == "已启用":
            return True
        else:
            return False

    def OFF_all(self): #全部停用
        self.find_element(self.ElementCss["全部选择"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["全部停用"]).click()
        time.sleep(2)
        self.web_handler.accept_confirm_msg()
        time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        new_stat = self.find_element(self.ElementCss["启停用状态"]).text
        if new_stat == "已停用":
            return True
        else:
            return False

    def DELETE_all(self): #全部删除
        self.find_element(self.ElementCss["全部选择"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["全部删除"]).click()
        time.sleep(2)
        try:
            self.web_handler.accept_confirm_msg()
        except:
            time.sleep(1)
        time.sleep(2)
        time.sleep(10)
        try:
            self.find_element(self.ElementCss["单独停用"])
            return False
        except:
            return True

    def Check_ADD(self):
        if not self.bool and self.TestData["预期结果"] == "添加失败":
            return True
        elif self.bool and self.TestData["预期结果"] == "添加成功":
            return True
        else:
            return False

    def Check_RealLink(self):  # 验证功能
        # 验证后台是否为实时连接数类型
        output = self.ssh_handler.exec_cmd("cat /tmp/pcc.txt")
        seat1 = output.find("con")
        seat2 = output.find("wan1")
        seat3 = output.find("wan2")
        if seat1 < 0 or seat2 < 0 or seat3 < 0:
            return False

        # 验证后台的比例是否与配置一致
        temp_str = output.split(" ")
        factor = []
        for str in temp_str:
            if ("factor" in str):
                ustr = str.split(":")
                factor.append(ustr[1])
        if (factor[0] != self.TestData["比例1"] or factor[1] != self.TestData["比例2"]):
            return False

        # 访问网页生成连接数
        output1 = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack | grep remote_if=wan1 | wc -l")
        num1_old = int(output1)
        output2 = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack | grep remote_if=wan2 | wc -l")
        num2_old = int(output2)
        self.web_handler.open_webpage("http://www.qq.com")
        time.sleep(2)
        self.web_handler.open_webpage("http://www.jd.com")
        time.sleep(2)
        new_output1 = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack | grep remote_if=wan1 | wc -l")
        num1 = int(new_output1)
        new_output2 = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack | grep remote_if=wan2 | wc -l")
        num2 = int(new_output2)
        weight1 = self.TestData["比例1"]
        weight2 = self.TestData["比例2"]
        print("\t\t 配置比例：>>> wan1:wan2 = %s:%s" % (weight1, weight2))
        print("\t\t 原有连接：>>> wan1:%s  wan2:%s " % (num1_old, num2_old))
        print("\t\t 现有连接：>>> wan1:%s  wan2:%s " % (num1, num2))
        self.web_handler.close_webpage()
        time.sleep(2)
        self.web_handler.close_webpage()
        time.sleep(1)

        config_scale = int(weight1 )/int(weight2)
        if config_scale >= 1:
            min_scale = config_scale - 0.5
            max_scale = config_scale + 0.5
        elif config_scale > 0.2:
            min_scale = config_scale - 0.2
            max_scale = config_scale + 0.2
        else:
            min_scale = 0
            max_scale = config_scale

        if num1 != 0 and num2 != 0:
            scale1 = num1 / num2
            if (min_scale <= scale1 <= max_scale):
                return True
            else:
                return False
        else:
            return False

    def Check_NewLink(self):  # 验证功能
        #验证后台是否为实时连接数类型
        output = self.ssh_handler.exec_cmd("cat /tmp/pcc.txt")
        seat1 = output.find("con")
        seat2 = output.find("wan1")
        seat3 = output.find("wan2")
        if seat1 < 0 or seat2 < 0 or seat3 < 0:
            return False

        #验证后台的比例是否与配置一致
        temp_str = output.split(" ")
        factor = []
        for str in temp_str:
            if ("factor" in str):
                ustr = str.split(":")
                factor.append(ustr[1])
        if (factor[0] != self.TestData["比例1"] or factor[1] != self.TestData["比例2"]):
            return False

        #访问网页生成连接数
        output1 = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack | grep remote_if=wan1 | wc -l")
        num1_old = int(output1)
        output2 = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack | grep remote_if=wan2 | wc -l")
        num2_old = int(output2)
        self.web_handler.open_webpage("http://www.qq.com")
        time.sleep(3)
        self.web_handler.open_webpage("http://www.jd.com")
        time.sleep(2)
        new_output1 = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack | grep remote_if=wan1 | wc -l")
        num1 = int(new_output1)
        new_output2 = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack | grep remote_if=wan2 | wc -l")
        num2 = int(new_output2)
        weight1 = self.TestData["比例1"]
        weight2 = self.TestData["比例2"]
        print("\t\t 配置比例：>>> wan1:wan2 = %s:%s" % (weight1, weight2))
        print("\t\t 原有连接：>>> wan1:%s  wan2:%s " % (num1_old, num2_old))
        print("\t\t 现有连接：>>> wan1:%s  wan2:%s " % (num1, num2))
        self.web_handler.close_webpage()
        time.sleep(2)
        self.web_handler.close_webpage()
        time.sleep(1)

        config_scale = int(weight1 )/int(weight2)
        if config_scale >= 1:
            min_scale = config_scale - 0.5
            max_scale = config_scale + 0.5
        elif config_scale > 0.2:
            min_scale = config_scale - 0.2
            max_scale = config_scale + 0.2
        else:
            min_scale = 0
            max_scale = config_scale

        #验证功能是否生效
        num1_add = num1 - num1_old
        num2_add = num2 - num2_old

        if num1_add != 0 and num2_add != 0:
            scale1 = num1_add / num2_add
            if (min_scale <= scale1 <= max_scale) :
                return True
            else:
                 return False
        else:
            return False

    def Check_SIP_DIP(self):
        #后台验证
        output = self.ssh_handler.exec_cmd("sqlite3 /etc/mnt/ikuai/config.db 'select * from pcc_dist' -line")
        output = SSHA.IkSSHUtils.get_one_block_data(output)
        output = SSHA.IkSSHUtils.parse_data_to_dict(output, "=")
        if (output["state"] != "up" or
            output["mode"] != "1" or
            output["comment"] != self.TestData["备注"]):
            print("NG1")
            return False

        output = self.ssh_handler.exec_cmd("cat /tmp/pcc.txt")
        seat1 = output.find("ip")
        seat2 = output.find("wan1")
        seat3 = output.find("wan2")
        if seat1 < 0 or seat2 < 0 or seat3 < 0:
            print("NG2")
            return False

        temp_str = output.split(" ")
        factor = []
        for str in temp_str:
            if ("factor" in str):
                ustr = str.split(":")
                factor.append(ustr[1])
            else:
                continue
        if factor[0] != self.TestData["比例1"] or factor[1] != self.TestData["比例2"] :
            print("NG3")
            return False

        self.ssh_handler.exec_cmd("conntrack -F")
        time.sleep(2)
        self.web_handler.open_webpage("http://www.qq.com") # open webpage before check
        time.sleep(1)
        qq_add = socket.gethostbyname('www.qq.com')
        print(qq_add)
        output = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack | grep src=" + Topo.TEST_PC + "| grep dst=" + qq_add)
        all_num = output.count("dst=" + qq_add)
        wan1_num = output.count("remote_if=wan1")
        wan2_num = output.count("remote_if=wan2")
        weight1 = self.TestData["比例1"]
        weight2 = self.TestData["比例2"]
        print("\t\t 配置比例：>>> wan1:wan2 = %s:%s" % (weight1, weight2))
        print("\t\t 现有连接：>>> all:wan1:wan2 = %s:%s:%s" % (all_num,wan1_num,wan2_num))
        self.web_handler.close_webpage()  # close webpage after check
        if all_num == 0:
            print("NG4")
            return False
        elif weight1 >= weight2 and wan1_num == all_num:
            return True
        elif weight2 > weight1 and wan2_num == all_num:
            return True
        elif wan1_num / all_num > 0.9 or wan2_num / all_num > 0.9:
            return True
        else:
            print("NG5")
            return False

    def Check_SIP(self):
        # 后台验证
        output = self.ssh_handler.exec_cmd("sqlite3 /etc/mnt/ikuai/config.db 'select * from pcc_dist' -line")
        output = SSHA.IkSSHUtils.get_one_block_data(output)
        output = SSHA.IkSSHUtils.parse_data_to_dict(output, "=")
        if (output["state"] != "up" or
                    output["mode"] != "6" or
                    output["comment"] != self.TestData["备注"]):
            print("NG1")
            return False

        output = self.ssh_handler.exec_cmd("cat /tmp/pcc.txt")
        seat1 = output.find("sip")
        seat2 = output.find("wan1")
        seat3 = output.find("wan2")
        if seat1 < 0 or seat2 < 0 or seat3 < 0:
            print("NG2")
            return False

        temp_str = output.split(" ")
        factor = []
        for str in temp_str:
            if ("factor" in str):
                ustr = str.split(":")
                factor.append(ustr[1])
            else:
                continue
        if factor[0] != self.TestData["比例1"] or factor[1] != self.TestData["比例2"]:
            print("NG3")
            return False

        self.ssh_handler.exec_cmd("conntrack -F")
        time.sleep(2)
        self.web_handler.open_webpage("http://www.qq.com")  # open webpage before check
        time.sleep(1)
        self.web_handler.open_webpage("http://www.jd.com")  # open webpage before check
        time.sleep(1)
        output = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack | grep src=" + Topo.TEST_PC)
        all_num = output.count("src="+Topo.TEST_PC)
        wan1_num = output.count("remote_if=wan1")
        wan2_num = output.count("remote_if=wan2")
        lan_num = output.count("remote_if=lan1")
        # print("all:", all_num,"lan:",lan_num)
        wan_num = all_num - lan_num
        weight1 = self.TestData["比例1"]
        weight2 = self.TestData["比例2"]
        print("\t\t 配置比例：>>> wan1:wan2 = %s:%s" % (weight1, weight2))
        print("\t\t 实际连接：>>> all:wan1:wan2 = %s:%s:%s" % (wan_num, wan1_num, wan2_num))
        self.web_handler.close_webpage()
        time.sleep(1)# close webpage after check
        self.web_handler.close_webpage()
        if all_num == 0 :
            print("NG4")
            return False
        elif weight1 >=weight2 and wan1_num/wan_num > 0.9:
            return True
        elif  weight2 >weight1 and wan2_num/wan_num > 0.9:
            return True
        elif wan1_num / all_num > 0.9 or wan2_num / all_num > 0.9:
            return True
        else:
            print("NG5")
            return False

    def Check_SIP_DIP_DPORT(self):
        output = self.ssh_handler.exec_cmd("sqlite3 /etc/mnt/ikuai/config.db 'select * from pcc_dist' -line")
        output = SSHA.IkSSHUtils.get_one_block_data(output)
        output = SSHA.IkSSHUtils.parse_data_to_dict(output, "=")
        if (output["state"] != "up" or
                    output["comment"] != self.TestData["备注"] or
                    output["mode"] != "0"):
            return False

        output = self.ssh_handler.exec_cmd("cat /tmp/pcc.txt")
        seat1 = output.find("ip+dport")
        seat2 = output.find("wan1")
        seat3 = output.find("wan2")
        if (seat1 < 0 or seat2 < 0 or seat3 < 0):
            return False

        temp_str = output.split(" ")
        factor = []
        for str in temp_str:
            if ("factor" in str):
                ustr = str.split(":")
                factor.append(ustr[1])
            else:
                continue
        weight1 = self.TestData["比例1"]
        weight2 = self.TestData["比例2"]
        if factor[0] != weight1 or factor[1] != weight2:
            return False

        self.ssh_handler.exec_cmd("conntrack -F")
        jd_add = socket.gethostbyname('www.jd.com')
        self.web_handler.open_webpage("www.jd.com")
        time.sleep(5)
        output = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack | grep src=" + Topo.TEST_PC + " | grep dst=" + jd_add + " | grep dport=443" )
        all_num = output.count("dst=" + jd_add)
        wan1_num = output.count("remote_if=wan1")
        wan2_num = output.count("remote_if=wan2")
        print("\t\t 配置比例：>>> wan1:wan2 = %s:%s" % (weight1, weight2))
        print("\t\t 实际连接：>>> all:wan1:wan2: = %s:%s:%s" % (all_num, wan1_num, wan2_num))
        self.web_handler.close_webpage()
        time.sleep(1)# close webpage after check
        if all_num == 0 :
            print("NG4")
            return False
        elif weight1 >weight2 and wan1_num/all_num > 0.9:
            return True
        elif  weight2 >weight1 and wan2_num/all_num > 0.9:
            return True
        elif wan1_num/all_num > 0.9 or wan2_num/all_num > 0.9:
            return True
        else:
            print("NG5")
            return False

    def Check_RealFlow(self):
        output = self.ssh_handler.exec_cmd("sqlite3 /etc/mnt/ikuai/config.db 'select * from pcc_dist' -line")
        output = SSHA.IkSSHUtils.get_one_block_data(output)
        output = SSHA.IkSSHUtils.parse_data_to_dict(output, "=")
        if (output["state"] != "up" or
                    output["comment"] != self.TestData["备注"] or
                    output["mode"] != "3"):
            return False

        output = self.ssh_handler.exec_cmd("cat /tmp/pcc.txt")
        seat1 = output.find("download")
        seat2 = output.find("wan1")
        seat3 = output.find("wan2")
        if (seat1 < 0 or seat2 < 0 or seat3 < 0):
            return False

        temp_str = output.split(" ")
        factor = []
        for str in temp_str:
            if ("factor" in str):
                ustr = str.split(":")
                factor.append(ustr[1])
            else:
                continue
        weight1 = self.TestData["比例1"]
        weight2 = self.TestData["比例2"]
        if factor[0] != weight1 or factor[1] != weight2:
            return False

    def Check_SIP_SPORT(self):
        output = self.ssh_handler.exec_cmd("sqlite3 /etc/mnt/ikuai/config.db 'select * from pcc_dist' -line")
        output = SSHA.IkSSHUtils.get_one_block_data(output)
        output = SSHA.IkSSHUtils.parse_data_to_dict(output, "=")
        if (output["state"] != "up" or
                    output["comment"] != self.TestData["备注"] or
                    output["mode"] != "7"):
            print("NG1")
            return False

        output = self.ssh_handler.exec_cmd("cat /tmp/pcc.txt")
        seat1 = output.find("sip+sport")
        seat2 = output.find("wan1")
        seat3 = output.find("wan2")
        if (seat1 < 0 or seat2 < 0 or seat3 < 0):
            print("NG2")
            return False

        temp_str = output.split(" ")
        factor = []
        for str in temp_str:
            if ("factor" in str):
                ustr = str.split(":")
                factor.append(ustr[1])
            else:
                continue
        weight1 = self.TestData["比例1"]
        weight2 = self.TestData["比例2"]
        if factor[0] != weight1 or factor[1] != weight2:
            print("NG3")
            return False

        # 访问网页生成连接数
        output1 = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack | grep remote_if=wan1 | wc -l")
        num1_old = int(output1)
        output2 = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack | grep remote_if=wan2 | wc -l")
        num2_old = int(output2)
        self.web_handler.open_webpage("http://www.qq.com")
        time.sleep(3)
        self.web_handler.open_webpage("http://www.jd.com")
        time.sleep(2)
        new_output1 = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack | grep remote_if=wan1 | wc -l")
        num1 = int(new_output1)
        new_output2 = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack | grep remote_if=wan2 | wc -l")
        num2 = int(new_output2)
        weight1 = self.TestData["比例1"]
        weight2 = self.TestData["比例2"]
        print("\t\t 配置比例：>>> wan1:wan2 = %s:%s" % (weight1, weight2))
        print("\t\t 原有连接：>>> wan1:%s  wan2:%s " % (num1_old, num2_old))
        print("\t\t 现有连接：>>> wan1:%s  wan2:%s " % (num1, num2))
        self.web_handler.close_webpage()
        time.sleep(2)
        self.web_handler.close_webpage()
        time.sleep(1)

        config_scale = int(weight1) / int(weight2)
        if config_scale >= 1:
            min_scale = config_scale - 0.5
            max_scale = config_scale + 0.5
        elif config_scale > 0.2:
            min_scale = config_scale - 0.2
            max_scale = config_scale + 0.2
        else:
            min_scale = 0
            max_scale = config_scale

        # 验证功能是否生效
        num1_add = num1 - num1_old
        num2_add = num2 - num2_old

        if num1_add != 0 and num2_add != 0:
            scale1 = num1_add / num2_add
            if (min_scale <= scale1 <= max_scale):
                return True
            else:
                print("NG4")
                return False
        else:
            print("NG5")
            return False
