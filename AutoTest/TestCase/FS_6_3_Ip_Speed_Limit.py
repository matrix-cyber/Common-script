# coding=utf-8
import sys
from types import FunctionType
sys.path.append("..")
import ik_web_autotest.ik_web_test_stats as IKSTATS
import ik_utils.ik_ssh_utils as IKSU
import ik_web_autotest.ik_speedtest as IKSP
import time

class IpSpeedLimit:
    def __init__(self, web_handler, ssh_handler, Ip):
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.Ip = Ip

    def test1_ip_speed(self):
        # 测试例：手工流控限速值小，IP限速值大，结果：手工流控限速生效
        ret = IKSTATS.TestCaseRet()
        print("<1> set ip speed limit：手工流控策略低，IP限速高，手工流控生效")
        # 1 配置一键流控
        # 1.1 关闭一键流控
        print("\t >>>>> close onekey flow-control")
        time.sleep(2)
        self.web_handler.find_element_by_xpath(".//*[@id='menu']/li[6]/ul/li[1]/a").click()
        time.sleep(1)
        controltatus = self.web_handler.find_element_by_xpath("//div/div/div[1]/label/div/span").get_attribute("class")
        time.sleep(2)
        if controltatus == "rounded G_bg":
            self.web_handler.find_element_by_xpath("//div/div/div[1]/label/div/span").click()
        #配置手工流控带宽
        self.web_handler.find_element_by_xpath("html/body/div[10]/ul/li[6]/ul/li[1]/a").click()
        time.sleep(2)
        # 1.2 配置WAN1带宽，删除独立限速条目
        self.web_handler.find_element_by_xpath("html/body/div[11]/div[2]/div/div/table[2]/tbody/tr[2]/td[5]/a[1]").click()
        self.web_handler.find_element_by_xpath("html/body/div[11]/div[2]/div/div/table[2]/tbody/tr[3]/td[2]/input").clear()
        self.web_handler.find_element_by_xpath("html/body/div[11]/div[2]/div/div/table[2]/tbody/tr[3]/td[2]/input").send_keys("1024")
        self.web_handler.find_element_by_xpath("html/body/div[11]/div[2]/div/div/table[2]/tbody/tr[3]/td[3]/input").clear()
        self.web_handler.find_element_by_xpath("html/body/div[11]/div[2]/div/div/table[2]/tbody/tr[3]/td[3]/input").send_keys("1024")
        self.web_handler.find_element_by_xpath("html/body/div[11]/div[2]/div/div/table[2]/tbody/tr[3]/td[5]/a[1]").click()
        time.sleep(1)

        while(1):
            try:
                link = self.web_handler.find_element_by_xpath("html/body/div[11]/div[2]/div/div/table[4]/tbody/tr[2]/td[11]/a[4]")
                link.click()
                time.sleep(1)
                link = self.web_handler.find_element_by_xpath("html/body/div[3]/div[2]/table/tbody/tr[2]/td/div/input[2]")
                link.click()
                time.sleep(3)
            except Exception as e:
                break
        time.sleep(2)
        # 2 配置手工流控
        print("\t >>>>> set manual flow-control")
        self.web_handler.find_element_by_xpath("html/body/div[10]/ul/li[6]/ul/li[2]/a").click()
        time.sleep(2)
        # 2.1 删除所有原来的策略
        try:
            self.web_handler.find_element_by_xpath("html/body/div[11]/div[2]/div/div/table[4]/tbody/tr[2]/td[1]")
            self.web_handler.find_element_by_xpath("html/body/div[11]/div[2]/div/div/table[4]/tbody/tr[1]/th[12]/input").click()
            self.web_handler.find_element_by_xpath("html/body/div[11]/div[2]/div/div/div[4]/a[1]").click()
            self.web_handler.find_element_by_xpath("html/body/div[3]/div[2]/table/tbody/tr[2]/td/div/input[2]").click()
        except Exception as e:
            pass
        # 2.2 添加新的手工策略。限速为700KB/S
        time.sleep(2)
        self.web_handler.find_element_by_xpath("//div[2]/div/div/div[4]/a[6]").click()
        self.web_handler.find_element_by_xpath("//div[2]/table/tbody/tr[1]/td[2]/input").send_keys("TEST")
        self.web_handler.find_element_by_xpath("//div[2]/table/tbody/tr[2]/td[2]/div/input").click()
        self.web_handler.find_element_by_xpath("//div[2]/table/tbody/tr[2]/td[2]/div/ul/li[1]").click()
        self.web_handler.find_element_by_xpath("//div[2]/table/tbody/tr[3]/td[2]/div/input").click()
        self.web_handler.find_element_by_xpath("//div[2]/table/tbody/tr[3]/td[2]/div/ul/li[1]").click()
        self.web_handler.find_element_by_xpath(".//*[@id='protocol-tree']/tbody/tr/td[1]/div/ul/li/span").click()
        self.web_handler.find_element_by_xpath(".//*[@id='protocol-tree']/tbody/tr/td[2]/a[1]").click()
        self.web_handler.find_element_by_xpath("//tr[6]/td[2]/table/tbody/tr[1]/td[1]/div[1]/input").send_keys(self.Ip[2])
        self.web_handler.find_element_by_xpath("//tr[6]/td[2]/table/tbody/tr[1]/td[2]/a[1]").click()
        self.web_handler.find_element_by_xpath("//table/tbody/tr[9]/td[2]/input").send_keys("100")
        self.web_handler.find_element_by_xpath("//table/tbody/tr[10]/td[2]/input").send_keys("1000")
        self.web_handler.find_element_by_xpath("//table/tbody/tr[13]/td[2]/input").send_keys("100")
        self.web_handler.find_element_by_xpath("//table/tbody/tr[14]/td[2]/input").send_keys("1000")
        self.web_handler.find_element_by_xpath("//table/tbody/tr[16]/td[2]/input").send_keys("400")
        self.web_handler.find_element_by_xpath("//table/tbody/tr[17]/td[2]/input").send_keys("400")
        self.web_handler.find_element_by_xpath("html/body/div[13]/div[3]/div[2]/input[2]").click()
        time.sleep(2)


        # 3 配置IP限速
        print("\t >>>>> set IP speedlimit")
        self.web_handler.find_element_by_xpath(".//*[@id='menu']/li[6]/ul/li[3]/a").click()
        time.sleep(1)

        while(1):
            try:
                link = self.web_handler.find_element_by_xpath("html/body/div[11]/div[2]/div/div/table[1]/tbody/tr[2]/td[8]/a[4]")
                link.click()
                time.sleep(1)
                link = self.web_handler.find_element_by_xpath("html/body/div[3]/div[2]/table/tbody/tr[2]/td/div/input[2]")
                link.click()
                time.sleep(3)
            except Exception as e:
                break

        # 3.2 添加限速条目
        time.sleep(2)
        self.web_handler.find_element_by_xpath("//div[11]/div[2]/div/div/div[3]/a[4]").click()
        self.web_handler.find_element_by_xpath("//div/table[1]/tbody/tr[3]/td[1]/input").click()
        time.sleep(2)
        self.web_handler.find_element_by_xpath("//tr/td[2]/table/tbody/tr[1]/td[1]/div[1]/input").send_keys(self.Ip[2])
        self.web_handler.find_element_by_xpath("//tr/td[2]/table/tbody/tr[1]/td[2]/a[1]").click()
        self.web_handler.find_element_by_xpath(".//*[@id='add-ipgroup-box']/div[3]/div[2]/input[2]").click()
        time.sleep(1)
        self.web_handler.find_element_by_xpath("//table[1]/tbody/tr[3]/td[2]/input").clear()
        self.web_handler.find_element_by_xpath("//table[1]/tbody/tr[3]/td[2]/input").send_keys("600")
        self.web_handler.find_element_by_xpath("//table[1]/tbody/tr[3]/td[3]/input").clear()
        self.web_handler.find_element_by_xpath("//table[1]/tbody/tr[3]/td[3]/input").send_keys("600")
        self.web_handler.find_element_by_xpath("//table[1]/tbody/tr[3]/td[7]/input").send_keys("TESTLIMIT")
        self.web_handler.find_element_by_xpath("//table[1]/tbody/tr[3]/td[8]/a[1]").click()
        time.sleep(1)

        # 后台验证
        print("\t >>>>> check IP speedlimit by ssh")
        output = self.ssh_handler.exec_cmd("sqlite3 /etc/mnt/ikuai/config.db 'select * from simple_qos;' -line")
        output = IKSU.IkSSHUtils.get_one_block_data(output)
        output = IKSU.IkSSHUtils.parse_data_to_dict(output, "=")
        if (output["state"] == "up" and
            output["comment"] == "TESTLIMIT" and
            output["ip_addr"] == self.Ip[2] and
            output["upload"] == "600" and
            output["download"] == "600" and
            output["week"] == "1234567" and
            output["time"] == "00:00-23:59"):
            pass
        else:
            ret.set_error("Fail to set IP speedlimit by ssh")
            return ret

        # 3.3 speed test
        print("\t >>>>> check the function")
        speed = IKSP.IkSpeedtest()
        speed1 = speed.test_ik_speed()
        speed.tearDown()
        set_upload = output["upload"]
        set_download = output["download"]
        var_upload = int(set_upload) / 128
        var_download = int(set_download) / 128
        manual_speed = float(400/128)
        print("\t 手工流控配置: upload: ", float(400/128), " Mps, download: ", float(400/128), " Mps")
        print("\t IP限速配置: upload: ", var_upload, " Mps, download: ", var_download, " Mps")
        print("\t 测试结果： upload: %s Mps, download: %s Mps" % (speed1[0], speed1[1]))
        if (float(speed1[0]) > 1.5*manual_speed or float(speed1[1]) > 1.5*manual_speed  or float(speed1[0]) < 0.5*manual_speed  or float(speed1[1]) < 0.5*manual_speed ):
            ret.set_error("Function of IP speed-limit is invalid")
            return ret

        print("<2> change the IP speed Limit：手工流控限速高，IP限速低，IP限速生效")
        # 添加手工流控
        print("\t >>>>> set flow-control")
        time.sleep(1.5)
        self.web_handler.find_element_by_xpath(".//*[@id='menu']/li[6]/ul/li[2]/a").click()
        time.sleep(2)
        self.web_handler.find_element_by_xpath("html/body/div[11]/div[2]/div/div/table[4]/tbody/tr[2]/td[11]/a[1]").click()
        self.web_handler.find_element_by_xpath("//div[2]/table/tbody/tr[1]/td[2]/input").send_keys("TEST_NEW")
        self.web_handler.find_element_by_xpath("//div[2]/table/tbody/tr[2]/td[2]/div/input").click()
        self.web_handler.find_element_by_xpath("//div[2]/table/tbody/tr[2]/td[2]/div/ul/li[1]").click()
        self.web_handler.find_element_by_xpath("//div[2]/table/tbody/tr[3]/td[2]/div/input").click()
        self.web_handler.find_element_by_xpath("//div[2]/table/tbody/tr[3]/td[2]/div/ul/li[1]").click()
        self.web_handler.find_element_by_xpath("//tr[6]/td[2]/table/tbody/tr[1]/td[1]/div[1]/input").send_keys(self.Ip[2])
        self.web_handler.find_element_by_xpath("//tr[6]/td[2]/table/tbody/tr[1]/td[2]/a[1]").click()
        link = self.web_handler.find_element_by_xpath("//table/tbody/tr[9]/td[2]/input")
        link.clear()
        link.send_keys("100")
        link = self.web_handler.find_element_by_xpath("//table/tbody/tr[10]/td[2]/input")
        link.clear()
        link.send_keys("800")
        link = self.web_handler.find_element_by_xpath("//table/tbody/tr[13]/td[2]/input")
        link.clear()
        link.send_keys("100")
        link = self.web_handler.find_element_by_xpath("//table/tbody/tr[14]/td[2]/input")
        link.clear()
        link.send_keys("800")
        link = self.web_handler.find_element_by_xpath("//table/tbody/tr[16]/td[2]/input")
        link.clear()
        link.send_keys("600")
        link = self.web_handler.find_element_by_xpath("//table/tbody/tr[17]/td[2]/input")
        link.clear()
        link.send_keys("600")
        self.web_handler.find_element_by_xpath("html/body/div[13]/div[3]/div[2]/input[2]").click()
        time.sleep(2)

        print("\t >>>>> check by ssh")
        output = self.ssh_handler.exec_cmd("sqlite3 /etc/mnt/ikuai/config.db 'select * from layer7_qos;' -line")
        output = IKSU.IkSSHUtils.get_one_block_data(output)
        output = IKSU.IkSSHUtils.parse_data_to_dict(output, "=")
        if (output["state"] == "up" and
            output["interface"] == "wan1" and
            output["prio"] == "1" and
            output["ip_addr"] == self.Ip[2] and
            output["app_proto"] == "所有协议" and
            output["week"] == "1234567" and
            output["time"] == "00:00-23:59" and
            output["min_up"] == "100" and
            output["min_down"] == "100" and
            output["max_up"] == "800" and
            output["max_down"] == "800" and
            output["avg_up"] == "600" and
            output["avg_down"] == "600"):
            pass
        else:
            ret.set_error("Fail to set flow control strategy in ssh after change")
            return ret

        # 编辑IP限速
        self.web_handler.find_element_by_xpath("html/body/div[10]/ul/li[6]/ul/li[3]/a").click()
        time.sleep(2)
        self.web_handler.find_element_by_xpath("html/body/div[11]/div[2]/div/div/table[1]/tbody/tr[2]/td[8]/a[1]").click()
        self.web_handler.find_element_by_xpath("html/body/div[11]/div[2]/div/div/table[1]/tbody/tr[3]/td[1]/input").clear()
        self.web_handler.find_element_by_xpath("html/body/div[11]/div[2]/div/div/table[1]/tbody/tr[3]/td[1]/input").send_keys(self.Ip[2])
        self.web_handler.find_element_by_xpath("//table[1]/tbody/tr[3]/td[2]/input").clear()
        self.web_handler.find_element_by_xpath("//table[1]/tbody/tr[3]/td[2]/input").send_keys("300")
        self.web_handler.find_element_by_xpath("//table[1]/tbody/tr[3]/td[3]/input").clear()
        self.web_handler.find_element_by_xpath("//table[1]/tbody/tr[3]/td[3]/input").send_keys("300")
        self.web_handler.find_element_by_xpath("//table[1]/tbody/tr[3]/td[7]/input").clear()
        self.web_handler.find_element_by_xpath("//table[1]/tbody/tr[3]/td[7]/input").send_keys("TESTLIMIT")
        self.web_handler.find_element_by_xpath("//table[1]/tbody/tr[3]/td[8]/a[1]").click()
        time.sleep(1)

        # 后台验证
        print("\t >>>>> check limit by ssh after change")
        output = self.ssh_handler.exec_cmd("sqlite3 /etc/mnt/ikuai/config.db 'select * from simple_qos;' -line")
        output = IKSU.IkSSHUtils.get_one_block_data(output)
        output = IKSU.IkSSHUtils.parse_data_to_dict(output, "=")
        if (output["state"] == "up" and
            output["comment"] == "TESTLIMIT" and
            output["ip_addr"] == self.Ip[2] and
            output["upload"] == "300" and
            output["download"] == "300" and
            output["week"] == "1234567" and
            output["time"] == "00:00-23:59"):
            pass
        else:
            ret.set_error("Fail to check the IP Speed Limit in ssh after change")
            return ret

        ## speed test
        print("\t >>>>> check limit by speed after changing speed")
        speed = IKSP.IkSpeedtest()
        speed1 = speed.test_ik_speed()
        speed.tearDown()
        set_upload = output["upload"]
        set_download = output["download"]
        var_upload = int(set_upload) / 128
        var_download = int(set_download) / 128
        print("\t 手工流控配置: upload: ", float(600/128), " Mps, download: ", float(600/128), " Mps")
        print("\t IP限速配置: upload: ", var_upload, " Mps, download: ", var_download, " Mps")
        print("\t 测试结果： upload: %s Mps, download: %s Mps" % (speed1[0], speed1[1]))
        if (float(speed1[0]) > 1.5 * var_upload or float(speed1[1]) > 1.5 * var_download or float(speed1[0]) < 0.5 *var_upload or float(speed1[1]) < 0.5 * var_download):
            ret.set_error("speedlimit is invalid after changing speed")
            return ret
        # IP 限速停用后，手工流控的600KB/S生效
        ret = IKSTATS.TestCaseRet()
        print("<3> stop the IP-speedlimit")
        self.web_handler.find_element_by_xpath("//table[1]/tbody/tr[2]/td[8]/a[3]").click()
        time.sleep(2)
        self.web_handler.find_element_by_xpath("html/body/div[3]/div[2]/table/tbody/tr[2]/td/div/input[2]").click()
        time.sleep(2)

        print(">>>>> check by ssh after stopping IP-speedlimit")
        output = self.ssh_handler.exec_cmd("sqlite3 /etc/mnt/ikuai/config.db 'select * from simple_qos;' -line")
        output = IKSU.IkSSHUtils.get_one_block_data(output)
        output = IKSU.IkSSHUtils.parse_data_to_dict(output, "=")
        if output["state"] != "down":
            ret.set_error("Fail to set by ssh after stopping IP-speedlimit")
            return ret

        print(">>>>> check the function after stopping IP-speedlimit")
        time.sleep(5)
        speed = IKSP.IkSpeedtest()
        speed1 = speed.test_ik_speed()
        speed.tearDown()
        set_upload = "600"
        set_download = "600"
        var_upload = int(set_upload) / 128
        var_download = int(set_download) / 128
        print("\t 手工流控配置: upload: ", float(600/128), " Mps, download: ", float(600/128), " Mps")
        print("\t IP限速配置: 停用")
        print("\t 停用IP限速—测试结果： upload: %s Mps, download: %s Mps" % (speed1[0], speed1[1]))
        if (float(speed1[0]) > 1.5 * var_upload or float(speed1[1]) > 1.5 * var_download or float(speed1[0]) < 0.5 * var_upload or float(speed1[1]) < 0.5 * var_download):
            ret.set_error("speedlimit is invalid after stopping IP-speedlimit")
            return ret
        return ret

    def run_tests(self):
        test_stats = IKSTATS.IkWebTestStats()
        for name, func in sorted(IpSpeedLimit.__dict__.items()):
            if type(func) == FunctionType and name.startswith("test"):
                ret = func(self)
                if ret.is_ok():
                    test_stats.add_pass_test_case(name)
                else:
                    test_stats.add_fail_test_case(name, ret.error_str())
            else:
                continue
        test_stats.show_result()
        pass
