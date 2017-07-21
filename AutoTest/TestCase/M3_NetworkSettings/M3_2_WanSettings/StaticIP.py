import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
from types import FunctionType
import TestBase.ActionBase.Base_Action.Result_Action as TR
import TestBase.ActionBase.M3_NetworkSettings.M3_2_WanSettings.StaticIP as ACTION
import TestBase.ActionBase.Base_Action.SSH_Action as SA
import TestBase.DataBase as TD
import inspect
import time

class StaticIP:#基于VLAN的多拨
    #初始化：（1）将WEB句柄交给此模块  （2）导入该模块的CSS元素库及测试数据  （3）进入该模块页面  （4）定义全局变量
    def __init__(self, web_handler, ssh_handler, **TestData): #模块初始化
        #初始化参数
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu #目录元素库
        self.ElementCss = CSS.ElementBase.StaticIP#模块元素库
        self.TestData = TestData #测试数据
        self.LoginData = TD.TestData.Login
        self.ACTION = ACTION.StaticIP(self.web_handler,self.ssh_handler, self.TestData)
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
        self.find_element(self.ElementCss["静态IP"]).click()
        time.sleep(1)
        if not self.ACTION.ADD():
            self.test_state.set_error("添加结果不符合预期")
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
            self.test_state.set_error("线路连接不符合预期")
            return False

    def TestMethod3(self):# 验证默认网关
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

    def TestMethod4(self):#验证掉线切换
        if not self.TestMethod2():
            return False
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        self.ACTION.EDIT_LinkSwitch()
        time.sleep(60)
        if self.ACTION.Check_DefaultRoute():
            self.test_state.set_error("开启掉线切换不生效")
            return False
        else:
            return True

    def TestMethod5(self):  # 验证时间段控制
        if not self.TestMethod2():
            return False
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        self.ACTION.EDIT_TimeControl() # 开始时间为现在时间+2分钟，结束时间为现在时间+4分钟
        time.sleep(10)
        if self.ACTION.Check_DefaultRoute(): #配置后，现在不在时间内，所以该路由不存在
            self.test_state.set_error("时间段控制不生效")
            return False
        time.sleep(150)
        if not self.ACTION.Check_DefaultRoute():  # 等2分钟后，在时间段内了，路由应添加上
            self.test_state.set_error("开始时间不生效")
            return False
        time.sleep(180)
        if self.ACTION.Check_DefaultRoute():  # 等4分钟后，在时间段内了，路由应添加上
            self.test_state.set_error("结束时间不生效")
            return False
        else:
            return True

    def run_Method(self):
        i = 0
        for Fname, Func in StaticIP.__dict__.items():
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
        TestData_all = TD.TestData.StaticIP
        DataLen = len(TestData_all)
        RunTestNum = 0
        for i in range(0, DataLen):
            if TestData_all[i]["是否执行"] == "Y":
                print(TestData_all[i]["测试例"])
                NEW_RUN = StaticIP(self.web_handler, self.ssh_handler, **TestData_all[i])
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