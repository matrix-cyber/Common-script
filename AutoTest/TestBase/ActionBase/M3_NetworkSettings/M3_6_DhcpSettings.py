import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
import time


class M3_6_DhcpSettings:
    #初始化：（1）将WEB句柄交给此模块  （2）导入该模块的CSS元素库及测试数据
    def __init__(self, web_handler,ssh_handler,TestData): #模块初始化
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu #目录元素库
        self.ElementCss = CSS.ElementBase.DhcpSettings #模块元素库
        self.TestData = TestData #测试数据
        self.bool = True

    # 封装查找命令
    def find_element(self, para): #公用
        return self.web_handler.find_element_by_css_selector(para)

    # def ADD(self):
    #     time.sleep(2)
    #     self.find_element(self.ElementCss["账号"]).clear()
    #     self.find_element(self.ElementCss["账号"]).send_keys(self.TestData["账号"])
    #     self.find_element(self.ElementCss["密码"]).clear()
    #     self.find_element(self.ElementCss["密码"]).send_keys(self.TestData["密码"])
    #     self.find_element(self.ElementCss["上行带宽"]).clear()
    #     self.find_element(self.ElementCss["上行带宽"]).send_keys(self.TestData["上行带宽"])
    #     self.find_element(self.ElementCss["下行带宽"]).clear()
    #     self.find_element(self.ElementCss["下行带宽"]).send_keys(self.TestData["下行带宽"])
    #     self.find_element(self.ElementCss["服务器名"]).clear()
    #     self.find_element(self.ElementCss["服务器名"]).send_keys(self.TestData["服务器名"])
    #     gateway_stat = self.find_element(self.ElementCss["默认网关"]).get_attribute("checked")
    #     if gateway_stat == None:
    #         self.find_element(self.ElementCss["默认网关"]).click()
    #     DNS_stat = self.find_element(self.ElementCss["添加DNS"]).get_attribute("checked")
    #     if DNS_stat == None:
    #         self.find_element(self.ElementCss["添加DNS"]).click()
    #     TimeRst_stat = self.find_element(self.ElementCss["定时重拨"]).get_attribute("checked")
    #     if TimeRst_stat == None:
    #         self.find_element(self.ElementCss["定时重拨"]).click()
    #     time.sleep(1)
    #     self.find_element(self.ElementCss["定时1"]).clear()
    #     self.find_element(self.ElementCss["定时1"]).send_keys(self.TestData["定时1"])
    #     self.find_element(self.ElementCss["定时2"]).clear()
    #     self.find_element(self.ElementCss["定时2"]).send_keys(self.TestData["定时2"])
    #     self.find_element(self.ElementCss["定时3"]).clear()
    #     self.find_element(self.ElementCss["定时3"]).send_keys(self.TestData["定时3"])
    #     cyctime_stat = self.find_element(self.ElementCss["间隔时长重拨"]).get_attribute("checked")
    #     if cyctime_stat == None:
    #         self.find_element(self.ElementCss["间隔时长重拨"]).click()
    #     time.sleep(1)
    #     self.find_element(self.ElementCss["间隔时长"]).clear()
    #     self.find_element(self.ElementCss["间隔时长"]).send_keys(self.TestData["间隔时长"])
    #     self.find_element(self.ElementCss["线路检测选项"]).click()
    #     time.sleep(1)
    #     self.find_element(self.ElementCss["线路检测PING"]).click()
    #     time.sleep(1)
    #     self.find_element(self.ElementCss["线路检测地址"]).clear()
    #     self.find_element(self.ElementCss["线路检测地址"]).send_keys(self.TestData["线路检测地址"])
    #     time.sleep(2)
    #     self.find_element(self.ElementCss["全局保存"]).click()
    #     time.sleep(2)
    #     try:
    #         self.find_element(self.ElementCss["连接"]).click()
    #         time.sleep(1)
    #     except:
    #         time.sleep(1)
    #     try:
    #         self.find_element(self.ElementCss["保存确定"]).click()
    #         time.sleep(1)
    #     except:
    #         time.sleep(1)
    #     try:
    #         self.find_element(self.ElementCss["密码错误"])
    #         self.bool = False
    #     except:
    #         time.sleep(1)
    #     try:
    #         self.find_element(self.ElementCss["时间错误"])
    #         self.bool = False
    #     except:
    #         time.sleep(1)
    #     try:
    #         self.find_element(self.ElementCss["上行带宽错误"])
    #         self.bool = False
    #     except:
    #         time.sleep(1)
    #     try:
    #         self.find_element(self.ElementCss["下行带宽错误"])
    #         self.bool = False
    #     except:
    #         time.sleep(1)
    #     try:
    #         self.find_element(self.ElementCss["间隔时长错误"])
    #         self.bool = False
    #     except:
    #         time.sleep(1)
    #     return self.Check_Add()

    def EDIT_DNS(self):
        self.find_element(self.MenuCss["DHCP设置"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["编辑"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["主DNS"]).clear()
        self.find_element(self.ElementCss["主DNS"]).send_keys(self.TestData["主DNS"])
        time.sleep(1)
        self.find_element(self.ElementCss["次DNS"]).clear()
        self.find_element(self.ElementCss["次DNS"]).send_keys(self.TestData["次DNS"])
        self.find_element(self.ElementCss["确定"]).click()
        time.sleep(2)

    #
    # def Check_Add(self): #公用
    #     # print(self.bool)
    #     # print(self.TestData["预期结果"])
    #     if not self.bool and (self.TestData["预期结果"] == "添加失败"):
    #         return True
    #     elif self.bool and self.TestData["预期结果"] == "认证成功"or"认证失败":
    #         return True
    #     else:
    #         return False

    def Check_DNS(self):
        self.web_handler.refresh_page()
        time.sleep(2)
        MainDNS = self.find_element(self.ElementCss["获取主DNS"]).get_attribute("title")
        print("\t 主DNS：", MainDNS)
        print("\t 次DNS：", self.TestData["次DNS"])
        if MainDNS == self.TestData["主DNS"] and self.TestData["预期结果"] == "修改成功":
            return True
        else:
            return False