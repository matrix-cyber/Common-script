import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
from types import FunctionType
import TestBase.ActionBase.Base_Action.Result_Action as TR
import TestBase.ActionBase.M3_NetworkSettings.M3_2_WanSettings.WAN_Public as ACTION
import TestBase.DataBase as TD
import TestCase.M3_NetworkSettings.M3_2_WanSettings.StaticIP as StaticIP
import inspect
import time

class WAN_Public:#基于VLAN的多拨
    #初始化：（1）将WEB句柄交给此模块  （2）导入该模块的CSS元素库及测试数据  （3）进入该模块页面  （4）定义全局变量
    def __init__(self, web_handler, ssh_handler, **TestData): #模块初始化
        #初始化参数
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu #目录元素库
        self.ElementCss = CSS.ElementBase.WAN_Public#模块元素库
        self.TestData = TestData #测试数据
        self.LoginData = TD.TestData.Login
        self.ACTION = ACTION.WAN_Public(self.web_handler,self.ssh_handler, self.TestData)
        self.ClassName = self.__class__.__name__ #类名称
        self.FunctionName = ""
        self.test_count = TR.Result_Count()
        self.test_state = TR.Result_Action()
        self.StaticIP_TestData = TD.TestData.StaticIP[1]

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
        self.ACTION.UNBunding()
        time.sleep(3)
        self.ACTION.Bunding()
        time.sleep(2)
        WAN_StaticIP = StaticIP.StaticIP(self.web_handler, self.ssh_handler, **self.StaticIP_TestData)
        WAN_StaticIP.TestMethod1()
        self.ACTION.EDIT_CloneMAC()
        if not self.ACTION.Check_EditMAC():
            self.test_state.set_error("克隆MAC添加失败")
            return False
        if not self.ACTION.Check_CloneMAC():
            self.test_state.set_error("克隆MAC功能不生效")
            return False
        else:
            return True


    def run_Method(self):
        i = 0
        for Fname, Func in WAN_Public.__dict__.items():
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
        TestData_all = TD.TestData.WAN_Public
        DataLen = len(TestData_all)
        RunTestNum = 0
        for i in range(0, DataLen):
            if TestData_all[i]["是否执行"] == "Y":
                print(TestData_all[i]["测试例"])
                NEW_RUN = WAN_Public(self.web_handler, self.ssh_handler, **TestData_all[i])
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