import sys
sys.path.append("..")
import TestBase.ElementBase as CSS
import TestBase.TopoBase as Topo
import time


class ProtocolFlow:
    def __init__(self, web_handler, ssh_handler, TestData):
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu
        self.ElementCss = CSS.ElementBase.ProFlow
        self.TestData = TestData
        self.bool = True

    def find_element(self, pera):
        return self.web_handler.find_element_by_css_selector(pera)

    def find_element_value(self, pera, get):
        return self.web_handler.find_element_by_css_selector(pera).get_attribute(get)

    def syn_proxy_state(self):
        txt = self.find_element(self.ElementCss['开启增强分流']).get_attribute('checked')
        if txt != "true":
            self.find_element(self.ElementCss['开启增强分流']).click()
            time.sleep(1)
            self.find_element(self.ElementCss['开启增强确定']).click()
        time.sleep(1)

    def add(self):
        self.find_element(self.ElementCss['全选']).click()
        self.find_element(self.ElementCss['删除多']).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        self.web_handler.refresh_page()
        time.sleep(1)
        self.find_element(self.ElementCss['添加']).click()
        self.find_element(self.ElementCss['编辑线路']).click()
        if self.TestData['线路'] != '':
            self.find_element(self.ElementCss['指定线路1'] + self.TestData['线路'] + self.ElementCss['指定线路2']).click()
        self.find_element(self.ElementCss['线路确定']).click()
        self.find_element(self.ElementCss['编辑协议']).click()
        if self.TestData['协议'] != '':
            for t in range(4, 13):
                self.find_element(self.ElementCss['所有协议1'] + str(t) + self.ElementCss['所有协议2']).click()
            self.find_element(self.ElementCss['添加协议']).click()
        self.find_element(self.ElementCss['协议确定']).click()
        self.find_element(self.ElementCss['编辑源地址']).click()
        self.find_element(self.ElementCss['IP地址']).send_keys(self.TestData['源地址'])
        self.find_element(self.ElementCss['添加IP']).click()
        self.find_element(self.ElementCss['地址确定']).click()
        self.find_element(self.ElementCss['编辑备注']).clear()
        self.find_element(self.ElementCss['编辑备注']).send_keys(self.TestData['备注'])
        self.find_element(self.ElementCss['保存']).click()
        return True

    def check_action(self, web):
        self.ssh_handler.exec_cmd('conntrack -F')
        time.sleep(1)
        self.web_handler.open_webpage(web)
        time.sleep(1)
        address = self.ssh_handler.exec_cmd('nslookup ' + web + ' | grep -A 5 Name | awk \'{print $3}\' | grep [0-9] | sed ":a ;N;s/\\n/|/;t a;"')
        address = address.replace("\n", "")
        con_num = self.ssh_handler.exec_cmd('cat /proc/net/nf_conntrack | grep -E ' + address + ' | grep ' + Topo.TEST_PC + '| grep ' +  self.TestData['线路'] + ' | wc -l')
        if (int(con_num) > 2 and self.TestData['预期结果'] == '成功'):
            return True
        elif (int(con_num) == 0 and self.TestData['预期结果'] == '失败'):
            return True
        else:
            return False

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

    def off_one(self):
        self.find_element(self.ElementCss['停用']).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        return True

    def on_one(self):
        time.sleep(1)
        self.find_element(self.ElementCss['启用']).click()
        time.sleep(1)
        return True

    def off_all(self):
        self.find_element(self.ElementCss['全选']).click()
        self.find_element(self.ElementCss['停用多']).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        return True

    def on_all(self):
        self.find_element(self.ElementCss['全选']).click()
        self.find_element(self.ElementCss['启用多']).click()
        return True

    def delete_one(self):
        self.ElementCss(self.ElementCss['删除']).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        return True

    def delete_all(self):
        self.find_element(self.ElementCss["全选"]).click()
        time.sleep(1)
        self.find_element(self.ElementCss["删除多"]).click()
        time.sleep(1)
        self.web_handler.accept_confirm_msg()
        time.sleep(1)
        return True

    def change_action(self):
        self.find_element(self.ElementCss['修改']).click()
        self.find_element(self.ElementCss['编辑线路']).click()
        if self.TestData['二次线路'] != '':
            self.find_element(self.ElementCss['全部线路']).click()
            self.find_element(self.ElementCss['全部线路']).click()
            self.find_element(self.ElementCss['指定线路1'] + self.TestData['二次线路'] + self.ElementCss['指定线路2']).click()
        self.find_element(self.ElementCss['线路确定']).click()
        self.find_element(self.ElementCss['编辑源地址']).click()
        if self.TestData['二次地址'] != '':
            try:
                self.find_element(self.ElementCss['已添加IP']).click()
                self.find_element(self.ElementCss['删除IP']).click()
            except:
                pass
            self.find_element(self.ElementCss['IP地址']).send_keys(self.TestData['二次地址'])
            self.find_element(self.ElementCss['添加IP']).click()
        self.find_element(self.ElementCss['地址确定']).click()
        time.sleep(1)
        self.find_element(self.ElementCss['保存']).click()
        time.sleep(2)
        return True
