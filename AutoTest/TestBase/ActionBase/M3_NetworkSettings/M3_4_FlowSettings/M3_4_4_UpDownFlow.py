import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
import time
import os
import TestBase.ActionBase.Base_Action.Public_Action as PA
import TestBase.TopoBase as Topo


class UpDownFlow:
    def __init__(self, web_handler,ssh_handler,TestData): #模块初始化
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu #目录元素库
        self.ElementCss = CSS.ElementBase.UpDownFlow #模块元素库
        self.TestData = TestData #测试数据
        self.bool = True
        self.fun_bool = True

    # 封装查找命令
    def find_element(self, para): #公用
        return self.web_handler.find_element_by_css_selector(para)

    def add(self):
        time.sleep(3)
        self.find_element(self.ElementCss["添加"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["协议"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss[self.TestData["协议"]]).click()
        time.sleep(3)
        self.find_element(self.ElementCss["上行线路"]).click()
        time.sleep(2)
        try:
            self.find_element(self.ElementCss[self.TestData["上行线路"]]).click()
            pass
        except:
            pass
        time.sleep(2)
        self.find_element(self.ElementCss["线路确定"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["下行线路"]).click()
        time.sleep(2)
        try:
            self.find_element(self.ElementCss[self.TestData["下行线路"]]).click()
            pass
        except:
            pass
        time.sleep(2)
        self.find_element(self.ElementCss["线路确定"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["源地址"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["IP"]).clear()
        time.sleep(2)
        if self.TestData["SIP"] == "localhost":
            test_sip = Topo.TEST_PC
        else:
            test_sip = self.TestData["SIP"]
        self.find_element(self.ElementCss["IP"]).send_keys(test_sip)
        time.sleep(2)
        self.find_element(self.ElementCss["添加IP"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["确定IP"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["目的地址"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["IP"]).clear()
        time.sleep(2)
        self.find_element(self.ElementCss["IP"]).send_keys(self.TestData["DIP"])
        time.sleep(2)
        self.find_element(self.ElementCss["添加IP"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["确定IP"]).click()

        self.find_element(self.ElementCss["源端口"]).send_keys(self.TestData["SPORT"])
        self.find_element(self.ElementCss["目的端口"]).send_keys(self.TestData["DPORT"])
        self.find_element(self.ElementCss["备注"]).send_keys(self.TestData["备注"])
        time.sleep(2)
        self.find_element(self.ElementCss["确定"]).click()
        try:
            self.find_element(self.ElementCss["源端口错误"])
            self.bool = False
            return self.check_add()
        except:
            pass
        try:
            self.find_element(self.ElementCss["目的端口错误"])
            self.bool = False
            return self.check_add()
        except:
            pass
        try:
            self.find_element(self.ElementCss["上行线路错误"])
            self.bool = False
            return self.check_add()
        except:
            pass
        try:
            self.find_element(self.ElementCss["下行线路错误"])
            self.bool = False
            return self.check_add()
        except:
            pass
        try:
            self.find_element(self.ElementCss["备注错误"])
            self.bool = False
            return self.check_add()
        except:
            pass
        return self.check_add()

    def delete_all(self):#删除全部上下行策略
        time.sleep(2)
        self.find_element(self.ElementCss["全选按钮"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["全选删除"]).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        return True

    def del_one(self):#删除第一个上下行策略
        time.sleep(2)
        self.find_element(self.ElementCss["单机删除"]).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        return True

    def off_one(self):#关闭地址一个上下行策略
        time.sleep(2)
        self.find_element(self.ElementCss["单机停用"]).click()
        time.sleep(2)
        self.web_handler.accept_confirm_msg()
        return True

    def off_all(self):#关闭全部上下行策略
        time.sleep(2)
        self.find_element(self.ElementCss["全选按钮"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["全选停用"]).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        return True

    def on_one(self):#打开第一个上下行策略
        time.sleep(2)
        self.find_element(self.ElementCss["单机启用"]).click()
        return True

    def on_all(self):#打开全部上下行策略
        time.sleep(2)
        self.find_element(self.ElementCss["全选按钮"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["全选启用"]).click()
        return True

    def edit_pro(self):#编辑修改协议是tcp 源是测试机器ip 目标为空 源端口为空 目的端口是80
        time.sleep(1)
        self.find_element(self.ElementCss["单机编辑"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["协议"]).click()
        time.sleep(1)
        pro = self.TestData["协议"]
        self.find_element(self.ElementCss[pro]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["确定"]).click()
        return True

    def edit_sip(self):
        time.sleep(2)
        self.find_element(self.ElementCss["单机编辑"]).click()
        self.find_element(self.ElementCss["源地址"]).click()
        while (1):
            time.sleep(2)
            try:
                self.find_element(self.ElementCss["删除IP"]).click()
                self.find_element(self.ElementCss["删除IP按钮"]).click()
            except:
                break
        # self.find_element(self.ElementCss["IP"]).clear()
        # self.find_element(self.ElementCss["IP"]).send_keys(Topo.TEST_PC)
        time.sleep(2)
        self.find_element(self.ElementCss["IP"]).send_keys(self.TestData["EDIT_SIP"])
        time.sleep(2)
        self.find_element(self.ElementCss["添加IP"]).click()
        self.find_element(self.ElementCss["确定IP"]).click()
        self.find_element(self.ElementCss["确定"]).click()
        return True

    def edit_dip(self):
        time.sleep(2)
        self.find_element(self.ElementCss["单机编辑"]).click()
        self.find_element(self.ElementCss["目的地址"]).click()
        while (1):
            time.sleep(2)
            try:
                self.find_element(self.ElementCss["删除IP"]).click()
                self.find_element(self.ElementCss["删除IP按钮"]).click()
            except:
                break
        time.sleep(2)
        self.find_element(self.ElementCss["IP"]).clear()
        time.sleep(2)
        self.find_element(self.ElementCss["IP"]).send_keys(self.TestData["EDIT_DIP"])
        time.sleep(2)
        self.find_element(self.ElementCss["添加IP"]).click()
        self.find_element(self.ElementCss["确定IP"]).click()
        self.find_element(self.ElementCss["确定"]).click()
        return True

    def edit_dport(self):
        time.sleep(2)
        self.find_element(self.ElementCss["单机编辑"]).click()

        dport = self.find_element(self.ElementCss["目的端口"])
        dport.clear()
        time.sleep(1)
        dport.send_keys(self.TestData["EDIT_DPORT"])
        self.find_element(self.ElementCss["确定"]).click()
        return True

    def edit_sport(self):
        time.sleep(2)
        self.find_element(self.ElementCss["单机编辑"]).click()
        sport = self.find_element(self.ElementCss["源端口"])
        sport.clear()
        sport.send_keys(self.TestData["EDIT_SPORT"])

        self.find_element(self.ElementCss["确定"]).click()
        return True

    def check_add(self):
        if self.bool and self.TestData["预期结果"] == "添加成功" or "分离成功" or "分离失败":
            return True
        elif not self.bool and self.TestData["预期结果"] == "添加失败":
            return True
        else:
            return False

    def check_add_web(self):  # 这个微博校验只能校验ADD 添加的 编辑之后请勿使用此校验
        time.sleep(2)
        p = self.find_element(self.ElementCss["协议"]).get_attribute("value")
        sip = self.find_element(self.ElementCss["源地址"]).get_attribute("value")
        dip = self.find_element(self.ElementCss["目的地址"]).get_attribute("value")
        comment = self.find_element(self.ElementCss["备注"]).get_attribute("value")
        sport = self.find_element(self.ElementCss["源端口"]).get_attribute("value")
        dport = self.find_element(self.ElementCss["目的端口"]).get_attribute("value")
        if self.TestData["SIP"] == "localhost":
            sip_show = Topo.TEST_PC
        else:
            sip_show = self.TestData["SIP"]
        if sip != sip_show or \
           dip != self.TestData["DIP"] or \
           p != self.TestData["协议"] or \
           comment != self.TestData["备注"] or \
           sport != self.TestData["SPORT"] or \
           dport != self.TestData["DPORT"]:
            print(sip,dip,p,comment,sport,dport)
            return False
        else:
            return True

    def check_tcp(self):#上行为wan1 下行为wan2 协议为tcp 访问ikuai8.com  tcp80端口
        time.sleep(2)
        self.ssh_handler.exec_cmd("conntrack -F")
        url = "www.ikuai8.com"
        self.web_handler.open_webpage(url)
        wan2 = self.ssh_handler.exec_cmd("ip addr | grep wan2 | grep inet | awk  \'{print $2}\'|awk  -F \'/\'  \'{print $1}\'")
        tcp = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack|grep " + Topo.TEST_PC + "| grep -v " + Topo.DUT + "| grep tcp| head -n 1")
        if wan2.strip() in tcp:
            return self.check_function()
        else:
            self.fun_bool = False
            return self.check_function()

    def check_icmp(self):#上行为wan1 下行为wan2 协议为icmp ssh校验ping的是114.114.114.114这个ip地址
        time.sleep(2)
        self.ssh_handler.exec_cmd("conntrack -F")
        PA.ping("114.114.114.114")
        wan2 = self.ssh_handler.exec_cmd("ip addr | grep wan2 | grep inet | awk  \'{print $2}\'|awk  -F \'/\'  \'{print $1}\'")
        icmp = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack|grep "+ Topo.TEST_PC+"| grep icmp | grep \"114.114.114.114\"| head -n 1")
        if wan2.strip() in icmp:
            return self.check_function()
        else:
            self.fun_bool = False
            return self.check_function()

    def check_udp(self):#上行为wan1 下行为wan2 协议udp ping qq baidu hao123 dns解析使用目标端口53
        time.sleep(2)
        self.ssh_handler.exec_cmd("conntrack -F")
        aaa = os.popen("ipconfig /flushdns", "r")
        PA.ping("www.qq.com",1)
        PA.ping("www.baidu.com",1)
        PA.ping("www.hao123.com",1)
        wan2 = self.ssh_handler.exec_cmd("ip addr | grep wan2 | grep inet | awk  \'{print $2}\'|awk  -F \'/\'  \'{print $1}\'")
        udp = self.ssh_handler.exec_cmd("cat /proc/net/nf_conntrack| grep 53|grep " + Topo.TEST_PC + "|grep udp| head -n 1")
        if wan2.strip() in udp:
            return self.check_function()
        else:
            self.fun_bool = False
            return self.check_function()

    def check_function(self):
        if self.fun_bool and self.TestData["预期结果"] == "分离成功":
            return True
        elif not self.fun_bool and self.TestData["预期结果"] == "分离失败":
            return True
        else:
            return False


