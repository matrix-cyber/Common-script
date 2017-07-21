import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
import TestBase.DataBase as TD
import time
import TestBase.ActionBase.Base_Action.Public_Action as PA
import TestBase.ActionBase.Base_Action.SSH_Action as SHA


class M3_3_DnsSettings:
    #初始化：（1）将WEB句柄交给此模块  （2）导入该模块的CSS元素库及测试数据
    def __init__(self, web_handler,ssh_handler,TestData): #模块初始化
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu #目录元素库
        self.ElementCss = CSS.ElementBase.DnsSettings #模块元素库
        self.TestData = TestData #测试数据
        self.DHCP_TestData = TD.TestData.DhcpSettings
        self.bool = True

    # 封装查找命令
    def find_element(self, para): #公用
        return self.web_handler.find_element_by_css_selector(para)

    def EDIT_DNS(self):
        time.sleep(2)
        self.find_element(self.ElementCss["首选DNS"]).clear()
        self.find_element(self.ElementCss["首选DNS"]).send_keys(self.TestData["首选DNS"])
        time.sleep(1)
        self.find_element(self.ElementCss["备选DNS"]).clear()
        self.find_element(self.ElementCss["备选DNS"]).send_keys(self.TestData["备选DNS"])
        time.sleep(2)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        try:
            self.find_element(self.ElementCss["保存确定"]).click()
            time.sleep(1)
        except:
            time.sleep(1)

    def ON_DnsQuick(self):
        stat = self.find_element(self.ElementCss["DNS加速服务"]).get_attribute("checked")
        if stat == None:
            self.find_element(self.ElementCss["DNS加速服务"]).click()
            time.sleep(2)
            self.find_element(self.ElementCss["全局保存"]).click()
            time.sleep(1)
            self.find_element(self.ElementCss["保存确定"]).click()
            time.sleep(1)

    def OFF_DnsQuick(self):
        stat = self.find_element(self.ElementCss["DNS加速服务"]).get_attribute("checked")
        if stat != None:
            self.find_element(self.ElementCss["DNS加速服务"]).click()
            time.sleep(2)
            self.find_element(self.ElementCss["全局保存"]).click()
            time.sleep(1)
            self.find_element(self.ElementCss["保存确定"]).click()
            time.sleep(1)

    def OPEN_CacheMode(self):
        self.find_element(self.ElementCss["DNS加速模式"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["缓存模式"]).click()
        time.sleep(1)
        time.sleep(2)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(1)

    def OPEN_AgentMode(self):
        time.sleep(2)
        self.find_element(self.ElementCss["DNS加速模式"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["代理模式"]).click()
        time.sleep(1)
        time.sleep(2)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(1)

    def ON_ForceAgent(self):
        stat = self.find_element(self.ElementCss["强制代理"]).get_attribute("checked")
        if stat == None:
            self.find_element(self.ElementCss["强制代理"]).click()
            self.find_element(self.ElementCss["全局保存"]).click()
            time.sleep(1)
            self.find_element(self.ElementCss["保存确定"]).click()
            time.sleep(1)

    def OFF_ForceAgent(self):
        stat = self.find_element(self.ElementCss["强制代理"]).get_attribute("checked")
        if stat != None:
            self.find_element(self.ElementCss["强制代理"]).click()
            time.sleep(2)
            self.find_element(self.ElementCss["全局保存"]).click()
            time.sleep(1)
            self.find_element(self.ElementCss["保存确定"]).click()
            time.sleep(1)

    def Check_EditDns(self):
        self.web_handler.refresh_page()
        time.sleep(2)
        MainDNS = self.find_element(self.ElementCss["首选DNS"]).get_attribute("value")
        SecondaryDNS = self.find_element(self.ElementCss["备选DNS"]).get_attribute("value")
        print("\t首选DNS：", MainDNS)
        print("\t备选DNS：", SecondaryDNS)
        if MainDNS == self.TestData["首选DNS"] and self.TestData["预期结果"] == "解析成功" or "解析失败":
            return True
        elif MainDNS != self.TestData["首选DNS"] and self.TestData["预期结果"] == "修改失败":
            return True
        else:
            return False

    def Check_DnsFunction(self):
        time.sleep(2)
        DnsLookup = PA.nslookup("www.jd.com")
        # print(DnsLookup)
        time.sleep(5)
        if not DnsLookup and self.TestData["预期结果"] == "解析失败":
            return True
        elif DnsLookup and self.TestData["预期结果"] == "解析成功":
            return True
        else:
            return False

    def Get_NFconntrack(self):
        self.ssh_handler.exec_cmd("conntrack -F")
        time.sleep(2)
        PA.ping("www.jd.com",5)
        time.sleep(1)
        cmd = "cat /proc/net/nf_conntrack | grep udp | grep dport=53"
        output = self.ssh_handler.exec_cmd(cmd)
        newput = SHA.IkSSHUtils.GetNF_Conntrack(output)
        return newput

    def Check_DnsAdress(self,newput,DNSstr):
        newput_len = len(newput)
        # print("找到连接跟踪列表个数：", newput_len)
        # print(newput)
        num = 0
        for i in range(0,newput_len):
            str_dict = newput[i]
            if str_dict["src"] == DNSstr:
                num = num + 1
            elif str_dict["dst"] == DNSstr:
                num = num + 1
            else:
                continue
        # print("找到DNS个数：", num)
        return num

    def Check_MDNS(self,newput):
        num = self.Check_DnsAdress(newput, self.TestData["首选DNS"])
        if num>0:
            return True
        else:
            return False

    def Check_SDNS(self,newput):
        num = self.Check_DnsAdress(newput, self.TestData["备选DNS"])
        if num > 0:
            return True
        else:
            return False



