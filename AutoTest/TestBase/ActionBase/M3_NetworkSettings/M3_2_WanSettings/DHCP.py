import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
import TestBase.DataBase as TD
import time
import TestBase.ActionBase.Base_Action.SSH_Action as SA
import TestBase.ActionBase.Base_Action.Public_Action as PA
import TestBase.ActionBase.Base_Action.Web_Action as WA
import TestBase.TopoBase as Topo

class DHCP:
    #初始化：（1）将WEB句柄交给此模块  （2）导入该模块的CSS元素库及测试数据
    def __init__(self, web_handler,ssh_handler,TestData): #模块初始化
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu #目录元素库
        self.ElementCss = CSS.ElementBase.DHCP #模块元素库
        self.DNS_Element = CSS.ElementBase.DnsSettings
        self.TestData = TestData #测试数据
        self.DHCP_Gateway = ""
        self.bool = True

    # 封装查找命令
    def find_element(self, para): #公用
        return self.web_handler.find_element_by_css_selector(para)

    def ADD(self):
        time.sleep(2)
        self.find_element(self.ElementCss["上行带宽"]).clear()
        self.find_element(self.ElementCss["上行带宽"]).send_keys(self.TestData["上行带宽"])
        self.find_element(self.ElementCss["下行带宽"]).clear()
        self.find_element(self.ElementCss["下行带宽"]).send_keys(self.TestData["下行带宽"])
        stat = self.find_element(self.ElementCss["默认网关"]).get_attribute("checked")
        if stat == None:
            self.find_element(self.ElementCss["默认网关"]).click()
        DNS_stat = self.find_element(self.ElementCss["添加DNS"]).get_attribute("checked")
        if DNS_stat == None:
            self.find_element(self.ElementCss["添加DNS"]).click()
        self.find_element(self.ElementCss["线路检测选项"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["线路检测HTTP"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["线路检测地址"]).clear()
        time.sleep(1)
        self.find_element(self.ElementCss["线路检测地址"]).send_keys(self.TestData["线路检测地址"])
        time.sleep(2)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        try:
            self.find_element(self.ElementCss["保存确定"]).click()
            time.sleep(1)
        except:
            time.sleep(1)
        try:
            self.find_element(self.ElementCss["连接"]).click()
            time.sleep(2)
        except:
            time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        time.sleep(2)
        try:
            self.find_element(self.ElementCss["上行填写错误"])
            self.bool = False
            return self.Check_Add()
        except:
            self.bool = True
            return self.Check_Add()

    def EDIT_LinkSwitch(self):
        self.find_element(self.ElementCss["掉线切换"]).click()
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(2)
        self.web_handler.refresh_page()
        time.sleep(2)

    def OFF_UPDUT_WAN(self):
        login = TD.TestData.Login[0]
        host = Topo.DUT_UPLink_Device2
        self.web_handler = WA.Web_Action(url="http://" + host, user=login["用户名"], pwd=login["密码"])
        self.web_handler.connect()

    def EDIT_SwitchDefaultRoute(self):
        time.sleep(2)
        self.find_element(self.ElementCss["WAN1"]).click()
        time.sleep(4)
        self.find_element(self.ElementCss["WAN1默认网关"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["WAN1保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(2)


    def Check_Add(self): #公用
        if not self.bool and (self.TestData["预期结果"] == "添加失败"):
            return True
        elif self.bool and self.TestData["预期结果"] == "连接成功":
            return True
        else:
            return False

    def Check_Link(self):
        DHCP_IP = self.find_element(self.ElementCss["获取IP"]).get_attribute("value")
        self.DHCP_Gateway = self.find_element(self.ElementCss["网关"]).get_attribute("value")
        print("\t获取IP：",DHCP_IP)
        if DHCP_IP != "" and PA.ping("www.jd.com"):
            return True
        else:
            return False

    def Check_DefaultRoute(self):
        output = self.ssh_handler.exec_cmd("route -n")
        Route = SA.IkSSHUtils.GetRoute(output)
        print("\t默认网关：",Route["Gateway"])
        if self.DHCP_Gateway != Route["Gateway"]:
            return False
        else:
            return True

    def OFF_AutoDNS(self):
        AutoDNS_stat = self.find_element(self.ElementCss["添加DNS"]).get_attribute("checked")
        if AutoDNS_stat != None:
            self.find_element(self.ElementCss["添加DNS"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(2)

    def Edit_RouteDNS(self):
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

    def EDIT_UpDownLink(self):
        self.find_element(self.ElementCss["断开"]).click()
        time.sleep(10)
        self.find_element(self.ElementCss["连接"]).click()
        time.sleep(10)
        self.web_handler.refresh_page()
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
        if Main_DNS == Topo.DHCP_Mdns and Secondary_DNS == Topo.DHCP_Sdns:
            return True
        else:
            return False





