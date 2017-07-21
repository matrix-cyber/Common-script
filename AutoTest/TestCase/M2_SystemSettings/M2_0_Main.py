# 只接一个X1 AP
import sys
sys.path.append("..")
import TestCase.M2_SystemSettings.M2_4_2_WebAccountManage as WAM
class M2_0_Main:
    def __init__(self, web_handler, TestData):
        self.web_handler = web_handler
        self.TestData = TestData

    def run_tests(self):
        WebManage = WAM.M2_4_2_WebAccountManage(self.web_handler, self.TestData)
        WebManage.run_tests()

# if __name__ == "__main__":
#     Mdict = M2_0_Main.__dict__
#     len1 = len(Mdict)
#     for (i,j) in Mdict.items():
#         if i.find("run")!= -1:
#             print(i,"is",j)



