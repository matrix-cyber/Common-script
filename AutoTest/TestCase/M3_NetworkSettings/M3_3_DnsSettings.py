import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
from types import FunctionType
import TestBase.ActionBase.Base_Action.Result_Action as TR
import TestBase.ActionBase.M3_NetworkSettings.M3_3_DnsSettings as ACTION
import TestBase.DataBase as TD
import inspect
import time

class M3_3_DnsSettings: #基于物理网卡的多拨
    #初始化：（1）将WEB句柄交给此模块  （2）导入该模块的CSS元素库及测试数据  （3）进入该模块页面  （4）定义全局变量
    def __init__(self, web_handler, ssh_handler, **new_TestData): #模块初始化
        #初始化参数
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu #目录元素库
        self.ElementCss = CSS.ElementBase.DnsSettings#模块元素库
        self.TestData = new_TestData #测试数据
        self.LoginData = TD.TestData.Login
        self.ACTION = ACTION.M3_3_DnsSettings(self.web_handler,self.ssh_handler, self.TestData)
        self.ClassName = self.__class__.__name__ #类名称
        self.test_count = TR.Result_Count()
        self.test_state = TR.Result_Action()

    # 封装查找命令
    def find_element(self, para):
        return self.web_handler.find_element_by_css_selector(para)

    # 返回当前函数名称
    def get_current_function_name(self):
        return inspect.stack()[1][3]

    def TestMethod1(self):#测试添加和认证
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        self.ACTION.EDIT_DNS()
        if not self.ACTION.Check_EditDns():
            self.test_state.set_error("编辑结果与预期不符")
            return False
        else:
            return True

    # def Reconnect(self):
    #     login = TD.TestData.Login[0]
    #     self.web_handler = WA.Web_Action(url="http://" + Topo.DUT, user=login["用户名"], pwd=login["密码"])
    #     self.ssh_handler = SA.IkSSHHandler(Topo.DUT)
    #     self.web_handler.connect()
    #     self.ssh_handler.connect()

    def TestMethod2(self): #当关闭DNS加速，DHCP中DNS服务器生效
        if not self.TestMethod1():
            return False
        time.sleep(2)
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        time.sleep(2)
        self.ACTION.OFF_DnsQuick()
        time.sleep(2)
        DNS_bool = self.ACTION.Check_DnsFunction() #检测DNS功能
        if not DNS_bool:
            self.test_state.set_error("DNS功能不生效")
            return False
        output = self.ACTION.Get_NFconntrack()
        if self.ACTION.Check_MDNS(output) or self.ACTION.Check_SDNS(output):
            self.test_state.set_error("DNS选择不正确")
            return False
        else:
            return True

    def TestMethod3(self): #当DHCP设置中DNS为知名服务器时，开启DNS代理模式，DHCP中DNS服务器生效
        if not self.TestMethod1():
            return False
        time.sleep(2)
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        time.sleep(3)
        self.ACTION.ON_DnsQuick()
        time.sleep(2)
        self.ACTION.OPEN_AgentMode()
        time.sleep(2)
        DNS_bool = self.ACTION.Check_DnsFunction() #检测DNS功能
        if not DNS_bool:
            self.test_state.set_error("DNS功能不生效")
            return False
        output = self.ACTION.Get_NFconntrack()
        if self.ACTION.Check_MDNS(output) or self.ACTION.Check_SDNS(output):
            self.test_state.set_error("DNS选择不正确")
            return False
        else:
            return True


    def TestMethod4(self):  # 当DHCP设置中DNS为知名服务器时，开启DNS缓存模式，DHCP中DNS服务器生效
        if not self.TestMethod1():
            return False
        time.sleep(2)
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        time.sleep(3)
        self.ACTION.ON_DnsQuick()
        time.sleep(2)
        self.ACTION.OPEN_CacheMode()
        time.sleep(2)
        DNS_bool = self.ACTION.Check_DnsFunction()  # 检测DNS功能
        if not DNS_bool:
            self.test_state.set_error("DNS功能不生效")
            return False
        output = self.ACTION.Get_NFconntrack()
        if self.ACTION.Check_MDNS(output) or self.ACTION.Check_SDNS(output):
            self.test_state.set_error("DNS选择不正确")
            return False
        else:
            return True

    def TestMethod5(self):  # 当DHCP设置中DNS为知名服务器时，开启DNS强制代理模式，DNS设置中首选DNS服务器生效
        if not self.TestMethod1():
            return False
        time.sleep(2)
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        time.sleep(3)
        self.ACTION.ON_DnsQuick()
        time.sleep(2)
        self.ACTION.OPEN_AgentMode()
        time.sleep(2)
        self.ACTION.ON_ForceAgent()
        time.sleep(2)
        DNS_bool = self.ACTION.Check_DnsFunction()  # 检测DNS功能
        if not DNS_bool:
            self.test_state.set_error("DNS功能不生效")
            return False
        output = self.ACTION.Get_NFconntrack()
        if not self.ACTION.Check_MDNS(output) and not self.ACTION.Check_SDNS(output):
            self.test_state.set_error("DNS选择不正确")
            return False
        else:
            return True

    def TestMethod6(self):  # 当DHCP设置中DNS为知名服务器时，开启DNS强制代理模式，DNS设置中首选DNS服务器为不可达地址，备选DNS生效
        if not self.TestMethod1():
            return False
        time.sleep(2)
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        time.sleep(3)
        self.ACTION.ON_DnsQuick()
        time.sleep(2)
        self.ACTION.OPEN_AgentMode()
        time.sleep(2)
        self.ACTION.ON_ForceAgent()
        time.sleep(2)
        DNS_bool = self.ACTION.Check_DnsFunction()  # 检测DNS功能
        if not DNS_bool:
            self.test_state.set_error("DNS功能不生效")
            return False
        output = self.ACTION.Get_NFconntrack()
        if self.ACTION.Check_MDNS(output) or not self.ACTION.Check_SDNS(output):
            self.test_state.set_error("DNS选择不正确")
            return False
        else:
            return True

    def TestMethod7(self):  # 当DHCP设置中DNS为知名服务器时，开启DNS强制代理模式，DNS设置中首选DNS和备选服务器为不可达地址，解析失败
        if not self.TestMethod1():
            return False
        time.sleep(2)
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        time.sleep(3)
        self.ACTION.ON_DnsQuick()
        time.sleep(2)
        self.ACTION.OPEN_AgentMode()
        time.sleep(2)
        self.ACTION.ON_ForceAgent()
        time.sleep(2)
        DNS_bool = self.ACTION.Check_DnsFunction()  # 检测DNS功能
        if not DNS_bool:
            self.test_state.set_error("DNS功能不生效")
            return False
        output = self.ACTION.Get_NFconntrack()
        if self.ACTION.Check_MDNS(output) or self.ACTION.Check_SDNS(output):
            self.test_state.set_error("DNS选择不正确")
            return False
        else:
            return True

    def TestMethod8(self):  # 当DHCP设置中DNS为网关路由时，开启DNS代理模式，DNS设置中首选DNS生效
        if not self.TestMethod1():
            return False
        time.sleep(2)
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        time.sleep(3)
        self.ACTION.ON_DnsQuick()
        time.sleep(2)
        self.ACTION.OPEN_AgentMode()
        time.sleep(2)
        DNS_bool = self.ACTION.Check_DnsFunction()  # 检测DNS功能
        if not DNS_bool:
            self.test_state.set_error("DNS功能不生效")
            return False
        output = self.ACTION.Get_NFconntrack()
        if not self.ACTION.Check_MDNS(output) and not self.ACTION.Check_SDNS(output):
            self.test_state.set_error("DNS选择不正确")
            return False
        else:
            return True

    def TestMethod9(self):  # 当DHCP设置中DNS为网关路由时，开启DNS缓存模式，DNS设置DNS不生效，解析失败
        if not self.TestMethod1():
            return False
        time.sleep(2)
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        time.sleep(3)
        self.ACTION.ON_DnsQuick()
        time.sleep(2)
        self.ACTION.OPEN_CacheMode()
        time.sleep(2)
        DNS_bool = self.ACTION.Check_DnsFunction()  # 检测DNS功能
        if not DNS_bool:
            self.test_state.set_error("DNS功能不生效")
            return False
        output = self.ACTION.Get_NFconntrack()
        if self.ACTION.Check_MDNS(output) or self.ACTION.Check_SDNS(output):
            self.test_state.set_error("DNS选择不正确")
            return False
        else:
            return True

    def TestMethod10(self):  # 当DHCP设置中DNS为网关路由时，开启DNS强制代理模式，DNS设置中首选DNS生效
        if not self.TestMethod1():
            return False
        time.sleep(2)
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        time.sleep(3)
        self.ACTION.ON_DnsQuick()
        time.sleep(2)
        self.ACTION.OPEN_AgentMode()
        time.sleep(2)
        self.ACTION.ON_ForceAgent()
        DNS_bool = self.ACTION.Check_DnsFunction()  # 检测DNS功能
        if not DNS_bool:
            self.test_state.set_error("DNS功能不生效")
            return False
        output = self.ACTION.Get_NFconntrack()
        if not self.ACTION.Check_MDNS(output) and not self.ACTION.Check_SDNS(output):
            self.test_state.set_error("DNS选择不正确")
            return False
        else:
            return True

    def run_Method(self):
        time.sleep(10)
        i = 0
        for Fname, Func in M3_3_DnsSettings.__dict__.items():
            if type(Func) == FunctionType and self.TestData["测试方法"] == Fname:
                i = i + 1
                if Func(self):
                    self.test_state.show_ok_result()
                    return True
                else:
                    self.test_state.show_error_result()
                    return False
            else:
                continue
        if i == 0:
            print("没有此测试方法")
            return False

    def run_tests(self):
        TestData_all = TD.TestData.DnsSettings
        DataLen = len(TestData_all)
        RunTestNum = 0
        for i in range(0, DataLen):
            if TestData_all[i]["是否执行"] == "Y":
                print(TestData_all[i]["测试例"])
                NEW_RUN = M3_3_DnsSettings(self.web_handler, self.ssh_handler, **TestData_all[i])
                bool = NEW_RUN.run_Method()
                if bool:
                    self.test_count.add_RightNum()
                else:
                    self.test_count.add_ErrorNum()
                time.sleep(3)
                RunTestNum = RunTestNum + 1
            else:
                continue
        if RunTestNum == 0:
            print("无执行的测试例")
        else:
            self.test_count.show_all_result()