import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
from types import FunctionType
import TestBase.ActionBase.Base_Action.Result_Action as TR
import TestBase.ActionBase.M2_SystemSettings.M2_4_2_WebAccountManage as ACTION
import TestBase.DataBase as TD
import inspect


class M2_4_2_WebAccountManage:
    #初始化：（1）将WEB句柄交给此模块  （2）导入该模块的CSS元素库及测试数据  （3）进入该模块页面  （4）定义全局变量
    def __init__(self, web_handler, TestData): #模块初始化
        #初始化参数
        self.web_handler = web_handler
        self.MenuCss = CSS.ElementBase.Menu #目录元素库
        self.ElementCss = CSS.ElementBase.WebAccountMange #模块元素库
        self.TestData = TestData #测试数据
        self.LoginData = TD.TestData.Login
        self.ClassName = self.__class__.__name__ #类名称
        self.ACTION = ACTION.WebAccountManage(self.web_handler, self.TestData)

    # 封装查找命令
    def find_element(self, para):
        return self.web_handler.find_element_by_css_selector(para)

    # 返回当前函数名称
    def get_current_function_name(self):
        return inspect.stack()[1][3]

    # TM1:添加：验证包含不支持的字符的用户名、密码则添加失败，其它能添加成功
    def TestMethod1(self):
        FunctionName = self.get_current_function_name()
        test = TR.Result_Action(self.ClassName, FunctionName)
        if not self.ACTION.DELETE_all():
            test.set_error("全部删除有问题")
            return test.show_error_result()
        elif not self.ACTION.ADD_Access():
            test.set_error("添加有问题")
            return test.show_error_result()
        else:
            test.show_ok_result()


    # TM2:添加并登录：针对访问权限用户，验证用户名和密码合法的账号，用安全IP登录成功，非安全IP登录失败
    def TestMethod2(self):
        FunctionName = self.get_current_function_name()
        test = TR.Result_Action(self.ClassName, FunctionName)
        if not self.ACTION.DELETE_all():
            test.set_error("全部删除有问题")
            return test.show_error_result()
        elif not self.ACTION.ADD_Access():
            test.set_error("添加有问题")
            return test.show_error_result()
        elif not self.ACTION.Login():
            test.set_error("登录有问题")
            return test.show_error_result()
        else:
            test.show_ok_result()

    # TM3:添加并登录：针对访问修改权限用户，验证用户名和密码合法的账号，用安全IP登录成功，非安全IP登录失败
    def TestMethod3(self):
        FunctionName = self.get_current_function_name()
        test = TR.Result_Action(self.ClassName, FunctionName)
        if not self.ACTION.DELETE_all():
            test.set_error("全部删除有问题")
            return test.show_error_result()
        elif not self.ACTION.ADD_Access_Modify():
            test.set_error("添加有问题")
            return test.show_error_result()
        elif not self.ACTION.Login():
            test.set_error("登录有问题")
            return test.show_error_result()
        else:
            test.show_ok_result()

    # TM4:添加并登录：针对访问修改删除权限用户，验证用户名和密码合法的账号，用安全IP登录成功，非安全IP登录失败
    def TestMethod4(self):
        FunctionName = self.get_current_function_name()
        test = TR.Result_Action(self.ClassName, FunctionName)
        if not self.ACTION.DELETE_all():
            test.set_error("全部删除有问题")
            return test.show_error_result()
        elif not self.ACTION.ADD_Access_Modify_Delete():
            test.set_error("添加有问题")
            return test.show_error_result()
        elif not self.ACTION.Login():
            test.set_error("登录有问题")
            return test.show_error_result()
        else:
            test.show_ok_result()

    #TM5:访问权限：验证访问的权限功能，能访问但不能修改或删除
    def TestMethod5(self):
        FunctionName = self.get_current_function_name()
        test = TR.Result_Action(self.ClassName, FunctionName)
        self.TestMethod2()
        if self.ACTION.Check_Access_Authority():
            return test.show_ok_result()
        else:
            test.set_error("访问权限功能不正确")
            return test.show_error_result()

    # TM6:访问修改权限：验证访问修改的权限功能，能访问修改但不能删除
    def TestMethod6(self):
        FunctionName = self.get_current_function_name()
        test = TR.Result_Action(self.ClassName, FunctionName)
        self.TestMethod3()
        if self.ACTION.Check_Access_Modify_Authority():
            return test.show_ok_result()
        else:
            test.set_error("访问修改权限功能不正确")
            return test.show_error_result()


    # TM7:访问修改删除权限：验证访问修改的权限功能，能访问修改以及删除
    def TestMethod7(self):
        FunctionName = self.get_current_function_name()
        test = TR.Result_Action(self.ClassName, FunctionName)
        self.TestMethod4()
        if self.ACTION.Check_Access_Modify_Delete_Authority():
            return test.show_ok_result()
        else:
            test.set_error("访问修改删除权限功能不正确")
            return test.show_error_result()

    # TM8:验证新建用户停用后，登录失败
    def TestMethod8(self):
        FunctionName = self.get_current_function_name()
        test = TR.Result_Action(self.ClassName, FunctionName)
        self.TestMethod1()
        if not self.ACTION.OFF_one():
            test.set_error("单独停用按钮不可用")
            return test.show_error_result()
        elif self.ACTION.Login():
            return test.show_ok_result()
        else:
            test.set_error("单独停用功能不生效")
            return test.show_error_result()

    # TM9:验证新建用户停用再启用后，登录成功
    def TestMethod9(self):
        FunctionName = self.get_current_function_name()
        test = TR.Result_Action(self.ClassName, FunctionName)
        self.TestMethod1()
        if not self.ACTION.OFF_one():
            test.set_error("单独停用按钮不可用")
            return test.show_error_result()
        elif not self.ACTION.ON_one():
            test.set_error("单独启用按钮不可用")
            return test.show_error_result()
        elif self.ACTION.Login():
            return test.show_ok_result()
        else:
            test.set_error("单独启用功能不生效")
            return test.show_error_result()

    # TM10:验证全部停用按钮是否生效，非管理员用户登录失败
    def TestMethod10(self):
        FunctionName = self.get_current_function_name()
        test = TR.Result_Action(self.ClassName, FunctionName)
        self.TestMethod1()
        if not self.ACTION.OFF_all():
            test.set_error("全部停用按钮不可用")
            return test.show_error_result()
        elif not self.ACTION.Login():
            test.set_error("全部停用功能不生效")
            return test.show_error_result()
        else:
            return test.show_ok_result()

    # TM11:验证停用后再全部启用，非管理员用户登录成功
    def TestMethod11(self):
        FunctionName = self.get_current_function_name()
        test = TR.Result_Action(self.ClassName, FunctionName)
        self.TestMethod1()
        if not self.ACTION.OFF_all():
            test.set_error("全部停用按钮不可用")
            return test.show_error_result()
        elif not self.ACTION.ON_all():
            test.set_error("全部启用按钮不可用")
            return test.show_error_result()
        elif not self.ACTION.Login():
            test.set_error("全部启用功能不生效")
            return test.show_error_result()
        else:
            return test.show_ok_result()


    # TM12:验证编辑功能，新建用户为访问权限编辑为访问修改删除权限后，验证是否生效
    def TestMethod12(self):
        FunctionName = self.get_current_function_name()
        test = TR.Result_Action(self.ClassName, FunctionName)
        self.TestMethod1()
        if not self.ACTION.EDIT_Access_Modify_Delete():
            test.set_error("编辑功能不生效")
            return test.show_error_result()
        elif not self.ACTION.Check_Access_Modify_Delete_Authority():
            test.set_error("访问修改删除功能不生效")
            return test.show_error_result()
        else:
            return test.show_ok_result()


    def run_tests(self):
        i = 0
        for Fname, Func in M2_4_2_WebAccountManage.__dict__.items():
            if type(Func) == FunctionType and self.TestData["测试方法"] == Fname:
                Func(self)
                i = i + 1
            else:
                continue
        if i == 0:
            print("没有此测试例")
            return False