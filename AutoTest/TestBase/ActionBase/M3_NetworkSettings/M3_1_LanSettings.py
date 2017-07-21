import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
import TestBase.DataBase as TD
import time

class LanSettings:
    #初始化：（1）将WEB句柄交给此模块  （2）导入该模块的CSS元素库及测试数据
    def __init__(self, web_handler,TestData): #模块初始化
        self.web_handler = web_handler
        self.MenuCss = CSS.ElementBase.Menu #目录元素库
        self.ElementCss = CSS.ElementBase.LanSettings #模块元素库
        self.TestData = TestData #测试数据
        self.bool = True

    # 封装查找命令
    def find_element(self, para): #公用
        return self.web_handler.find_element_by_css_selector(para)

    def ADD_Lan(self):
        time.sleep(2)
        self.find_element(self.ElementCss["添加"]).click()
        time.sleep(3)
        self.find_element(self.ElementCss["选网卡"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["eth1"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["绑定"]).click()
        time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        try:
            self.find_element(self.ElementCss["解绑"])
            return True
        except:
            return False

    def DELETE_Lan(self):
        self.find_element(self.ElementCss["解绑"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["删除此LAN口"]).click()
        time.sleep(2)
        self.web_handler.refresh_page()
        time.sleep(2)
        try:
            self.find_element(self.ElementCss["LAN2"])
            return False
        except:
            return True

    def BaseSettings(self):
        self.find_element(self.ElementCss["克隆MAC"]).clear()
        self.find_element(self.ElementCss["克隆MAC"]).send_keys(self.TestData["克隆MAC"])
        self.find_element(self.ElementCss["IP"]).clear()
        self.find_element(self.ElementCss["IP"]).send_keys(self.TestData["IP"])
        self.find_element(self.ElementCss["子网掩码"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["24位掩码"]).click()
        self.find_element(self.ElementCss["添加扩展IP"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["扩展IP"]).send_keys(self.TestData["扩展IP"])
        self.find_element(self.ElementCss["扩展IP掩码"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["扩展24位掩码"]).click()
        self.find_element(self.ElementCss["确认"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["保存"]).click()
        self.web_handler.refresh_page()
        time.sleep(2)
        try:
            if self.TestData["克隆MAC"] == self.find_element(self.ElementCss["克隆MAC"]).get_attribute("value") \
                    and self.TestData["IP"] == self.find_element(self.ElementCss["IP"]).get_attribute("value")\
                    and self.TestData["扩展IP"] == self.find_element(self.ElementCss["扩展IP"]).get_attribute("value"):
                self.bool = True
            else:
                self.bool = False
        except:
            self.bool = False
        if self.Check_ADD():
            return True
        else:
            return False

    def BindExtendCard(self):
        self.find_element(self.ElementCss["扩展网卡绑定"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["eth2"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["保存"]).click()
        time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        self.find_element(self.ElementCss["扩展网卡绑定"]).click()
        time.sleep(1)
        try:
            self.find_element(self.ElementCss["选中eth2"])
            return True
        except:
            return False

    def LAN_Access(self):
        self.find_element(self.ElementCss["高级设置"]).click()
        time.sleep(2)
        try:
            if "true" == self.find_element(self.ElementCss["LAN互访"]).get_attribute("checked"):
                return True
            else:
                self.find_element(self.ElementCss["LAN互访"]).click()
                time.sleep(1)
                self.find_element(self.ElementCss["保存"]).click()
                time.sleep(1)
                return True
        except:
            print("OK")
            return False

    def LAN_NOT_Access(self):
        self.find_element(self.ElementCss["高级设置"]).click()
        time.sleep(2)
        lan_state = self.find_element(self.ElementCss["LAN互访"]).get_attribute("checked")
        if lan_state == "true":
            self.find_element(self.ElementCss["LAN互访"]).click()
            time.sleep(1)
            self.find_element(self.ElementCss["保存"]).click()
            time.sleep(1)
            return True
        else:
            return True

    def Access_LAN1(self):
        self.find_element(self.ElementCss["LAN1"]).click()
        time.sleep(1)

    def Access_LAN2(self):
        self.find_element(self.ElementCss["LAN2"]).click()
        time.sleep(2)

    def Check_ADD(self):
        if not self.bool and self.TestData["预期结果"] == "添加失败":
            return True
        elif self.bool and self.TestData["预期结果"] == "添加成功":
            return True
        else:
            return False







