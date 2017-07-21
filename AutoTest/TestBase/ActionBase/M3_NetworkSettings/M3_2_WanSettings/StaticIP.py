import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
import time
import TestBase.ActionBase.Base_Action.SSH_Action as SA
import TestBase.ActionBase.Base_Action.Public_Action as PA
import datetime

class StaticIP:
    #初始化：（1）将WEB句柄交给此模块  （2）导入该模块的CSS元素库及测试数据
    def __init__(self, web_handler,ssh_handler,TestData): #模块初始化
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu #目录元素库
        self.ElementCss = CSS.ElementBase.StaticIP #模块元素库
        self.DNS_Element = CSS.ElementBase.DnsSettings
        self.TestData = TestData #测试数据
        self.bool = True

    # 封装查找命令
    def find_element(self, para): #公用
        return self.web_handler.find_element_by_css_selector(para)

    def ADD(self):
        time.sleep(2)
        self.find_element(self.ElementCss["IP"]).clear()
        self.find_element(self.ElementCss["IP"]).send_keys(self.TestData["IP"])
        self.find_element(self.ElementCss["网关"]).clear()
        self.find_element(self.ElementCss["网关"]).send_keys(self.TestData["网关"])
        self.find_element(self.ElementCss["上行带宽"]).clear()
        self.find_element(self.ElementCss["上行带宽"]).send_keys(self.TestData["上行带宽"])
        self.find_element(self.ElementCss["下行带宽"]).clear()
        self.find_element(self.ElementCss["下行带宽"]).send_keys(self.TestData["下行带宽"])
        while(1):
            try:
                self.find_element(self.ElementCss["删除"]).click()
            except:
                break
        self.find_element(self.ElementCss["添加"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["扩展IP"]).send_keys(self.TestData["扩展IP"])
        self.find_element(self.ElementCss["确定"]).click()
        stat = self.find_element(self.ElementCss["默认网关"]).get_attribute("checked")
        if stat == None:
            self.find_element(self.ElementCss["默认网关"]).click()
        DNS_stat = self.find_element(self.ElementCss["掉线切换"]).get_attribute("checked")
        if DNS_stat != None:
            self.find_element(self.ElementCss["掉线切换"]).click()
        Time_stat = self.find_element(self.ElementCss["上网时间段控制"]).get_attribute("checked")
        if Time_stat == None:
            self.find_element(self.ElementCss["上网时间段控制"]).click()
        self.find_element(self.ElementCss["开始时间"]).clear()
        self.find_element(self.ElementCss["开始时间"]).send_keys(self.TestData["开始时间"])
        self.find_element(self.ElementCss["结束时间"]).clear()
        self.find_element(self.ElementCss["结束时间"]).send_keys(self.TestData["结束时间"])
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

    def SetTime(self, hour, new_minute):
        if int(hour) < 10 and new_minute < 10:
            set_time = "0" + hour + ":0" + str(new_minute)
        elif int(hour) < 10:
            set_time = "0" + hour + ":" + str(new_minute)
        elif new_minute < 10:
            set_time = hour + ":0" + str(new_minute)
        else:
            set_time = hour + ":" + str(new_minute)
        return set_time

    def EDIT_TimeControl(self):  # 编辑定时重拨
        self.find_element(self.ElementCss["开始时间"]).clear()
        time.sleep(1)
        old_time = datetime.datetime.now()
        hour = old_time.strftime("%H")
        minute = old_time.strftime("%M")
        start_minute = int(minute) + 2
        end_minute = int(minute) + 4
        start_hour = hour
        end_hour = hour
        if start_minute >= 60:
            start_hour = int(hour) + 1
            start_minute = start_minute - 60
            end_hour = start_hour
            end_minute = start_minute + 2
        elif end_minute >= 60:
            end_hour = int(hour) + 1
            end_minute = end_minute - 60
        start_time = self.SetTime(start_hour, start_minute)
        end_time = self.SetTime(end_hour, end_minute)
        self.find_element(self.ElementCss["开始时间"]).clear()
        self.find_element(self.ElementCss["开始时间"]).send_keys(start_time)
        time.sleep(1)
        self.find_element(self.ElementCss["结束时间"]).clear()
        self.find_element(self.ElementCss["结束时间"]).send_keys(end_time)
        time.sleep(1)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()

    def Check_Add(self): #公用
        if not self.bool and (self.TestData["预期结果"] == "添加失败"):
            return True
        elif self.bool and self.TestData["预期结果"] == "连接成功" or "连接失败":
            return True
        else:
            return False

    def Check_Link(self):
        link_bool = PA.ping("www.qq.com")
        if link_bool and self.TestData["预期结果"] == "连接成功":
            return True
        elif not link_bool and self.TestData["预期结果"] == "连接失败":
            return True
        else:
            return False

    def Check_DefaultRoute(self):
        output = self.ssh_handler.exec_cmd("route -n")
        Route = SA.IkSSHUtils.GetRoute(output)
        # print("\t默认网关：",Route["Gateway"])
        # print("\t配置网关：",self.TestData["网关"])
        if self.TestData["网关"] != Route["Gateway"]:
            return False
        else:
            return True






