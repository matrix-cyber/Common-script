# 只接一个X1 AP
import sys
sys.path.append("..")
# import TestCase.M3_NetworkSettings.M3_4_FlowSettings.M3_4_2_ProtocolFlow as MPRF
import TestCase.M3_NetworkSettings.M3_4_FlowSettings.M3_4_1_PortFlow as MPF
import TestBase.ActionBase.Base_Action.Result_Action as TR
import TestBase.ElementBase as CSS
import time

class M3_0_Main:
    def __init__(self, web_handler,ssh_handler):
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu

    def run_tests(self):
        # 进入模块
        self.web_handler.find_element_by_css_selector(self.MenuCss["网络设置"]).click()
        time.sleep(2)
        # print("3-1 内网设置：")
        # self.web_handler.find_element_by_css_selector(self.MenuCss["内网设置"]).click()
        # time.sleep(2)
        # print(">>>>>>>>>> 内网设置 <<<<<<<<<")
        # Adsl_Lan = LST.M3_1_LANSettings(self.web_handler)
        # Adsl_Lan.run_tests()
        # print("3-2 外网设置：")
        # self.web_handler.find_element_by_css_selector(self.MenuCss["外网设置"]).click()
        # time.sleep(2)
        # print(">>>>>>>>>> 外网公共 <<<<<<<<<")
        # Adsl_Lan = WAN_Public.WAN_Public(self.web_handler, self.ssh_handler)
        # Adsl_Lan.run_tests()
        # print(">>>>>>>>>> 静态IP <<<<<<<<<")
        # Adsl_Lan = WAN_StaticIP.StaticIP(self.web_handler, self.ssh_handler)
        # Adsl_Lan.run_tests()
        # print(">>>>>>>>>> DHCP/动态IP <<<<<<<<<")
        # Adsl_Lan = WAN_DHCP.DHCP(self.web_handler, self.ssh_handler)
        # Adsl_Lan.run_tests()
        # print(">>>>>>>>>> ADSL/PPPOE拨号 <<<<<<<<<")
        # Adsl_Lan = WAN_ADSL.ADSL(self.web_handler, self.ssh_handler)
        # Adsl_Lan.run_tests()
        # print(">>>>>>>>>> 基于VLAN的多拨 <<<<<<<<<<")
        # Adsl_Vlan = WAN_ADSL_by_Vlan.ADSL_by_Vlan(self.web_handler, self.ssh_handler)
        # Adsl_Vlan.run_tests()
        # print(">>>>>>>>>> 基于VLAN的静态IP <<<<<<<<<")
        # Adsl_Lan = WAN_StaticIP_by_Vlan.StaticIP_by_Vlan(self.web_handler, self.ssh_handler)
        # Adsl_Lan.run_tests()
        # print(">>>>>>>>>> 基于物理网卡的多拨 <<<<<<<<<")
        # Adsl_Lan = WAN_ADSL_by_Lan.ADSL_by_Lan(self.web_handler, self.ssh_handler)
        # Adsl_Lan.run_tests()
        #
        # print("3-6 DHCP设置：")
        # self.web_handler.find_element_by_css_selector(self.MenuCss["DHCP设置"]).click()
        # time.sleep(2)
        # print(">>>>>>>>>> DHCP设置 <<<<<<<<<")
        # DHCP_Settings = MDS.M3_6_DhcpSettings(self.web_handler, self.ssh_handler)
        # DHCP_Settings.run_tests()
        #
        # print("3-3 DNS设置：")
        # self.web_handler.find_element_by_css_selector(self.MenuCss["DNS设置"]).click()
        # time.sleep(2)
        # print(">>>>>>>>>> DNS设置 <<<<<<<<<")
        # DHCP_Settings = MDN.M3_3_DnsSettings(self.web_handler, self.ssh_handler)
        # DHCP_Settings.run_tests()

        print("3-5 分流设置：")
        self.web_handler.find_element_by_css_selector(self.MenuCss["分流设置"]).click()
        time.sleep(2)
        # print(">>>>>>>>>> 协议分流 <<<<<<<<<")
        # self.web_handler.find_element_by_css_selector(self.MenuCss['协议分流']).click()
        # pro_flow = MPRF.ProtocolFlow(self.web_handler, self.ssh_handler)
        # pro_flow.run_tests()
        print(">>>>>>>>>> 端口分流 <<<<<<<<<")
        port_flow = MPF.PortFlow(self.web_handler, self.ssh_handler)
        port_flow.run_tests()
        # print(">>>>>>>>>> 上下行分离 <<<<<<<<<")
        # up_down_flow = MUD.UpDownFlow(self.web_handler, self.ssh_handler)
        # up_down_flow.run_tests()

        # print("3-5 多线负载：")
        # self.web_handler.find_element_by_css_selector(self.MenuCss["多线负载"]).click()
        # time.sleep(2)
        # print(">>>>>>>>>> 多线负载 <<<<<<<<<")
        # MultiRoute = MMR.MultiRoute(self.web_handler, self.ssh_handler)
        # MultiRoute.run_tests()









