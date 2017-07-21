# -*- coding:utf-8 -*-
import inspect
import time
from types import FunctionType

import TestBase.ActionBase.Base_Action.Result_Action as TR
import TestBase.ActionBase.M5_FlowControl.M5_3_IPSpeedLimit as ACTION
import TestBase.DataBase as TD
import TestBase.ElementBase as CSS


class IPSpeedLimit:
    def __init__(self, web_handler, ssh_handler, **new_test_data):  # 模块初始化
        self.web_handler = web_handler  # 页面连接
        self.ssh_handler = ssh_handler  # 后台连接
        self.MenuCss = CSS.ElementBase.Menu  # 目录元素库
        self.LoginData = TD.TestData.Login  # 登录页面数据
        self.ClassName = self.__class__.__name__  # 类名称
        self.function_name = ""  # 函数名
        self.test_count = TR.Result_Count()  # 结果统计函数
        self.test_state = TR.Result_Action()  # 结果输出函数
        self.TestData = new_test_data   # 本模块测试数据——需更新
        self.ElementCss = CSS.ElementBase.IPSpeedLimit  # 本模块元素库——需更新
        self.ACTION = ACTION.IPSpeedLimit(self.web_handler, self.ssh_handler, self.TestData)  # 本模块动作库——需更新

    def __del__(self):
        self.ACTION.delete_all()

    def find_element(self, para):  # 封装查找命令
        return self.web_handler.find_element_by_css_selector(para)

    @staticmethod
    def get_current_function_name():  # 返回当前函数名称
        return inspect.stack()[1][3]

    def test_add(self):  # 验证添加
        function_name = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, function_name)
        self.ACTION.delete_all()
        if not self.ACTION.add():
            self.test_state.set_error("添加有问题")
            return False
        else:
            return True

    def test_host(self):
        if not self.test_add():
            self.test_state.set_error("添加有问题")
            return False
        function_name = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, function_name)
        if not self.ACTION.check_speed_limit():
            self.test_state.set_error("限速不生效")
            return False
        else:
            return True

    def run_method(self):
        i = 0
        for name, func in IPSpeedLimit.__dict__.items():
            j = i
            if type(func) == FunctionType and self.TestData["测试方法"] == name:
                i = j + 1
                if func(self):
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
        test_data_all = TD.TestData.IPSpeedLimit
        data_len = len(test_data_all)
        run_num = 0
        for i in range(0, data_len):
            new_run_num = run_num
            if test_data_all[i]["是否执行"] == "Y":
                print(test_data_all[i]["测试例"])
                new_run = IPSpeedLimit(self.web_handler, self.ssh_handler, **test_data_all[i])
                test_bool = new_run.run_method()
                if test_bool:
                    self.test_count.add_RightNum()
                else:
                    self.test_count.add_ErrorNum()
                time.sleep(3)
                run_num = new_run_num + 1
            else:
                continue
        if run_num == 0:
            print("无执行的测试例")
        else:
            self.test_count.show_all_result()
