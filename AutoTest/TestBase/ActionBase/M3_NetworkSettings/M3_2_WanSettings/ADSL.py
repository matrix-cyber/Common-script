import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
import TestBase.TopoBase as Topo
import datetime
import time

class ADSL:
    #初始化：（1）将WEB句柄交给此模块  （2）导入该模块的CSS元素库及测试数据
    def __init__(self, web_handler,ssh_handler,TestData): #模块初始化
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu #目录元素库
        self.ElementCss = CSS.ElementBase.ADSL #模块元素库
        self.DNS_Element = CSS.ElementBase.DnsSettings
        self.TestData = TestData #测试数据
        self.bool = True
        self.ADSL_IP = "0.0.0.0"

    # 封装查找命令
    def find_element(self, para): #公用
        return self.web_handler.find_element_by_css_selector(para)

    def ADD(self):#添加
        time.sleep(2)
        self.find_element(self.ElementCss["账号"]).clear()
        self.find_element(self.ElementCss["账号"]).send_keys(self.TestData["账号"])
        self.find_element(self.ElementCss["密码"]).clear()
        self.find_element(self.ElementCss["密码"]).send_keys(self.TestData["密码"])
        self.find_element(self.ElementCss["上行带宽"]).clear()
        self.find_element(self.ElementCss["上行带宽"]).send_keys(self.TestData["上行带宽"])
        self.find_element(self.ElementCss["下行带宽"]).clear()
        self.find_element(self.ElementCss["下行带宽"]).send_keys(self.TestData["下行带宽"])
        self.find_element(self.ElementCss["服务器名"]).clear()
        self.find_element(self.ElementCss["服务器名"]).send_keys(self.TestData["服务器名"])
        gateway_stat = self.find_element(self.ElementCss["默认网关"]).get_attribute("checked")
        if gateway_stat == None:
            self.find_element(self.ElementCss["默认网关"]).click()
        DNS_stat = self.find_element(self.ElementCss["添加DNS"]).get_attribute("checked")
        if DNS_stat == None:
            self.find_element(self.ElementCss["添加DNS"]).click()
        TimeRst_stat = self.find_element(self.ElementCss["定时重拨"]).get_attribute("checked")
        if TimeRst_stat == None:
            self.find_element(self.ElementCss["定时重拨"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["定时1"]).clear()
        self.find_element(self.ElementCss["定时1"]).send_keys(self.TestData["定时1"])
        self.find_element(self.ElementCss["定时2"]).clear()
        self.find_element(self.ElementCss["定时2"]).send_keys(self.TestData["定时2"])
        self.find_element(self.ElementCss["定时3"]).clear()
        self.find_element(self.ElementCss["定时3"]).send_keys(self.TestData["定时3"])
        cyctime_stat = self.find_element(self.ElementCss["间隔时长重拨"]).get_attribute("checked")
        if cyctime_stat == None:
            self.find_element(self.ElementCss["间隔时长重拨"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["间隔时长"]).clear()
        self.find_element(self.ElementCss["间隔时长"]).send_keys(self.TestData["间隔时长"])
        self.find_element(self.ElementCss["线路检测选项"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["线路检测PING"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["线路检测地址"]).clear()
        self.find_element(self.ElementCss["线路检测地址"]).send_keys(self.TestData["线路检测地址"])
        time.sleep(2)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        try:
            self.find_element(self.ElementCss["连接"]).click()
            time.sleep(1)
        except:
            time.sleep(1)
        try:
            self.find_element(self.ElementCss["保存确定"]).click()
            time.sleep(1)
        except:
            time.sleep(1)
        try:
            self.find_element(self.ElementCss["密码错误"])
            self.bool = False
        except:
            time.sleep(1)
        try:
            self.find_element(self.ElementCss["时间错误"])
            self.bool = False
        except:
            time.sleep(1)
        try:
            self.find_element(self.ElementCss["上行带宽错误"])
            self.bool = False
        except:
            time.sleep(1)
        try:
            self.find_element(self.ElementCss["下行带宽错误"])
            self.bool = False
        except:
            time.sleep(1)
        try:
            self.find_element(self.ElementCss["间隔时长错误"])
            self.bool = False
        except:
            time.sleep(1)
        return self.Check_Add()

    def EDIT_ServerName(self): #编辑服务器名
        self.find_element(self.ElementCss["服务器名"]).clear()
        self.find_element(self.ElementCss["服务器名"]).send_keys("temp")
        time.sleep(2)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(2)

    def Edit_RouteDNS(self): #编辑路由的DNS设置
        # 从当前WAN2跳转到DNS设置页面
        self.find_element(self.MenuCss["DNS设置"]).click()
        time.sleep(2)
        self.find_element(self.DNS_Element["首选DNS"]).clear()
        self.find_element(self.DNS_Element["首选DNS"]).send_keys("1.2.3.4")
        self.find_element(self.DNS_Element["备选DNS"]).clear()
        self.find_element(self.DNS_Element["备选DNS"]).send_keys("2.3.4.5")
        self.find_element(self.DNS_Element["全局保存"]).click()
        time.sleep(1)
        self.find_element(self.DNS_Element["保存确定"]).click()
        time.sleep(2)
        Main_DNS = self.find_element(self.DNS_Element["首选DNS"]).get_attribute("value")
        Secondary_DNS = self.find_element(self.DNS_Element["备选DNS"]).get_attribute("value")
        print("\t首选DNS_old：", Main_DNS)
        print("\t备选DNS_old：", Secondary_DNS)
        self.find_element(self.MenuCss["外网设置"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["WAN2"]).click()
        time.sleep(2)

    def EDIT_DefaultRoute(self): #开启WAN1的默认路由
        self.find_element(self.ElementCss["WAN1"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["WAN1默认网关"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["WAN1保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(2)

    def EDIT_TimedRedial(self): #编辑定时重拨
        self.find_element(self.ElementCss["定时1"]).clear()
        time.sleep(1)
        old_time = datetime.datetime.now()
        hour = old_time.strftime("%H")
        minute = old_time.strftime("%M")
        new_minute = int(minute) + 2
        if int(hour) < 10 and new_minute < 10:
            set_time = "0"+hour + ":0" + str(new_minute)
        elif int(hour) < 10:
            set_time ="0"+ hour + ":" + str(new_minute)
        elif new_minute < 10:
            set_time = hour + ":0" + str(new_minute)
        else:
            set_time = hour + ":" + str(new_minute)
        self.find_element(self.ElementCss["定时1"]).send_keys(set_time)
        time.sleep(2)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(140)

    def EDIT_UpDownLink(self): # 断开重连接
        self.find_element(self.ElementCss["断开"]).click()
        time.sleep(10)
        self.find_element(self.ElementCss["连接"]).click()
        time.sleep(10)
        self.web_handler.refresh_page()
        time.sleep(2)

    def OFF_AutoDNS(self): #关闭自动添加DNS功能
        AutoDNS_stat = self.find_element(self.ElementCss["添加DNS"]).get_attribute("checked")
        if AutoDNS_stat != None:
            self.find_element(self.ElementCss["添加DNS"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(2)

    def Check_Add(self): #公用
        # print(self.bool)
        # print(self.TestData["预期结果"])
        if not self.bool and (self.TestData["预期结果"] == "添加失败"):
            return True
        elif self.bool and self.TestData["预期结果"] == "认证成功"or"认证失败":
            return True
        else:
            return False

    def Check_Auth(self): #检测认证是否成功
        time.sleep(10)
        self.web_handler.refresh_page()
        time.sleep(10)
        self.ADSL_IP = self.find_element(self.ElementCss["获取IP"]).get_attribute("value")
        # print("\t认证IP：", self.ADSL_IP)
        if self.ADSL_IP != "" and self.TestData["预期结果"] == "认证成功":
            return True
        elif self.ADSL_IP == "" and self.TestData["预期结果"] == "认证失败":
            return True
        else:
            return False

    def Check_RouteDNS(self): #检测路由的DNS信息
        self.find_element(self.MenuCss["DNS设置"]).click()
        time.sleep(2)
        Main_DNS = self.find_element(self.DNS_Element["首选DNS"]).get_attribute("value")
        Secondary_DNS = self.find_element(self.DNS_Element["备选DNS"]).get_attribute("value")
        print("\t首选DNS_new：", Main_DNS)
        print("\t备选DNS_new：", Secondary_DNS)
        # 从DNS设置页面再跳回外网设置的WAN2页面
        self.find_element(self.MenuCss["外网设置"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["WAN2"]).click()
        time.sleep(2)
        if Main_DNS == Topo.PPPOE_Mdns and Secondary_DNS == Topo.PPPOE_Sdns:
            return True
        else:
            return False