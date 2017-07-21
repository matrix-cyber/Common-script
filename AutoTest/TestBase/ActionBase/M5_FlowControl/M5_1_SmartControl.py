import sys

sys.path.append("..")
import TestBase.ElementBase as CSS
import TestBase.TopoBase as Topo
import time


class SmartControl:

    def __init__(self, web_handler, ssh_handler, TestData):
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu
        self.ElementCss = CSS.ElementBase.SmartControl
        self.TestData = TestData
        self.bool = True

    def find_element(self, pera):
        return self.web_handler.find_element_by_css_selector(pera)

    def find_element_value(self, pera, get):
        return self.web_handler.find_element_by_css_selector(pera).get_attribute(get)

    def check_on(self):
        txt = self.find_element(self.ElementCss['选择模式']).txt
        if txt == 'colorR fl':
            self.find_element(self.ElementCss['开启按钮']).click()
            time.sleep(1)
        return True

    def add_lines(self):
        num = int(self.find_element(self.ElementCss['全部线路']).size())
        num += 2
        for i in range(2, num):
            txt = self.find_element_value(self.ElementCss['条目线路1']+i+self.ElementCss['条目线路2'], 'title')
            if txt == self.TestData['流控接口']:
                self.find_element(self.ElementCss['条目修改1']+i+self.ElementCss['条目修改2']).click()
                self.find_element(self.ElementCss['条目上行1']+i+self.ElementCss['条目上行2']).clear()
                self.find_element(self.ElementCss['条目上行1']+i+self.ElementCss['条目上行2']).send_keys(self.TestData['线路上行'])
                self.find_element(self.ElementCss['条目下行1']+i+self.ElementCss['条目下行2']).clear()
                self.find_element(self.ElementCss['条目下行1']+i+self.ElementCss['条目下行2']).send_keys(self.TestData['线路上行'])
                self.find_element(self.ElementCss['条目确定1']+i+self.ElementCss['条目确定2']).click()
                txt = self.find_element_value(self.ElementCss['条目状态1']+i+self.ElementCss['条目状态2'], 'class')
                if txt == 'colorR':
                    self.find_element(self.ElementCss['条目加入1']+i+self.ElementCss['条目加入2']).click()
                    return True
            return False

    def add_smart(self):
        if self.TestData['上行'] == '':
            return True
        self.find_element(self.ElementCss['添加']).click()
        if self.TestData['内网IP'] == 'localhost':
            self.find_element(self.ElementCss['内网IP']).clear()
            self.find_element(self.ElementCss['内网IP']).send_keys(Topo.TEST_PC)
        self.find_element(self.ElementCss['独立上行']).clear()
        self.find_element(self.ElementCss['独立上行']).send_keys(self.TestData['独立上行'])
        self.find_element(self.ElementCss['独立下行']).clear()
        self.find_element(self.ElementCss['独立下行']).send_keys(self.TestData['独立下行'])
        if self.TestData['优先级'] != '':
            self.find_element(self.ElementCss['优先级']).click()
            self.find_element(self.ElementCss[self.TestData['优先级']]).click()
        if self.TestData['时间段'] != '':
            self.find_element(self.ElementCss['时间段']).clear()
            self.find_element(self.ElementCss['时间段']).send_keys(self.TestData['时间段'])
        self.find_element(self.ElementCss['备注']).clear()
        self.find_element(self.ElementCss['备注']).send_keys()
        self.find_element(self.ElementCss['确定']).click()
        time.sleep(1)
        return True

    def check_web(self):
        try:
            error = self.find_element('.input_error')
            if self.TestData['预期结果'] == '添加失败':
                return True
            elif self.TestData['预期结果'] != '添加失败':
                return False
        except:
            if self.TestData['预期结果'] == '添加失败':
                return False
            return  True

    def on_one(self):
        self.find_element(self.ElementCss['启用']).click()
        time.sleep(1)
        txt = self.find_element(self.ElementCss['限速状态']).txt
        if txt != '已启用':
            return False
        return True

    def on_all(self):
        self.find_element(self.ElementCss['全选']).click()
        self.find_element(self.ElementCss['启用多']).click()
        time.sleep(1)
        txt = self.find_element(self.ElementCss['限速状态']).txt
        if txt != '已启用':
            return False
        return True

    def off_one(self):
        self.find_element(self.ElementCss['停用']).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        time.sleep(1)
        txt = self.find_element(self.ElementCss['限速状态']).txt
        if txt != '已停用':
            return False
        return True

    def off_all(self):
        self.find_element(self.ElementCss['全选']).click()
        self.find_element(self.ElementCss['停用多']).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        time.sleep(1)
        txt = self.find_element(self.ElementCss['限速状态']).txt
        if txt != '已停用':
            return False
        return True

    def del_one(self):
        self.find_element(self.ElementCss['删除']).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        time.sleep(1)
        try:
            self.find_element(self.ElementCss['内网IP'])
            return False
        except:
            return True

    def del_all(self):
        self.find_element(self.ElementCss['全选']).click()
        self.find_element(self.ElementCss['删除多']).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        time.sleep(1)
        try:
            self.find_element(self.ElementCss['内网IP'])
            return False
        except:
            return True

    def change_action(self):
        return True