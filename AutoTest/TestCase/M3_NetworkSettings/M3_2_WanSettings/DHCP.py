import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
from types import FunctionType
import TestBase.ActionBase.Base_Action.Result_Action as TR
import TestBase.ActionBase.M3_NetworkSettings.M3_2_WanSettings.DHCP as ACTION
import TestBase.ActionBase.Base_Action.SSH_Action as SA
import TestBase.DataBase as TD
import inspect
import time

class DHCP:#DHCP/动态IP
    #初始化：（1）将WEB句柄交给此模块  （2）导入该模块的CSS元素库及测试数据  （3）进入该模块页面  （4）定义全局变量
    def __init__(self, web_handler, ssh_handler, **TestData): #模块初始化
        #初始化参数
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu #目录元素库
        self.ElementCss = CSS.ElementBase.DHCP#模块元素库
        self.TestData = TestData #测试数据
        self.LoginData = TD.TestData.Login
        self.ACTION = ACTION.DHCP(self.web_handler,self.ssh_handler, self.TestData)
        self.ClassName = self.__class__.__name__ #类名称
        self.FunctionName = ""
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
        self.find_element(self.ElementCss["WAN2"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["接入方式"]).click()
        time.sleep(3)
        self.find_element(self.ElementCss["DHCP"]).click()
        time.sleep(1)
        if not self.ACTION.ADD():
            self.test_state.set_error("添加有问题")
            return False
        else:
            return True

    def TestMethod2(self):#测试添加和线路连通性
        if not self.TestMethod1():
            return False
        self.FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, self.FunctionName)
        boolret = self.ACTION.Check_Link()
        if boolret:
            return True
        else:
            self.test_state.set_error("线路不通")
            return False

    def TestMethod3(self):# 验证默认线路
        if not self.TestMethod2():
            return False
        self.FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, self.FunctionName)
        time.sleep(5)
        output = self.ssh_handler.exec_cmd("route -n")
        Route = SA.IkSSHUtils.GetRoute(output)
        print("\t默认网关：", Route["Gateway"])
        if not self.ACTION.Check_DefaultRoute():
            self.test_state.set_error("开启默认线路选项不生效")
            return False
        self.ACTION.EDIT_SwitchDefaultRoute()
        time.sleep(5)
        output = self.ssh_handler.exec_cmd("route -n")
        Route = SA.IkSSHUtils.GetRoute(output)
        print("\t默认网关：", Route["Gateway"])
        if self.ACTION.Check_DefaultRoute():
            self.test_state.set_error("关闭默认线路选项不生效")
            return False
        else:
            return True

    def TestMethod4(self):#验证断开功能
        if not self.TestMethod2():
            return False
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        self.find_element(self.ElementCss["断开"]).click()
        time.sleep(5)
        if self.ACTION.Check_DefaultRoute():
            self.test_state.set_error("断开不生效")
            return False
        time.sleep(2)
        self.find_element(self.ElementCss["连接"]).click()
        time.sleep(5)
        if not self.ACTION.Check_DefaultRoute():
            self.test_state.set_error("连接不生效")
            return False
        else:
            return True

    def TestMethod5(self):  # 验证自动DNS
        # 修改路由的DSN
        self.ACTION.Edit_RouteDNS()
        # 配置外网信息并开启自动添加DNS
        if not self.TestMethod1():
            return False
        time.sleep(2)
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        time.sleep(2)
        self.ACTION.EDIT_UpDownLink()
        if not self.ACTION.Check_RouteDNS():
            self.test_state.set_error("开启自动添加DNS不生效")
            return False

        # 关闭外网的自动添加DNS
        self.ACTION.OFF_AutoDNS()
        # 修改路由的DNS
        self.ACTION.Edit_RouteDNS()
        self.ACTION.EDIT_UpDownLink()
        time.sleep(1)
        if self.ACTION.Check_RouteDNS():
            self.test_state.set_error("关闭自动添加DNS不生效")
            return False
        else:
            return True

    def run_Method(self):
        i = 0
        for Fname, Func in DHCP.__dict__.items():
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
        TestData_all = TD.TestData.DHCP
        DataLen = len(TestData_all)
        RunTestNum = 0
        for i in range(0, DataLen):
            if TestData_all[i]["是否执行"] == "Y":
                print(TestData_all[i]["测试例"])
                NEW_RUN = DHCP(self.web_handler, self.ssh_handler, **TestData_all[i])
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