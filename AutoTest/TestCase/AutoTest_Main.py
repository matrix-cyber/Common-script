
import sys
sys.path.append("..")
import TestBase.ActionBase.Base_Action.Web_Action as WA
import TestBase.ActionBase.Base_Action.SSH_Action as SA
import TestBase.ActionBase.Base_Action.Public_Action as PA
import TestBase.TopoBase as Topo
import TestBase.DataBase as TD
import TestCase.M3_NetworkSettings.M3_0_Main as M3
import TestCase.M5_FlowControl.M5_0_Main as M5
import time

class AutoTest_Main:
    def __init__(self, host):
        login = TD.TestData.Login[0]
        self.web_handler = WA.Web_Action(url="http://"+host, user=login["用户名"], pwd=login["密码"])
        self.ssh_handler = SA.IkSSHHandler(host)

    def connect(self):
        print("0-登录设备：")
        self.web_handler.connect()
        self.ssh_handler.connect()

    def Run_Tests(self):
        # test = M2.M2_0_Main(self.web_handler, self.TestData)
        # test.run_tests()
        # print("__________________________________________________________________________________________")
        # print("3-网络设置：")
        # test = M3.M3_0_Main(self.web_handler, self.ssh_handler)
        # test.run_tests()
        print("__________________________________________________________________________________________")
        print("5-流控设置：")
        test = M5.M5_0_Main(self.web_handler, self.ssh_handler)
        test.run_tests()

    def Restart_HostDhcp(self):
        PA.windows_cmd("ipconfig /release")
        time.sleep(2)
        PA.windows_cmd("ipconfig /renew")
        time.sleep(2)

if __name__ == "__main__":
    web_tests = AutoTest_Main(Topo.DUT)
    # web_tests.Restart_HostDhcp()
    web_tests.connect()
    web_tests.Run_Tests()








