import time

import TestBase.ActionBase.Base_Action.Public_Action as PA
import TestBase.ActionBase.Base_Action.UDP_Client as UC

import TestBase.ElementBase as CSS
import TestBase.TopoBase as Topo


class PortFlow:
    def __init__(self, web_handler,ssh_handler, test_data):  # 模块初始化
        self.web_handler = web_handler  # 页面连接
        self.ssh_handler = ssh_handler  # 后台连接
        self.MenuCss = CSS.ElementBase.Menu  # 目录元素库
        self.add_bool = True
        self.fun_bool = True
        self.ElementCss = CSS.ElementBase.PortFlow  # 本模块元素库——需更新
        self.TestData = test_data  # 本模块测试数据——需更新

    def find_element(self, para):   # 封装查找命令
        return self.web_handler.find_element_by_css_selector(para)

    def add(self):  # 添加基础规则
        time.sleep(2)
        self.find_element(self.ElementCss["添加"]).click()
        time.sleep(3)
        self.find_element(self.ElementCss["线路"]).click()
        time.sleep(1)
        wan = self.TestData["线路"]
        self.find_element(self.ElementCss[wan]).click()
        self.find_element(self.ElementCss["线路确定"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["源地址"]).click()
        time.sleep(1)
        if self.TestData["SIP"] == "localhost":
            test_sip = Topo.TEST_PC
        else:
            test_sip = self.TestData["SIP"]
        self.find_element(self.ElementCss["IP"]).send_keys(test_sip)
        self.find_element(self.ElementCss["添加IP"]).click()
        self.find_element(self.ElementCss["确定"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["目的地址"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["IP"]).send_keys(self.TestData["DIP"])
        self.find_element(self.ElementCss["添加IP"]).click()
        self.find_element(self.ElementCss["确定"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["备注"]).send_keys(self.TestData["备注"])
        time.sleep(1)
        self.find_element(self.ElementCss["编辑确定"]).click()
        time.sleep(1)
        try:
            self.find_element(self.ElementCss["备注填写错误"])
            self.bool = False
            return self.check_add()
        except:
            pass
        self.web_handler.refresh_page()
        time.sleep(1)
        try:
            self.find_element(self.ElementCss["编辑"])
            self.bool = True
            return self.check_add()
        except:
            self.bool = False
            return self.check_add()

    def edit_protocol(self):  # 编辑协议
        time.sleep(2)
        self.find_element(self.ElementCss["编辑"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["协议"]).click()
        time.sleep(1)
        protocol = self.TestData["协议"]
        self.find_element(self.ElementCss[protocol]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["编辑确定"]).click()

    def edit_sip(self):  # 编辑SIP
        time.sleep(2)
        self.find_element(self.ElementCss["编辑"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["源地址"]).click()
        try:
            self.find_element(self.ElementCss["已添加SIP"]).click()
            self.find_element(self.ElementCss["删除SIP"]).click()
        except:
            pass
        self.find_element(self.ElementCss["IP"]).clear()
        self.find_element(self.ElementCss["IP"]).send_keys(self.TestData["SIP"])
        self.find_element(self.ElementCss["添加IP"]).click()
        self.find_element(self.ElementCss["确定"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["编辑确定"]).click()

    def edit_dip(self):  # 编辑DIP
        time.sleep(2)
        self.find_element(self.ElementCss["编辑"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["目的地址"]).click()
        try:
            self.find_element(self.ElementCss["已添加IP"]).click()
            self.find_element(self.ElementCss["删除IP"]).click()
        except:
            pass
        self.find_element(self.ElementCss["IP"]).clear()
        self.find_element(self.ElementCss["IP"]).send_keys(self.TestData["DIP"])
        self.find_element(self.ElementCss["添加IP"]).click()
        self.find_element(self.ElementCss["确定"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["编辑确定"]).click()

    def edit_port(self):  # 编辑SPORT
        time.sleep(2)
        self.web_handler.refresh_page()
        time.sleep(2)
        self.find_element(self.ElementCss["编辑"]).click()
        time.sleep(2)
        if self.TestData["源端口"] != "":
            # self.find_element(self.ElementCss["源端口"]).clear()
            # time.sleep(1)
            self.find_element(self.ElementCss["源端口"]).send_keys(self.TestData["源端口"])
        elif self.TestData["目的端口"] != "":
            # self.find_element(self.ElementCss["目的端口"]).clear()
            # time.sleep(1)
            self.find_element(self.ElementCss["目的端口"]).send_keys(self.TestData["目的端口"])
        time.sleep(1)
        self.find_element(self.ElementCss["编辑确定"]).click()

    def on_one(self):  # 公用
        user_stat = self.find_element(self.ElementCss["已停用状态"]).text
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

    def off_one(self):  # 公用
        time.sleep(2)
        user_stat = self.find_element(self.ElementCss["已启用状态"]).text
        if user_stat == "已停用":
            return True
        else:
            self.find_element(self.ElementCss["单独停用"]).click()
            time.sleep(2)
            self.web_handler.accept_confirm_msg()
            time.sleep(2)
        time.sleep(2)
        new_stat = self.find_element(self.ElementCss["已停用状态"]).text
        if new_stat == "已停用":
            return True
        else:
            return False

    def delete_one(self):  # 公用
        self.find_element(self.ElementCss["删除"]).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        return True

    def on_all(self): #公用
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

    def off_all(self):  # 公用
        self.find_element(self.ElementCss["全部选择"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["全部停用"]).click()
        self.web_handler.accept_confirm_msg()
        time.sleep(2)
        self.web_handler.refresh_page()
        time.sleep(2)
        new_stat = self.find_element(self.ElementCss["已停用状态"]).text
        if new_stat == "已停用":
            return True
        else:
            return False

    def delete_all(self):  # 公用
        time.sleep(2)
        self.find_element(self.ElementCss["全部选择"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["全部删除"]).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        time.sleep(1)

    def check_tcp(self):  # 验证协议为TCP时的功能
        dip = self.TestData["DIP"]
        dport = self.TestData["目的端口"]
        wan = self.TestData["线路"]
        self.ssh_handler.exec_cmd("conntrack -F")
        time.sleep(1)
        if dip != '' and dport != '':
            self.web_handler.open_webpage(dip + ":" + dport)
            time.sleep(1)
            output = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack |grep dst=" + dip + " |grep dport=" + dport)
        else:
            if dport != '':
                time.sleep(1)
                self.web_handler.open_webpage("192.168.1.253:" + dport)
                output = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack |grep dst=192.168.1.253 |grep dport=" + dport)
            else:
                time.sleep(1)
                self.web_handler.open_webpage("192.168.1.253:80")
                output = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack |grep dst=192.168.1.253 |grep dport=80")
        tcp_num = output.count("tcp")
        wan_num = output.count("remote_if=" + wan)
        # self.web_handler.close_webpage(handler)
        if tcp_num == wan_num:
            self.fun_bool = True
            return self.check_function()
        else:
            self.fun_bool = False
            return self.check_function()

    def check_udp(self):  # 验证协议为TCP时的功能
        dip = self.TestData["DIP"]
        dport = self.TestData["目的端口"]
        wan = self.TestData["线路"]
        self.ssh_handler.exec_cmd("conntrack -F")
        time.sleep(1)
        if dip != '' and dport != '':
            UC.udp_client(dip, int(dport))
            time.sleep(1)
            output = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack |grep dst=" + dip + " |grep dport=" + dport)
        else:
            if dport != '':
                time.sleep(1)
                UC.udp_client("192.168.1.253", int(dport))
                output = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack |grep dst=192.168.1.253 |grep dport=" + dport)
            else:
                time.sleep(1)
                UC.udp_client("192.168.1.253", 6000)
                output = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack |grep dst=192.168.1.253 |grep dport=80")
        tcp_num = output.count("udp")
        wan_num = output.count("remote_if=" + wan)
        if tcp_num == wan_num:
            self.fun_bool = True
            return self.check_function()
        else:
            self.fun_bool = False
            return self.check_function()

    def check_icmp(self):
        dip = self.TestData["DIP"]
        wan = self.TestData["线路"]
        self.ssh_handler.exec_cmd("conntrack -F")
        time.sleep(1)
        if dip != '':
            PA.ping(dip)
            time.sleep(3)
            output = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack |grep icmp |grep dst=" + dip)
        else:
            PA.ping("8.8.8.8")
            time.sleep(3)
            output = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack |grep dst=8.8.8.8 |grep icmp")
        # print(output)
        tcp_num = output.count("icmp")
        wan_num = output.count("remote_if=" + wan)
        # print(tcp_num, wan_num)
        if tcp_num == wan_num:
            self.fun_bool = True
            return self.check_function()
        else:
            self.fun_bool = False
            return self.check_function()

    def check_add(self):
        if self.add_bool and self.TestData["预期结果"] == "添加成功" or "分流成功" or "分流失败":
            return True
        elif not self.fun_bool and self.TestData["预期结果"] == "添加失败":
            return True
        else:
            return False

    def check_function(self):
        if self.fun_bool and self.TestData["预期结果"] == "分流成功":
            return True
        elif not self.fun_bool and self.TestData["预期结果"] == "分流失败":
            return True
        else:
            return False

