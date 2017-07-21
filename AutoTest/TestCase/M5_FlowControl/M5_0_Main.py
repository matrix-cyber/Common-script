# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
import TestCase.M5_FlowControl.M5_1_SmartControl as MSC
import TestCase.M5_FlowControl.M5_2_StratergyControl as MST
import TestCase.M5_FlowControl.M5_3_IPSpeedLimit as MIP
import TestBase.ActionBase.Base_Action.Result_Action as TR
import TestBase.ElementBase as CSS
import time

class M5_0_Main:
    def __init__(self, web_handler,ssh_handler):
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu

    def run_tests(self):
        # 进入模块
        self.web_handler.find_element_by_css_selector(self.MenuCss["流控设置"]).click()
        time.sleep(2)
        print("5-1 一键流控:")
        self.web_handler.find_element_by_css_selector(self.MenuCss['一键流控']).click()
        time.sleep(1)
        print(">>>>>>>>>> 一键流控 <<<<<<<<<")
        SmartControl = MSC.SmartControl(self.web_handler, self.ssh_handler)
        SmartControl.run_tests()

        print("5-3 手工流控:")
        self.web_handler.find_element_by_css_selector(self.MenuCss['手工流控']).click()
        time.sleep(1)
        print(">>>>>>>>>> 手工流控 <<<<<<<<<")
        StratergyControl = MST.StratergyControl(self.web_handler, self.ssh_handler)
        StratergyControl.run_tests()

        print("5-3 IP限速：")
        self.web_handler.find_element_by_css_selector(self.MenuCss["IP/MAC限速"]).click()
        time.sleep(2)
        print(">>>>>>>>>> IP限速 <<<<<<<<<")
        IPSpeedLimit = MIP.IPSpeedLimit(self.web_handler, self.ssh_handler)
        IPSpeedLimit.run_tests()









