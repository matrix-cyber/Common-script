# sys.path.append("..")
import inspect
import time
from types import FunctionType

import TestBase.ActionBase.Base_Action.Result_Action as TR
import TestBase.ActionBase.M3_NetworkSettings.M3_4_FlowSettings.M3_4_2_ProtocolFlow as FS_AC
import TestBase.DataBase as TD
import TestBase.ElementBase as CSS


class ProtocolFlow:

    def __init__(self, web_handler, ssh_handler, **new_test_data):
        # 初始化参数
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu
        self.Elements = CSS.ElementBase.ProFlow
        self.TestData = new_test_data
        self.LoginData = TD.TestData.Login
        self.ACTION = FS_AC.ProtocolFlow(self.web_handler, self.ssh_handler, self.TestData)
        self.ClassName = self.__class__.__name__
        self.FunctionName = ""
        self.test_count = TR.Result_Count()
        self.test_state = TR.Result_Action()

    def __del__(self):
        self.ACTION.delete_all()

    def find_element(self, pera):
        return self.web_handler.find_element_by_css_selector(pera)

    def find_element_value(self, pera, get):
        return self.web_handler.find_element_by_css_selector(pera).get_attribute(get)

    @staticmethod
    def get_current_function_name():
        return inspect.stack()[1][3]

    def add_flow(self):
        self.FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, self.FunctionName)
        time.sleep(1)
        self.ACTION.syn_proxy_state()
        if not self.ACTION.add():
            self.test_state.set_error('异常添加')
            return False

        if not self.ACTION.check_web():
            self.test_state.set_error('页面校验失败')
            return False

        if self.TestData['预期结果'] == '添加失败':
            return True

        if not self.ACTION.check_action(self.TestData['测试域名']):
            self.test_state.set_error('功能验证失败')
            return False
        return True

    def stop_flow(self):
        self.FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, self.FunctionName)
        time.sleep(1)
        if not self.ACTION.add():
            self.test_state.set_error('异常添加')
            return False

        if not self.ACTION.check_web():
            self.test_state.set_error('页面校验失败')
            return False

        if not self.ACTION.off_one():
            self.test_state.set_error('停用条目失败')
            return False

        if not self.ACTION.check_action(self.TestData['测试域名']):
            self.test_state.set_error('停用条目,功能校验失败')
            return False
        return True

    def start_flow(self):
        self.FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, self.FunctionName)
        time.sleep(1)
        if not self.ACTION.add():
            self.test_state.set_error('异常添加')
            return False

        if not self.ACTION.check_web():
            self.test_state.set_error('页面校验失败')
            return False

        if not self.ACTION.off_one():
            self.test_state.set_error('停用条目失效')
            return False

        if not self.ACTION.on_one():
            self.test_state.set_error('启用条目失效')
            return False

        if not self.ACTION.check_action(self.TestData['测试域名']):
            self.test_state.set_error('启用条目,功能验证失效')
            return False
        return True

    def change_flow(self):
        self.FunctionName = self.get_current_function_name()
        self.test_state = TR.Result_Action(self.ClassName, self.FunctionName)
        time.sleep(1)
        if not self.ACTION.add():
            self.test_state.set_error('异常添加')
            return False

        if not self.ACTION.check_web():
            self.test_state.set_error('页面校验失败')
            return False

        if not self.ACTION.change_action():
            self.test_state.set_error('修改条目失败')
            return False

        if not self.ACTION.check_action(self.TestData['测试域名']):
            self.test_state.set_error('修改条目,功能验证失败')
            return False
        return True

    def run_method(self):
        i = 0
        for name, func in ProtocolFlow.__dict__.items():
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
        test_data_all = TD.TestData.ProFlow
        data_len = len(test_data_all)
        run_num = 0
        for i in range(0, data_len):
            new_run_num = run_num
            if test_data_all[i]["是否执行"] == "Y":
                print(test_data_all[i]["测试例"])
                new_run = ProtocolFlow(self.web_handler, self.ssh_handler, **test_data_all[i])
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
