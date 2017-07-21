import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
from types import FunctionType
import TestBase.ActionBase.Base_Action.Result_Action as TR
import TestBase.ActionBase.M3_NetworkSettings.M3_5_MultiLoad.M3_5_1_MultiRoute as ACTION
import TestBase.DataBase as TD
import inspect
import time

class MultiRoute: #基于物理网卡的多拨
    #初始化：（1）将WEB句柄交给此模块  （2）导入该模块的CSS元素库及测试数据  （3）进入该模块页面  （4）定义全局变量
    def __init__(self, web_handler, ssh_handler, **new_TestData): #模块初始化
        #初始化参数
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu #目录元素库
        self.ElementCss = CSS.ElementBase.MultiRoute#模块元素库
        self.TestData = new_TestData #测试数据
        self.LoginData = TD.TestData.Login
        self.ACTION = ACTION.MultiRoute(self.web_handler,self.ssh_handler, self.TestData)
        self.ClassName = self.__class__.__name__ #类名称
        self.test_count = TR.Result_Count()
        self.test_state = TR.Result_Action()

    def __del__(self):
        self.find_element(self.ElementCss["全部选择"]).click()
        self.find_element(self.ElementCss["全部删除"]).click()
        self.web_handler.accept_confirm_msg()
        time.sleep(2)

    # 封装查找命令
    def find_element(self, para):
        return self.web_handler.find_element_by_css_selector(para)

    # 返回当前函数名称
    def get_current_function_name(self):
        return inspect.stack()[1][3]

    def TestMethod1(self):#验证实时连接
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        if not self.ACTION.ADD():
            self.test_state.set_error("添加失败")
            return False
        time.sleep(2)
        self.ACTION.EDIT_LineWeight()
        if not self.ACTION.Check_RealLink():
            self.test_state.set_error("功能不生效")
            return False
        else:
            return True

    def TestMethod2(self):#验证新建连接
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        if not self.ACTION.ADD():
            self.test_state.set_error("添加失败")
            return False
        time.sleep(2)
        self.ACTION.EDIT_LineWeight()
        if not self.ACTION.Check_NewLink():
            self.test_state.set_error("功能不生效")
            return False
        else:
            return True

    def TestMethod3(self):#验证实时流量
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        if not self.ACTION.ADD():
            self.test_state.set_error("添加失败")
            return False
        time.sleep(2)
        self.ACTION.EDIT_LineWeight()
        if not self.ACTION.Check_RealFlow():
            self.test_state.set_error("功能不生效")
            return False
        else:
            return True

    def TestMethod4(self):#验证源IP+目的IP
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        if not self.ACTION.ADD():
            self.test_state.set_error("添加失败")
            return False
        time.sleep(2)
        self.ACTION.EDIT_LineWeight()
        if not self.ACTION.Check_SIP_DIP():
            self.test_state.set_error("功能不生效")
            return False
        else:
            return True

    def TestMethod5(self):  # 验证源IP+目的IP+源端口
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        if not self.ACTION.ADD():
            self.test_state.set_error("添加失败")
            return False
        time.sleep(2)
        self.ACTION.EDIT_LineWeight()
        if not self.ACTION.Check_SIP_DIP_DPORT():
            self.test_state.set_error("功能不生效")
            return False
        else:
            return True

    def TestMethod6(self):  # 验证源IP
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        if not self.ACTION.ADD():
            self.test_state.set_error("添加失败")
            return False
        time.sleep(2)
        self.ACTION.EDIT_LineWeight()
        if not self.ACTION.Check_SIP():
            self.test_state.set_error("功能不生效")
            return False
        else:
            return True

    def TestMethod7(self):  # 验证源IP+源端口
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        if not self.ACTION.ADD():
            self.test_state.set_error("添加失败")
            return False
        time.sleep(2)
        self.ACTION.EDIT_LineWeight()
        if not self.ACTION.Check_SIP_SPORT():
            self.test_state.set_error("功能不生效")
            return False
        else:
            return True

    def run_Method(self):
        time.sleep(10)
        i = 0
        for Fname, Func in MultiRoute.__dict__.items():
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
        TestData_all = TD.TestData.MultiRoute
        DataLen = len(TestData_all)
        RunTestNum = 0
        for i in range(0, DataLen):
            if TestData_all[i]["是否执行"] == "Y":
                print(TestData_all[i]["测试例"])
                NEW_RUN = MultiRoute(self.web_handler, self.ssh_handler, **TestData_all[i])
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