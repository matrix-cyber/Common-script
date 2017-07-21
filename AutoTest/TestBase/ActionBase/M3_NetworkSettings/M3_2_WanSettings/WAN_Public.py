import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
import time


class WAN_Public:
    #初始化：（1）将WEB句柄交给此模块  （2）导入该模块的CSS元素库及测试数据
    def __init__(self, web_handler,ssh_handler,TestData): #模块初始化
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu #目录元素库
        self.ElementCss = CSS.ElementBase.WAN_Public #模块元素库
        self.TestData = TestData #测试数据
        self.bool = True

    # 封装查找命令
    def find_element(self, para): #公用
        return self.web_handler.find_element_by_css_selector(para)

    def UNBunding(self):
        time.sleep(4)
        self.find_element(self.ElementCss["解绑"]).click()
        time.sleep(2)
        self.web_handler.accept_confirm_msg()
        time.sleep(2)

    def Bunding(self):
        self.find_element(self.ElementCss["选择网卡"]).click()
        time.sleep(3)
        self.find_element(self.ElementCss["eth4"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["绑定"]).click()
        time.sleep(2)
        self.web_handler.refresh_page()
        time.sleep(2)

    def EDIT_CloneMAC(self):
        self.find_element(self.ElementCss["高级设置"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["克隆MAC"]).clear()
        self.find_element(self.ElementCss["克隆MAC"]).send_keys(self.TestData["克隆MAC"])
        time.sleep(1)
        self.find_element(self.ElementCss["全局保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["保存确定"]).click()
        time.sleep(2)
        self.web_handler.refresh_page()
        time.sleep(2)
        if self.find_element(self.ElementCss["克隆MAC"]).get_attribute("value") != self.TestData["克隆MAC"]:
            self.bool = False

    def Check_EditMAC(self):
        if not self.bool and (self.TestData["预期结果"] == "添加失败"):
            return True
        elif self.bool and self.TestData["预期结果"] == "添加成功" :
            return True
        else:
            return False

    def Check_CloneMAC(self):
        output = self.ssh_handler.exec_cmd("ifconfig")
        DataGroup = output.split("\n\n")
        len1 = len(DataGroup)
        i = 0
        for i in range(0, len1):
            if self.TestData["网卡"] in DataGroup[i]:
                if DataGroup[i].find(self.TestData["克隆MAC"]) > 0:
                    print(DataGroup[i])
                else:
                    continue
            else:
                continue
        if i==len1:
            return False
        else:
            return True


