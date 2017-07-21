import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
import time
import TestBase.TopoBase as Topo
import datetime

class ADSL_by_Vlan:
    #初始化：（1）将WEB句柄交给此模块  （2）导入该模块的CSS元素库及测试数据
    def __init__(self, web_handler,ssh_handler,TestData): #模块初始化
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu #目录元素库
        self.ElementCss = CSS.ElementBase.Adsl_by_Vlan #模块元素库
        self.DNS_Element = CSS.ElementBase.DnsSettings
        self.TestData = TestData #测试数据
        self.bool = True
        self.ADSL_IP = "0.0.0.0"

    # 封装查找命令
    def find_element(self, para): #公用
        return self.web_handler.find_element_by_css_selector(para)

    def ADD(self):
        time.sleep(2)
        self.find_element(self.ElementCss["添加"]).click()
        time.sleep(3)
        self.find_element(self.ElementCss["VLAN_ID"]).send_keys(self.TestData["VLAN_ID"])
        self.find_element(self.ElementCss["拨号名称"]).send_keys(self.TestData["拨号名称"])
        self.find_element(self.ElementCss["PPPOE账号"]).send_keys(self.TestData["PPPOE账号"])
        self.find_element(self.ElementCss["PPPOE密码"]).send_keys(self.TestData["PPPOE密码"])
        self.find_element(self.ElementCss["MAC"]).clear()
        self.find_element(self.ElementCss["MAC"]).send_keys(self.TestData["MAC"])
        self.find_element(self.ElementCss["上行"]).send_keys(self.TestData["上行"])
        self.find_element(self.ElementCss["下行"]).send_keys(self.TestData["下行"])
        self.find_element(self.ElementCss["默认网关"]).click()
        self.find_element(self.ElementCss["添加DNS"]).click()
        self.find_element(self.ElementCss["服务器名"]).send_keys(self.TestData["服务器名"])
        self.find_element(self.ElementCss["定时重拨"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["定时1"]).send_keys(self.TestData["定时1"])
        self.find_element(self.ElementCss["定时2"]).send_keys(self.TestData["定时2"])
        self.find_element(self.ElementCss["定时3"]).send_keys(self.TestData["定时3"])
        self.find_element(self.ElementCss["间隔时长重拨"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["间隔时长"]).send_keys(self.TestData["间隔时长"])
        self.find_element(self.ElementCss["线路检测选项"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["线路检测PING"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["线路检测地址"]).clear()
        self.find_element(self.ElementCss["线路检测地址"]).send_keys(self.TestData["线路检测地址"])
        time.sleep(2)
        self.find_element(self.ElementCss["配置确认"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(2)
        try:
            self.web_handler.accept_confirm_msg()
        except:
            time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        try:
            self.find_element(self.ElementCss["VLAN_ID"])
            self.bool = True
            return self.Check_Add()
        except:
            self.bool = False
            return self.Check_Add()

    def EDIT_ServerName(self):
        self.find_element(self.ElementCss["编辑"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["服务器名"]).clear()
        self.find_element(self.ElementCss["服务器名"]).send_keys("temp")
        time.sleep(2)
        self.find_element(self.ElementCss["配置确认"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(2)

    def EDIT_DefaultRoute(self):
        self.find_element(self.ElementCss["WAN1"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["WAN1默认网关"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["WAN1保存"]).click()
        time.sleep(2)

    def EDIT_TimedRedial(self):
        self.find_element(self.ElementCss["编辑"]).click()
        time.sleep(2)
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
        self.find_element(self.ElementCss["配置确认"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(140)


    def ON_one(self): #公用
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

    def OFF_one(self): #公用
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

    def DELETE_one(self): #公用
        self.find_element(self.ElementCss["删除"]).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        try:
            self.find_element(self.ElementCss["编辑用户名"])
            return False
        except:
            return True

    def ON_all(self): #公用
        self.find_element(self.ElementCss["全部选中"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["全部启用"]).click()
        self.web_handler.refresh_page()
        time.sleep(2)
        new_stat = self.find_element(self.ElementCss["启停用状态"]).text
        if new_stat == "已启用":
            return True
        else:
            return False

    def OFF_all(self): #公用
        self.find_element(self.ElementCss["全部选中"]).click()
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

    def DELETE_all(self): #公用
        self.find_element(self.ElementCss["全部选中"]).click()
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

    def Check_Add(self): #公用
        if not self.bool and (self.TestData["预期结果"] == "添加失败"):
            return True
        elif self.bool and self.TestData["预期结果"] == "认证成功"or"认证失败":
            return True
        else:
            print("拨号信息：", self.TestData)
            return False

    def OFF_AutoDNS(self):  # 关闭自动添加DNS功能
        self.find_element(self.ElementCss["编辑"]).click()
        time.sleep(2)
        AutoDNS_stat = self.find_element(self.ElementCss["添加DNS"]).get_attribute("checked")
        if AutoDNS_stat != None:
            self.find_element(self.ElementCss["添加DNS"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["配置确认"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(2)

    def Edit_RouteDNS(self):  # 编辑路由的DNS设置
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

    def Check_RouteDNS(self):
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

    def Check_Auth(self):
        time.sleep(10)
        self.web_handler.refresh_page()
        time.sleep(2)
        try:
            self.ADSL_IP = self.find_element(self.ElementCss["获取IP"]).get_attribute("value")
            if self.ADSL_IP != "" and self.TestData["预期结果"] == "认证成功":
                # print("\t认证IP：", self.ADSL_IP)
                return True
            elif self.ADSL_IP == "" and self.TestData["预期结果"] == "认证失败":
                return True
            else:
                return False
        except:
            if self.TestData["预期结果"] == "添加失败":
                return True
            else:
                return False
