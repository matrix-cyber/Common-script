# -*- coding:utf-8 -*-
import time
import TestBase.ActionBase.Base_Action.Speed_Test as ST
import TestBase.ElementBase as CSS
import TestBase.TopoBase as Topo


class IPSpeedLimit:
    def __init__(self, web_handler,ssh_handler, test_data):  # 模块初始化
        self.web_handler = web_handler  # 页面连接
        self.ssh_handler = ssh_handler  # 后台连接
        self.MenuCss = CSS.ElementBase.Menu  # 目录元素库
        self.add_bool = True
        self.fun_bool = True
        self.ElementCss = CSS.ElementBase.IPSpeedLimit # 本模块元素库——需更新
        self.TestData = test_data  # 本模块测试数据——需更新

    def find_element(self, para):   # 封装查找命令
        return self.web_handler.find_element_by_css_selector(para)

    def add(self):  # 添加基础规则
        time.sleep(2)
        self.find_element(self.ElementCss["添加"]).click()
        time.sleep(3)
        print("OK1")
        self.find_element(self.ElementCss["内网IP"]).click()
        print("OK2")
        time.sleep(2)
        self.find_element(self.ElementCss["IP"]).clear()
        if self.TestData["IP"] == "localhost":
            ip_addr = Topo.TEST_PC
        else:
            ip_addr = self.TestData["IP"]
        self.find_element(self.ElementCss["IP"]).send_keys(ip_addr)
        self.find_element(self.ElementCss["添加IP"]).click()
        self.find_element(self.ElementCss["内网IP确定"]).click()
        self.find_element(self.ElementCss["上行"]).clear()
        self.find_element(self.ElementCss["上行"]).send_keys(self.TestData["上行"])
        self.find_element(self.ElementCss["下行"]).clear()
        self.find_element(self.ElementCss["下行"]).send_keys(self.TestData["下行"])
        time.sleep(1)
        if self.TestData["周期"]!="":
            weekday = self.TestData["周期"]
            self.find_element(self.ElementCss["周期"]).click()
            self.find_element(self.ElementCss[weekday])
        else:
            pass
        time.sleep(1)
        self.find_element(self.ElementCss["时间段"]).clear()
        self.find_element(self.ElementCss["时间段"]).send_keys(self.TestData["时间段"])
        self.find_element(self.ElementCss["备注"]).send_keys(self.TestData["备注"])
        self.find_element(self.ElementCss["编辑确定"]).click()
        time.sleep(1)
        try:
            self.find_element(self.ElementCss["内网IP报错"])
            self.bool = False
            return self.check_add()
        except:
            pass
        try:
            self.find_element(self.ElementCss["上行报错"])
            self.bool = False
            return self.check_add()
        except:
            pass
        try:
            self.find_element(self.ElementCss["下行报错"])
            self.bool = False
            return self.check_add()
        except:
            pass
        try:
            self.find_element(self.ElementCss["周期报错"])
            self.bool = False
            return self.check_add()
        except:
            pass
        try:
            self.find_element(self.ElementCss["时间段报错"])
            self.bool = False
            return self.check_add()
        except:
            pass
        self.web_handler.refresh_page()
        time.sleep(1)
        try:
            self.find_element(self.ElementCss["单独停用"])
            self.bool = True
            return self.check_add()
        except:
            self.bool = False
            return self.check_add()

    def edit_ip(self):  # 编辑协议
        time.sleep(2)
        self.find_element(self.ElementCss["编辑"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["内网IP"]).click()
        self.find_element(self.ElementCss["选中IP"]).click()
        self.find_element(self.ElementCss["删除IP"]).click()
        if self.TestData["IP"] == "localhost":
            ip_addr = Topo.TEST_PC
        else:
            ip_addr = self.TestData["IP"]
        self.find_element(self.ElementCss["IP"]).send_keys(ip_addr)
        self.find_element(self.ElementCss["添加IP"]).click()
        self.find_element(self.ElementCss["内网IP确定"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["编辑确定"]).click()

    def edit_upload(self):  # 编辑SIP
        time.sleep(2)
        self.find_element(self.ElementCss["编辑"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["上行"]).clear()
        self.find_element(self.ElementCss["上行"]).send_keys(self.TestData["上行"])
        self.find_element(self.ElementCss["编辑确定"]).click()

    def edit_download(self):  # 编辑DIP
        time.sleep(2)
        self.find_element(self.ElementCss["编辑"]).click()
        time.sleep(2)
        self.find_element(self.ElementCss["下行"]).clear()
        self.find_element(self.ElementCss["下行"]).send_keys(self.TestData["下行"])
        self.find_element(self.ElementCss["编辑确定"]).click()

    def on_one(self):  # 公用
        user_stat = self.find_element(self.ElementCss["状态"]).text
        if user_stat == "已启用":
            return True
        else:
            self.find_element(self.ElementCss["单独启用"]).click()
            time.sleep(1)
        self.web_handler.refresh_page()
        time.sleep(2)
        new_stat = self.find_element(self.ElementCss["状态"]).text
        if new_stat == "已启用":
            return True
        else:
            return False

    def off_one(self):  # 公用
        time.sleep(2)
        user_stat = self.find_element(self.ElementCss["状态"]).text
        if user_stat == "已停用":
            return True
        else:
            self.find_element(self.ElementCss["单独停用"]).click()
            time.sleep(2)
            self.web_handler.accept_confirm_msg()
            time.sleep(2)
        time.sleep(2)
        new_stat = self.find_element(self.ElementCss["状态"]).text
        if new_stat == "已停用":
            return True
        else:
            return False

    def delete_one(self):  # 公用
        self.find_element(self.ElementCss["删除"]).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        return True

    def on_all(self): #公用
        self.find_element(self.ElementCss["全部选择"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["全部启用"]).click()
        self.web_handler.refresh_page()
        time.sleep(2)
        new_stat = self.find_element(self.ElementCss["状态"]).text
        if new_stat == "已启用":
            return True
        else:
            return False

    def off_all(self):  # 公用
        self.find_element(self.ElementCss["全部选择"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["全部停用"]).click()
        self.web_handler.accept_confirm_msg()
        time.sleep(2)
        self.web_handler.refresh_page()
        time.sleep(2)
        new_stat = self.find_element(self.ElementCss["状态"]).text
        if new_stat == "已停用":
            return True
        else:
            return False

    def delete_all(self):  # 公用
        time.sleep(2)
        self.find_element(self.ElementCss["全部选择"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["全部删除"]).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        time.sleep(1)

    def check_speed_limit(self):  # 验证限速
        speed = ST.IkSpeedtest()
        speed1 = speed.test_ik_speed()
        speed.tearDown()
        set_upload = self.TestData["上行"]
        set_download = self.TestData["下行"]
        var_upload = int(set_upload) / 128
        var_download = int(set_download) / 128
        print("\t 设置: 上行: ", var_upload, " Mps, 下行: ", var_download, " Mps")
        print("\t 实测：上行: %s Mps, 下行: %s Mps" % (speed1[0], speed1[1]))
        if (float(speed1[0]) > 1.5 * var_upload or float(speed1[1]) > 1.5 * var_download or float(
                speed1[0]) < 0.5 * var_upload or float(speed1[1]) < 0.5 * var_download):
            self.fun_bool=False
            return self.check_function()
        else:
            self.fun_bool = True
            return self.check_function()

    def check_add(self):
        if self.add_bool and self.TestData["预期结果"] != "添加失败":
            return True
        elif not self.fun_bool and self.TestData["预期结果"] == "添加失败":
            return True
        else:
            return False

    def check_function(self):
        if self.fun_bool and self.TestData["预期结果"] == "限速成功":
            return True
        elif not self.fun_bool and self.TestData["预期结果"] == "限速失败":
            return True
        else:
            return False

