import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
from types import FunctionType
import TestBase.ActionBase.Base_Action.Result_Action as TR
import TestBase.ActionBase.M3_NetworkSettings.M3_1_LanSettings as ACTION
import TestBase.DataBase as TD
import inspect
import time

class M3_1_LANSettings:
    #初始化：（1）将WEB句柄交给此模块  （2）导入该模块的CSS元素库及测试数据  （3）进入该模块页面  （4）定义全局变量
    def __init__(self, web_handler, **new_TestData): #模块初始化
        #初始化参数
        self.web_handler = web_handler
        self.MenuCss = CSS.ElementBase.Menu #目录元素库
        self.ElementCss = CSS.ElementBase.LanSettings#模块元素库
        self.TestData = new_TestData #测试数据
        self.LoginData = TD.TestData.Login
        self.ACTION = ACTION.LanSettings(self.web_handler, self.TestData)
        self.ClassName = self.__class__.__name__ #类名称
        self.test_count = TR.Result_Count()
        self.test_state = TR.Result_Action()

    # 封装查找命令
    def find_element(self, para):
        return self.web_handler.find_element_by_css_selector(para)

    # 返回当前函数名称
    def get_current_function_name(self):
        return inspect.stack()[1][3]

    def TestMethod1(self):
        FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, FunctionName)
        Add_state = self.ACTION.ADD_Lan()
        if not Add_state:
            self.test_state.set_error("绑定网卡失败")
            return False
        BaseSet_state = self.ACTION.BaseSettings()
        if not BaseSet_state:
            self.test_state.set_error("配置LAN口失败")
            return False
        Delete_state = self.ACTION.DELETE_Lan()
        if not Delete_state:
            self.test_state.set_error("解绑失败")
            return False
        else:
            return True

    def run_Method(self):
        i = 0
        for Fname, Func in M3_1_LANSettings.__dict__.items():
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
        TestData_all = TD.TestData.LanSettings
        DataLen = len(TestData_all)
        RunTestNum = 0
        for i in range(0, DataLen):
            if TestData_all[i]["是否执行"] == "Y":
                print(TestData_all[i]["测试例"])
                NEW_RUN = M3_1_LANSettings(self.web_handler, **TestData_all[i])
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




