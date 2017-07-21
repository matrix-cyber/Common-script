import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
import TestBase.DataBase as TD
import time

class WebAccountManage:
    #初始化：（1）将WEB句柄交给此模块  （2）导入该模块的CSS元素库及测试数据
    def __init__(self, web_handler,TestData): #模块初始化
        self.web_handler = web_handler
        self.MenuCss = CSS.ElementBase.Menu #目录元素库
        self.ElementCss = CSS.ElementBase.WebAccountMange #模块元素库
        self.TestData = TestData #测试数据
        self.bool = True

    # 封装查找命令
    def find_element(self, para): #公用
        return self.web_handler.find_element_by_css_selector(para)

    def ADD_Access(self):
        self.find_element(self.ElementCss["添加"]).click()
        self.find_element(self.ElementCss["用户名"]).send_keys(self.TestData["用户名"])
        self.find_element(self.ElementCss["密码"]).send_keys(self.TestData["密码"])
        time.sleep(2)
        self.find_element(self.ElementCss["权限等级"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["访问权限"]).click()
        self.find_element(self.ElementCss["权限等级保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["安全IP地址"]).send_keys(self.TestData["安全IP地址"])
        self.find_element(self.ElementCss["确定"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["确认密码"]).send_keys(self.TestData["密码"])
        self.find_element(self.ElementCss["确认密码保存"]).click()
        time.sleep(3)
        try:
            self.find_element(self.ElementCss["用户名已存在"])
            self.find_element(self.ElementCss["重复用户确定"]).click()
            return False
        except:
            time.sleep(2)

        self.web_handler.refresh_page()
        try:
            self.find_element(self.ElementCss["编辑用户名"])
            self.bool = True
            return self.Check_Add()
        except:
            self.bool = False
            return self.Check_Add()

    def ADD_Access_Modify(self):
        self.find_element(self.ElementCss["添加"]).click()
        self.find_element(self.ElementCss["用户名"]).send_keys(self.TestData["用户名"])
        self.find_element(self.ElementCss["密码"]).send_keys(self.TestData["密码"])
        time.sleep(2)
        self.find_element(self.ElementCss["权限等级"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["访问修改权限"]).click()
        self.find_element(self.ElementCss["权限等级保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["安全IP地址"]).send_keys(self.TestData["安全IP地址"])
        self.find_element(self.ElementCss["确定"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["确认密码"]).send_keys(self.TestData["密码"])
        self.find_element(self.ElementCss["确认密码保存"]).click()
        time.sleep(3)
        try:
            self.find_element(self.ElementCss["用户名已存在"])
            self.find_element(self.ElementCss["重复用户确定"]).click()
            return False
        except:
            time.sleep(2)

        self.web_handler.refresh_page()
        try:
            self.find_element(self.ElementCss["编辑用户名"])
            self.bool = True
            return self.Check_Add()
        except:
            self.bool = False
            return self.Check_Add()


    def ADD_Access_Modify_Delete(self):
        self.find_element(self.ElementCss["添加"]).click()
        self.find_element(self.ElementCss["用户名"]).send_keys(self.TestData["用户名"])
        self.find_element(self.ElementCss["密码"]).send_keys(self.TestData["密码"])
        time.sleep(2)
        self.find_element(self.ElementCss["权限等级"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["访问修改权限"]).click()
        self.find_element(self.ElementCss["权限等级保存"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["安全IP地址"]).send_keys(self.TestData["安全IP地址"])
        self.find_element(self.ElementCss["确定"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["确认密码"]).send_keys(self.TestData["密码"])
        self.find_element(self.ElementCss["确认密码保存"]).click()
        time.sleep(3)
        try:
            self.find_element(self.ElementCss["用户名已存在"])
            self.find_element(self.ElementCss["重复用户确定"]).click()
            return False
        except:
            time.sleep(2)

        self.web_handler.refresh_page()
        try:
            self.find_element(self.ElementCss["编辑用户名"])
            self.bool = True
            return self.Check_Add()
        except:
            self.bool = False
            return self.Check_Add()

    def EDIT_Access_Modify(self):
        self.find_element(self.ElementCss["编辑"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["编辑权限"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["访问修改权限"]).click()
        self.find_element(self.ElementCss["权限等级保存"]).click()
        time.sleep(2)
        self.web_handler.refresh_page()
        time.sleep(2)
        if self.find_element(self.ElementCss["编辑用户名"]).get_attribute("value") == self.TestData["用户名"]:
            return True
        else:
            return False

    def EDIT_Access_Modify_Delete(self):  #编辑权限
        self.find_element(self.ElementCss["编辑"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["编辑权限"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["访问修改删除权限"]).click()
        self.find_element(self.ElementCss["权限等级保存"]).click()
        time.sleep(2)
        self.web_handler.refresh_page()
        time.sleep(2)
        if self.find_element(self.ElementCss["编辑用户名"]).get_attribute("value")==self.TestData["用户名"]:
            return True
        else:
            return False

    def ON_one(self): #公用
        user_stat = self.find_element(self.ElementCss["启停用状态"]).text
        if user_stat == "已启用":
            return True
        else:
            self.find_element(self.ElementCss["启用"]).click()
            time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        new_stat = self.find_element(self.ElementCss["启停用状态"]).text
        if new_stat == "已启用":
            return True
        else:
            return False

    def OFF_one(self): #公用
        user_stat = self.find_element(self.ElementCss["启停用状态"]).text
        if user_stat == "已停用":
            return True
        else:
            self.find_element(self.ElementCss["停用"]).click()
            time.sleep(2)
            self.web_handler.accept_confirm_msg()
            time.sleep(2)
        self.web_handler.refresh_page()
        time.sleep(3)
        new_stat = self.find_element(self.ElementCss["启停用状态"]).text
        if new_stat == "已停用":
            return True
        else:
            return False

    def DELETE_one(self): #公用
        self.find_element(self.ElementCss["删除"]).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        try:
            self.find_element(self.ElementCss["编辑用户名"])
            return False
        except:
            return True

    def ON_all(self): #公用
        self.find_element(self.ElementCss["全部选中"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["全部启用"]).click()
        self.web_handler.refresh_page()
        time.sleep(2)
        new_stat = self.find_element(self.ElementCss["启停用状态"]).text
        if new_stat == "已启用":
            return True
        else:
            return False

    def OFF_all(self): #公用
        self.find_element(self.ElementCss["全部选中"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["全部停用"]).click()
        time.sleep(2)
        self.web_handler.accept_confirm_msg()
        time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        new_stat = self.find_element(self.ElementCss["启停用状态"]).text
        if new_stat == "已停用":
            return True
        else:
            return False

    def DELETE_all(self): #公用
        self.find_element(self.ElementCss["全部选中"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["全部删除"]).click()
        time.sleep(2)
        self.web_handler.accept_confirm_msg()
        time.sleep(2)
        try:
            self.find_element(self.ElementCss["编辑用户名"])
            return False
        except:
            return True

    def Access_Authority(self):
        self.find_element(self.ElementCss["编辑权限"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["访问权限"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["权限等级保存"]).click()
        time.sleep(2)

    def Access_Modify_Authority(self):
        self.find_element(self.ElementCss["编辑权限"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["访问修改权限"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["权限等级保存"]).click()
        time.sleep(2)

    def Access_Modify_Delete_Authority(self):
        self.find_element(self.ElementCss["编辑权限"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["访问修改删除权限"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["权限等级保存"]).click()
        time.sleep(2)

    def Login(self):
        self.find_element(self.ElementCss["退出登录"]).click()
        time.sleep(2)
        link = self.find_element(self.ElementCss["登录用户"])
        link.clear()
        link.send_keys(self.TestData["用户名"])
        link = self.find_element(self.ElementCss["登录密码"])
        link.clear()
        link.send_keys(self.TestData["密码"])
        self.find_element(self.ElementCss["登录"]).click()
        time.sleep(5)
        self.web_handler.refresh_page()
        time.sleep(2)
        try:
            self.find_element(self.ElementCss["登录用户"])
            self.bool = False
            return self.Check_Login()
        except:
            self.bool = True
            return self.Check_Login()

    def Check_Add(self): #公用
        if self.bool and (self.TestData["预期结果"] == "添加失败"):
            print("用户信息：", self.TestData)
            return False
        elif not self.bool and self.TestData["预期结果"] == "登录成功":
            print("用户信息：",self.TestData)
            return False
        else:
            return True

    def Check_Login(self):
        if not self.bool and self.TestData["预期结果"] == "登录成功":
            return False
        elif self.bool and self.TestData["预期结果"] == "登录失败":
            return False
        else:
            return True

    def Check_Access_Authority(self):
        NetworkElement = CSS.ElementBase.DnsSettings
        NetworkData = TD.TestData.DnsSettings
        try:
            self.find_element(self.MenuCss["网络设置"]).click()
            time.sleep(2)
            self.find_element(self.MenuCss["DNS设置"]).click()
            time.sleep(2)
        except:
            return False
        self.find_element(NetworkElement["添加"]).click()
        time.sleep(1)
        self.find_element(NetworkElement["域名"]).send_keys(NetworkData[0]["域名"])
        self.find_element(NetworkElement["IP"]).send_keys(NetworkData[0]["IP"])
        self.find_element(NetworkElement["备注"]).send_keys(NetworkData[0]["备注"])
        try:
            self.find_element(NetworkElement["确定"]).click()
            time.sleep(1)
            self.web_handler.accept_confirm_msg()
            return False
        except:
            time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        try:
            self.find_element(NetworkElement["全部选择"]).click()
            time.sleep(1)
            self.find_element(NetworkElement["全部删除"]).click()
            time.sleep(1)
            self.web_handler.accept_confirm_msg()
            return False
        except:
            return True

    def Check_Access_Modify_Authority(self):
        NetworkElement = CSS.ElementBase.DnsSettings
        NetworkData = TD.TestData.DnsSettings
        try:
            self.find_element(self.MenuCss["网络设置"]).click()
            time.sleep(2)
            self.find_element(self.MenuCss["DNS设置"]).click()
            time.sleep(2)
        except:
            return False
        self.find_element(NetworkElement["添加"]).click()
        time.sleep(1)
        self.find_element(NetworkElement["域名"]).send_keys(NetworkData[0]["域名"])
        self.find_element(NetworkElement["IP"]).send_keys(NetworkData[0]["IP"])
        self.find_element(NetworkElement["备注"]).send_keys(NetworkData[0]["备注"])
        self.find_element(NetworkElement["确定"]).click()
        time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        try:
            self.find_element(NetworkElement["域名"])
        except:
            return False
        try:
            self.find_element(NetworkElement["单独删除"]).click()
            time.sleep(1)
            self.web_handler.accept_confirm_msg()
            return False
        except:
            time.sleep(1)
            self.web_handler.refresh_page()
            time.sleep(2)
        try:
            self.find_element(NetworkElement["全部选择"]).click()
            time.sleep(1)
            self.find_element(NetworkElement["全部删除"]).click()
            time.sleep(1)
            self.web_handler.accept_confirm_msg()
            return False
        except:
            return True

    def Check_Access_Modify_Delete_Authority(self):
        NetworkElement = CSS.ElementBase.DnsSettings
        NetworkData = TD.TestData.DnsSettings
        try:
            self.find_element(self.MenuCss["网络设置"]).click()
            time.sleep(2)
            self.find_element(self.MenuCss["DNS设置"]).click()
            time.sleep(2)
        except:
            return False
        self.find_element(NetworkElement["添加"]).click()
        time.sleep(1)
        self.find_element(NetworkElement["域名"]).send_keys(NetworkData[0]["域名"])
        self.find_element(NetworkElement["IP"]).send_keys(NetworkData[0]["IP"])
        self.find_element(NetworkElement["备注"]).send_keys(NetworkData[0]["备注"])
        self.find_element(NetworkElement["确定"]).click()
        time.sleep(1)
        try:
            self.find_element(NetworkElement["权限提示框"])
            print("OK1")
            return False
        except Exception as e:
            time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        try:
            self.find_element(NetworkElement["域名"])
        except:
            print("OK2")
            return False
        try:
            self.find_element(NetworkElement["单独删除"]).click()
            time.sleep(2)
            self.web_handler.accept_confirm_msg()
        except:
            return False
        time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        self.find_element(NetworkElement["全部选择"]).click()
        time.sleep(1)
        try:
            self.find_element(NetworkElement["全部删除"]).click()
            time.sleep(2)
            self.web_handler.accept_confirm_msg()
        except:
            return False
        time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        try:
            self.find_element(NetworkElement["暂无数据"])
            return True
        except:
            return False