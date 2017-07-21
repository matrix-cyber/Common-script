import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
import time
import TestBase.ActionBase.Base_Action.SSH_Action as SA
import TestBase.ActionBase.Base_Action.Public_Action as PA

class StaticIP_by_Vlan:
    #初始化：（1）将WEB句柄交给此模块  （2）导入该模块的CSS元素库及测试数据
    def __init__(self, web_handler,ssh_handler,TestData): #模块初始化
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu #目录元素库
        self.ElementCss = CSS.ElementBase.StaticIP_by_Vlan #模块元素库
        self.TestData = TestData #测试数据
        self.bool = True

    # 封装查找命令
    def find_element(self, para): #公用
        return self.web_handler.find_element_by_css_selector(para)

    def ADD(self):
        time.sleep(4)
        self.find_element(self.ElementCss["添加"]).click()
        time.sleep(3)
        self.find_element(self.ElementCss["VLAN_ID"]).send_keys(self.TestData["VLAN_ID"])
        self.find_element(self.ElementCss["名称"]).send_keys(self.TestData["名称"])
        self.find_element(self.ElementCss["IP"]).send_keys(self.TestData["IP"])
        self.find_element(self.ElementCss["子网掩码"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["掩码长度"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["网关"]).send_keys(self.TestData["网关"])
        self.find_element(self.ElementCss["MAC"]).clear()
        self.find_element(self.ElementCss["MAC"]).send_keys(self.TestData["MAC"])
        self.find_element(self.ElementCss["上行"]).send_keys(self.TestData["上行"])
        self.find_element(self.ElementCss["下行"]).send_keys(self.TestData["下行"])
        self.find_element(self.ElementCss["默认网关"]).click()
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
        try:
            self.web_handler.accept_confirm_msg()
            time.sleep(2)
        except:
            self.find_element(self.ElementCss["保存确定"]).click()
            time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        try:
            self.find_element(self.ElementCss["单独停用"])
            self.bool = True
            return self.Check_Add()
        except:
            self.bool = False
            return self.Check_Add()

    def EDIT_LinkSwitch(self):
        self.find_element(self.ElementCss["编辑"]).click()
        time.sleep(3)
        self.find_element(self.ElementCss["掉线切换"]).click()
        self.find_element(self.ElementCss["配置确认"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(2)
        self.web_handler.refresh_page()
        time.sleep(2)

    def EDIT_GateWay(self):
        self.find_element(self.ElementCss["编辑"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["网关"]).clear()
        self.find_element(self.ElementCss["网关"]).send_keys("1.2.3.4")
        time.sleep(1)
        self.find_element(self.ElementCss["配置确认"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(2)

    def EDIT_IP(self):
        self.find_element(self.ElementCss["编辑"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["IP"]).clear()
        self.find_element(self.ElementCss["IP"]).send_keys("88.1.1.5")
        time.sleep(1)
        self.find_element(self.ElementCss["网关"]).clear()
        self.find_element(self.ElementCss["网关"]).send_keys("88.1.1.1")
        time.sleep(1)
        self.find_element(self.ElementCss["配置确认"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(2)

    def EDIT_SwitchDefaultRoute(self):
        self.find_element(self.ElementCss["WAN1"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["WAN1默认网关"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["WAN1保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(2)

    def ON_one(self): #公用
        user_stat = self.find_element(self.ElementCss["启停用状态"]).text
        if user_stat == "已启用":
            return True
        else:
            self.find_element(self.ElementCss["单独启用"]).click()
            time.sleep(1)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(2)
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
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
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
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(2)
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
        time.sleep(1)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(2)
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
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(2)
        self.web_handler.refresh_page()
        time.sleep(2)
        new_stat = self.find_element(self.ElementCss["启停用状态"]).text
        if new_stat == "已停用":
            return True
        else:
            return False

    def DELETE_all(self): #公用
        time.sleep(1)
        self.find_element(self.ElementCss["全部选中"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["全部删除"]).click()
        time.sleep(2)
        self.web_handler.accept_confirm_msg()
        time.sleep(3)
        try:
            self.find_element(self.ElementCss["单独停用"])
            return False
        except:
            return True

    def Check_Add(self): #公用
        if not self.bool and (self.TestData["预期结果"] == "添加失败"):
            return True
        elif self.bool and self.TestData["预期结果"] == "连接成功" or "连接失败":
            return True
        else:
            return False

    def Check_Link(self):
        boolret = PA.ping("www.baidu.com")
        if not boolret and (self.TestData["预期结果"] == "连接失败"):
            return True
        elif boolret and (self.TestData["预期结果"] == "连接成功"):
            return True
        else:
            return False

    def Check_DefaultRoute(self):
        output = self.ssh_handler.exec_cmd("route -n")
        Route = SA.IkSSHUtils.GetRoute(output)
        print("\t默认路由:", Route["Gateway"])
        if self.TestData["网关"] != Route["Gateway"]:
            return False
        else:
            return True
